class Main:
    pass

print("testando o codigo")

from Cliente import Cliente

from Conta import Conta

c1= Cliente("João", "12345-6789")
conta= Conta(c1.get_nome(), 1222, 0)

conta.deposita(100)
conta.saque(50)
conta.extrato()

