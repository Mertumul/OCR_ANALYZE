import re

async def extract_patterns(text):
    patterns = {
        "PHONE_NUMBER": '^(\+\d{1,2}\s)?\(?\d{3}\)?[\s.-]\d{3}[\s.-]\d{4}$',  # Başka bir rakam veya harf takip etmiyor
        "ID_NUMBER": r"\b\d{11}\b",
        "CREDIT_CARD_NUMBER": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
        "PLATE": r"[A-Za-z]{1,3}-[A-Za-z]{1,2}-[0-9]{1,4}",
        "DATE": r"\b\d{1,2}\/\d{1,2}\/\d{4}\b", # Düzeltilmiş DATE regex deseni
        "EMAIL": r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+.[A-Z|a-z]{2,}\b',
        "URL": r"https?:\/\/(?:www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)",
        "DOMAIN": r"(?:(?<=:\/\/)|(?<=\s))((?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})(?![\w.-])",
        "HASH": r"[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64}",
        "COMBOLIST": r"\b(?:[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:[a-zA-Z0-9]{4,}\b)"    
        }

    extracted_data = {}

    for pattern_name, pattern in patterns.items():
        matches = re.findall(pattern, text)
        if matches:
            extracted_data[pattern_name] = matches

    return extracted_data
