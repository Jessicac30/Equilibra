# Equilibra
Serviço que seleciona frases motivacionais

# Instalação
- Clone do projeto

```ruby
git clone [https://github.com/](https://github.com/Jessicac30/Equilibra.git)
``` 
- Iniciar virtual venv
  
``` ruby
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
```
ou 

``` ruby
make venv
```

# Instalar Dependências
  
``` ruby
pip3 install -r requirements.txt
```
ou

``` ruby
make install
```
# Executar aplicação
- Na porta http://127.0.0.1:8000
  
``` ruby
uvicorn main:app --reload
```
ou
``` ruby
make run 
```

# No windows

## Instalar pacote pip
``` ruby
python -m pip install --upgrade pip --user
```

## Instalar as dependências
``` ruby
pip install uvicorn fastapi --user
```
e
``` ruby
pip install fastapi pydantic --user
```
## Executar aplicação
- Na porta http://127.0.0.1:8000

``` ruby
python -m uvicorn main:app --reload
```

