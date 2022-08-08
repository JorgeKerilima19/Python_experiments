
list=["[","}","}","[","]","}","}"]
New_list=["[","{","}","[","]","{","]"]
lista3=["[","{","}","[","]","{","]","{","{","[","[","]",]

def comprobador(lst):
    variables_sin_par=[]
    while len(lst)>0:
        pares=[]
        variable1=lst[0]
        variable2=None

        if variable1==chr(93) and chr(91) in lst:
            variable2=lst.index(chr(91))
            lst.pop(variable2)
            par=[variable1,variable2]

        elif variable1==chr(91) and chr(93) in lst:
            variable2=lst.index(chr(93))
            lst.pop(variable2)
            par=[variable2,variable1]

        elif variable1==chr(123) and chr(125) in lst:
            variable2=lst.index(chr(125))
            lst.pop(variable2)
            par=[variable1,variable2]

        elif variable1==chr(125) and chr(123) in lst:
            variable2=lst.index(chr(123))
            lst.pop(variable2)
            par=[variable2,variable1]

        else:
            variables_sin_par.append(variable1)
        lst.pop(0)
        pares.append(par)
    print("Los elementos sin un par son ",len(variables_sin_par)," Y son los siguientes: ",variables_sin_par)

comprobador(lista3)
"""print(ord("{"))#123
print(ord("}"))#125
print(ord("["))#91
print(ord("]"))#93"""
