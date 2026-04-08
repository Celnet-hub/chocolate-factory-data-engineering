import pandas as pd
from db_conn import get_engine

def get_clean_data(data_frames: dict) -> dict:
    """
    Cleans and standardizes the extracted DataFrames.
    """
    print("Starting Data Transformation...")
    cleaned_data = {}

    for name, df in data_frames.items():
        print(f"Cleaning {name} table...")
        
        # Handle Duplicates
        initial_len = len(df)
        df = df.drop_duplicates()
        if len(df) < initial_len:
            print(f"  -> Dropped {initial_len - len(df)} duplicate rows.")

        # Standardize Column Names
        # Convert all column names to lowercase and replace spaces with underscores
        df.columns = df.columns.str.lower().str.replace(' ', '_')

        # Handle Missing Values
        missing_count = df.isna().sum().sum()
        if missing_count > 0:
            df = df.dropna()
            print(f"  -> Dropped rows containing missing values (Total missing: {missing_count}).")

        cleaned_data[name] = df

    # Standardize Specific Formats - dates
    print("Standardizing date formats...")
    if 'calendar' in cleaned_data and 'date' in cleaned_data['calendar'].columns:
        cleaned_data['calendar']['date'] = pd.to_datetime(cleaned_data['calendar']['date'])

    if 'customers' in cleaned_data and 'join_date' in cleaned_data['customers'].columns:
        cleaned_data['customers']['join_date'] = pd.to_datetime(cleaned_data['customers']['join_date'])
    
    if 'sales' in cleaned_data and 'order_date' in cleaned_data['sales'].columns:
        cleaned_data['sales']['order_date'] = pd.to_datetime(cleaned_data['sales']['order_date'])
    
    # verify
    for name, df in cleaned_data.items():
        print(df.info())

    print("Data Transformation complete!")
    return cleaned_data