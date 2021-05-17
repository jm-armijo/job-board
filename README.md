# Sidekicker Coding Challenge

## Setup
* Install [Docker](https://docs.docker.com/get-started/)
* Build: `docker-compose build`
* Run: `docker-compose up`
* Execute tasks: `docker-compose exec <container_name> <cmd>`. 
  * e.g. `docker-compose exec coding-challenge-backend php artisan migrate`

To insert data into the databse, do:

```
cd csv_parser
python parser.py 'jobs.csv'
```

## Development
* React frontend: http://localhost
* Lumen backend: http://localhost:8000
