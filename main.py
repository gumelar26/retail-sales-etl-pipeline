from config.setting import PRODUCTS_PATH, USERS_PATH, TRANSACTIONS_PATH, OUTPUT_PATH
from scripts.extract import extract_csv, extract_json

# Extract
products_df = extract_csv(PRODUCTS_PATH)
transactions_df = extract_csv(TRANSACTIONS_PATH)
users_df = extract_json(USERS_PATH)

# Transform