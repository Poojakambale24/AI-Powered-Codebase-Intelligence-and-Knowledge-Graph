# Processing Workflow
## Code input
1. Validate Git URL or ZIP and resource limits.
2. Clone or safely extract into temporary storage.
3. Exclude generated folders, binaries and secrets.
4. Detect languages and parse source using Tree-sitter.
5. Extract symbols, imports, calls, routes and source locations.
6. Create AST-aware chunks.
7. Generate embeddings and store chunks/vectors in pgvector.
8. Create graph nodes and relationships in Neo4j.

## Documentation input
1. Validate PDF, DOCX, TXT or Markdown.
2. Extract text; OCR scanned documents if needed.
3. Preserve filename, page, heading and section metadata.
4. Split by document structure and token limits.
5. Embed and store chunks in pgvector.

## RAG question answering
Embed question -> retrieve relevant chunks -> optionally retrieve Neo4j context -> assemble grounded context -> call pretrained LLM -> answer with source references.

RAG is not model training. Fine-tuning is optional future work.
