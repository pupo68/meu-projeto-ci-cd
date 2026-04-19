from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "message": "API CI/CD funcional"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}
