import re


def clean_text(text):
    cleaned_text = re.sub(r"\s+", " ", text).strip()

    return cleaned_text
