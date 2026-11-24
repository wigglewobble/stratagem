from fastapi import FastAPI
app=FastAPI(
    title="Stratagem API",
    description="Backend API for the Stratagem Game Theory Simulator",
    version="0.1.0",
)
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