import customtkinter as ctk

app = ctk.CTk()

app.title("MiNI SIEM")
texto_label = "Teste do Mini SIEM"
app.geometry("800x500")

label_boa_vindas = ctk.CTkLabel(master=app, text=texto_label, font=("Arial", 24))
label_boa_vindas.pack(pady=20)

def analisar_logs():
    print("Analisando logs...")

ctkButton = ctk.CTkButton(master=app, text="Analisar Logs", command=analisar_logs)
ctkButton.pack(pady=10)




app.mainloop()