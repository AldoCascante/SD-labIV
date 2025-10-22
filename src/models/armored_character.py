from src.models.character import Character


class ArmoredCharacter(Character):
    def __init__(self, name, health=100, dmg_reduction=0):
        super().__init__(name, health)
        self.defense = dmg_reduction

    def take_damage(self, damage):
        modifiedDamage = damage - self.defense
        if modifiedDamage < 0:
            modifiedDamage = 0

        self.health -= modifiedDamage
        if self.health <= 0:
            self.health = 0
            self.is_alive = False