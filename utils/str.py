import json
import logging 


def read_json(file_path: str) -> dict:
    """reads a json file and returns it as a dict.
    Args:

        file_path (str): _description_
    Returns:
        dict: _description_
    """

    try:
        with open(file_path, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        logging.error("File not found: %s" % file_path)
    except Exception as e:
        logging.error("Exception: %s" % e)