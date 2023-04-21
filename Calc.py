#!/usr/bin/python3
from functools import reduce
from tkinter import *
import re
import math



window = Tk()
calc_input = ""
result = ""
calc_final = ""
calc_process = ""
x = ""

window.rowconfigure(0, weight=1)
window.rowconfigure(1, weight=0)
window.rowconfigure(2, weight=0)
window.rowconfigure(3, weight=0)
window.rowconfigure(4, weight=0)
window.rowconfigure(5, weight=0)
window.rowconfigure(6, weight=0)
window.rowconfigure(7, weight=0)
window.rowconfigure(8, weight=0)
# On force la taille des colonne avec le paramètre uniform. "same_group" est texte libre.
# Le fait que les 4 colonnes utilisent la même chaîne force la même taille. 
# Les paramètres weight servent uniquement pour que les 4 colonnes utilisent 100% de la 
# largeur de la fenêtre.
window.columnconfigure(0, weight=1, uniform="same_group")
window.columnconfigure(1, weight=1, uniform="same_group")
window.columnconfigure(2, weight=1, uniform="same_group")
window.columnconfigure(3, weight=1, uniform="same_group")

# On définit quelques éléments de style pour nos boutons.
default_button_style = {
    "bg": "#595959", "fg": "white", "highlightthickness": 0,
    "font": ("Arial", 25, "bold")
}

default_close_style = default_button_style | {"bg": "#ffffff", "fg": "black", }
equal_button_style = default_button_style | {"bg": "#f05a2D"}
default_button_grid = {"padx": 10, "pady": 10, "sticky": "nsew"}
default_result_grid = {"padx": 10, "pady": 0, "sticky": "nsew"}


 # Première ligne
result_text = StringVar()
calc_input_text = StringVar()

calc_label = Label(window, textvariable=calc_input_text, anchor='e', bg="#a2af78", fg="white", font=("Arial", 25))
calc_label.grid(column=0, row=0, columnspan=4, **default_result_grid)

result_label = Label(window, textvariable=result_text, anchor='e', bg="#a2af77", fg="white", font=("Arial", 25))
result_label.grid(column=0, row=1, columnspan=4, **default_result_grid)

# Seconde ligne
mc = Button(window, text="MC", command=lambda: clear(), **default_button_style)
mc.grid(column=0, row=2, **default_button_grid)

cos = Button(window, text="Cos", command=lambda: input_key("Cos("), **default_button_style)
cos.grid(column=1, row=2, **default_button_grid)

div = Button(window, text="/", command=lambda: input_key("/"), **default_button_style)
div.grid(column=2, row=2, **default_button_grid)

mul = Button(window, text="*", command=lambda: input_key("*"), **default_button_style)
mul.grid(column=3, row=2, **default_button_grid)

# Troisième ligne
d7 = Button(window, text="7", command=lambda: input_key("7"), **default_button_style)
d7.grid(column=0, row=3, **default_button_grid)

d8 = Button(window, text="8", command=lambda: input_key("8"), **default_button_style)
d8.grid(column=1, row=3, **default_button_grid)

d9 = Button(window, text="9", command=lambda: input_key("9"), **default_button_style)
d9.grid(column=2, row=3, **default_button_grid)

sub = Button(window, text="-", command=lambda: input_key("-"), **default_button_style)
sub.grid(column=3, row=3, **default_button_grid)

# Quatrième ligne
d4 = Button(window, text="4", command=lambda: input_key("4"), **default_button_style)
d4.grid(column=0, row=4, **default_button_grid)

d5 = Button(window, text="5", command=lambda: input_key("5"), **default_button_style)
d5.grid(column=1, row=4, **default_button_grid)

d6 = Button(window, text="6", command=lambda: input_key("6"), **default_button_style)
d6.grid(column=2, row=4, **default_button_grid)

add = Button(window, text="+", command=lambda: input_key("+"), **default_button_style)
add.grid(column=3, row=4, **default_button_grid)

