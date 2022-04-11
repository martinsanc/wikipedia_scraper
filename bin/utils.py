import re


def clean_string(s):
    try:
        s = re.sub(r"\[.*\]", "", s) # Elimina referencias ("[a]", "[1]"...) del texto
        s = re.sub(r"[^a-zA-Z0-9\s\.]", "", s) # Elimina caracteres no deseados
        s = re.sub(r"\n", " ", s) #Elimina saltos de linea
        s = s.strip() # Elimina espacios iniciales y finales
    except TypeError:
        pass
    return s
