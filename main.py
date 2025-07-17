##Crie programa que o usuário digita o seu nome e retorna o número de caracteres

#print(len(input("Digite seu nome: ")))



##Criar um programa onde o usuário digite dois valores e apareça a soma

#print(int(input("Digite o primeiro valor: ")) + int(input("Digite o segundo valor: ")))

#print("valor total: ")


## Desafio
# 1) Solicita ao usuário que digite seu nome

# 2) Solicita ao usuário que digite o valor do seu salário
# Converte a entrada para um número de ponto flutuante

# 3) Solicita ao usuário que digite o valor do bônus recebido
# Converte a entrada para um número de ponto flutuante

# 4) Calcule o valor do bônus final

# 5) Imprima cálculo do KPI para o usuário

# 6) Imprime a mensagem personalizada incluindo o nome do usuário, salário e bônus

# Bônus: Quantos bugs e riscos você consegue identificar nesse programa?

CONSTANTE_BONUS = 1000
nome = input("Digite seu nome: ")
salario = float(input("Digite o valor do seu salário: "))
bonus = float(input("Digite o valor do bônus recebido: "))
bonus_final = CONSTANTE_BONUS + salario * bonus

print(f"O usuário {nome} tem um salário de R$ {salario:.2f} e recebeu um bônus de R$ {bonus:.2f}.Daniel, Salario + Bônus = R$ {bonus_final:.2f}")


# Bugs e riscos:
# 1) O usuário pode digitar um valor não numérico para salário ou bônus,
# o que causaria um erro de conversão.
# 2) Não há validação para garantir que o salário e o bônus sejam positivos.
# 3) O programa não lida com casos onde o salário é zero, o que causaria uma divisão por zero.
# 4) O programa não trata exceções, o que pode levar a falhas inesperadas.
# 5) O programa não verifica se o nome está vazio ou contém caracteres inválidos.
# 6) O programa não oferece uma maneira de o usuário corrigir entradas inválidas.
# 7) O programa não informa o usuário sobre o que fazer em caso de erro.
# 8) O programa não possui comentários ou documentação para explicar o que faz.
# 9) O programa não possui testes automatizados para verificar se funciona corretamente.