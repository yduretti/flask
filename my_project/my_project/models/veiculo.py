class veiculo:
    def __init__(self, 
                cor: str, 
                tipo: str,
                potencia: int,
                velocidade: float) -> None:
        self.cor = cor
        self.tipo = tipo
        self.potencia = potencia
        self.velocidade = velocidade

    def acelerar(self, velocidade: float):
        self.velocidade = velocidade
        print(f"Velocidade é {self.velocidade}")

    def freiar(self):
        self.velocidade = 0
        print(f"Freiando, a Velocidade é {self.velocidade}")

    def repintar(self, cor: str):
        self.cor = cor
        print(f"Cor é {self.velocidade}")

    def tunar(self, potencia: str):
        self.potencia = potencia
        print(f"Minha potencia é {self.potencia}")