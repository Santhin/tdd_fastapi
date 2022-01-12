# TDD FASTAPI example

## Environment Variables

| Variable Name | Suggested development value | Description      |
| ------------- | --------------------------- | ---------------- |
| ENVIRONMENT   | dev                         | Deployment stage |
| TESTING       | 0                           | Testing flag     |

### How to create .env file

Create a .env file in the root of your project

```
touch .env # create a new .env file
vim .env # open the .env file in the vim
```

You can then add your environment variables like this:

```
ENVIRONMENT=dev
TESTING=0
```

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
