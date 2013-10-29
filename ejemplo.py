

""" ejemplo """

#tk = [3, "*", "(", "(", 4, "-", 6, ")", "+", "(", 15, "/", 3, ")", ")", "-", 2]
#tk = [1, "+", 2]
tk = [1]
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
	if len(tk)==1:
		if type(tk[i])==int or type(tk[i])==float: continue 
		else: 
			flag_bool = False
			break 
	elif len(tk)==2:
		if tk[i]=='(' and tk[i+1]==')': continue 
		elif (tk[i]=='+' or tk[i]=='-') and (type(tk[i+1])==int or type(tk[i+1])==float): continue 
		else:
			flag_bool = False
			break 
	else:
		if (i==0) and (tk[i]=='+' or tk[i]=='-') and (tk[i+1]=='(' or type(tk[i+1])==int or type(tk[i+1])==float): 
			continue 
		elif (i==0) and (tk[i]=='(') and (tk[i+1]=='(' or tk[i+1]=='+' or tk[i+1]=='-' or type(tk[i+1])==int or type(tk[i+1])==float): 
			cont_p += 1
			continue 
		elif (i==0) and (type(tk[i])==int or type(tk[i])==float) and (tk[i+1]=='+' or tk[i+1]=='-' or tk[i+1]=='*' or tk[i+1]=='/' or tk[i+1]=='^'): 
			continue 
		elif (i>0 and i<(len(tk)-1)):
			if tk[i]=='(': 
				cont_p += 1
			elif tk[i]==')': 
				cont_p -= 1
	        continue
	    elif (i==(len(tk)-1)) and (((tk[i-1]=='+' or tk[i-1]=='-' or tk[i-1]=='*' or tk[i-1]=='/' or tk[i-1]=='^') and (type(tk[i])==int or type(tk[i])==float)) or ((tk[i-1]==')' or (type(tk[i-1])==int or type(tk[i-1])==float)) and tk[i]==')')): 
	    	if tk[i]==')': 
				cont_p -= 1 
				continue 
	    #else:
	    #	flag_bool = False
	    #	break 
	    #elif (i>0 and i<(len(tk)-1)) and (((tk[i]=='(' and tk[i-1]=='(' and (type(tk[i+1])==int or type(tk[i+1])==float)) or (tk[i]=='(' and (tk[i-1]=='+' or tk[i-1]=='-' or tk[i-1]=='*' or tk[i-1]=='/' or tk[i-1]=='^') and (type(tk[i+1])==int or type(tk[i+1])==float)) or (tk[i]=='(' and tk[i-1]=='(' and (tk[i+1]=='+' or tk[i+1]=='-')) or (tk[i]=='(' and (tk[i-1]=='+' or tk[i-1]=='-' or tk[i-1]=='*' or tk[i-1]=='/' or tk[i-1]=='^') and (tk[i+1]=='+' or tk[i+1]=='-'))) or ((tk[i-1]=='(' and (tk[i]=='+' or tk[i]=='-') and (type(tk[i+1])==int or type(tk[i+1])==float)) or ((type(tk[i-1])==int or type(tk[i-1])==float) and (tk[i]=='+' or tk[i]=='-' or tk[i]=='*' or tk[i]=='/' or tk[i]=='^') and (type(tk[i+1])==int or type(tk[i+1])==float)) or ((tk[i-1]=='(' and (tk[i]=='+'or tk[i]=='-') and tk[i+1]=='(') or ((type(tk[i-1])==int or type(tk[i-1])==float) and (tk[i]=='+' or tk[i]=='-' or tk[i]=='*' or tk[i]=='/' or tk[i]=='^') and tk[i+1]=='('))) or ((tk[i-1]=='(' and (type(tk[i])==int or type(tk[i])==float) and (tk[i+1]==')' or (tk[i+1]=='+' or tk[i+1]=='-' or tk[i+1]=='*' or tk[i+1]=='/' or tk[i+1]=='^'))) or ((tk[i-1]=='+' or tk[i-1]=='-' or tk[i-1]=='*' or tk[i-1]=='/' or tk[i-1]=='^') and (type(tk[i])==int or type(tk[i])==float) and (tk[i+1]==')' or (tk[i+1]=='+' or tk[i+1]=='-' or tk[i+1]=='*' or tk[i+1]=='/' or tk[i+1]=='^'])))) or ((tk[i-1]==')' and tk[i]==')' and (tk[i+1]==')' or (tk[i+1]=='+' or tk[i+1]=='-' or tk[i+1]=='*' or tk[i+1]=='/' or tk[i+1]=='^'))) or ((type(tk[i-1])==int or type(tk[i-1])==float) and tk[i]==')' and (tk[i+1]==')' or (tk[i+1]=='+' or tk[i+1]=='-' or tk[i+1]=='*' or tk[i+1]=='/' or tk[i+1]=='^'))))): 
	        

if cont_p != 0:
	print "Expresion no valida"
elif flag_bool:
	print "Expresion valida"
else:
	print "Expresion no valida"

