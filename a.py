temperaturas = [[28, 31, 34, 33], [25, 27, 29, 28], [32, 35, 36, 34], [24, 26, 25, 27]]
criticos=[]
media=[]
maior_cri=0
sala_risco=0

for i in temperaturas:
    media.append((sum(i))/len(i))


for i in range(len(temperaturas)):
    criticos.append(0)
    for j in temperaturas[i]:
        if j>=33:
            criticos[i]+=1
        
for i in range(len(criticos)):
   if  criticos[i]> maior_cri:
       maior_cri=criticos[i]
       sala_risco=i + 1



print(f"""
media das salas:
sala 1
Media: {media[0]:.1f}
Registro critico: {criticos[0]}

sala 2
Media: {media[1]:.2f}
Registro critico: {criticos[1]}

sala 3
Media: {media[2]:.2f}
Registro critico: {criticos[2]}

sala 4
Media: {media[3]:.1f}
Registro critico: {criticos[3]}


Sala com maior risco: Sala {sala_risco}
""")