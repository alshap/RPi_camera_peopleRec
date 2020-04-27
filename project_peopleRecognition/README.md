# People recognition

## Introduction

We will take code from examples to build the project on Python which find people amount on RPi camera and sends data to the Postgree database

## Database config

**config.py** file parses **database.ini** as database credentials. This was done for code convenience. In **main.py** this config is implemented in **postgre_insert** function.
```
params = config()
connection = psycopg2.connect(**params)
```

## How code works

