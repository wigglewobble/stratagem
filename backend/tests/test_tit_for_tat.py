from game_engine.strategies import TitForTat

def test_tit_for_tat_cooperates_first():
    strategy=TitForTat()

    assert strategy.choose_action()=="cooperate"

def test_tit_for_tat_copies_opponent():
    strategy=TitForTat()

    assert strategy.choose_action("defect")=="defect"
    assert strategy.choose_action("cooperate")=="cooperate"