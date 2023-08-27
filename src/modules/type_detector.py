import sys

sys.path.append("../../")
import re

from config import patterns


async def extract_patterns(text):
    extracted_data = {}

    for pattern_name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_data[pattern_name] = matches

    return extracted_data
