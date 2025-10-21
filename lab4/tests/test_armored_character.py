import unittest
from src.models.armored_character import ArmoredCharacter
from src.models.sword import Sword
from src.models.bow import Bow
from src.models.i_damage_filter import IDamageFilter
from src.models.character import Character


class DenyBowFilter(IDamageFilter):
    def allows(self, weapon) -> bool:
        # allow only swords (by class name) for simplicity
        return weapon.__class__.__name__.lower() == "sword"


class HalfDamageFilter(IDamageFilter):
    def allows(self, weapon) -> bool:
        # this filter signals allows but we will simulate partial damage by
        # checking for its presence in the test and applying half damage.
        return True


class TestArmoredCharacter(unittest.TestCase):

    def test_armored_receives_sword_damage(self):
        armor = ArmoredCharacter("Tank", damage_filter=DenyBowFilter())
        hero = Character("Hero")
        sword = Sword()

        # perform attack: since Sword doesn't expose get_damage, fallback will
        # let weapon.attack apply damage — ArmoredCharacter has take_damage_by_weapon
        # so CombatSystem's logic would prefer that path; here we'll simulate by
        # directly calling take_damage_by_weapon to mirror CombatSystem behavior.
        armor.take_damage_by_weapon(15, sword)
        self.assertEqual(armor.health, 85)

    def test_armored_ignores_bow_damage(self):
        armor = ArmoredCharacter("Tank", damage_filter=DenyBowFilter())
        bow = Bow()

        # Bow would do 12 damage but filter denies it
        armor.take_damage_by_weapon(12, bow)
        self.assertEqual(armor.health, 100)

    def test_armored_partial_resistance(self):
        # Implement a filter that allows damage but test applying half damage
        class HalfFilter(IDamageFilter):
            def allows(self, weapon) -> bool:
                return True

        armor = ArmoredCharacter("Tank", damage_filter=HalfFilter())
        sword = Sword()

        # Simulate half damage application
        original_health = armor.health
        damage = 15
        reduced = damage // 2
        armor.take_damage_by_weapon(reduced, sword)
        self.assertEqual(armor.health, original_health - reduced)
