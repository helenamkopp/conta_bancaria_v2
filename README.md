# conta_bancaria_v2
# Pequeno projeto Orientado a Objetos construido utilizando o PyCharm contendo para construção de aprendizado de conceitos 
# de herança e polimorfismo. 

# Arquivo main.py:
# * class Employee: possui método construtor com dados/ informações de funcionários: nome, cpf e pagamento; possui um método get_bonus: 
#onde calcula bonificações dos funcionarios de acordo com o seu pagamento. 

# * class Manager: sub classe de Employee, onde todo Manager é também um Employee, no seu método construtor temos atributos exclusivos do manager 
# e utilizamos o super() para chamar name, cpf, pay; reescrevemos o método get_bonus, pois a bonificação para esse cargo segue o mesmo calculo, porem com um acrescimo de 1000. 

# * class Bonus_Control: método construtor iniciando o bonus_total = 0, nao permitindo que um cliente por exemplo acesse essa classe(como vemos no método def register)

# Arquivo extra.py: mostra que é impossivel aplicar um bonus a um cliente, considerando que ele precisa ter o método get_bonus para funcionar. 


#Arquivo test_main.py:
# realiza alguns testes unitários referentes ao arquivo main.py