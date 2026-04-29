from extract.extract_data import extract
#from transform.transform_data import transform
from load.load_data import load

def run_pipeline():
    df=extract()
    #df=transform(df)
    load(df)

if __name__== "__main__":
    run_pipeline()