# Cinquième ligne
d1 = Button(window, text="1", command=lambda: input_key("1"), **default_button_style)
d1.grid(column=0, row=5, **default_button_grid)

d2 = Button(window, text="2", command=lambda: input_key("2"), **default_button_style)
d2.grid(column=1, row=5, **default_button_grid)

d3 = Button(window, text="3", command=lambda: input_key("3"), **default_button_style)
d3.grid(column=2, row=5, **default_button_grid)

equalsymb = Button(window, text="=", command=lambda: filterString(),**equal_button_style)
equalsymb.grid(column=3, row=5, rowspan=2, **default_button_grid)

# Cinquième ligne
d0 = Button(window, text="0", command=lambda: input_key("0"), **default_button_style)
d0.grid(column=0, row=6, columnspan=2, **default_button_grid)

dot = Button(window, text=".", command=lambda: input_key("."), **default_button_style)
dot.grid(column=2, row=6, **default_button_grid)

open = Button(window, text="(", command=lambda: input_key("("), **default_button_style)
open.grid(column=0, row=7, **default_button_grid)

close = Button(window, text=")", command=lambda: input_key(")"), **default_button_style)
close.grid(column=1, row=7, **default_button_grid)

tan = Button(window, text="Tan", command=lambda: input_key("Tan("), **default_button_style)
tan.grid(column=2, row=7, **default_button_grid)

Sin = Button(window, text="Sin", command=lambda: input_key("Sin("), **default_button_style)
Sin.grid(column=3, row=7, **default_button_grid)

quitbut = Button(window, text="Close", command=window.quit, **default_close_style)
quitbut.grid(column=0, row=8, columnspan=4, **default_button_grid)

# On change la couleur de fond et les marges de la fenêtre.
window.configure(bg="#333333", padx=10, pady=10)

# On dimensionne la fenêtre (500 pixels de large par 200 de haut).
window.geometry("400x600")

# On ajoute un titre à la fenêtre
window.title("Tut Calculator")


   

def input_key(value):
    global calc_input
    if value == '-' and (len(calc_input) == 0 or re.search(r'[-+*/(\s][-+]*$', calc_input)):
        calc_input += ' '
        print('adding a space')
    calc_input += value
    
    calc_input_text.set(calc_input)
    print(calc_input)

# def input_key(value):
#     global calc_input
#     calc_input += value
#     calc_input_text.set(calc_input)
#     print(calc_input)

def equal(calcul, result):
    # global calc_input
    # global result
    # additions = calc_input.split("+")
    calc_input_text.set(calcul)
    calc_input = str(calcul)
    result_text.set(result)  
    print(result)
   
   
def CosFunc(string, calc_process):
    func_res = str(math.cos(string))
    trigopattern = r'(Cos)\((\d+)\)'
    lookfortrigo = re.search(trigopattern, calc_process)
    if lookfortrigo:
        calc_process = calc_process[:lookfortrigo.start()] + func_res + calc_process[lookfortrigo.end():]
        print('je return le new calc_process:', calc_process)
        calc_process = verifyString(calc_process)
   

def SinFunc(string, calc_process):
    func_res = str(math.sin(string))
    trigopattern = r'(Sin)\((\d+)\)'
    lookfortrigo = re.search(trigopattern, calc_process)
    if lookfortrigo:
        calc_process = calc_process[:lookfortrigo.start()] + func_res + calc_process[lookfortrigo.end():]
        print('je return le new calc_process:', calc_process)
        calc_process = verifyString(calc_process)

def TanFunc(string, calc_process):
    func_res = str(math.tan(string))
    trigopattern = r'(Tan)\((\d+)\)'
    lookfortrigo = re.search(trigopattern, calc_process)
    if lookfortrigo:
        calc_process = calc_process[:lookfortrigo.start()] + func_res + calc_process[lookfortrigo.end():]
        print('je return le new calc_process:', calc_process)
        calc_process = verifyString(calc_process)
    
    
    
    
