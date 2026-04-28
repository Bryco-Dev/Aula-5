def atualizar_hist(hist,paciente):
    if paciente in hist:
        hist.remove(paciente)
    hist.append(paciente)
    return hist
def main():
    hist = ['ana', 'Carlos', ' Beatriz']
    novo = 'Carlos'
    print (f'Hist_atual {hist}')
    hist = atualizar_hist (hist, novo)
    print (f'His atualizado: {hist}')
main()