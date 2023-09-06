
from tkinter import *
import tkinter as tk
import Input as i
from Table import Table
from constants import *
from functions import *
from PfeFrame import *
root = Tk()
experiment = PfeFrame(root)
root.configure(background=BACKGROUND)
varList = {
    "lambda": StringVar(),
    "mu": StringVar(),
    "k": StringVar(), 
    "N": StringVar(), 
    "start": StringVar(), 
    "end": StringVar(),
    "N_exp": StringVar(), 
    "lambda_min": StringVar(), 
    "lambda_max": StringVar(),
    "mu_min": StringVar(),
    "mu_max": StringVar(),
}

def work_pfe(Event):
    try:
        lambda_min = float(varList["lambda_min"].get())
        lambda_max = float(varList["lambda_max"].get())
        mu_min = float(varList["mu_min"].get())
        mu_max = float(varList["mu_max"].get())
        count = float(varList["N"].get())
        global lab
        va = experiment.run(
            lambda_min=lambda_min,
            lambda_max=lambda_max,
            mu_max=mu_max,
            mu_min=mu_min, 
            count=count, 
        )
        vals = []
        for i in range(len(va)):
            if va[i] > 0 and i != 0:
                vals.append("+{:.3f}".format(va[i]))
            else:
                vals.append("{:.3f}".format(va[i]))
        lab.config(text = "Лин. модель: y={}*x0{}*x1{}*x2; Чнл модель: y={}*x0{}*x1{}*x2{}*x12".format(vals[0],
                                                                                                            vals[1],
                                                                                                            vals[2],
                                                                                                            vals[0],
                                                                                                            vals[1],
                                                                                                            vals[2],
                                                                                                            vals[3]))
        add_button.config(state='normal')
    except ValueError:
        tk.messagebox.showinfo(title="error", message="Ошибка ввода параметров!")

def work_one(Event): 
    lam = float(varList["lambda"].get())
    mu = float(varList["mu"].get())
    experiment.count_one(lam=lam, mu=mu,)

def pfe_inputs(root):

    frame_inputs = Frame(root)
    items_1 = [
        i.Item(text="Минимум:", var=varList["lambda_min"], value=0.02), # 0.099
        i.Item(text="Максимум:", var=varList["lambda_max"], value=0.1), # 0.1
    ]
    items_2 = [
        i.Item(text="Минимум:", var=varList["mu_min"], value=0.15), # 0.098
        i.Item(text="Максимум:", var=varList["mu_max"], value=0.2), # 0.1
    ]
    i_list_1 = i.InputList(master=frame_inputs, items=items_1, title="Интенсивность поступления заявок")
    i_list_2 = i.InputList(master=frame_inputs, items=items_2, title="Интенсивность обработки заявок")

    i_list_1.pack(side=LEFT, padx=10, pady=10)
    i_list_2.pack(side=LEFT,  padx=10, pady=10)

    frame_inputs.grid(column=1)

    items_4 = [
        i.Item(text="Число заявок:", var=varList["N"], value=5000), 
    ]

    i_list_4 = i.InputList(master=root, items=items_4)
    i_list_4.grid(column=1,  padx=10, pady=10)

    btn = Button(root, text="Запуск", background=BACKGROUND)
    btn.bind("<Button-1>", work_pfe)
      
    btn.grid(column=1, padx=10, pady=10) 

def draw_new_point(root):
    items = [
        i.Item(text="Интенсивность поступления заявок:", var=varList["lambda"], value=0.08),
        i.Item(text="Интенсивность обслуживания заявок:", var=varList["mu"], value=0.18),
    ]
    i_list = i.InputList(master=root, items=items, title="Добавление точки факторного пространства")
    i_list.grid(column=1)

    btn = Button(root, text="Добавить", state=DISABLED, background=BACKGROUND)
    btn.bind("<Button-1>", work_one)       
    btn.grid(column=1, padx=10, pady=10)
    btn.config(state="disabled")
    return btn

if __name__ == '__main__':
    f_pfe = Frame(root, highlightbackground="black",  background=BACKGROUND)
    f_one = Frame(root, highlightbackground="black", background=BACKGROUND)
    lab = tk.Label(f_pfe, text="Лин. модель: y=b0*x0+b1*x1+b2*x2; Чнл модель: y=b0*x0+b1*x1+b2*x2+b12*x12")
    lab.grid(column=1,  padx=10, pady=10)
    
    pfe_inputs(f_pfe)
    add_button = draw_new_point(f_one)
    f_pfe.grid(row=0, column=0,  padx=100, pady=10)
    f_one.grid(row=1, column=0,  padx=100, pady=10)

    experiment.grid(row=2, column=0, columnspan=2,   padx=10, pady=10)

    
    root.mainloop()
    

    
