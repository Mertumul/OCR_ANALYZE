from dynaconf import Dynaconf

settings = Dynaconf(
    envvar_prefix="DYNACONF",
    settings_files=["settings.toml", ".secrets.toml"],
)

patterns = {
    "PHONE_NUMBER": r"(?<!\d)(?:\+|00)?(?:90|0)?[- ]?\d{3}[- ]?\d{3}[- ]?\d{2}[- ]?\d{2}(?!\d)|\+98\s?\d{3}\s?\d{3}\s?\d{4}",
    "ID_NUMBER": r"\b[1-9]\d{10}\b",
    "CREDIT_CARD_NUMBER": r"\b\d{4}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b",
    "PLATE": r"\b([0-9]{2} [A-Z]{1,3} [0-9]{1,5})\b",
    "DATE": r"\b\d{1,2}/\d{1,2}/\d{4}\b",
    "EMAIL": r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b",
    "URL": (
        r"https?://(?:www\.)?"
        r"[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}"
        r"\b(?:[-a-zA-Z0-9()@:%_\+.~#?&\/=]*)"
    ),
    "DOMAIN": (
        r"(?:(?<=://)|(?<=\s))"
        r"((?:[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?\.)+[a-zA-Z]{2,})"
        r"(?![\w.-@])"
    ),
    "HASH": r"[a-fA-F0-9]{32}|[a-fA-F0-9]{40}|[a-fA-F0-9]{64}",
    "COMBOLIST": (
        r"\b(?:[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+:" r"[a-zA-Z0-9]{4,}\b)"
    ),
}
