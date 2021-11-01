import re
import random
import unidecode
import enum
from tkinter import Tk

tableLenght = 5 #Change this to change the number of rows generated
class Type(enum.Enum):
    #Change the keywords to recognize more types of data
    #Change the values to generare different kinds of data
    #             keywords                                    values
    dataT   = (0,["data","date"],                           ["2021-11-04","2004-05-15","1997-11-04"])
    intT    = (1,["matricola","numero","telefono","codice"],["123","0","1","2"])
    numT    = (2,["voto"],                                  ["27.5","18","22.1"])
    stringT = (3,[""],                                      ["a","b","th","lo"])

    def __init__(self, order,keywords,values):
        self.order = order
        self.keywords = keywords
        self.values = values

def stripSpacesAndAccents(text):
    return unidecode.unidecode(text.strip())

def findType(text):
    text = text.lower()
    for type in Type:
        if any(ext in text for ext in type.keywords):
            return type
    return Type.stringT

def listOfDataOfTypes(types):
    return list(map(lambda x:random.choice(x.values),types))

def joinWithComma(text):
    return ', '.join(text)

def tableInRelaX(tableName,columnsStr,data):
    toRet = tableName + " = {" + joinWithComma(columnsStr)+'\n'+"\n".join(map(joinWithComma,data))+"}\n\n"
    return toRet

output = """group: eserToRelax
description[[

This database was made with eserToRelaX,
you can find it here: https://github.com/Calonca/eserToRelaX

]]

"""
input("Copy the text in the format \nTableName1(culumnName1,culumnName2)\nTableName2(columnName1,columnName2)\nthen press enter")

r = Tk()
inSt = r.clipboard_get()
lines = inSt.split('\n')
for line in lines:
    x=line.split('(')
    tableName = stripSpacesAndAccents(x[0]).replace(" ","_")
    columnsStr = list(map(stripSpacesAndAccents,re.split("[)]",x[1])[0].split(',')))
    types = list(map(findType,columnsStr))
    data = list(map(lambda x:listOfDataOfTypes(types),range(0,tableLenght)))
    output += tableInRelaX(tableName,columnsStr,data)

print("Paste the following inside the group editor, it has also been copied to the clipboard\n")
print(output)

r.withdraw()
r.clipboard_clear()
r.clipboard_append(output)
r.update() # now it stays on the clipboard after the window is closed
r.destroy()
input()
