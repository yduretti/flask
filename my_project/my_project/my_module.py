from my_project.models import veiculo, carro

def my_method():

    meu_veiculo = veiculo(cor='Azul', tipo='carro', potencia=1300, velocidade=260)
    meu_carro = carro(cor='Azul', tipo='SUV', potencia=1300, velocidade=260, rodas=4, boia=False)

    #print('holla!')
    print(f'Veiculos: {meu_veiculo}')
    print(f'Carros: {meu_carro}')

    #Veiculos
    meu_veiculo.acelerar(300)
    meu_veiculo.freiar()
    meu_veiculo.acelerar(50)
    meu_veiculo.repintar(cor='Red')
    meu_veiculo.tunar(potencia=1800)

    print('#######')

    #Carro
    meu_carro.acelerar(200)
    meu_carro.freiar()
    meu_carro.acelerar(100)
    meu_carro.repintar(cor='Preto')
    meu_carro.tunar(potencia=1350)


def my_method2():
    print('holla 2!')

