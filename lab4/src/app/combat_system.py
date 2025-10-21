
from src.app.i_combat_system import ICombatSystem


class CombatSystem(ICombatSystem):
    def __init__(self, damage_calculator):
        self.damage_calculator = damage_calculator

    def perform_attack(self, attacker, weapon, target):
        if not target.is_alive:
            return f"{target.name} ya est\u00e1 derrotado"

        # Prefer weapons that expose a `get_damage(attacker, target)` method.
        damage = None
        if hasattr(weapon, "get_damage"):
            try:
                damage = weapon.get_damage(attacker, target)
            except TypeError:
                # defensive: fall back to simple call
                damage = None

        # If the target provides a weapon-aware damage hook, use it to apply damage
        # without relying on weapon.attack to mutate state.
        message = None
        if damage is not None and hasattr(target, "take_damage_by_weapon"):
            # apply damage through target's hook
            target.take_damage_by_weapon(damage, weapon)
            # Try to get a human-friendly message from the weapon (optional)
            if hasattr(weapon, "describe_attack"):
                message = weapon.describe_attack(attacker, target, damage)
        else:
            # fallback: let the weapon perform its attack (existing behavior)
            message = weapon.attack(attacker, target)

        if message is None:
            message = f"{attacker.name} ataca a {target.name}"  # generic message

        critical = self.damage_calculator.check_critical_hit()

        if critical:
            bonus_damage = 10
            # Use weapon-aware hook if available
            if hasattr(target, "take_damage_by_weapon"):
                target.take_damage_by_weapon(bonus_damage, weapon)
            else:
                target.take_damage(bonus_damage)
            message += f" \u00a1GOLPE CR\u00cdTICO! +{bonus_damage} da\u00f1o extra"

        return message