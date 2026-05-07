import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
# Dados de exemplo
aluno = {
    "nome": "Diogo Rocha",
    "foto": "foto_aluno.jpg",  # Substituir pelo caminho real da foto
    "ufcds": [
        "UFCD 0344 – Interpretação de Esquemas Elétricos",
        "UFCD 0345 – Instalação de Sistemas Elétricos",
        "UFCD 0346 – Proteção e Comando de Instalações",
        "UFCD 0347 – Normas e Segurança em Eletricidade",
        "UFCD 0348 – Manutenção de Instalações Elétricas"
    ]
}
# Criação da janela principal
janela = tk.Tk()
janela.title("Ficha do Aluno - Instalações Elétricas")
janela.geometry("500x550")
janela.configure(bg="#f0f0f0")
# Título
titulo = tk.Label(janela, text="Aluno de Instalações Elétricas", font=("Arial", 16, "bold"), bg="#f0f0f0")
titulo.pack(pady=10)
# Carregar e exibir a foto
try:
    img = Image.open(aluno["foto"])
    img = img.resize((150, 150))
    foto = ImageTk.PhotoImage(img)
    lbl_foto = tk.Label(janela, image=foto, bg="#f0f0f0")
    lbl_foto.pack(pady=5)
except:
    lbl_foto = tk.Label(janela, text="[Foto não disponível]", bg="#f0f0f0", fg="red")
    lbl_foto.pack(pady=20)
# Nome do aluno
lbl_nome = tk.Label(janela, text=aluno["nome"], font=("Arial", 14, "bold"), bg="#f0f0f0")
lbl_nome.pack(pady=10)
# Lista de UFCDs
lbl_ufcds = tk.Label(janela, text="UFCDs:", font=("Arial", 12, "underline"), bg="#f0f0f0")
lbl_ufcds.pack(pady=5)
lista = tk.Listbox(janela, width=60, height=10, font=("Arial", 10))
for ufcd in aluno["ufcds"]:
    lista.insert(tk.END, ufcd)
lista.pack(pady=10)
# Botão de sair
btn_sair = ttk.Button(janela, text="Fechar", command=janela.destroy)
btn_sair.pack(pady=10)
# Iniciar interface
janela.mainloop()