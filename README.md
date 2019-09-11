# cv-base
Sistema Web para arquivar currículos


## Requisitos
- python 3.6
- pip
- virtualenvwrapper (recomendado)
- docker (opcional)

## todo
lorem ipsum

### Usando docker-compose
Caso seja executado usando docker, copiar o arquivo `.env.example` para `.env` e ajustar conforme necessário.

```sh
cp .env.example .env
```

Na primeira execução o banco de dados será criado, para iniciar o container do banco em plano de fundo:
```sh
docker-compose up -d db
```

Executar as migrações:
```sh
docker-compose run app python manage.py migrate
```

Criar um novo superusuário:
```sh
docker-compose run app python manage.py createsuperuser
```

Após a primeira execução do banco e aplicar as migrações é possivel inicar a aplicação usando:
```sh
docker-compose up
```
