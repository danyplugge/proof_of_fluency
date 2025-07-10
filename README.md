# Proof of Fluency
### Overview
This project aims to demonstrate fluency in data handling and analysis by integrating data from the Occupational Employment and Wage Statistics (OEWS) and O*NET databases. The project involves setting up a PostgreSQL database, loading data, creating SQL views, and performing data analysis using Python and Pandas.

## How to run

#### Start up Docker Postgres Database 
to start up the database run the following commmands:
    docker-compose up -d

    docker exec -it proof_of_fluency-postgres-1 psql -U admin -d oews_onet

#### Load Data 
Run file load_data.py and both the oews_raw and onet_skills tables will be loaded into the database.

TODO: I am not importing the data from the public data site correctly.

TODO: create a dependencies file so you don't have to install the dependencies manually

#### Views
Run the view.sql in the database to generate the views, which defines two views that facilitate further analysis.

TODO: I was not able to make a runner for this so I created a data sample in analysis so that the notebook is runable. There is a read function as well to demonstrate how that would be done with a view.

#### Analysis
Run the Jupyter notebook (analysis.ipynb) to visualize the data and perform analysis. This notebook includes various visualizations and aggregations based on the created views.


# Assignment Params
### Practical Mini-Challenge: OEWS × O*NET “Proof of Fluency”


Total time box: ≤ 2 hours.  Stub or sketch anything that would push you over the limit; we’ll review choices live.



### Task Overview


1. DevOps (optional)

    - Spin up Postgres in Docker

    - docker-compose.yml (or skip → assume DB admin / admin)

2. Python → Postgres

    - Fetch two public data files and load them

    - load_data.py (readable, commented; need not run)

3. SQL fluency

    - Define two views that implement the matching rules below

    - views.sql

4. Pandas fluency

    - Read one of the views and do a non-trivial aggregation

    - analysis.py or analysis.ipynb


### Data Sources

OEWS by State – https://www.bls.gov/oes/tables.htm

O*NET Skills & Occupation files – https://www.onetcenter.org/database.html#individual-files



#### Detailed Instructions



1 · Set up Postgres (skip if short on time)


- Provide a minimal docker-compose.yml that launches Postgres ≥ 15 with database oews_onet and user admin:admin.

- If you skip, note it in your README—later tasks assume the database exists.




2 · Ingest data with Python

- Download one OEWS state table and the O*NET “Skills” (plus any helper O*NET occupation file you need for codes/titles).

- Create tables oews_raw and onet_skills (schemas are up to you).

- Bulk-load the data.  Emphasise clean structure and docstrings; runtime success is a bonus.




3 · Show SQL fluency — 
define two views


- Create a script views.sql that, when run, produces:


    1. vw_oews_avg_over_onet

        - For each 6-digit OEWS occ_code (e.g., 29-1141), compute wage metrics (e.g., a_mean, employment, etc.) by averaging across all O*NET SOC codes whose codes start with that 6-digit prefix (29-1141.00, 29-1141.01, …).

    2. vw_onet_closest_oews

        - For each O*NET SOC code (e.g., 29-1141.01), attach the single OEWS record whose 6-digit occ_code matches its prefix (29-1141). Return both the skills columns and the associated wage metrics.

Hints (no need to implement every column, just demonstrate that you have collected a couple of features by job category.

Use any functions/operators you like; clarity and correctness of matching logic matter more than syntax perfection.




4 · Pandas follow-up

- Read one of the views (vw_onet_closest_oews is fine) via pandas.read_sql.

- Perform a brief aggregation or visualization, e.g. average wage by major group, top 10 SOC codes by predicted wage, etc.

- A few comments interpreting the result are welcome.



Submission Checklist

      your-repo/

           ├── README.md # how to run / where you stubbed

           ├── docker-compose.yml   # (optional)

           ├── load_data.py

           ├── views.sql

           └── analysis.ipynb (or analysis.py)

Push to GitHub (public or private) and share the link.



#### Evaluation Matrix Dimension

What We Look For

1. Clarity

- Well-named files, docstrings, concise README.

- Python fundamentals

- Modular code; correct libraries (requests, pandas, sqlalchemy, etc.).

2. SQL expressiveness

- Views implement prefix-matching rules cleanly; readable CTEs or joins.

- Pandas proficiency

- Correct use of groupby, aggregation, or plotting.

3. Time awareness

- Sensible scoping—TODOs instead of rabbit holes.

4. Bonus

- Working Docker stack, tests, CI—but only if it fits the 2-hour window.

Remember: stubs or brief notes are perfectly fine where time runs out. We’ll walk through your approach together—have fun!

