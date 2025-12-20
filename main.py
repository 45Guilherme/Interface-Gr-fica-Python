
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

def analisar_logs():
    label_boa_vindas.configure(text="Status: Analisando logs...")


Botao = ctk.CTkButton(master=frame, text="Selecionar Arquivo de Logs", command=analisar_logs)
Botao.pack(pady=10)


app.mainloop()