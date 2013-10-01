

""" ejemplo """

#tk = [3, "*", "(", "(", 4, "-", 6, ")", "+", "(", 15, "/", 3, ")", ")", "-", 2]
#tk = [1, "+", 2]
#tk = [1]
#tk = ["*"]
#tk = ["("]
#tk = ["(", ")"]
#tk = ["+", 4]
#tk = ["*", 5]
#tk = [4, "/"]
#tk = ["(", 3, ")"]
#tk = ["(", "+",")"]
#tk = [4, "*", 3, "-"]
#tk = [1, "+", 2, "-", "(", 5, ")"]


print tk
print 


cont_p = 0
flag_bool = True
for i in range(len(tk)):
	if len(tk) == 1:
		if type(tk[i])==int or type(tk[i])==float: continue
		else:
			flag_bool = False
			break
	elif len(tk) == 2:
		if (tk[0]=="(") and (tk[1]==")"): continue
		elif (tk[0]=="+" or tk[0]=="-") and (type(tk[1])==int or type(tk[1])==float): continue
		else:
			flag_bool = False
			break 
	elif len(tk) == 3:
		if (tk[0]=="(") and (type(tk[1])==int or type(tk[1])==float) and (tk[2]==")"): continue 
		elif (type(tk[0])==int or type(tk[0])==float) and (tk[1]=="+" or tk[1]=="-" or tk[1]=="*" or tk[1]=="/" or tk[1]=="^") and (type(tk[2])==int or type(tk[2])==float): continue
		else:
			flag_bool = False
			break 
	else:
		



if cont_p != 0:
	print "Expresion no valida"
elif flag_bool:
	print "Expresion valida"
else:
	print "Expresion no valida"

