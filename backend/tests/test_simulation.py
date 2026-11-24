import pytest
from game_engine.game import Game
from game_engine.payoff import PayoffMatrix
from game_engine.strategies import AlwaysCooperate, AlwaysDefect
from game_engine.simulation import run_simulation

@pytest.fixture
def prisoners_dilemma():
    matrix=PayoffMatrix({
        ("cooperate","cooperate"):(3,3),
        ("cooperate","defect"):(0,5),
        ("defect","cooperate"):(5,0),
        ("defect","defect"):(1,1),
    })
    return Game(
        name="Prisoner's Dilemma",
        actions=("cooperate","defect"),
        payoff_matrix=matrix,
    )

def test_simulation_scores(prisoners_dilemma):
    result=run_simulation(
        prisoners_dilemma,
        AlwaysCooperate(),
        AlwaysDefect(),
        10,
    )
    assert result["score_a"]==0
    assert result["score_b"]==50
    assert len(result["history"])==10

def test_simulation_records_rounds(prisoners_dilemma):
    result=run_simulation(
        prisoners_dilemma,
        AlwaysCooperate(),
        AlwaysDefect(),
        3,
    )
    first_round=result["history"][0]
    
    assert first_round["round"]==1
    assert first_round["action_a"]=="cooperate"
    assert first_round["action_b"]=="defect"
    assert first_round["payoff_a"]==0
    assert first_round["payoff_b"]==5

def test_simulation_rejects_zero_rounds(prisoners_dilemma):
    with pytest.raises(ValueError):
        run_simulation(
            prisoners_dilemma,
            AlwaysCooperate(),
            AlwaysDefect(),
            0,
        )