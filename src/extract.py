import csv
import logging

logging.basicConfig(level=logging.INFO)

def extract_raw_data(file_path):
    """Extract raw transaction data from CSV."""
    data = []
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                data.append(row)
        logging.info(f"Extracted {len(data)} transactions from {file_path}")
        return data
    except FileNotFoundError:
        logging.error(f"File not found: {file_path}")
        raise
    except Exception as e:
        logging.error(f"Error extracting data: {e}")
        raise
        