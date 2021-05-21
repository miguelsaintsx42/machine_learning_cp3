'''
FIAP
Defesa Cibernética - 1TDCF - 2021
Development e Coding for Security
Prof. Ms. Fábio H. Cabrini 
Atividade: Check Point 3
Alunos
Nome: miguel batista dos santos neto - RM 87666
Nome: ariel levi ponzoni galvani de oliveira - RM 87502
'''
from sklearn import tree
features = [[126,127, 130], [140,144, 150], [160, 167,170],[171,172,173],[174,175,178],[179,180,181],[182,183,184],[190,192,193],[194,195,196],[200,202,210], [50, 54,55], [60, 64,65], [ 70, 74,75],[76,77,78],[80,81,82],[83,84,85],[87,88,89],[90,91,92],[93,94,95],[96,97,98], [100,101, 102], [103, 104,105], [106,107, 108],[109,110,111],[112,113,114],[115,116,117],[118,119,120],[121,122,123],[124,124,125],[125,125,125]]
labels = [0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,2,2,2,2,2,2,2,2,2,2]
classif = tree.DecisionTreeClassifier()
classif.fit(features, labels)
glicemina = float(input("Digite o nível da glicemina em jejum: "))
peso = float(input("Digite o peso da pessoa: "))
risco = float(input("digite o valor do segundo teste "))
x = classif.predict([[glicemina, peso, risco]])
if x == 0:
    print("tem diabets!")
elif x == 1:
    print("não tem diabets! ")
else:
    print(" risco de diabets! ")
print("procure um médico mais especializado para ter uma conclusão mais acertiva de sua situação!")
