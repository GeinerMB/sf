from src.models.character import Character
from src.models.i_damage_filter import IDamageFilter
from typing import Optional


class ArmoredCharacter(Character):
    """Character that may ignore or alter damage based on an injected damage filter.

    By default it has no filter and behaves like a normal Character. Inject an
    implementation of `IDamageFilter` to control which weapon damage is applied.
    """

    def __init__(self, name: str, health: int = 100, damage_filter: Optional[IDamageFilter] = None):
        super().__init__(name, health)
        self.damage_filter = damage_filter

    def take_damage_by_weapon(self, damage: int, weapon):
        """Apply damage only if the filter allows it (or if no filter is set)."""
        if self.damage_filter is None or self.damage_filter.allows(weapon):
            self.take_damage(damage)
        # else: ignore damage
