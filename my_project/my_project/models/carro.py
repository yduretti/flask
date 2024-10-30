from my_project.models.veiculo import veiculo

class carro(veiculo):
    def __init__(self, 
                cor: str, 
                tipo: str,
                potencia: int,
                velocidade: float,
                rodas: int,
                boia: bool) -> None:
        
        super().__init__(cor, tipo, potencia, velocidade)
        self.rodas = rodas
        self.boia = boia
