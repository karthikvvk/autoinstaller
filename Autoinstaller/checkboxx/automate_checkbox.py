"""
cr_checkbox(): takes the tkinter window object and the items to be listed as arguments and return checkbox objects as list.
fetch_cked_val(): takes the list returned by cr_checkbox() as argument and return a list of checked/selected items.
**NOTE: ONLY WORK FOR TKINTER.
    >Default  layout managers is .grid()
    >Please change according  to your prefered layout managers(.place(), .pack(), etc..).
"""
from tkinter import *

vari = []
seq = []


def cr_checkbox(tk_window_object, sequence, bg='white', fg='black', row_lb=0, column_lb=0):
    global vari, seq
    vari, seq, row_l = [], [], []
    len_seq = len(sequence)
    seq = sequence

    for y in range(row_lb, len_seq + row_lb):
        row_l.append(y)

    for i in range(len_seq):
        vari.append('a' + str(i))
        vari[i] = BooleanVar(tk_window_object, value=False)

    for i in range(len_seq):
        Checkbutton(tk_window_object, text=sequence[i], variable=vari[i], bg=bg, justify='left', fg=fg).grid(
            row=row_l[i], column=column_lb)

    return vari


def fetch_cked_val(chbx_obj):
    global seq

    bx_chked = []
    t = 0
    for t in range(len(seq)):
        if chbx_obj[t].get() == True:
            bx_chked.append(seq[t])

    return bx_chked
