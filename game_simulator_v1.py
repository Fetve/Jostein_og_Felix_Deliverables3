# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon


class Character:
    """Represents a character in the RPG"""

    def __init__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None) -> None:
        """
        Initialise the Character

        Args:
            name (str): The name of the character.
            hp_max (int): Max hit points (default = 100)
            damage (int): Damage delt when character attacks (default = 10)
            weapon (Weapon | None): Optional equipped weapon (default = None)
        """
        self.name = name
        self._hp = hp_max  # Note: _hp indicated private attribute
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target: "Character") -> None:
        """Angriper en annen figur med våpenet eller figurens vanlige skade."""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage
        target.take_damage(damage)
        
    def take_damage(self, amount: int) -> None:
        """Reduserer figurens helse uten at den kan bli lavere enn null."""
        self._hp = max(self._hp - amount, 0)
    
    def heal(self, amount: int) -> None:
        """Øker figurens helse, men aldri over maksimal helse."""
        self._hp = min(self._hp + amount, self.hp_max)
        
    @property
    def is_alive(self) -> bool:
        """Returnerer True hvis figuren fortsatt har helse igjen."""
        return self._hp > 0
    
    def introduce(self) -> None:
        """Skriver ut en kort introduksjon av figuren."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        """Representation of character object"""
        return f"<Character name={self.name} hp={self.hp} damage={self.damage}>"

    def __str__(self) -> str:
        """String representation of character object"""
        return f"Character: {self.name} with {self.hp} HP and {self.damage} damage"

    @property
    def hp(self) -> int:
        """Public read-only property to inspect HP without allowing direct, unsafe edits."""
        return self._hp
    
class Warrior(Character):
    """En figurtype som reduserer skade med rustning."""

    def __int__(self, name: str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, armor: int = 5) -> None:
        """Setter opp krigeren med standardverdier og en rustningsverdi."""
        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor
    
    def take_damage(self, amount: int) -> None:
        """Trekker rustningen fra innkommende skade før helsen reduseres."""
        reduced = max(amount - self.armor, 0)
        super().take_damage(reduced)

class Mage(Character):
    """En figurtype som bruker mana til å utføre sterkere angrep."""

    def __int__(self, name:str, hp_max: int = 100, damage: int = 10, weapon: Weapon | None = None, mana: int = 30, mana_max: int = 30) -> None:
        """Setter opp magikeren med helse, skade og mana."""
        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max
        
    def attack(self, target: Character) -> None:
        """Bruker 10 mana for dobbelt skade, eller et vanlig angrep uten nok mana."""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage*2)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)
            