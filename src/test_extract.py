from extract import extract_raw_data

# Testing the function
transactions = extract_raw_data('data/raw_transactions.csv')
print(transactions[0]) # Prints the first transaction
print(f"Total: {len(transactions)} transactions") 