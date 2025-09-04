from datetime import datetime

# Solicitar data de nascimento
nascimento = input("Digite sua data de nascimento (DD/MM/AAAA): ")

# Converter para data
data_nasc = datetime.strptime(nascimento, "%d/%m/%Y")
ano_atual = datetime.now().year

# Calcular idades
idade_atual = ano_atual - data_nasc.year
idade_2050 = 2050 - data_nasc.year

# Mostrar resultados
print(f"\nVocê tem {idade_atual} anos.")
print(f"Em 2050, você terá {idade_2050} anos.")