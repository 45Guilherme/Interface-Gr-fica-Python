

def detectar_ataques(contador_ips, limite=3):
    ataques = {}
    for ip, contagem in contador_ips.items():
        if contagem >= limite:
            ataques[ip] = contagem
    return ataques
