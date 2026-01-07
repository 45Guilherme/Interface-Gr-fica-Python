
import customtkinter as ctk
from tkinter import filedialog
from leitor_logs import ler_logs
from detector_log import detectar_ataques
from historico_ataques import salvar_historico
ctk.set_appearance_mode("dark")

app = ctk.CTk()

app.title("MiNI SIEM")
file_path = None
texto_label = "Teste do Mini SIEM"
app.geometry("800x500")

label_boa_vindas = ctk.CTkLabel(
    master=app,
    text="Teste do Mini SIEM",
    font=("Arial", 24)
)
label_boa_vindas.pack(pady=20)

frame = ctk.CTkFrame(master=app)
frame.pack(pady=20, padx=60, fill="both", expand=True)

frame_usuario_ssh = ctk.CTkEntry(master=frame, width=250, placeholder_text="Usuário SSH")
frame_usuario_ssh.pack(pady=10)

label_ssh = ctk.CTkLabel(master=frame, text=f"Status: aguardando ação")
label_ssh.pack(pady=10)

def analisar_logs():
    label_boa_vindas.configure(text="Status: Analisando logs...")
    ssh = frame_usuario_ssh.get()
    label_ssh.configure(text=f"Status: Analisando logs para o usuário SSH: {ssh}")
    if ssh == "":
        print(f"Status: usuário SSH não informado.")
    else:
        print(f"Status: Analisando logs para o usuário SSH: {ssh}")
    if ssh == "":
        label_ssh.configure(text_color="red")
    else:
        label_ssh.configure(text_color="green")

def selecionar_arquivo():
    global file_path
    file_path = filedialog.askopenfilename(title="Selecione o arquivo de logs")
    if file_path == "":
        label_ssh.configure(text = "Nenhum arquivo selecionado.", text_color="yellow")
        file_path = None
    else:
        label_ssh.configure(text=f"Arquivo selecionado:\n{file_path}", text_color="green")

def formatar_ataques(ataques):
    texto = "🚨 ATAQUES DETECTADOS 🚨\n\n"
    for ip, tentativas in ataques.items():
        texto += f"IP: {ip}\n"
        texto += f"Tentativas: {tentativas}\n\n"
    return texto



def detectar_logs():
    if not file_path:
        label_ssh.configure(
            text="Selecione um arquivo de logs primeiro!",
            text_color="red"
        )
        return

    contador_ips = ler_logs(file_path)
    ataques = detectar_ataques(contador_ips)

    if ataques:
        label_ssh.configure(
            text=f"Ataques detectados:\n{formatar_ataques(ataques)}",
            text_color="red"
        )
    else:
        label_ssh.configure(
            text="Nenhum ataque detectado.",
            text_color="green"
        )


Botao = ctk.CTkButton(master=frame, text="Selecionar Arquivo de Logs", command=analisar_logs)
Botao.pack(pady=10)
Botao_file = ctk.CTkButton(master=frame, text="Selecionar Arquivo", command=selecionar_arquivo)
Botao_file.pack(pady=10)
Botao_detectar = ctk.CTkButton(master=frame, text="Detectar Ataques", command=detectar_logs)
Botao_detectar.pack(pady=10)

if __name__ == "__main__":
    app.mainloop()