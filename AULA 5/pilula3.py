def atender (fila):
    if len (fila) == 0:
        print('Fila Vazia')
        return fila
    paciente = fila.pop(0)
    print (f'Atendendo {paciente}')
    return fila

def main():
    fila = ['Ana', 'Carlos', 'Beatriz', 'João']
    print(f'Fila inicial {fila}')
    fila = atender (fila)
    print (f'Fila alterada {fila}')
    