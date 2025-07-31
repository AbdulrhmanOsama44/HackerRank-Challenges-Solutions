def mutate_string(string, position, character):
    
    lista = list(string)
    lista[position] = character
    new_string = ''.join(lista)
    
    return new_string