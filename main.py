from extract_load_raw import start_process
from transform import get_clean_data

if __name__ == "__main__":
    print("--- Starting ETL Pipeline ---")
    
    # Extract
    raw_data = start_process()
    
    # Transform
    clean_data = get_clean_data(raw_data)
    
    print("Pipeline Execution Complete")