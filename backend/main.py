from fastapi import FastAPI

app = FastAPI(title="AI Research Assistant")

@app.get("/")
def root():
    return {"message": "Backend is running 🚀"}

@app.post("/query")
def query_paper(query: str):
    # Week 2 we'll add real agents
    return {"query": query, "response": "This will be handled by agents soon"}
