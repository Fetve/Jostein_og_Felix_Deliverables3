from game_simulator_v1 import Character


class Battle:
    
    def __init__(self, hero: Character, enemy: Character) -> None:
        
        self.hero = hero
        self.enemy = enemy
        self.round = 0
    
    def play_round(self) -> None:
        self.round += 1
        self.hero.attack(self.enemy)
        if self.enemy.is_alive:
            self.enemy.attack(self.hero)
            
    def simulate_battle(self):
        while True:
            if self.enemy.is_alive and self.hero.is_alive:
                self.play_round()
            else:
                winner = self.hero if self.hero.is_alive else self.enemy
                print(f"{winner.name} wins!")
                break
            