import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

app = ctk.CTk()
app.title("Teste CustomTkinter")
app.geometry("400x360")

ctk.CTkLabel(app, text="Nome:", font=("Arial", 12, "bold")).pack()
ctk.CTkEntry(app, width=200, placeholder_text="Nome Completo").pack()

ctk.CTkLabel(app, text="Email:", font=("Arial", 12, "bold")).pack()
ctk.CTkEntry(app, width=200, placeholder_text="Seu Email").pack()

ctk.CTkLabel(app, text="Senha:", font=("Arial", 12, "bold")).pack()
ctk.CTkEntry(app, width=200, placeholder_text="Sua Senha", show="*").pack()
ctk.CTkButton(app, text="Enviar", fg_color="blue", command=app.destroy).pack(pady=10)

app.mainloop()