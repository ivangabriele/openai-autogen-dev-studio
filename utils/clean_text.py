import re


def clean_text(text):
    lines = text.split("\n")
    cleaned_lines = [re.sub(r"\s+", " ", line).strip() for line in lines]
    cleaned_text = "\n".join(cleaned_lines)
    cleaned_text = cleaned_text.strip()

    return cleaned_text
