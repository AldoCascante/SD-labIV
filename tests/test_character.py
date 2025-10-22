import unittest
from src.models.character import Character

class TestCharacter(unittest.TestCase):

    def test_character_starts_alive_with_full_health(self):
        """Test que un personaje nuevo tiene salud completa y está vivo"""
        warrior = Character("Conan")
        self.assertEqual(warrior.health, 100)
        self.assertTrue(warrior.is_alive)

    def test_take_damage_reduces_health(self):
        """Test que el daño reduce salud y puede matar al personaje"""
        mage = Character("Gandalf")
        mage.take_damage(30)
        self.assertEqual(mage.health, 70)
        

    def test_take_damage_can_kill(self):
        """Test que el daño reduce salud y puede matar al personaje"""
        mage = Character("Gandalf")
        mage.take_damage(100)
        self.assertEqual(mage.health, 0)
        self.assertFalse(mage.is_alive)