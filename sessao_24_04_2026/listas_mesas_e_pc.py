#ciclo principal
while True:
    # dados de entrada
   mesa1 = { "tamanho": {"comprimento": 1.5, 
                        "largura": 0.8, 
                        "altura": 0.75},
                        "cor": "Branco",
                        "material": "Madeira",},



   mesa2 = {"tamanho": {"comprimento": 1.5, 
                        "largura": 0.8, 
                        "altura": 0.75},
                        "cor": "preto",
                        "material": "Ferro",},
   

   quadroeletrico ={"referencia": " QEL-001",
                    
                    "tamanho": {"comprimento": 0.5, 
                                "largura": 0.3, 
                                "altura": 0.2},

                    "dinjuntores": [{"Referencia": "14551320",
                                     "Marca": "Hager",
                                      "Intensidade": 16}],
                                      "Numero de Modulos": "2",
                                      "Material": "Metal",},
                                                        

   computador1 = {"marca": 
                 "Dell", 
                 "modelo": 
                 "XPS 15", 
                 "processador": "Intel Core i7", 
                 "ram": "16GB", 
                 "armazenamento": "512GB SSD"}, 
   
   computador2 = {"marca": "Apple",
                  "modelo": "MacBook Pro", 
                 "processador": "Apple M1", 
                 "ram": "16GB", 
                 "armazenamento": "512GB SSD"},
   
   computador3= {"Marca": "Lenovo", 
                 "modelo": "ThinkPad X1 Carbon", 
                 "processador": "Intel Core i7", 
                 "ram": "16GB", 
                 "armazenamento": "512GB SSD"},
   
   computador4= {"marca": "HP", 
                 "modelo": "Spectre x360", 
                 "processador": "Intel Core i7", 
                 "ram": "16GB", 
                 "armazenamento": "512GB SSD"},
   
   Computador5= {"marca": "Asus", 
                 "modelo": "ZenBook 14",        
                "processador": "Intel Core i7",
                "ram": "16GB",
                "armazenamento": "512GB SSD"},  
   
   lista_das_mesas = [mesa1,mesa2,mesa1,mesa2,mesa1],
   lista_dos_computadores = [computador1, computador2, computador3, computador4, Computador5],
   lista_dos_formandos = ["diogo", "joão", "rui machado","ricardo", "José"],

Print["Lista_das_mesas","Listas_dos_computadores", "Lista_dos_formandos" ]



