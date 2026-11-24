from fastapi import FastAPI, HTTPException
from pydantic import BaseModel,Field

from game_engine.payoff import PayoffMatrix
from game_engine.game import Game
from game_engine.strategies import(
    AlwaysCooperate,
    AlwaysDefect,
    RandomStrategy,
    TitForTat,
)
from game_engine.simulation import run_simulation
from game_engine.statistics import calculate_statistics

app=FastAPI(
    title="Stratagem API",
    description="Backend API for the Stratagem Game Theory Simulator",
    version="0.1.0",
)

class SimulationRequest(BaseModel):
    strategy_a:str
    strategy_b:str
    rounds:int =Field(gt=0,le=10000)

@app.get("/")
def root():
    return {
        "message":"Welcome to Stratagem",
        "status":"running",
    }

@app.get("/health")
def health_check():
    return {
        "status":"healthy",
    }

@app.post("/simulate")
def simulate(request: SimulationRequest):
    payoff_matrix=PayoffMatrix({
        ("cooperate","cooperate"):(3,3),
        ("cooperate","defect"):(0,5),
        ("defect","cooperate"):(5,0),
        ("defect","defect"):(1,1),
    })
    game=Game(
        name="Prisoner's Dilemma",
        actions=("cooperate","defect"),
        payoff_matrix=payoff_matrix,
    )
    strategies={
        "cooperate":AlwaysCooperate(),
        "defect":AlwaysDefect(),
        "random":RandomStrategy(),
        "tit_for_tat":TitForTat(),
    }
    strategy_a=strategies.get(request.strategy_a)
    strategy_b=strategies.get(request.strategy_b)

    if strategy_a is None or strategy_b is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid strategy. Use cooperate, defect, or random."
        )
    result=run_simulation(
        game,
        strategy_a,
        strategy_b,
        request.rounds,
    )
    statistics=calculate_statistics(result)

    return {
        "game": game.name,
        "strategy_a":request.strategy_a,
        "strategy_b":request.strategy_b,
        "simulation":result,
        "statistics":statistics,
    }
