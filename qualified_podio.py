
def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3):
    if tempo_chegada1 < tempo_chegada2 < tempo_chegada3:
        primeiro = tempo_chegada1
        segundo = tempo_chegada2
        terceiro = tempo_chegada3
        nome1 = nome_corredor1
        nome2 = nome_corredor2
        nome3 = nome_corredor3
    elif tempo_chegada3 < tempo_chegada2 < tempo_chegada1:
        primeiro = tempo_chegada3
        segundo = tempo_chegada2
        terceiro = tempo_chegada1
        nome1 = nome_corredor3
        nome2 = nome_corredor2
        nome3 = nome_corredor1
    elif tempo_chegada2 < tempo_chegada3 < tempo_chegada1:
        primeiro = tempo_chegada2
        segundo = tempo_chegada3
        terceiro = tempo_chegada1
        nome1 = nome_corredor2
        nome2 = nome_corredor3
        nome3 = nome_corredor1
    elif tempo_chegada1 < tempo_chegada3 < tempo_chegada2:
        primeiro = tempo_chegada1
        segundo = tempo_chegada3
        terceiro = tempo_chegada2
        nome1 = nome_corredor1
        nome2 = nome_corredor3
        nome3 = nome_corredor2
    elif tempo_chegada2 < tempo_chegada1 < tempo_chegada3:
        primeiro = tempo_chegada2
        segundo = tempo_chegada1
        terceiro = tempo_chegada3
        nome1 = nome_corredor2
        nome2 = nome_corredor1
        nome3 = nome_corredor3
    elif tempo_chegada3 < tempo_chegada1 < tempo_chegada2:
        primeiro = tempo_chegada3
        segundo = tempo_chegada1
        terceiro = tempo_chegada2
        nome1 = nome_corredor3
        nome2 = nome_corredor1
        nome3 = nome_corredor2

    resultado = f'1 - {nome1} - {primeiro} minutos\n2 - {nome2} - {segundo} minutos\n3 - {nome3} - {terceiro} minutos\n'
    return print(resultado)


tempo_chegada1 = 100
tempo_chegada2 = 10
tempo_chegada3 = 5
nome_corredor1 = "alan dek"
nome_corredor2 = "chris brow"
nome_corredor3 = "lian depons"

podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3, nome_corredor1, nome_corredor2, nome_corredor3)