#TODO: create dependency loader functionality (package.json)
import pandas as pd
import psycopg2

const = {
    ## TODO: find a better way to access this data in JSON- place holder is xlsx file in project folder
    "oews_source": "https://www.bls.gov/oes/tables.htm", ## state labor data for MD
    "oews_local": "./Data/oesm24st/state_M2024_dl.xlsx",
    "onet": "https://www.onetcenter.org/database.html#individual-files",
    "onet_local": "./Data/Skills.xls",
    ## TODO: put sensetive consts in protected folder and allow for enviromental differences
    "db_user": "admin",
    "db_password": "admin",
    "db_host": "localhost",
    "db_port": "5432",
    "db_name": "oews_onet",
}

def load_data(source, table_name, sheet, columns, data_types):
    data = pd.read_excel(source, sheet_name=sheet)
    #usecols=columns
    print(data.columns)

    sql =  f"CREATE TABLE {table_name} ({", ".join([f"{columns} {data_types}" for columns, data_types in zip(columns, data_types)])}) "
    try:
        conn = psycopg2.connect(get_connection_string())
        cur = conn.cursor()
        cur.execute(sql, data)
        conn.commit()
        cur.close()
        print("success")
    except (Exception, psycopg2.DatabaseError) as error:
        #TODO: better error handling
        print(error)
    finally:
        if conn is not None:
            conn.close()

def get_connection_string():
    return f'postgresql://{const["db_user"]}:{const["db_password"]}@{const["db_host"]}:{const["db_port"]}/{const["db_name"]}'


def oews_raw():
    columns = ["AREA", "OCC_TITLE", "H_MEAN", "A_MEAN" ]
    data_types = ["VARCHAR(50)", "VARCHAR(100)", "FLOAT", "FLOAT",]
    load_data(const["oews_local"], "oews_raw", "state_M2024_dl", columns, data_types)

def onet_skills():
    columns = ["O*NET-SOC Code", "Title", "Element Name", "Element ID", "Data Value"]
    data_types = ["VARCHAR(50)", "VARCHAR(100)", "VARCHAR(50)", "VARCHAR(20)" "FLOAT",]
    load_data(const["onet_local"], "onet_skills" , "Skills", columns, data_types)


if __name__ == "__main__":
    #TODO check for if the table exists and only run new tables. 
    #     functionality to update the table might also be wanted
    # oews_raw()
    onet_skills()
