# API Doação de Livros

Essa é uma API simples feita com Flask e SQLite3 para fins de estudos da escola Vai na Web, ela permite cadastrar e listar livros doados.

## Como rodar o projeto

1. Faça um clone do repositório:
```bash
git clone <URL_DO_REPOSITÓRIO>
cd nome-do-projeto
```

2. Crie um ambiente virtual (obrigatório):
```bash
python -m venv venv
source venv/Scripts/activate
```
3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Inicie o servidor:
```bash
python app.py
```
> A api está disponível em http: http://127.0.0.1:5000/

## Endpoints

### POST /doar

Endpoint para cadastrar um novo livro

**Formato de envio dos dados**

```json
{
    "titulo":"50 Tons de dívida",
    "categoria":"Finanças",
    "autor":"Fernanda Polia",
    "imagem_url":"http://exemplo.com
}
```

**Resposta 201 (Created)**:
```json
{
    "mensagem":"Livros cadastrado com sucesso"
}
```
---

### GET /livros

Retorna todos os livros cadastrados em nossa API.

**Resposta (200)**:
```json
{
    "titulo":"50 Tons de dívida",
    "categoria":"Finanças",
    "autor":"Fernando Polia",
    "image_url":"https://exemplo.com"
}
```

---






