import re


def clean_string(s):
    try:
        s = re.sub(r"\[.*\]", "", s) # Elimina referencias ("[a]", "[1]"...) del texto
        s = re.sub(r"[^a-zA-Z0-9\s\.\-]", "", s) # Elimina caracteres no deseados
        s = re.sub(r"\n", " ", s) #Elimina saltos de linea
        s = s.strip() # Elimina espacios iniciales y finales
        s = clean_countries(s)
    except TypeError:
        pass
    return s


def clean_countries(s):
    if s == 'United States':
        s = 'United States of America'
    elif s == 'DR Congo' or s == 'Democratic Republic of the Congo':
        s = 'Dem. Rep. Congo'
    elif s == 'Dominican Republic':
        s = 'Dominican Rep.'
    elif s == 'South Sudan':
        s = 'S. Sudan'
    elif s == 'North Macedonia':
        s = 'Macedonia'
    elif s == 'Bosnia and Herzegovina':
        s = 'Bosnia and Herz.'
    elif s == 'Czech Republic':
        s = 'Czechia'
    elif s == 'Eswatini':
        s = 'eSwatini'
    elif s == 'Equatorial Guinea':
        s = 'Eq. Guinea'
    elif s == 'Republic of the Congo':
        s = 'Congo'
    elif s == 'Central African Republic':
        s = 'Central African Rep.'
    elif s == 'Ivory Coast':
        s = "Côte d'Ivoire"
    elif s == 'East Timor':
        s = 'Timor-Leste'
    return s