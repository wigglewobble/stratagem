from typing import Hashable
from game_engine.payoff import PayoffMatrix

class Game:
    def __init__(
        self,
        name: str,
        actions: tuple[Hashable, ...],
        payoff_matrix: PayoffMatrix
    ):
        self.name=name
        self.actions=actions
        self.payoff_matrix= payoff_matrix

    def get_payoff(
        self,
        action_a: Hashable,
        action_b: Hashable
    ) -> tuple[float,float]:

        if action_a not in self.actions:
            raise ValueError(f"Invalid action: {action_a}")

        if action_b not in self.actions:
            raise ValueError(f"Invalid action: {action_b}")

        return self.payoff_matrix.calculate(
            action_a,
            action_b
        )