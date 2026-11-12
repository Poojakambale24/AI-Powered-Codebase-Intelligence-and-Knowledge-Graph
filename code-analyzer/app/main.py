from fastapi import FastAPI
app = FastAPI(title="Graphence Code Analyzer", version="0.1.0")
@app.get("/health")
def health():
    return {"status": "ok", "service": "graphence-code-analyzer"}
@app.get("/")
def root():
    return {"message": "Graphence analyzer starter", "next_milestone": "repository scanning and Tree-sitter parsing"}
