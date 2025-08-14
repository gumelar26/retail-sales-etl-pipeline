# from config.setting import PRODUCTS_PATH, USERS_PATH, TRANSACTIONS_PATH, OUTPUT_PATH
import config.setting as cs
from scripts.extract import extract_csv, extract_json
from scripts.transform import transform_data
from scripts.load import save_to_csv

# Extract
products_df = extract_csv(PRODUCTS_PATH)
transactions_df = extract_csv(TRANSACTIONS_PATH)
users_df = extract_json(USERS_PATH)

# Transform
final_df = transform_data(products_df, transactions_df, users_df)

# Load
save_to_csv(final_df, OUTPUT_PATH)
print(f"ETL selesai! file disimpan di {OUTPUT_PATH}")