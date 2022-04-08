import re


def clean_string(s):
    # Elimina referencias ("[a]", "[1]"...) del texto
    s = re.sub(r"\[.*\]", "", s)

    # Elimina caracteres no deseados
    return re.sub(r"[^a-zA-Z0-9\s\,\.]", "", s)
