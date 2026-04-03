import json
import os
import logging

from .logger_config import setup_logger

setup_logger()

DEFAULT_DATA = {
    "students": [],
    "courses": [],
    "enrollments": []
}

DATA_FILE = "data/gradebook.json"


def load_data(path=DATA_FILE):
    """Load data from JSON file."""
    try:
        with open(path, "r", encoding="utf-8") as file:
            data = json.load(file)
            logging.info("Data loaded successfully from %s", path)
            return data

    except FileNotFoundError:
        logging.info("Data file not found. Starting with empty gradebook.")
        return DEFAULT_DATA.copy()

    except json.JSONDecodeError:
        logging.error("Invalid JSON found in %s", path)
        print("Error: gradebook.json contains invalid JSON. Starting with empty data.")
        return DEFAULT_DATA.copy()

    except Exception as error:
        logging.error("Unexpected error while loading data: %s", error)
        print(f"Error loading data: {error}")
        return DEFAULT_DATA.copy()


def save_data(data, path=DATA_FILE):
    """Save data to JSON file."""
    try:
        folder = os.path.dirname(path)
        if folder:
            os.makedirs(folder, exist_ok=True)

        with open(path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=4)

        logging.info("Data saved successfully to %s", path)

    except Exception as error:
        logging.error("Error saving data: %s", error)
        print(f"Error saving data: {error}")