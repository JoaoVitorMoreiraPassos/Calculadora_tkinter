from tkinter import Tk
from tkinter import Button
from tkinter import Label
from tkinter import PhotoImage
from functools import partial
        

class Calculator():
    def __init__(self):
        self.start()
        
    def start(self):
        self.equation = ''
        self.interface()
            
    def add_num(self, num):
        if self.equation:
            if self.equation[-1] == ')':
                self.equation += 'x'   
        self.equation += num
        self.input_equation['text'] = self.equation
        self.calc()
       
    def isnum(self, var):
        try:
            float(var)
            return True
        except:
            return False
    def isoperator(self, op):
        if op == 'x' or op == '/' or op == '-' or op == '+' or op == '%':
            return True
        return False
    
    def add_operation(self, operator):
        if self.equation:
            temp = self.equation[-1]
            if temp == 'x' or temp == '/' or temp == '-' or temp == '+' or temp == '%' or temp == ',':
                self.equation = self.equation[:-1]
            self.equation += operator
            self.input_equation['text'] = self.equation
    
    def add_separetor(self):
        try:
            temp = int(self.equation[-1])
            self.equation += ','
        except:
            if self.equation:
                if self.equation[-1] == ')':
                    self.equation += 'x'
            self.equation += '0,' 
        self.input_equation['text'] = self.equation
             
    def add_parentheses(self):
        open = 0
        close = 0
        pos = 0
        for i in self.equation:
            if i == '(':
                open += 1
                ṕos = i
            if i == ')':
                close += 1

        if open == close or open == 0:
            try:
                temp = self.equation[-1]                    
                if temp == ')' or self.isnum(temp) or temp == ',':
                    self.equation += 'x'    
            except:
                pass
            self.equation += '('
        else:
            if self.isoperator(self.equation[-1]) or self.equation[-1] == '(':
                self.equation += "("
            else:
                self.equation += ')'
        self.input_equation['text'] = self.equation
        self.calc()
    
    def calc(self):
        equation = self.equation
        equation = equation.replace('x', '*')
        equation = equation.replace(',', '.')
        if '%' in equation:
            try:
                equation = equation.split('%')
                x = eval(equation[0])
                for i in range(1, len(equation)):
                    x = (x / 100) * eval(equation[i])
                self.result['text'] = round(x, 2)
            except:
                pass
        else:
            try:
                if(str(eval(equation)) != equation):
                    self.result['text'] = eval(equation)
                else:
                    self.result['text'] = ''
            except:
                self.result['text'] = ''
    
    def backspace(self):
        self.equation = self.equation[:-1]
        self.input_equation['text'] = self.equation
        self.calc()
            
    def clean(self):
        self.equation = ''
        self.input_equation['text'] = ''
        self.result['text'] = ''
        
    def interface(self):
        self.win = Tk()
        self.win.title("Calculator")
        self.win.geometry('265x460')
        self.win.resizable(width=False, height=False)
        self.win['bg'] = '#000'
    
        self.input_equation = Label(self.win, justify='right', anchor='e', font=30, wraplength=250, bg='#000', padx=15, foreground='white')
        self.result         = Label(self.win, justify='right', anchor='e', font=16, bg='#000', padx=15, foreground='white')
        self.input_equation.place(x=5,y=0, width=265, height=80)
        self.result.place(x=5,y=70, width=265, height=35)
        
        w, h = 60, 60
        img_clean   = PhotoImage(file="imagens/clean.png")
        img_par     = PhotoImage(file="imagens/parentheses.png")
        img_percent = PhotoImage(file="imagens/percent.png"   )
        img_div     = PhotoImage(file="imagens/div.png"       )
        img_7       = PhotoImage(file="imagens/7.png"         )
        img_8       = PhotoImage(file="imagens/8.png"         )
        img_9       = PhotoImage(file="imagens/9.png"         )
        img_multi   = PhotoImage(file="imagens/multi.png"     )
        img_4       = PhotoImage(file="imagens/4.png"         )
        img_5       = PhotoImage(file="imagens/5.png"         )
        img_6       = PhotoImage(file="imagens/6.png"         )
        img_less    = PhotoImage(file="imagens/less.png"      )
        img_1       = PhotoImage(file="imagens/1.png"         )
        img_2       = PhotoImage(file="imagens/2.png"         )
        img_3       = PhotoImage(file="imagens/3.png"         )
        img_plus    = PhotoImage(file="imagens/plus.png"     )
        img_equal   = PhotoImage(file="imagens/equal.png"     )
        img_sep     = PhotoImage(file="imagens/sep.png"       )
        img_back    = PhotoImage(file="imagens/back.png"      )
        img_0       = PhotoImage(file="imagens/0.png"         )
        
        clean   = Button(self.win, image=img_clean  , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0,command=self.clean)
        paren   = Button(self.win, image=img_par    , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0, command=self.add_parentheses)
        percent = Button(self.win, image=img_percent, bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0, command=partial(self.add_operation, '%'))
        div     = Button(self.win, image=img_div    , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0, command=partial(self.add_operation, '/'))
        
        btn7    = Button(self.win, image=img_7      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '7'))
        btn8    = Button(self.win, image=img_8      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '8'))
        btn9    = Button(self.win, image=img_9      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '9'))
        multi   = Button(self.win, image=img_multi  , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0, command=partial(self.add_operation, 'x'))
        
        btn4    = Button(self.win, image=img_4      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '4'))
        btn5    = Button(self.win, image=img_5      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '5'))
        btn6    = Button(self.win, image=img_6      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '6'))
        less    = Button(self.win, image=img_less   , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0, command=partial(self.add_operation, '-'))
        
        btn1    = Button(self.win, image=img_1      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '1'))
        btn2    = Button(self.win, image=img_2      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '2'))
        btn3    = Button(self.win, image=img_3      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '3'))
        plus    = Button(self.win, image=img_plus   , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0, command=partial(self.add_operation, '+'))
        
        equal   = Button(self.win, image=img_equal  , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=self.calc)
        sep     = Button(self.win, image=img_sep    , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0     , command=self.add_separetor)
        backsp  = Button(self.win, image=img_back   , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=self.backspace)
        zero    = Button(self.win, image=img_0      , bg='#000', activebackground="#000",anchor="center", borderwidth=0, highlightbackground="#000", border=0   , bd=0  , command=partial(self.add_num, '0'))

        clean.place  (x= 5        , y= 145 , width= w, height= h)
        paren.place  (x= w + 10   , y= 145 , width= w, height= h)
        percent.place(x= w*2 + 15 , y= 145 , width= w, height= h)
        div.place    (x= w*3 + 20 , y= 145 , width= w, height= h)
        
        btn7.place   (x= 5        , y= 205 , width= w, height= h)
        btn8.place   (x= w + 10   , y= 205 , width= w, height= h)
        btn9.place   (x= w*2 + 15 , y= 205 , width= w, height= h)           
        multi.place  (x= w*3 + 20 , y= 205 , width= w, height= h)
        
        btn4.place   (x= 5        , y= 265, width= w, height= h)
        btn5.place   (x= w + 10   , y= 265, width= w, height= h)
        btn6.place   (x= w*2 + 15 , y= 265, width= w, height= h)           
        less.place   (x= w*3 + 20 , y= 265, width= w, height= h)
        
        btn1.place   (x= 5        , y= 325, width= w, height= h)
        btn2.place   (x= w + 10   , y= 325, width= w, height= h)
        btn3.place   (x= w*2 + 15 , y= 325, width= w, height= h)           
        plus.place   (x= w*3 + 20 , y= 325, width= w, height= h)
        
        backsp.place (x=5         , y= 385, width= w, height= h) 
        zero.place   (x= w + 10   , y= 385, width= w, height= h)
        sep.place    (x= w*2 + 15 , y= 385, width= w, height= h)
        equal.place  (x= w*3 + 20 , y= 385, width= w, height= h)
        self.win.mainloop()
        
        
if __name__ == '__main__':
    Calculator()