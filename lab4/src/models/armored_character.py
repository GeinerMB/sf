from src.models.character import Character
from src.models.i_damage_filter import IDamageFilter
from typing import Optional


class ArmoredCharacter(Character):
    """Personaje con armadura que filtra el daño recibido según un filtro de daño.
    """

    def __init__(self, name: str, health: int = 100, damage_filter: Optional[IDamageFilter] = None):
        super().__init__(name, health)
        self.damage_filter = damage_filter

    def take_damage_by_weapon(self, damage: int, weapon):
        """Aplica daño solo si el filtro lo permite (o si no se establece ningún filtro)."""
        if self.damage_filter is None or self.damage_filter.allows(weapon):
            self.take_damage(damage)
        # else: ignore damage
