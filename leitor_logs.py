with open('leitor_logs.txt', 'w')as file:
    file.write("2026-01-05 10:12:01 IP 192.168.1.10 ACCESS_ACCEPTED\n")
    file.write("2026-01-05 10:12:15 IP 203.0.113.45 ACCESS_DENIED\n")
    file.write("2026-01-05 10:13:02 IP 192.168.1.15 ACCESS_ACCEPTED\n")
    file.write("2026-01-05 10:13:40 IP 198.51.100.23 ACCESS_DENIED\n")
    file.write("2026-01-05 10:14:05 IP 192.168.1.20 ACCESS_ACCEPTED\n")
    file.write("2026-01-05 10:14:55 IP 203.0.113.89 ACCESS_DENIED\n")
    file.write("2026-01-05 10:15:18 IP 192.168.1.30 ACCESS_ACCEPTED\n")
    file.write("2026-01-05 10:15:59 IP 198.51.100.77 ACCESS_DENIED\n")
    file.write("2026-01-05 10:16:22 IP 192.168.1.50 ACCESS_ACCEPTED\n")
    file.write("2026-01-05 10:16:48 IP 203.0.113.120 ACCESS_DENIED\n")


def ler_logs(selecionar_arquivo):
    cont = {}

    with open(selecionar_arquivo, 'r') as file:
        logs = file.readlines()

        for linha in logs:
            partes = linha.split()
            ip = partes[3]
            status = partes[4]

            if status == "ACCESS_DENIED":
                if ip in cont:
                    cont[ip] += 1
                else:
                    cont[ip] = 1

    return cont











