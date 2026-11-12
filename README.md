# Jostein_og_Felix_Deliverables3

GenAI use – summary

We used Claude (Anthropic) as a tutor and code reviewer while working on Deliverable 3.

Planning: Asked for a step-by-step overview of the assignment and how to structure the project into modules (dice.py, items.py, the character file, battle.py).
Task 1 (Character): We wrote take_damage, heal and is_alive ourselves. Claude pointed out bugs: damage should come from the attacker as a parameter, heal used max instead of min, and is_alive printed instead of returning a bool and needed @property. Claude also showed how attack() should call target.take_damage() instead of changing _hp directly.
Task 2 (Dice): We asked what n >= 2 means and wrote most of the class ourselves. Claude suggested __repr__ and __call__ and confirmed the final version.
Task 3 (Weapon): Claude provided a skeleton for Weapon and the changes to Character.__init__ and attack().
Task 4 (Warrior/Mage): Claude provided the subclass code and explained super(), armor reduction and the mana logic.
Task 5 (Battle): Claude provided a Battle skeleton. We wrote our own simulate_battle(), and Claude explained why it looped forever (missing play_round() call, and or instead of and).
Other help: Where imports go, why Ruff warned about unsorted imports (I001), and why Dice should be in its own file (to avoid circular imports).

Reflection: GenAI was most useful for finding bugs and explaining why our code was wrong. We reviewed and tested all suggested code ourselves before using it