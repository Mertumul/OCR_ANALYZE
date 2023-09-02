import sys
import re
sys.path.append("../../")
from config import patterns


async def extract_patterns(text: str) -> dict:
    """
    Extracts sensitive data patterns from the given text using regular expressions.

    Args:
        text (str): The text to be analyzed for sensitive data patterns.

    Returns:
        dict: A dictionary containing extracted data for each pattern.
            The keys are pattern names, and the values are lists of matching data.
    """
    extracted_data = {}

    for pattern_name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_data[pattern_name] = matches

    return extracted_data
