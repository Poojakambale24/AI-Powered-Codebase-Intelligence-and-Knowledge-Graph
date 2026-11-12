# Proposed Architecture
React + TypeScript frontend
  -> NestJS API (projects, uploads, jobs)
  -> Code ingestion: Git clone / ZIP -> filtering -> Tree-sitter/AST -> code chunks
  -> Document ingestion: PDF/DOCX/TXT/Markdown -> extraction -> structure-aware chunks
  -> Embedding generation
  -> PostgreSQL + pgvector (chunks and vectors)
  -> Neo4j (code entities and relationships)
  -> LangChain retrieval + pretrained LLM
  -> LangGraph orchestration
  -> answers, documentation, knowledge graph and impact analysis

LangGraph orchestrates AI workflows; Neo4j stores code relationships. They are different components.
