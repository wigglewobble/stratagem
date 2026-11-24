from game_engine.statistics import calculate_statistics
def test_calculate_statistics():
    result={
        "rounds":2,
        "score_a":5,
        "score_b":3,
        "history":[
            {
                "round":1,
                "payoff_a":5,
                "payoff_b":0,
            },
            {
                "round":2,
                "payoff_a":0,
                "payoff_b":3,
            },
        ],
    }
    stats=calculate_statistics(result)
    
    assert stats["average_score_a"]==2.5
    assert stats["average_score_b"]==1.5
    assert stats["wins_a"]==1
    assert stats["wins_b"]==1
    assert stats["ties"]==0
    assert stats["win_rate_a"]==50
    assert stats["win_rate_b"]==50