"""
Na programação POO, o termo factory (fábrica) refere-se a uma classe ou método
que é responsável por criar objetos.
Vantagens:
    -Permitem criar um sistema com baixo acoplamento entre classes porque
    ocultam as classes que criam os objetos do código cliente.
    -Facilitam a adição de novas classes ao código, porque o cliente não
    conhece e nem utiliza a implementação da classe (utiliza a factory).
    -Podem facilitar o processo de "cache" ou criação de "singletons" porque a
    fábrica pode retornar um objeto já criado para o cliente, ao invés de criar
    novos objetos sempre que o cliente precisar.
Desvantagens:
    -Podem introduzir muitas classes no código
Vamos ver 2 tipos de Factory da GoF: Factory method e Abstract Factory
Nessa aula:
Simple Factory <- Uma espécie de Factory Method parametrizado
Simple Factory pode não ser considerado um padrão de projeto por si só
Simple Factory pode quebrar princípios do SOLID
"""
from abc import ABC, abstractmethod
# Verificar os arquivos na pasta


class Veiculo(ABC):  # Product
    # polimorfismo de metodos abstractos (métodos que não tem implementação)
    # Força que todas as subclasses de Veiculo implementem o método abstrato
    @abstractmethod
    def buscar_cliente(self) -> None: pass


class CarroLuxo(Veiculo):  # Concrete Product1
    def buscar_cliente(self) -> None:
        print('Carro de luxo esta buscando o cliente...')


class CarroPopular(Veiculo):  # Concrete Product2
    def buscar_cliente(self) -> None:
        print('Carro popular esta buscando o cliente...')


class Moto(Veiculo):  # Concrete Product3
    # Adição
    def buscar_cliente(self) -> None:
        print('Moto esta buscando o cliente...')


# Simple Factory
class VeiculoFactory:  # Factory
    # Acoplamento entre classes
    @staticmethod
    def get_carro(tipo: str) -> Veiculo:
        # Factory Method(cria um objeto para o cliente)
        if tipo == 'Luxo':
            return CarroLuxo()
        if tipo == 'Popular':
            return CarroPopular()
        if tipo == 'Moto':
            return Moto()
        assert 0, 'Veiculo não existe'


if __name__ == '__main__':
    from random import choice
    carros_disponiveis = ['Luxo', 'Popular', 'Moto']

    for i in range(10):  # Cliente usa o objeto criado pela factory
        carro = VeiculoFactory.get_carro(choice(carros_disponiveis))
        carro.buscar_cliente()
