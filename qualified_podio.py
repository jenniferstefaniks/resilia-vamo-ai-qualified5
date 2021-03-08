
def podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3):
    if tempo_chegada1 < tempo_chegada2 < tempo_chegada3:
        primeiro = tempo_chegada1
        segundo = tempo_chegada2
        terceiro = tempo_chegada3
    elif tempo_chegada3 < tempo_chegada2 < tempo_chegada1:
        primeiro = tempo_chegada3
        segundo = tempo_chegada2
        terceiro = tempo_chegada1
    elif tempo_chegada2 < tempo_chegada3 < tempo_chegada1:
        primeiro = tempo_chegada2
        segundo = tempo_chegada3
        terceiro = tempo_chegada1
    elif tempo_chegada1 < tempo_chegada3 < tempo_chegada2:
        primeiro = tempo_chegada1
        segundo = tempo_chegada3
        terceiro = tempo_chegada2
    elif tempo_chegada2 < tempo_chegada1 < tempo_chegada3:
        primeiro = tempo_chegada2
        segundo = tempo_chegada1
        terceiro = tempo_chegada3
    elif tempo_chegada3 < tempo_chegada1 < tempo_chegada2:
        primeiro = tempo_chegada3
        segundo = tempo_chegada1
        terceiro = tempo_chegada2
        
    resultado = f'1 - {primeiro} minutos\n2 - {segundo} minutos\n3 - {terceiro} minutos\n'
    return resultado

tempo_chegada1 = 100
tempo_chegada2 = 10
tempo_chegada3 = 5

podio_olimpico(tempo_chegada1, tempo_chegada2, tempo_chegada3)