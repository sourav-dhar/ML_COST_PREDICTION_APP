import yaml
import os,sys
import pandas as pd

def write_schema_yaml(csv_file):
    df = pd.read_csv(csv_file)
    
    num_cols = len(df.columns)
    column_names = df.columns.tolist()
    column_dtypes = df.dtypes.astype(str).tolist()
    
    #Create schema Dictionary
    schema = {
        "filename": os.path.basename(csv_file),
        "NumberOfColumns": num_cols,
        "ColumnNames": dict(zip(column_names,column_dtypes))
    }
    
    #Write schema to schema.yaml file
    
    ROOT_DIR = os.getcwd()
    SCHEMA_FILE_PATH = os.path.join(ROOT_DIR, "config", "schema.yaml")
    
    with open(SCHEMA_FILE_PATH, "w") as file:
        yaml.dump(schema, file)
