class Main:
    pass

print("testando o codigo")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("João", "12345-6789")
conta= Conta(c1.nome, 6565, 0)

print(conta.titular, " Numero: ", conta.numero, "Seu saldo: ", conta.saldo)