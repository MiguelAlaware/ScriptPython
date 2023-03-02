def achevogais(frase:str) -> set:
    """Acha vogais em uma palavra redigida."""
    vogais = set('aeiou')
    return vogais.intersection(set(frase))
achevogais('doido')

def acheletras(frase:str, letras:str='aeiou') -> set:
    """Retorna um conjunto de 'letras' em 'frase'."""
    return set(letras).intersection(set(frase))

