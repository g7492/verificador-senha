print("=== Verificador de Força de Senha ===\n")

senha = input("Digite a senha para analisar: ")

pontos = 0
dicas = []

if len(senha) >= 8:
    pontos += 1
else:
    dicas.append("- Use pelo menos 8 caracteres")

if any(c.isupper() for c in senha):
    pontos += 1
else:
    dicas.append("- Adicione letras maiúsculas")

if any(c.islower() for c in senha):
    pontos += 1
else:
    dicas.append("- Adicione letras minúsculas")

if any(c.isdigit() for c in senha):
    pontos += 1
else:
    dicas.append("- Adicione números")

if any(c in "!@#$%^&*()_+-=[]{}|;:,.<>?" for c in senha):
    pontos += 1
else:
    dicas.append("- Adicione símbolos (!@#$ etc)")

print(f"\nPontuação: {pontos}/5")

if pontos <= 2:
    print("Força: FRACA")
elif pontos <= 4:
    print("Força: MÉDIA")
else:
    print("Força: FORTE")

if dicas:
    print("\nDicas para melhorar:")
    for dica in dicas:
        print(dica)
