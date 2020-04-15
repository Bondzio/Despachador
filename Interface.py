from tkinter import *
from functools import partial 

class MultiListbox(Frame):
    def __init__(self, master, lists):
        Frame.__init__(self, master)
        self.lists = []
        for l,w in lists:
            frame = Frame(self); frame.pack(side=LEFT, expand=YES, fill=BOTH)
            Label(frame, text=l, borderwidth=1, relief=RAISED).pack(fill=X)
            lb = Listbox(frame, width=w, borderwidth=0, selectborderwidth=0,
                 relief=FLAT, exportselection=FALSE)
            lb.pack(expand=YES, fill=BOTH)
            self.lists.append(lb)
            lb.bind('<B1-Motion>', lambda e, s=self: s._select(e.y))
            lb.bind('<Button-1>', lambda e, s=self: s._select(e.y))
            lb.bind('<Leave>', lambda e: 'break')
            lb.bind('<B2-Motion>', lambda e, s=self: s._b2motion(e.x, e.y))
            lb.bind('<Button-2>', lambda e, s=self: s._button2(e.x, e.y))
        frame = Frame(self); frame.pack(side=LEFT, fill=Y)
        Label(frame, borderwidth=1, relief=RAISED).pack(fill=X)
        sb = Scrollbar(frame, orient=VERTICAL, command=self._scroll)
        sb.pack(expand=YES, fill=Y)
        self.lists[0]['yscrollcommand']=sb.set

    def _select(self, y):
        row = self.lists[0].nearest(y)
        self.selection_clear(0, END)
        self.selection_set(row)
        return 'break'

    def _button2(self, x, y):
        for l in self.lists: l.scan_mark(x, y)
        return 'break'

    def _b2motion(self, x, y):
        for l in self.lists: l.scan_dragto(x, y)
        return 'break'

    def _scroll(self, *args):
        for l in self.lists:
            apply(l.yview, args)

    def curselection(self):
        return self.lists[0].curselection()

    def delete(self, first, last=None):
        for l in self.lists:
            l.delete(first, last)

    def get(self, first, last=None):
        result = []
        for l in self.lists:
            result.append(l.get(first,last))
            if last: return apply(map, [None] + result)
            return result
        
    def index(self, index):
        self.lists[0].index(index)

    def insert(self, index, *elements):
        for e in elements:
            i = 0
            for l in self.lists:
                l.insert(index, e[i])
                i = i + 1

    def size(self):
        return self.lists[0].size()

    def see(self, index):
        for l in self.lists:
            l.see(index)

    def selection_anchor(self, index):
        for l in self.lists:
            l.selection_anchor(index)

    def selection_clear(self, first, last=None):
        for l in self.lists:
            l.selection_clear(first, last)

    def selection_includes(self, index):
        return self.lists[0].selection_includes(index)

    def selection_set(self, first, last=None):
        for l in self.lists:
            l.selection_set(first, last)

if __name__ == '__main__':

    tk = Tk()
    originalList = [["B",300],["D",100],["F",500],["H",700],["J",300],["L",3000],["N",50],["O",600],["A",400],["C",50],["E",1000],["G",10],["I",450],["K",100],["M",80],["P",800],["Ñ",500]]
    tk.geometry('1180x400')
    tk.title("Despachador")

    quantum = StringVar()
    contexto = StringVar()
    bloqueo = StringVar()

    l1 = Label(tk, text="Quantum", font=("Arial", 15))
    l1.grid(column=0, row=0)
    tx1 = Entry(tk, textvariable=quantum, width=10)
    tx1.grid(column=1, row=0)
    l2 = Label(tk, text="Cambio de Contexto", font=("Arial", 15))
    l2.grid(column=0, row=1)
    tx2 = Entry(tk, textvariable=contexto, width=10)
    tx2.grid(column=1, row=1)
    l3 = Label(tk, text="Tiempo de Bloqueo", font=("Arial", 15))
    l3.grid(column=0, row=2)
    tx3 = Entry(tk, textvariable=bloqueo, width=10)
    tx3.grid(column=1, row=2)
    l3 = Label(tk)
    l3.grid(column=0, row=3)

    def operacion(n1, n2, n3):  
        num1 = (n1.get())  
        num2 = (n2.get())
        num3 = (n3.get()) 
        sum_num = int(num1)+int(num2)+int(num3) 


        for i in range(len(originalList)):
        	mlb.insert(END, (originalList[i][0], tx2.get(), originalList[i][1], tx1.get(), tx3.get(), sum_num+originalList[i][1], '0', sum_num+originalList[i][1]))
          

    operacion = partial(operacion, quantum, contexto, bloqueo)

    btn1 = Button(tk, text="Calcular", fg="blue", command=operacion)
    btn1.grid(column=4, row=1)

    btn2 = Button(tk, text="Resetear", fg="blue")
    btn2.grid(column=5, row=1)

    mlb = MultiListbox(tk, (('Proceso', 20), ('TCC', 10), ('TE', 10),('TVC', 10),('TB', 10),('TT', 20),('TI', 10),('TF', 10)))
    mlb.grid(row=4,column=1)

    tk.mainloop()


























