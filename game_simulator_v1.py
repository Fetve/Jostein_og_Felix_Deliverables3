# Object-oriented game simulator
# Turid Torheim, NMBU, 2026

from items import Weapon


class Character:
    """Represents a character in the RPG."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
    ) -> None:
        if hp_max < 0:
            raise ValueError("Maximum HP cannot be negative.")
        if damage < 0:
            raise ValueError("Damage cannot be negative.")

        self.name = name
        self._hp = hp_max
        self.hp_max = hp_max
        self.damage = damage
        self.weapon = weapon

    def attack(self, target: "Character") -> None:
        """Attack using a weapon or base damage."""
        if self.weapon is not None:
            damage = self.weapon.roll_damage()
        else:
            damage = self.damage

        target.take_damage(damage)

    def take_damage(self, amount: int) -> None:
        """Reduce HP without going below zero."""
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")

        self._hp = max(self._hp - amount, 0)

    def heal(self, amount: int) -> None:
        """Restore HP without exceeding maximum HP."""
        if amount < 0:
            raise ValueError("Healing amount cannot be negative.")

        self._hp = min(self._hp + amount, self.hp_max)

    @property
    def is_alive(self) -> bool:
        """Return whether the character is alive."""
        return self._hp > 0

    @property
    def hp(self) -> int:
        """Read-only access to current HP."""
        return self._hp

    def introduce(self) -> None:
        """Print a short introduction."""
        print(f"Hi, my name is {self.name}!")

    def __repr__(self) -> str:
        return (
            f"<Character name={self.name} "
            f"hp={self.hp} damage={self.damage}>"
        )

    def __str__(self) -> str:
        return (
            f"Character: {self.name} with "
            f"{self.hp} HP and {self.damage} damage"
        )


class Warrior(Character):
    """A character that reduces incoming damage using armor."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        armor: int = 5,
    ) -> None:
        if armor < 0:
            raise ValueError("Armor cannot be negative.")

        super().__init__(name, hp_max, damage, weapon)
        self.armor = armor

    def take_damage(self, amount: int) -> None:
        """Apply armor before reducing HP."""
        if amount < 0:
            raise ValueError("Damage amount cannot be negative.")

        reduced_damage = max(amount - self.armor, 0)
        super().take_damage(reduced_damage)


class Mage(Character):
    """A character that uses mana to cast stronger attacks."""

    def __init__(
        self,
        name: str,
        hp_max: int = 100,
        damage: int = 10,
        weapon: Weapon | None = None,
        mana: int = 30,
        mana_max: int = 30,
    ) -> None:
        if mana_max < 0:
            raise ValueError("Maximum mana cannot be negative.")
        if not 0 <= mana <= mana_max:
            raise ValueError("Mana must be between zero and maximum mana.")

        super().__init__(name, hp_max, damage, weapon)
        self.mana = mana
        self.mana_max = mana_max

    def attack(self, target: Character) -> None:
        """Cast a spell or use a normal attack and restore mana."""
        if self.mana >= 10:
            self.mana -= 10
            target.take_damage(self.damage * 2)
        else:
            super().attack(target)
            self.mana = min(self.mana + 5, self.mana_max)