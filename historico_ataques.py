

def salvar_historico(ataque):
    with open("historico_ataques.txt", "a") as f:
        f.write(f"{ataque}\n")