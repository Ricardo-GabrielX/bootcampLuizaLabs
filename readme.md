# Bootcamp Backend com Python - LuizaLabs 🐍🚀

Repositório dedicado ao versionamento dos desafios, exercícios e projetos práticos desenvolvidos durante o bootcamp **Back-end com Python**, oferecido pela LuizaLab em parceria com a DIO.

---

## 🎯 Objetivo
Organizar e documentar minha evolução na construção de aplicações modernas com Python, consolidando conceitos de desenvolvimento backend assíncrono, APIs.

## 🛠️ Tecnologias Utilizadas
* **Python 3.14+**
* **Poetry** (Gerenciamento de dependências e ambientes virtuais)
* **FastAPI** (Framework para APIs de alta performance)
* **Uvicorn** (Servidor ASGI)
* **SQlite** (local)
* **SQlite Viewer** (Extensão do VsCode pra visualizar banco de dados)




## 📂 Estrutura de Atividades
* **api_conceitos_fundamentais/**: Conceitos básicos de APIs e tipos, Rest, RESTful, GraphQL.
* **FundamentosDePython&Lógica/**: Orientações básicas de python, como python funciona e suas características e exercícios práticos para treinar.
* **apis_assincronas_fastapi/dio-blog**: Desenvolvimento de uma API de Blog utilizando FastAPI, explorando rotas, schemas e injeção de dependência.
* **banco de dados**: Trabalhando conceitos de queries em banco de dados com python, como fazer conexões do python com SQLite, como tratar dados em retornos, maneiras de evitar injeção SQL(boas práticas com SQL) e como lidar com gerenciamento de trasações(roolback e commit).


---

## 🚀 Como executar os projetos

### Pré-requisitos
Certifique-se de ter o **Python** e o **Poetry** instalados e configurados nas suas variáveis de ambiente (PATH).

```bash
# 1. Clone o repositório
git clone [https://github.com/Ricardo-GabrielX/bootcampLuizaLabs.git](https://github.com/Ricardo-GabrielX/bootcampLuizaLabs.git)

# 2. Navegue até a pasta do projeto desejado
cd bootcampLuizaLabs/apis_assincronas_fastapi/dio-blog

# 3. Instale as dependências configuradas no pyproject.toml
poetry install

# 4. Ative o ambiente virtual do projeto
poetry shell

# 5. Execute o servidor de desenvolvimento
# Substitua 'main:app' pelo arquivo principal do seu projeto
uvicorn main:app --reload