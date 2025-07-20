from src.etl.extract import extract_data
from src.etl.transform import transform_data
from src.etl.load import load_to_mongo

if __name__ == '__main__':
    data = extract_data()
    clean_data = transform_data(data)
    load_to_mongo(clean_data)

