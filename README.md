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

### Load data

These are manual steps for now:

```
docker cp t_jobs.csv coding-challenge-db:/tmp
docker cp t_applicants.csv coding-challenge-db:/tmp
```

```
mysql --host=localhost --user=root --password=your_mysql_root_password
CREATE DATABASE jobs_board;
USE JOBS_BOARD;

create table jobs (title VARCHAR(100), description VARCHAR(200), location VARCHAR(100), date DATE);
create table applicants (id INTEGER, applicant VARCHAR(100));

LOAD DATA LOCAL INFILE '/tmp/t_jobs.csv' into table jobs FIELDS TERMINATED BY ',' ENCLOSED BY '"';
LOAD DATA LOCAL INFILE '/tmp/t_applicants.csv' into table applicants FIELDS TERMINATED BY ',' ENCLOSED BY '"';
```

## Future work:
- Have a user with less privileges (instead of using root)
- Remove passwords from the repository
- Create primary/foreign keys and indexes in tables
- When parsing, beware of commas withing the values (Ex: location: "Docklands, Melbourne")
- Tune the size of each column to avoid wasting space: consider using other data types perhaps.

## Development
* React frontend: http://localhost
* Lumen backend: http://localhost:8000
