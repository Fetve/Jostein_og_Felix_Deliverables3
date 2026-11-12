from dice import Dice


class Weapon:
    """Representerer et våpen som bruker en terning til å bestemme skade."""

    def __init__(self, name: str, damage_dice: Dice) -> None:
        """Lagrer våpenets navn og skadeterning."""
        self.name = name
        self.damage_dice = damage_dice
        
    def roll_damage(self) -> int:
        """Kaster skadeterningen og returnerer resultatet."""
        return self.damage_dice.roll()
    
    def __repr__(self) -> str:
        """Returnerer en tekstlig representasjon av våpenet."""
        return f"Weapon(name={self.name!r}, damage_dice={self.damage_dice})"
    
    
    
    
    