import re


def clean_string(str):
    # Elimina referencias ("[a]", "[1]"...) del texto
    return re.sub("\[.*â€?\]","",str)