import random


class Dice:
    """Representerer en terning med et valgfritt antall sider."""

    def __init__(self, sides: int = 6):
        """Oppretter terningen og kontrollerer at den har minst to sider."""
        if sides < 2:
            raise ValueError("A dice must have at least 2 sides")
        self.sides = sides
        
    def roll(self) -> int:
        """Returnerer et tilfeldig heltall fra 1 til antall sider."""
        return random.randint(1, self.sides)    
    
    def __repr__(self):
        """Returnerer en tekstlig representasjon av terningen."""
        return f"Dice(sides={self.sides})"
    
    def __call__(self) -> int:
        """Lar terningen rulles ved å kalle objektet som en funksjon."""
        return self.roll()

