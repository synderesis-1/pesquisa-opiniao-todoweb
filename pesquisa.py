# Inicialização de variáveis e contadores
total_entrevistados = 50  # Altere para 10 se quiser realizar o teste rápido solicitado
qtd_excelente = 0
qtd_ruim = 0

print("=== PESQUISA DE OPINIÃO - TUDOWEB ===")
print("Opções de atendimento:")
print("1: EXCELENTE")
print("2: BOM")
print("3: RUIM")
print("-" * 35)

# Estrutura de repetição para coletar os dados dos entrevistados
for i in range(1, total_entrevistados + 1):
    print(f"\nEntrevistado {i}:")
    
    # Coleta de dados básicos
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    
    # Validação simples para garantir que a opção seja válida (1, 2 ou 3)
    opiniao = int(input("Digite a opinião (1-Excelente, 2-Bom, 3-Ruim): "))
    
    while opiniao < 1 or opiniao > 3:
        print("Opção inválida! Digite novamente.")
        opiniao = int(input("Digite a opinião (1-Excelente, 2-Bom, 3-Ruim): "))
        
    # Estruturas de decisão para contabilizar as respostas
    if opiniao == 1:
        qtd_excelente += 1
    elif opiniao == 3:
        qtd_ruim += 1
    # Nota: A opção 2 (BOM) é coletada mas não necessita de contador específico conforme o enunciado.

# Exibição dos resultados finais ao término da pesquisa
print("\n" + "=" * 35)
print("RESULTADO FINAL DA PESQUISA")
print("=" * 35)
print(f"Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"Quantidade de respostas 'RUIM': {qtd_ruim}")
