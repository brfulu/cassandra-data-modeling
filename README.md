# cassandra-data-modeling

### Udacity Data Engineer Nanodegree project
An imaginery startup called Sparkify wants to analyze the data they've been collecting on songs and user activity on their new music streaming app. The analytics team is particularly interested in understanding what songs users are listening to. Currently, they don't have an easy way to query their data, which resides in a directory of JSON logs on user activity on the app, as well as a directory with JSON metadata on the songs in their app.

They'd like a data engineer to create a Postgres database with tables designed to optimize queries on song play analysis. The task is to create a star schema for Postgres and develop an ETL pipleine which will transfer the data from local files to the database.

### Requirements for running locally
- Python3 
- Docker
- Docker-Compose 

### Project structure explanation
```
postgres-data-modeling
│   README.md                 # Project description
│   docker-compose.yml        # Postgres container description   
│   requirements.txt          # Python dependencies
|
└───event_data                # The dataset partitioned by day
|   | ...
|                 
└───src                       # Source code
|   |               
│   └───notebooks             # Jupyter notebooks
│   |   │  music_app.ipynb    # Interactive notebook instead of python scripts
|   |   
|   └───scripts
|       |  process_events.py  # Collect records in one csv file
│       │  create_tables.py   # Schema creation script
|       |  etl.py             # ETL script
|       |  csql_queries.py    # Definition of all csql queries
```

### Instructions for running locally

Clone repository to local machine
```
https://github.com/brfulu/cassandra-data-modeling.git
```

Change directory to local repository
```
cd cassandra-data-modeling
```

Create python virtual environment
```
python3 -m venv venv             # create virtualenv
source venv/bin/activate         # activate virtualenv
pip install -r requirements.txt  # install requirements (this can take couple of minutes)
```

Start cassandra container
```
docker-compose up  # run this command in new terminal window or tab
```

Run scripts
```
cd src/
python -m scripts.process_events # collect events into one csv (event_datafile_new.csv)
python -m scripts.create_tables  # create database schema
python -m scripts.etl            # load data
```

Run everything inside jupyter notebook or check results
```
jupyter notebook  # launch jupyter notebook app

# The notebook interface will appear in a new browser window or tab.
# Navigate to src/notebooks/music_app.ipynb and run the code cells
```