from modulos import PacoteAlarme, PacoteProducao
lista_mensagem =[]
def iniciar():
    while True:
        print("""
        1 -chegou um alarme
        2 -chegou Dados de produção
        3 -Processar Fila inteira
        4 -Sair""")
        opc = int(input("Digite a opção desejada: "))
        if opc == 1:
            origem = input("Digite a origem do alarme: ")
            data_hora = input("Digite a data e hora do alarme: ")
            gravidade = input("Digite a gravidade do alarme (ALTA, MEDIA, BAIXA): ")
            pacote_alarme = PacoteAlarme(origem, data_hora, gravidade)
            lista_mensagem.append(pacote_alarme)
        elif opc == 2:
            origem = input("Digite a origem dos dados de produção: ")
            data_hora = input("Digite a data e hora dos dados de produção: ")
            try:
                quantidade = int(input("Digite a quantidade de peças produzidas: "))
                pacote_producao = PacoteProducao(origem, data_hora, quantidade)
                lista_mensagem.append(pacote_producao)
            except ValueError:
                print("valor errado. Por favor, digite um número inteiro.")
        elif opc == 3:
            for pro in lista_mensagem:
                pro.processar
            lista_mensagem.clear()
        elif opc == 4:
            print("Encerrando o programa.")
            break
iniciar()