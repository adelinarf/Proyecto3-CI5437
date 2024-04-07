import time
import csv
from CSP import *


unassigned_var = [mrv,first_unassigned_variable]
order_domain = [lcv,unordered_domain_values]
inf = [forward_checking, mac,no_inference]


def Sudoku_e(s,dom,entry,a=0):
	results = []
	e = Sudoku(s,dom,entry)
	for unassigned in unassigned_var:
		for order in order_domain:
			for i in inf:
				start=time.time()
				try:
					if a==3:
						AC3(e)
					elif a==4:
						AC4(e)
					sol = backtracking_search(e, select_unassigned_variable=unassigned,order_domain_values=order, inference=i)
					end=time.time()
					results.append([sol,end-start,unassigned,order,i])
				except:
					end=time.time()
	return results


def tests_sudoku(test,doms,entry):
	results = [[],[],[],[]]
	s=[]
	s = [0,3,4]
	for x in range(len(test)):
		for f in s:
			res = Sudoku_e(test[x],doms[x],entry,f)
			results[x].append([f,res])
	return results


def create_csv(tests,name):
	with open(name, 'w', newline='') as file:
	    writer = csv.writer(file)
	    field = ["Sudoku","Tiempo","AC3","AC4","FU", "MRV", "UD","LCV","NI","FC","MAC"]
	    writer.writerow(field)
	    for x in range(len(tests)):
	    	for f in range(len(tests[x])):
	    		for y in range(len(tests[x][f][1])):
		    		time = tests[x][f][1][y][1]
		    		unassigned = tests[x][f][1][y][2]
		    		order =  tests[x][f][1][y][3]
		    		inference = tests[x][f][1][y][4]
		    		name = ""
		    		row = []
		    		name = NAMES[x]
		    		if tests[x][f][0]==0:
		    			A = "No"
		    			row = [name,str(time),"","","","","","","","",""]
		    		if tests[x][f][0]==3:
		    			A = "AC3"
		    			row = [name,str(time),"X","","","","","","","",""]
		    		if tests[x][f][0]==4:
		    			A = "AC4"
		    			row = [name,str(time),"","X","","","","","","",""]
		    		if unassigned==unassigned_var[0]: #"First Unassigned Variable"
		    			row[4] = "X"
		    		elif unassigned==unassigned_var[1]: #mrv
		    			row[5] = "X"
		    		if order == order_domain[0]: #unordered domain
		    			row[6] = "X"
		    		elif order == order_domain[1]: #lcv
		    			row[7] = "X"
		    		if inference == inf[0]: #no inference
		    			row[8] = "X"
		    		elif inference == inf[1]: #forward checking
		    			row[9] = "X"
		    		elif inference == inf[2]: #mac
		    			row[10] = "X"
		    		writer.writerow(row)

entry = new_grid_size(3)
NAMES=["EMPTY","HARD1","HARD2","EASY1"]
start = time.time()
test = tests_sudoku([empty,harder1,harder2,easy1],[dom9,dom9,dom9,dom9],entry)
end = time.time()
print("Tiempo de ejecución para pruebas 9x9:",end-start,"segundos")
create_csv(test,"test9x9.csv")

entry = new_grid_size(4)
NAMES = ["HARD16","EMPTY"]
start = time.time()
test = tests_sudoku([superhard16, empty16],[dom16,dom16],entry)
end = time.time()
print("Tiempo de ejecución para pruebas 16x16:",end-start,"segundos")
create_csv(test,"test16x16.csv")

entry = new_grid_size(5)
NAMES = ["EMPTY","HARD25"]
start = time.time()
test =  tests_sudoku([empty25,hard25],[dom25,dom25],entry)
end = time.time()
print("Tiempo de ejecución para pruebas 25x25:",end-start,"segundos")
create_csv(test,"test25x25.csv")

with multiprocessing.pool.Pool() as pool:
	pool.terminate()
