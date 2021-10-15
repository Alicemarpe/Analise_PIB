f  =  open ('pib_municipio_2010_a_2018.txt' , 'r' )   # abrindo o arquivo.

arquivo  = []                        #salvando numa lista.
f . readline ()
for  linha  in   f :        
    arquivo . append ( linha . split ( ';' ))   #adicionando split para fazer a quebra de linha.
f . close()


qtd_anos  =  0       # var para armazenar os anos do dataset.
registros  = []      # var para guardar os registros.

pib_bruto  =  []     # var para guardar os valores para somar.


for  linha  in  arquivo :                                              
    if linha [3] == "Manaus":
        pib_bruto +=(linha[4],linha[5],linha[6],linha[7],linha[8]) 
        float_list = list(map(float,pib_bruto))                       #conversão em float.
        registros.append(f'{linha[0]:} - {linha[2]} - {linha[3]} - {linha[4]}- {linha[5]} - {linha[6]} - {linha[7]} - {linha[8]}')
        qtd_anos += 1

Soma= sum(float_list)
Media_Pib_Bruto = Soma/qtd_anos

def saída():
    out =open ( '\python\DesafioTrainee\questão_02\saida_q2.txt' , 'a' , encoding = "utf-8" ) 
    out . write ('\nAno -  Estado - Cidade - Vlr Agr - Vlr Ind - Vlr Serv - Vlr Adm - Impostos \n')
    for  n  in  registros :
        out.write(f'{ n }\n')
    out.write("\n A soma do PIB Bruto da cidade de Manaus  no período que abrange o dataset é: R${:.2f}".format(Soma))
    out.write("\n A média do PIB Bruto da cidade de Manaus  no período que abrange o dataset é: R${:.2f}".format(Media_Pib_Bruto))
    out.close()

    
print("A soma do PIB Bruto da cidade de Manaus  no período que abrange o dataset é: R${:.2f}".format(Soma))
print("A média do PIB Bruto da cidade de Manaus  no período que abrange o dataset é: R${:.2f}".format(Media_Pib_Bruto))

saída()
