class PacoteBase:
    def __init__(self,origem,data_hora):
        self.origem = origem
        self.data_hora = data_hora
    @property
    def processar(self):
        return f"Processando pacote genérico"
class PacoteAlarme(PacoteBase):
    def __init__(self,origem,data_hora,gravidade):
        super().__init__(origem,data_hora)
        self.grav = gravidade   
    @property
    def processar(self):
        if self.grav.upper() == "ALTA":
            print(" alerta maximo")
        elif self.grav.upper() == "MEDIA":
            print(" alerta medio")
        elif self.grav.upper() == "BAIXA":
            print(" alerta baixo")
        else:            print("gravidade desconhecida")    
class PacoteProducao(PacoteBase):
    def __init__(self,origem,data_hora,quantidade):
        super().__init__(origem,data_hora)
        self.quant = quantidade
    @property
    def processar(self):
        print(f"Processando quantidade de peças salvas no Banco de DADOS: {self.quant}")

