import pandas as pd

def transform_data(products_df, transactions_df):
    # Dataframe Product
    products_df['currency'] = products_df['price'].str[:2]
    products_df['price'] = products_df['price'].str[3:].astype(int)

    # Dataframe Transactions
    transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    return transactions_df