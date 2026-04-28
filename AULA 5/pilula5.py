def processar_consultas (registros):
    tempo = {}
    cont = {}
    status = {}
    for reg in registros:
        p = reg['paciente']
        if p not in tempo:
            tempo [p] = 0
            cont [p] = 0
        tempo[p] += reg ['tempo']
        cont [p] += 1
    
    for p in tempo:
        t = tempo [p]
        if t < 2:
            status[p] = 'leve'
        elif t < 5:
            status[p] = 'moderado'
        else:
            status [p] = 'crítico'
    for p in tempo:
        print(f'{p} | Tempo: {tempo[p]} | Qtd: {cont[p]} | Status: {status[p]}')
            
        
def main():
    registros = [
        {'paciente': 'Ana', 'tempo': 1},
        {'paciente': 'Ana', 'tempo': 2},
        {'paciente': 'Carlos', 'tempo': 4}, 
    ]
    
    processar_consultas(registros)
main()    