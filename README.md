# SGRH Flask com PostgreSQL

## Requisitos
- Python 3.9+
- pip
- PostgreSQL

## Instalação
1. Clone o repositório.
2. Crie o ambiente virtual e instale as dependências:
## pip install -r requirements.txt
3. Configure o banco de dados PostgreSQL:
- Crie um banco de dados e usuário.
- Defina as variáveis de ambiente ou edite `app.py` com as credenciais.
4. Aplicar migrações:
## flask db upgrade


## Execução
```bash
flask run
```
## Rotas Principais
/login

/register

/dashboard

/pessoa (CRUD para Pessoa)

/profissao (CRUD para Profissão/Cargo)

/folha (CRUD para Folha de Pagamento)

/capacitacao (CRUD para Capacitação)


---

### **10. Execução do Projeto**
```bash
# Ative o ambiente virtual
source venv/bin/activate

# Execute a aplicação
flask run

# Acesse o aplicativo em http://localhost:5000

