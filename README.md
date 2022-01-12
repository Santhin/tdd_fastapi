# TDD FASTAPI example

## Environment Variables

| Variable Name     | Suggested development value | Description        |
| ----------------- | --------------------------- | ------------------ |
| ENVIRONMENT       | dev                         | Deployment stage   |
| TESTING           | 0                           | Testing flag       |
| POSTGRES_USER     | root                        | Postgres user name |
| POSTGRES_PASSWORD | password                    | Postgres password  |

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
POSTGRES_USER=root
POSTGRES_PASSWORD=password
```

## Usage <a name = "usage"></a>

Local

```
make build
```

Tests

```
make tests
```

### Aerich

Initialize the config file and migrations location:

```
make aeirich init
make aeirich init-db
```
