"""
Creates checkboxes using the given sequence and return the checkbox objects in 'vari'
Also can get the checked items using fetch_cked_val(); return as list
That is 'print(cr_checkbox(tk_window_object, sequence)[1])' will print all the checkbox's objects.
And

for i in cr_checkbox(tk_window_object, sequence)[1]:
        print(i.get())

the above will print the value(1 or 0), that is the status of checked(1) or unchecked(0).
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
