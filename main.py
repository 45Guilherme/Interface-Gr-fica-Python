
import customtkinter as ctk

app = ctk.CTk()

ctkFrame = ctk.CTkFrame(master=app)
ctkFrame.pack(pady=20, padx=60, fill="both", expand=True)



app.title("MiNI SIEM")
texto_label = "Teste do Mini SIEM"
app.geometry("800x500")

label_boa_vindas = ctk.CTkLabel(master=app, text=texto_label, font=("Arial", 24))
label_boa_vindas.pack(pady=20)

def analisar_logs():
    label_boa_vindas.configure(text="Status: Analisando logs...")


ctkFrameButton = ctk.CTkButton(master=ctkFrame, text="Selecionar Arquivo de Logs")
ctkFrameButton.pack(pady=10, padx=10)






app.mainloop()