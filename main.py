from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "online", "message": "API CI/CD funcional"}

@app.get("/health")
def health_check():
    return {"status": "healthy"}

@app.get("/soma")
def calculate_sum(a: int, b: int):
    return {"resultado": a + b}

@app.get("/items/{item_id}")
def read_item(item_id: int):
    return {"item_id": item_id, "category": "generic" if item_id < 100 else "premium"}

@app.get("/reverse")
def reverse_text(texto: str):
    return {"original": texto, "invertido": texto[::-1]}
