# Criar o ambiente virtual
venv: clean_venv
	virtualenv venv

# Instalar as dependências
install: venv
	. venv/bin/activate && pip install -r requirements.txt

# Iniciar o servidor
run: venv
	. venv/bin/activate && uvicorn main:app --reload

# Limpar o ambiente virtual
clean_venv:
	rm -rf venv



