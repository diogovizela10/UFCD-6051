#ciclo principal
while True:
    # dados de entrada
    capital = 10000       # valor do empréstimo
    taxa_anual = 2      # taxa de juro 
    anos = 10          # duração em anos

    # Converter taxa anual para mensal
    taxa_mensal = (taxa_anual / 100) / 12 # taxa mensal percentagem
    meses = anos * 12

    # Cálculo da prestação
    if taxa_mensal == 0: #se a taxa de juro for 0, a prestação é dividida igualmente pelo o numero de meses 
        prestacao = capital / meses
    else:
        prestacao = capital * (taxa_mensal * (1 + taxa_mensal)**meses) / ((1 + taxa_mensal)**meses - 1) #formula de calculo da prestação mensal 


    # Resultados
    print("Prestação mensal:",round(prestacao,2), "€")
    print("Anos do emprestimo:", anos)
    print("Total de juros:", round(prestacao * meses - capital, 2), "€")
    print("Custo total do empréstimo:", round(prestacao * meses, 2), "€")
    break #sai do ciclo apos 1 ciclo
