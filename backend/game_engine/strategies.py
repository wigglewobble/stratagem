from typing import Hashable
import random

class Strategy:
    def choose_action(self)->Hashable:
        raise NotImplementedError(
            "Each strategy must implement choose_action()"
        )

class AlwaysCooperate(Strategy):
    def choose_action(self,opponent_last_action=None)->str:
        return "cooperate"

class AlwaysDefect(Strategy):
    def choose_action(self,opponent_last_action=None)->str:
        return "defect"

class RandomStrategy(Strategy):
    def choose_action(self,opponent_last_action=None)->str:
        return random.choice(["cooperate","defect"])

class TitForTat(Strategy):
    def choose_action(self,opponent_last_action=None)-> str: 
        if opponent_last_action is None:
            return "cooperate"
        return opponent_last_action