import logging
from datetime import datetime

def is_valid_amount(amount_str):
    """Check if amount is valid (positive number)."""
    try:
        amount = float(amount_str)
        return amount > 0
    except ValueError:
        return False
    
def is_valid_date(date_str):
    """Check if the date is in valid format (YYYY-MM-DD)."""
    try:
        datetime.strptime(date_str, '%Y-%m-%d')
        return True
    except ValueError:
        return False
    
def clean_transaction(transaction):
    """Clean and validate a single transaction."""
    cleaned = transaction.copy()
    # Convert amount to float
    try:
        cleaned['amount'] = float(transaction['amount'])
    except ValueError:
        cleaned['amount'] = None

    # Flag invalid records
    is_valid = (
        cleaned['amount'] is not None and 
        cleaned['amount'] > 0 and
        is_valid_date(transaction['transaction_date'])
    )
    cleaned['is_valid'] = is_valid
    cleaned['reason_invalid'] = None

    if not is_valid:
        if cleaned['amount'] is None:
            cleaned['reason_invalid'] = 'Invalid amount format'
        elif cleaned['amount'] <= 0:
            cleaned['reason_invalid'] = 'Amount must be positive'
        elif not is_valid_date(transaction['transaction_date']):
            cleaned['reason_invalid'] = 'Invalid date format'

    return cleaned 

def transform_data(raw_data):
    """Transform raw data: clean, validate, separate valid/invalid."""
    valid_transactions = []
    invalid_transactions = []

    for transaction in raw_data:
        cleaned = clean_transaction(transaction)
        if cleaned['is_valid']:
            valid_transactions.append(cleaned)
        else:
            invalid_transactions.append(cleaned)

    logging.info(f"Valid: {len(valid_transactions)}, Invalid: {len(invalid_transactions)}")

    return valid_transactions, invalid_transactions
