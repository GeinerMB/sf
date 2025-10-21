from src.app.i_combat_system import ICombatSystem
from src.app.i_combat_system import ICombatSystem


class CombatSystem(ICombatSystem):
    def __init__(self, damage_calculator):
        self.damage_calculator = damage_calculator

    def perform_attack(self, attacker, weapon, target):
        if not target.is_alive:
            return f"{target.name} ya está derrotado"

        # Preferir armas que expongan un método `get_damage(attacker, target)`.
        damage = None
        if hasattr(weapon, "get_damage"):
            try:
                damage = weapon.get_damage(attacker, target)
            except TypeError:
                # defensivo: volver a la llamada simple en caso de error
                damage = None

        # Si el objetivo provee un hook consciente del arma, usarlo para aplicar
        # el daño sin depender de que `weapon.attack` mutile el estado.
        message = None
        if damage is not None and hasattr(target, "take_damage_by_weapon"):
            # aplicar daño mediante el hook del objetivo
            target.take_damage_by_weapon(damage, weapon)
            # intentar obtener un mensaje legible desde el arma (opcional)
            if hasattr(weapon, "describe_attack"):
                message = weapon.describe_attack(attacker, target, damage)
        else:
            # alternativa: dejar que el arma realice su ataque (comportamiento existente)
            message = weapon.attack(attacker, target)

        if message is None:
            message = f"{attacker.name} ataca a {target.name}"  # mensaje genérico

        critical = self.damage_calculator.check_critical_hit()

        if critical:
            bonus_damage = 10
            # Usar hook consciente del arma si está disponible
            if hasattr(target, "take_damage_by_weapon"):
                target.take_damage_by_weapon(bonus_damage, weapon)
            else:
                target.take_damage(bonus_damage)
            message += f" ¡GOLPE CRÍTICO! +{bonus_damage} daño extra"

        return message