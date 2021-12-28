# TDD FASTAPI example

## Environment Variables
| Variable Name                    | Suggested development value        | Description
|----------------------------------|------------------------------------|------------
|STAGE                             | stage                              | Deployment stage
|TESTING                           | 0                                  | Testing flag 
|POSTGRES_USER                     | root                               | Postgres user name
|POSTGRES_PASSWORD                 | password                           | Postgres password


## Usage <a name = "usage"></a>


Local 
```
docker compose up --build
```
Tests
```
docker compose -f docker-compose.yml run tdd-services pytest -vv
```

### Aerich

Initialize the config file and migrations location:
```
docker compose -f docker-compose.yml run tdd-services aerich init -t app.db.TORTOISE_ORM
```


aerich init-db