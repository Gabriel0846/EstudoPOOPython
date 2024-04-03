class Pessoa:
    "Isto é uma classe nova chamada pessoa"

    idade = 15

    def saudacao(self):
        print("Olá Pessoas!") 

# Output: 15
print(Pessoa.idade)

# Output: <function Pessoa.saudacao>
print(Pessoa.saudacao)

# Output: "Isto é uma classe nova chamada Pessoa"
print(Pessoa.__doc__)