def verifyString(calc_process):
    #checking the prio V1
        global calc_input
        global calc_final
      
        print('my process: ',calc_process)
        
        
        #clear trigo first then we have fun
        trigopattern = r'(Cos|Sin|Tan)\((\d+)\)'
        lookfortrigo = re.search(trigopattern, calc_process)
        if lookfortrigo:
            func_name = lookfortrigo.group(1)
            x = float(lookfortrigo.group(2))
            if func_name == 'Cos':
                print('jappelle Cos')
                calc_process = CosFunc(x, calc_process)
            elif func_name == 'Sin':
                calc_process = SinFunc(x, calc_process)
            elif func_name == 'Tan':
                calc_process = TanFunc(x, calc_process)
        
        else:
            print('this is my calc process', calc_process)
            pattern = r"\(([^\(\)]+)\)"
            match = re.search(pattern, calc_process)
            if match:
                calc_final= match.group(1)
                print('Found: ', calc_final)        
            else: 
                calc_final = calc_process
            s = re.findall(r"(?<!\d)-?\d+(?:\.\d+)?(?!\d)|\D", calc_final.replace(' ', ''))
            s = [elem for elem in s if elem]

            print('my split: ', s)
            
            for i in range(len(s)):
                if s[i] == "":
                    s[i] = 0
            print('MY LENTGH IS: ',len(s))
            print('I HAVE: ',s)
            
            pattern = r"\(([^\(\)]+)\)"
            match = re.search(pattern, calc_process)
            if match and len(s) == 1:
                    print('jai un solo parenthese:', s)
                    r = float(s[0])
                    if r < 0:
                        calc_process = calc_process.replace('( {})'.format(s[0]),str(r))
                        print('Found go back and process negative: ', calc_process) 
                        return verifyString(calc_process)
                    else:
                        calc_process = calc_process.replace('({})'.format(s[0]),str(r))
                        print('Found go back and process positive: ', calc_process) 
                        return verifyString(calc_process)
            
            
            if len(s) > 1: 
                while len(s) > 1:
                    
                    if ('/' in s or
                        '*' in s):
                        for i in range(len(s)):
                            print('check multiplier',s)
                            if s[i] == '/':
                                print('divide',s)
                                s[i] = float(s[i-1]) / float(s[i+1])
                                s.pop(i-1)
                                s.pop(i)
                            
                                break
                            elif s[i] == '*':
                                print('multiply',s)
                                s[i] = float(s[i-1]) * float(s[i+1])
                                s.pop(i-1)
                                s.pop(i)
                                break
                    else:
                        for i in range(len(s)):
                            if s[i] == '-':
                                print('minus',s)
                                s[i] = float(s[i-1]) - float(s[i+1])
                                s.pop(i-1)
                                s.pop(i)
                                break
                            elif s[i] == '+':
                                print('plus',s)
                                s[i] = float(s[i-1]) + float(s[i+1])
                                s.pop(i-1)
                                s.pop(i)
                                break
                    result = s[0]
                    print('current res', result)
                #check if there are parentheses
            
                pattern = r"\(([^\(\)]+)\)"
                match = re.search(pattern, calc_process)
                if match:
                    calc_process = calc_process.replace('({})'.format(calc_final),str(result))
                    print('Found go back and process: ', calc_process) 
                    return verifyString(calc_process)
                else:
                    
                    
                    print('fini voici la string final', calc_process)
                    result = float(result)
                    equal(calc_input, result)
                    
                    return result
            else:
                result = float(s)
                print(calc_input)
                print('my result is: ', result)
                print('my calcul is: ', calc_input)
                equal(calc_input, result)


        
    
def filterString():
    global calc_input
    global calc_process   
    calc_process = calc_input 
    verifyString(calc_process)
       
    
    
    
   
def clear():
    
    global calc_input
    result = 0
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set("")
    
window.mainloop()


