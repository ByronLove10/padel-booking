from fastapi import FastAPI

app = FastAPI(title="Padel Booking API")

@app.get("/health")
def health_check():
    return {"status": "ok"}
