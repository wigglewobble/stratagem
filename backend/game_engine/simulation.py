from game_engine.game import Game
from game_engine.strategies import Strategy

def run_simulation(
    game: Game,
    strategy_a: Strategy,
    strategy_b: Strategy,
    rounds: int
)->dict:
    if rounds <= 0:
        raise ValueError("Rounds must be greater than zero")
    score_a=0
    score_b=0
    history=[]
    last_action_a=None
    last_action_b=None
    for round_number in range(1,rounds+1):
        action_a=strategy_a.choose_action(last_action_b)
        action_b=strategy_b.choose_action(last_action_a)

        payoff_a,payoff_b=game.get_payoff(
            action_a,
            action_b
        )
        score_a+=payoff_a
        score_b+=payoff_b

        history.append({
            "round": round_number,
            "action_a": action_a,
            "action_b": action_b,
            "payoff_a": payoff_a,
            "payoff_b": payoff_b,
        })
        last_action_a=action_a
        last_action_b=action_b
    return{
        "rounds": rounds,
        "score_a": score_a,
        "score_b": score_b,
        "history": history,
    }