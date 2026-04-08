import kagglehub
import pandas as pd
from pathlib import Path
from db_conn import get_engine


def get_data() -> dict:
    output_dir = Path("./source_data")

    # Download the dataset
    print("Downloading dataset from Kaggle...")
    kagglehub.dataset_download(
        "ssssws/chocolate-sales-dataset-2023-2024",
        output_dir=str(output_dir),
        force_download=True
    )

    print("Loading files into DataFrames...")

    calendar = pd.read_csv(output_dir / "calendar.csv")
    customers = pd.read_csv(output_dir / "customers.csv")
    products = pd.read_csv(output_dir / "products.csv")
    sales = pd.read_csv(output_dir / "sales.csv")
    stores = pd.read_csv(output_dir / "stores.csv")

    # Log the metadata (row counts)
    print(f"Extraction successful!")
    print(f"Records loaded -> Customers: {len(customers)}, Calendar: {len(calendar)}, "
          f"Products: {len(products)}, Sales: {len(sales)}, Stores: {len(stores)}")

    # Return the actual DataFrames for the next pipeline stage
    return {
        "calendar": calendar,
        "customers": customers,
        "products": products,
        "sales": sales,
        "stores": stores,
    }


def load_data(df: dict) -> None:
    engine = get_engine()

    print("Staging data to db")
    # access dataframes
    calendar_df = df["calendar"]
    customers_df = df["customers"]
    products_df = df["products"]
    sales_df = df["sales"]
    stores_df = df["stores"]

    calendar_df.to_sql('calendar_raw', engine,
                       if_exists='replace', index=False)

    customers_df.to_sql('customers_raw', engine,
                        if_exists='replace', index=False)

    products_df.to_sql('products_raw', engine, schema='public',
                       if_exists='replace', index=False)

    sales_df.to_sql('sales_raw', engine, if_exists='replace', index=False)

    stores_df.to_sql('stores_raw', engine, if_exists='replace', index=False)

    print("Raw Data Staged successfully")


def start_process() -> dict:
    """Wrapper function to initiate the extraction."""
    data_frames = get_data()
    load_data(data_frames)
    return data_frames
