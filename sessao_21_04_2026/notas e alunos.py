#ciclo principal
while True:
    # Lista de alunos (nome, nota)
    alunos = [
        ("Diogo", 19),
        ("Machado", 16),
        ("João", 12),
        ("Pedro", 8),
        ("Ricardo", 14)
    ]

    for nome, nota in alunos: #percorre a lista de alunos e imprime o nome, nota e classificação
        print("Nome:",nome)
        print("Nota:",nota)

        if nota >= 18:
            classificacao = "Excelente"
        else:
            if nota >= 14:
                classificacao = "Satisfaz Bastante"
            else:
                if nota >= 10:
                    classificacao = "Satisfaz"
                else:
                    classificacao = "Não Satisfaz"

        print("Classificação:",classificacao)
