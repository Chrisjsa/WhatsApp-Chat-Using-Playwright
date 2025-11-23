import re


def clean_text_for_logging(text, max_length=100):
    clean_text = re.sub(r'[^a-zA-Z0-9\s.,+!?\-á-ú*@()|=]', '_', text)

    if len(clean_text) > max_length:
        clean_text = clean_text[:max_length] + '...'

    return clean_text
