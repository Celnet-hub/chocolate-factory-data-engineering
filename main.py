from extract_load_raw import start_process

if __name__ == "__main__":
    print("--- Starting ETL Pipeline ---")
    
    # Extract
    raw_data = start_process()
    
    # Transform
    # clean_data = clean_data(raw_data)
    
    print("Pipeline Execution Complete")