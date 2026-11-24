def calculate_statistics(result: dict)->dict:
    history= result["history"]
    rounds= result["rounds"]

    wins_a=0
    wins_b=0
    ties=0

    for round_data in history:
        payoff_a=round_data["payoff_a"]
        payoff_b=round_data["payoff_b"]

        if payoff_a>payoff_b:
            wins_a+=1
        elif payoff_b>payoff_a:
            wins_b+=1
        else:
            ties+=1

    return {
        "average_score_a": result["score_a"]/rounds,
        "average_score_b": result["score_b"]/rounds,
        "wins_a": wins_a,
        "wins_b": wins_b,
        "ties":ties,
        "win_rate_a": wins_a/rounds * 100,
        "win_rate_b":wins_b/rounds * 100,
    }