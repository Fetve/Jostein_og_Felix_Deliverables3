from game_simulator_v1 import Character


class Battle:
    """Styrer en kamp mellom en helt og en fiende."""

    def __init__(self, hero: Character, enemy: Character) -> None:
        """Lagrer deltakerne og setter kampens rundeteller til null."""
        self.hero = hero
        self.enemy = enemy
        self.round = 0
    
    def play_round(self) -> None:
        """Spiller én runde: helten angriper først, deretter fienden hvis den lever."""
        self.round += 1
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
            
    def simulate_battle(self):
        """Spiller runder til en deltaker er beseiret, og skriver ut vinneren."""
        while True:
            if self.enemy.is_alive and self.hero.is_alive:
                self.play_round()
            else:
                # Hvis helten er beseiret, er fienden vinneren.
                winner = self.hero if self.hero.is_alive else self.enemy
                print(f"{winner.name} wins!")
                break
