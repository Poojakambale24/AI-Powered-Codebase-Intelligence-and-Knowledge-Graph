# Graphence
AI-Powered Code Understanding & Knowledge Graph

Initial project scaffold. Current stage: planning and starter setup; full processing features are not implemented yet.

## Inputs
1. GitHub repository URL
2. ZIP project folder
3. Existing documentation (PDF, DOCX, TXT, Markdown)

## Planned stack
- Frontend: React + TypeScript + Vite
- Main API: NestJS
- Analyzer: Python + FastAPI + Tree-sitter
- Graph: Neo4j
- Database/vector search: PostgreSQL + pgvector
- RAG: LangChain + pretrained LLM
- Workflow: LangGraph

## Run locally
Start databases: `docker compose up -d`
Frontend: `cd frontend && npm install && npm run dev`
Backend: `cd backend && npm install && npm run start:dev`
Analyzer (PowerShell):
`cd code-analyzer`
`python -m venv .venv`
`.\.venv\Scripts\Activate.ps1`
`pip install -r requirements.txt`
`uvicorn app.main:app --reload --port 8000`

Local URLs: frontend http://localhost:5173, backend http://localhost:3000,
analyzer http://localhost:8000/docs, Neo4j http://localhost:7474.

## Push to your GitHub repository
```bash
git init
git add .
git commit -m "Initial Graphence project structure"
git branch -M main
git remote add origin https://github.com/Poojakambale24/AI-Powered-Codebase-Intelligence-and-Knowledge-Graph.git
git push -u origin main
```
If `origin` already exists, use `git remote set-url origin <REPOSITORY_URL>`.

Security: never execute uploaded code; exclude secrets; validate Git URLs and ZIP paths; apply file and resource limits.
