from extract import extract_raw_data
from transform import transform_data, clean_transaction

# Extract data
raw_data = extract_raw_data('data/raw_transactions.csv')

# Test cleaning one transaction
print("=== Testing single transaction ===")
first_transaction = raw_data[0]
cleaned = clean_transaction(first_transaction)
print(f"Original: {first_transaction}")
print(f"Cleaned: {cleaned}")
print()

# Transform all data
print("=== Transforming all data ===")
valid, invalid = transform_data(raw_data)

print(f"\nValid transactions ({len(valid)}):")
for t in valid:
    print(f"  {t['transaction_id']}: {t['client_name']} - ${t['amount']}")

print(f"\nInvalid transactions ({len(invalid)}):")
for t in invalid:
    print(f"  {t['transaction_id']}: {t['client_name']} - {t['reason_invalid']}")