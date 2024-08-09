import os
import json
import logging
from typing import List, Optional

logging.basicConfig(level=logging.INFO)

def get_healthcheck_response():
    return "Everything is fine!"

def load_doughnuts() -> List[dict]:
    json_data_path = os.getenv('JSON_DATA_PATH', '../data/doughnuts.json')
    try:
        with open(json_data_path, 'r') as f:
            return json.load(f)['doughnut_data']
    except FileNotFoundError:
        logging.error(f"File not found: {json_data_path}")
        return []
    except json.JSONDecodeError:
        logging.error("JSON Decode Error - check the formatting of the JSON file.")
        return []

def filter_doughnuts(max_calories: Optional[int], contains_nuts: Optional[bool]) -> List[dict]:
    doughnuts = load_doughnuts()
    filtered_doughnuts = []
    for doughnut in doughnuts:
        if (max_calories is None or doughnut.get('calories', 0) <= max_calories) and \
           (contains_nuts is None or doughnut.get('contains_nuts', False) == contains_nuts):
            filtered_doughnuts.append(doughnut)
    return filtered_doughnuts
