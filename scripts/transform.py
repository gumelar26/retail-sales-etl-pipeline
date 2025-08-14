def transform_data(products_df):
    products_df['currency'] = products_df['price'].str[:2]
    products_df['price'] = products_df['price'].str[3:].astype(int)
    
    return products_df.info()