from typing import Hashable
import random

class Strategy:
    def choose_action(self)->Hashable:
        raise NotImplementedError(
            "Each strategy must implement choose_action()"
        )

class AlwaysCooperate(Strategy):
    def choose_action(self)->str:
        return "cooperate"

class AlwaysDefect(Strategy):
    def choose_action(self)->str:
        return "defect"

class RandomStrategy(Strategy):
    def choose_action(self)->str:
        return random.choice(["cooperate","defect"])