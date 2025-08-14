import pandas as pd

def transform_data(products_df, transactions_df, users_df):
    # Dataframe Product
    products_df['currency'] = products_df['price'].str[:2]
    products_df['price'] = products_df['price'].str[3:].astype(int)

    # Dataframe Transactions
    transactions_df['transaction_date'] = pd.to_datetime(transactions_df['transaction_date'], format='%d/%m/%Y').dt.strftime('%Y-%m-%d')

    # Dataframe Users
    users_df['email'] = users_df['email'].replace("", None)

    return