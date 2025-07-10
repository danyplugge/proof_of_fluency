#TODO: create dependency loader functionality (package.json)
import pandas as pd
from sqlalchemy import create_engine, text

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
#TODO: optimize params
def load_data(source, table_name, sheet, columns, data_types, engine):
    """
    use pandas to read the xls input and save it as a new table to the postgres database
    
    Parameters:
    source(string): Const location of path, 
    table_name(string): name of table being created, 
    sheet(string): Name of sheet in xls file, 
    columns(List:string): Columns to read and write, 
    data_types(List:string): datatypes to write, 
    engine(string): enigne to read pandas from {xls ="xlrd", xslx= "openpyxl" }, 
    
    """
    print(f" loading {table_name}")
    data = pd.read_excel(source, sheet_name=sheet, usecols=columns, engine=engine)
    sql =  f"CREATE TABLE {table_name} ({", ".join([f"{columns} {data_types}" for columns, data_types in zip(columns, data_types)])}) "
    print(sql)
    engine = create_engine(get_connection_string()) 
    conn = None 
    try:
        with engine.connect() as conn:
            conn.execute(text(f"DROP TABLE IF EXISTS {table_name} CASCADE;"))
            print("Table dropped")
            conn.execute(text(sql))
            data.to_sql(table_name, con=conn, if_exists='replace',index=False)
        print(f"{table_name} created successfully.")
    except Exception as error:
        #TODO: better error handling
        print(f"An error occurred: {error}")
    finally:
        if conn is not None:
            conn.close()


def get_connection_string():
     """
    connection string builder
    
    Returns:
    String path link to access db
    """
     return f'postgresql://{const["db_user"]}:{const["db_password"]}@{const["db_host"]}:{const["db_port"]}/{const["db_name"]}'

def oews_raw():
    """
    Runner for creating the oes_raw table in postgres database
    
    """
    columns = ["AREA", "OCC_TITLE", "OCC_CODE", "H_MEAN", "A_MEAN", "TOT_EMP" ]
    data_types = ["VARCHAR(50)", "VARCHAR(100)", "VARCHAR(15)", "FLOAT", "FLOAT", "FLOAT"]
    load_data(const["oews_local"], "oews_raw", "state_M2024_dl", columns, data_types, "openpyxl")

def onet_skills():
    """
    Runner for creating the oes_raw table in postgres database
    
    """
    ## TODO:create function to handle special chars
    columns = ["ONETSOC_Code", "Title", "Element_Name", "Element_ID", "Data_Value"]
    data_types = ["VARCHAR(50)", "VARCHAR(100)", "VARCHAR(50)", "VARCHAR(20)", "FLOAT",]
    load_data(const["onet_local"], "onet_skills" , "Skills", columns, data_types, "xlrd")


if __name__ == "__main__":

    oews_raw()
    onet_skills()
