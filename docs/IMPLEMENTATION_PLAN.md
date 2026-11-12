# Implementation Plan
1. Upload UI for GitHub, ZIP and documentation.
2. GitHub URL validation and safe cloning.
3. ZIP validation and safe extraction.
4. Document extraction.
5. File filtering and language detection.
6. Tree-sitter parsing for JavaScript/TypeScript first.
7. Extract symbols and relationships with line locations.
8. Code-aware and document chunking.
9. Embeddings and pgvector indexing.
10. Neo4j graph construction.
11. Hybrid retrieval and grounded RAG.
12. Documentation generation and impact analysis.
13. Tests, security, logging and deployment.

First MVP: one JS/TS repository -> scan -> parse -> chunk -> index -> graph -> one grounded Q&A.
