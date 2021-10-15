f  =  open ('pib_municipio_2010_a_2018.txt' , 'r' )

arquivo  = []
f . readline ()
for  linha  in   f :
    arquivo . append ( linha . split ( ';' ))
f . close()


pib_per_capita =  []
estados = []
cidades=[]
dados=[]

for  linha  in  arquivo :
    if linha [0] == "2018": #filtrei o ano 
        estados.append(f'{linha[2]}') # filtrei os estados
        estados=list(set(estados))    # apliquei função set para eliminar os estados repetidos
        cidades.append(f'{linha[3]}') # adicionei as cidades 
        pib_per_capita.append(float(linha[9]))  # adicionei o pib e fiz conversão para float 
        dados.append(f'{linha[0]:} - {linha[2]} - {linha[3]} - R${linha[9]}')  

#maior_pib = sorted(dados, key=lambda item: max(linha[9]),reverse=True)

def saída():
    out =open ( '\python\DesafioTrainee\questão_01\saida_q1.txt' , 'a' , encoding = "utf-8" ) 
    out . write ('\nAno -  Estado - Cidade - Pib per capita  \n')
    for  n  in  dados :
        out.write(f'{ n }\n')
    
    out.close()

saída()