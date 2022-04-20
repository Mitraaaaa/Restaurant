import re
import networkx as nx
import random
import string 
number_of_foods = int(input())
nod = int(input())
with open("test_data.txt", "w") as out:
	for _ in range(number_of_foods):
		le = 5
		foods = {}
		food_eff = {}
		for i in range(nod):
			s = ''.join(random.choices(string.ascii_uppercase + string.digits, k = le))
			foods[s] = []
			food_eff[s] = random.randint(1, 20)
		G=nx.gnp_random_graph(nod,0.5,directed=True)
		fl = list(foods.keys())
		DAG = nx.DiGraph([(fl[u],fl[v],{'weight':random.randint(-nod,nod)}) for (u,v) in G.edges() if u<v])
		for v in fl:
			for u in list(DAG.adj[v]):
				foods[u].append(v)
		out.write("New Food:\n")
		mn = list(nx.topological_sort(DAG))
		mn = mn[-1]
		out.write(mn+'\n')
		for f in fl:
			out.write(f+' ')
			for d in foods[f]:
				out.write(d+' '+str(food_eff[d])+' ')
			out.write('\n')
		out.write("End of instructions\n")	
	
