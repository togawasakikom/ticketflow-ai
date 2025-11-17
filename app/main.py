from fastapi import FastAPI

app = FastAPI(title="TicketFlow AI")

@app.get("/")
def read_root():
    return {"message": "Welcome to TicketFlow AI"}
