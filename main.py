
import customtkinter as ctk

app = ctk.CTk()

app.title("MiNI SIEM")
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



Botao = ctk.CTkButton(master=frame, text="Selecionar Arquivo de Logs", command=analisar_logs)
Botao.pack(pady=10)


app.mainloop()