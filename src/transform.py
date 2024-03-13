import pandas as pd

class Transformer:
    def __init__():
        pass

    def transform(self, extract_transformed_df):
        transformed_df = extract_transformed_df.copy()

        # Converting Timestamps to DateTime
        transformed_df['block_timestamp'] = pd.to_datetime(transformed_df['block_timestamp'])

        # Aggregating Data to know the total amount
        aggregated_data = transformed_df.groupby('sender')['amount'].sum().reset_index()

        # Filtering only successfull Data
        filtered_data = transformed_df[transformed_df['success'] == True]

        # Extracting relevant Columns
        selected_columns = transformed_df[['id', 'block_timestamp', 'amount', 'sender', 'to_addr']]

        # Adding a New Column to know transaction limits
        transformed_df['transaction_size'] = transformed_df['gas_limit'] * transformed_df['gas_price']

        # Converting Hex values to Decimal
        transformed_df['epoch_num'] = transformed_df['epoch_num'].apply(lambda x: int(x, 16) if pd.notnull(x) else x)

        # Data Type Conversion of amount column
        transformed_df['amount'] = transformed_df['amount'].astype(float)

        # Remove Unnecessary Columns
        transformed_df.drop(['signature', 'version'], axis=1, inplace=True)

        # Combining all transformations as needed
        result_transformed_df = pd.DataFrame({
            'Aggregated_Amount': aggregated_data['amount'],
            'Filtered_Successful_Transactions': filtered_data['id'],
            'Transaction_Size': transformed_df['transaction_size'],
            'Epoch_Num': transformed_df['epoch_num'],
            'Converted_Amount': transformed_df['amount'],
            'Other_Columns': transformed_df['block_number'],  # Add other columns as needed
        })

        return result_transformed_df
