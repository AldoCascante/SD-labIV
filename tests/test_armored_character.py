import unittest
from src.models.armored_character import ArmoredCharacter

class TestCharacter(unittest.TestCase):

    def test_armored_character_starts_alive_with_full_health(self):
        """Test que un personaje nuevo con armadura tiene salud completa y está vivo"""
        knight = ArmoredCharacter("Green unit")
        self.assertEqual(knight.health, 100)
        self.assertTrue(knight.is_alive)

    def test_take_damage_reduces_health(self):
        """Test que el daño reduce salud """
        knight = ArmoredCharacter("Green unit")
        knight.take_damage(30)
        self.assertEqual(knight.health, 70)
        
    def test_take_damage_can_kill(self):
        """Test que el daño puede matar al personaje"""
        knight = ArmoredCharacter("Green unit")
        knight.take_damage(100)
        self.assertEqual(knight.health, 0)
        self.assertFalse(knight.is_alive)

    def test_reduced_damage_taken(self):
        """Test que el daño a un personaje con armadura se reduce"""
        knight = ArmoredCharacter("Green unit", 100, 10)
        knight.take_damage(30)
        self.assertEqual(knight.health, 80) #100 - (30 - 10) = 20 damage
    
    def test_reduced_damage_to_zero(self):
        """Test que el daño a un personaje con armadura se reduce hasta 0"""
        knight = ArmoredCharacter("Green unit", 100, 50)
        knight.take_damage(30)
        self.assertEqual(knight.health, 100)
        knight.take_damage(10)
        self.assertEqual(knight.health, 100)