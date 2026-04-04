import kagglehub
import pandas as pd
from pathlib import Path
from sqlalchemy import create_engine


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


def load_data():
    pass

def start_process() -> dict:
    """Wrapper function to initiate the extraction."""
    data_frames = get_data()
    return data_frames
