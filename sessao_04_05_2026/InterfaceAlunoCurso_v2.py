import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

# 📌 Dados do aluno (já com estado e notas)
aluno = {
    "nome": "Diogo Rocha",
    "foto": r"C:\Users\Diogo\Desktop\Curso Eletricista\Programação\UFCD 6051\interface aluno\imagem.jpg",
    "ufcds": [
        {"nome": "UFCD 6051 – Programação", "feito": 1, "nota": "15"},
        {"nome": "UFCD 6052 – Portas Logicas", "feito": 1, "nota": "10"},
        {"nome": "UFCD 6053 – Organização Laboral", "feito": 1, "nota": "12"},
        {"nome": "UFCD 6054 – Segurança Elétrica", "feito": 1, "nota": "14"},
        {"nome": "UFCD 6055 – Manutenção de Instalações Elétricas", "feito": 0, "nota": "10"}
    ]
}

# 🪟 Janela principal
janela = tk.Tk()
janela.title("Técnico de Instalações Elétricas")
janela.geometry("520x600")
janela.configure(bg="#f0f0f0")

# 🏷️ Título
titulo = tk.Label(
    janela,
    text="Técnico de Instalações Elétricas",
    font=("Arial", 16, "bold"),
    bg="#f0f0f0"
)
titulo.pack(pady=10)

# 🖼️ Foto do aluno
try:
    img = Image.open(aluno["foto"])
    img = img.resize((150, 150))
    foto = ImageTk.PhotoImage(img)

    lbl_foto = tk.Label(janela, image=foto, bg="#f0f0f0")
    lbl_foto.image = foto
    lbl_foto.pack(pady=5)

except Exception as e:
    print("Erro imagem:", e)
    tk.Label(
        janela,
        text="[Foto não disponível]",
        fg="red",
        bg="#f0f0f0"
    ).pack(pady=10)

# 👤 Nome do aluno
tk.Label(
    janela,
    text=aluno["nome"],
    font=("Arial", 14, "bold"),
    bg="#f0f0f0"
).pack(pady=10)

# 📦 Frame das UFCDs
frame_ufcds = tk.Frame(janela, bg="#f0f0f0")
frame_ufcds.pack(pady=10)

# 🧠 guardar referências
ufcd_vars = []

# 📚 UFCDs com checkbox + nota
for ufcd in aluno["ufcds"]:
    linha = tk.Frame(frame_ufcds, bg="#f0f0f0")
    linha.pack(anchor="w", pady=3)

    # ✔ estado inicial (Sim/Não)
    var_check = tk.IntVar(value=ufcd["feito"])

    chk = tk.Checkbutton(
        linha,
        text=ufcd["nome"],
        variable=var_check,
        bg="#f0f0f0"
    )
    chk.pack(side="left")

    # 📝 texto "Nota"
    tk.Label(linha, text="Nota:", bg="#f0f0f0").pack(side="left", padx=5)

    # ✏️ nota já preenchida
    nota = tk.Entry(linha, width=5)
    nota.insert(0, ufcd["nota"])
    nota.pack(side="left")

    ufcd_vars.append((ufcd["nome"], var_check, nota))
    

# ❌ botão fechar
ttk.Button(janela, text="Fechar", command=janela.destroy).pack(pady=15)

# ▶️ iniciar app
janela.mainloop()