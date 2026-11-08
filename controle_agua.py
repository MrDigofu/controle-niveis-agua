from colorama import Fore, Style, init

# Inicializa o Colorama para exibir cores no terminal.
init(autoreset=True)

# Lista com as mensagens dos cinco níveis do reservatório.
niveis = [
    "Nível 1 - Muito baixo (CRÍTICO)",
    "Nível 2 - Baixo",
    "Nível 3 - Médio",
    "Nível 4 - Alto",
    "Nível 5 - Muito alto (ALERTA)"
]


def definir_cor(nivel):
    """Retorna a cor correspondente ao nível informado."""
    if nivel == 1:
        return Fore.RED
    elif nivel == 2:
        return Fore.YELLOW
    elif nivel == 3:
        return Fore.GREEN
    elif nivel == 4:
        return Fore.CYAN
    elif nivel == 5:
        return Fore.BLUE
    else:
        return Fore.WHITE


print("===== MONITORAMENTO DO RESERVATÓRIO =====\n")

# Percorre a lista e mostra cada situação com sua cor.
for indice, mensagem in enumerate(niveis):
    nivel_atual = indice + 1
    cor = definir_cor(nivel_atual)
    print(cor + mensagem + Style.RESET_ALL)

print("\n===== FIM DO MONITORAMENTO =====")
