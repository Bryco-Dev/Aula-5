def ranking(pacientes):
    ranking_paciente = []
    for paciente in pacientes:
        pontos = 0
        if paciente['gravidade'] > 4:
            pontos += 3
        elif paciente['gravidade'] > 2:
            pontos += 2

        if paciente['idade'] > 60:
            pontos += 2

        ranking_paciente.append({'nome': paciente['nome'], 'pontos': pontos})

    # bubble sort
    for i in range(len(ranking_paciente)):
        for j in range(i + 1, len(ranking_paciente)):
            if ranking_paciente[i]['pontos'] < ranking_paciente[j]['pontos']:
                ranking_paciente[i], ranking_paciente[j] = ranking_paciente[j], ranking_paciente[i]

    # print
    for item in ranking_paciente:                          # ← iterando o item diretamente
        print(f"{item['nome']}, {item['pontos']}")         # ← aspas duplas na f-string

def main():
    pacientes = [
        {'nome': 'Ana',     'idade': 70, 'gravidade': 3},
        {'nome': 'Carlos',  'idade': 40, 'gravidade': 5},
        {'nome': 'Beatriz', 'idade': 65, 'gravidade': 2},
        {'nome': 'João',    'idade': 30, 'gravidade': 1},
    ]
    ranking(pacientes)   # ← chamada que estava faltando

main()