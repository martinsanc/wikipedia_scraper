import re


def clean_string(str):
    # Elimina referencias ("[a]", "[1]"...) del texto
    str = re.sub(r"\[.*\]", "", str)

    # Elimina caracteres no deseados
    str = re.sub(r"[^a-zA-Z0-9\s]", "", str)

    # Elimina dobles espacios
    str = re.sub("\s\s", "\s", str)

    return str.strip()
