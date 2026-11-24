import pytest
from game_engine.payoff import PayoffMatrix
from game_engine.game import Game
@pytest.fixture
def prisoners_dilemma():
    payoffs={
        ("cooperate","cooperate"):(3,3),
        ("cooperate","defect"):(0,5),
        ("defect","cooperate"):(5,0),
        ("defect","defect"):(1,1),
    }
    return PayoffMatrix(payoffs)

def test_mutual_cooperation(prisoners_dilemma):
    result=prisoners_dilemma.calculate(
        "cooperate","cooperate"
    )
    assert result == (3,3)

def test_cooperation_vs_defect(prisoners_dilemma):
    result=prisoners_dilemma.calculate(
        "cooperate","defect"
    )
    assert result == (0,5)

def test_invalid_action(prisoners_dilemma):
    with pytest.raises(ValueError):
        prisoners_dilemma.calculate(
            "Invalid","defect"
        )

@pytest.fixture
def prisoners_dilemma_game(prisoners_dilemma):
    return Game(
        name="Prisoner's Dilemma",
        actions=("cooperate","defect"),
        payoff_matrix=prisoners_dilemma
    )

def test_game_returns_payoff(prisoners_dilemma_game):
    result=prisoners_dilemma_game.get_payoff(
        "cooperate",
        "defect"
    )
    assert result == (0,5)

def test_game_rejects_invalid_action(prisoners_dilemma_game):
    with pytest.raises(ValueError):
        prisoners_dilemma_game.get_payoff(
            "attack",
            "defect"
        )

from game_engine.strategies import (
    AlwaysCooperate,
    AlwaysDefect,
    RandomStrategy,
)

def test_always_cooperate():
    strategy=AlwaysCooperate()
    assert strategy.choose_action()=="cooperate"

def test_always_defect():
    strategy=AlwaysDefect()
    assert strategy.choose_action()=="defect"

def test_random_strategy():
    strategy=RandomStrategy()
    for _ in range(100):
        action=strategy.choose_action()
        assert action in ("cooperate","defect")