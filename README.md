# API CI/CD - Projeto Acadêmico

Este projeto demonstra um pipeline de DevOps completo com Python, FastAPI, GitHub Actions e Docker.

## Como rodar localmente (Docker)
1. Build da imagem: `docker build -t api-cicd .`
2. Run do container: `docker run -d -p 8000:8000 --name api-instance api-cicd`

## Testes
Rode `pytest` no terminal.
