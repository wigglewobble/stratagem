from typing import Hashable

class PayoffMatrix:
    def __init__(
        self,
        payoffs: dict[
            tuple[Hashable,Hashable],
            tuple[float,float]
        ]
    ):
        self.payoffs=payoffs

    def calculate(
        self,
        action_a: Hashable,
        action_b: Hashable
    )->tuple[float,float]:
        
        outcome=(action_a,action_b)
        if outcome not in self.payoffs:
            raise ValueError(
                f"Invalid action combination: {outcome}"
            )

        return self.payoffs[outcome]