def ordenar_promocoes(lista_codigos):
    n =len(lista_codigos)

    for i in range(n):
        indice_mais_antigo = i

        for j in range(i + 1, n):
            if lista_codigos[j][1] < lista_codigos[indice_mais_antigo][1]:
                indice_mais_antigo = j

        lista_codigos[i], lista_codigos[indice_mais_antigo] = lista_codigos[indice_mais_antigo], lista_codigos[i]
        
    return lista_codigos
                                                                                                       
                                                                                                       
funcionarios = [
    (102, "09-09-2009"),  
    (101, "05-08-2000"), 
    (104, "25-08-2015"),  
    (103, "15-01-2010"),  
    (105, "26-06-2022")   
]         

funcionarios_ordenados = ordenar_promocoes(funcionarios)

print("Funcionários ordenados por senioridade de matrícula:")
for funcionario in funcionarios_ordenados:
    print("Matrícula:", funcionario[0], " | Data de matrícula:", funcionario[1]) 