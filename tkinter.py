import tkinter as tk

janela = tk.Tk()
janela.title("Teste")
janela.geometry("400x400")

tk.Label(janela, text="Cadastro de usuário", font=("Arial", 14, "bold"), fg="blue").pack(pady=10)

tk.Label(janela, text="Nome:", font=("Arial", 12, "bold")).pack()
tk.Entry(janela, width=40).pack()
tk.Label(janela, text="").pack()

tk.Label(janela, text="Email:", font=("Arial", 12, "bold")).pack()
tk.Entry(janela, width=40).pack()
tk.Label(janela, text="").pack()

tk.Label(janela, text="Data de Nascimento:", font=("Arial", 12, "bold")).pack()
tk.Entry(janela, width=40).pack()
tk.Label(janela, text="").pack()

tk.Label(janela, text="Senha:", font=("Arial", 12, "bold")).pack()
tk.Entry(janela, width=40, show="*").pack()
tk.Label(janela, text="").pack()

tk.Button(janela, text="Fechar", font=("Arial", 12, "bold"), bg="blue", fg="white", width=15 ,command=janela.destroy).pack()

janela.mainloop()