import minha_funcao

A = True
B = False 

saida = not (((A and not B) or  (not A and B)))

saida1=minha_funcao.xnor(A,B)

C = True
D = False 

saida2 = minha_funcao.xnor(C,D)