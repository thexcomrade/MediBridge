from fastapi import FastAPI

app = FastAPI(
    title = "Medi Bridge AI",
    description="AI powered Unified Patient Medical Records",
    version = "1.0.0"
)

#api frst endpoints
@app.get("/")
def home():
    return {
        "message": "Welcome to MediBridge AI",
        "status": "Running",
        "version": "0.1.0"
            }

#health check endpoint
@app.get("/health")
def health_check():
    return {
        "message": "MediBridge AI is healthy",
        "status": "Running",
        "version": "0.1.0"
            }