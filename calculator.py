from tkinter import *
from tkinter import messagebox
from math import *


def clear_all():
    output['state'] = NORMAL
    output.delete(0, 'end')
    output.insert(0, '0')
    output['state'] = DISABLED


def add_long(a, b):
    check = 0
    final = ''
    if len(a) >= len(b):
        length = len(a)
        b = '0' * (length - len(b)) + b
    else:
        length = len(b)
        a = '0' * (length - len(a)) + a
    for i in range(length):
        res = int(a[length - i - 1]) + int(b[length - i - 1]) + check
        check = res // 10
        sum = str(res % 10)
        final = sum + final
    return final


def sub_long(a, b):
    check = 0
    res = 0
    final = ''
    sign = ''
    if int(b) > int(a):
        c = a
        a = b
        b = c
        sign = '-'
    length = len(a)
    b = '0' * (length - len(b)) + b
    for i in range(length):
        res = int(a[length - i - 1]) - int(b[length - i - 1]) + check
        check = res // 10
        sum = str(abs(res % 10))
        final = sum + final
    j=0
    while j < len(final) and final[j] == '0':
        j += 1
    if j == len(final):
        final = '0'
    else:

        final = final[j:len(final)]
    return sign + final


def clear_1():
    temp = output.get()
    output['state'] = NORMAL
    output.delete(len(temp) - 1, 'end')
    if len(temp) == 1:
        output.delete(len(temp) - 1, 'end')
        output.insert(0, '0')
    output['state'] = DISABLED


def add_digit(digit):
    temp = output.get()
    output['state'] = NORMAL
    if temp[0] == '0' and len(temp) == 1:
        temp = temp[1:]
    output.delete(0, 'end')
    output.insert(0, temp + digit)
    output['state'] = DISABLED


def add_operation(operation):
    temp = output.get()
    output['state'] = NORMAL
    if temp[-1] in '+-*/^':
        temp = temp[:-1]
    elif len(temp) >= 2 and temp[-2] in '√(' and operation != '-':
        temp = temp[:-3]
    output.delete(0, 'end')
    output.insert(0, temp + operation)
    output['state'] = DISABLED


def add_root():
    temp = output.get()
    output['state'] = NORMAL
    square = '√('
    if temp[-1] == '0':
        temp = temp[:-1]
    elif temp[-1] not in '+-**/^':
        square = '*√('
    elif temp[-2] in '**':
        temp = temp[:-2]
    elif temp[-2] in '√(':
        temp = temp[:-2]
    output.delete(0, 'end')
    output.insert(0, temp + square)
    output['state'] = DISABLED


def find_num():
    temp = output.get()
    i = 0
    b = 0
    while i < len(temp):
        if temp[i] in '/*-+^√()':
            b = i
        i += 1
    c = temp[b + 1:len(temp)]
    return c


def add_dot():
    temp = output.get()
    output['state'] = NORMAL
    if '.' in find_num():
        print('error')
    elif temp[-1] in '/*-+^√()':
        print('error')
    else:
        output.delete(0, 'end')
        output.insert(0, temp + '.')
    output['state'] = DISABLED


def add_brackets(bracket):
    temp = output.get()
    output['state'] = NORMAL
    if bracket == '(':
        if temp[0] == '0' and len(temp) == 1:
            temp = temp[:-1]
        elif temp[-1] not in '/**-+^':
            bracket = '*('
    output.delete(0, 'end')
    output.insert(0, temp + bracket)
    output['state'] = DISABLED


def equal():
    temp = output.get()
    output['state'] = NORMAL
    output.delete(0, 'end')
    res_1 = temp.replace('^', '**')
    res = res_1.replace('√', 'sqrt')
    try:
        output.insert(0, eval(res))
    except (NameError, ValueError, SyntaxError, TypeError):
        messagebox.showinfo('Error', "It's impossible")
        output.insert(0, '0')
    except ZeroDivisionError:
        messagebox.showinfo('Error', "You can't divide by zero")
        output.insert(0, '0')
    output['state'] = DISABLED


def round_num():
    temp = output.get()
    output['state'] = NORMAL
    temp = str(round(float(temp)))
    output.delete(0, 'end')
    output.insert(0, temp)
    output['state'] = DISABLED


def make_button(digit):
    return Button(frame, text=digit, bg='white', font=('Arial', 35), command=lambda: add_digit(digit),
                  activebackground='yellow', background='#FFE089')


def make_operation(operation):
    return Button(frame, text=operation, bg='white', font=('Arial', 35), command=lambda: add_operation(operation),
                  activebackground='yellow', background='#FFE089', foreground='#A64E00')


def make_root():
    return Button(frame, text='√', bg='white', font=('Arial', 35), command=lambda: add_root(),
                  activebackground='yellow', background='#FFE089')


def make_dot():
    return Button(frame, text='.', bg='white', font=('Arial', 35), command=lambda: add_dot(), activebackground='yellow',
                  background='#FFE089')


def make_equal():
    return Button(frame, text='=', bg='white', font=('Arial', 35), command=lambda: equal(), activebackground='yellow',
                  background='#FFE089')


def make_brackets(bracket):
    return Button(frame, text=bracket, bg='white', font=('Arial', 35), command=lambda: add_brackets(bracket),
                  activebackground='yellow', background='#FFE089')


def press_key(key):
    if key.char.isdigit():
        add_digit(key.char)
    elif key.char in '+-*/':
        add_operation(key.char)
    elif key.char == '\x08':
        clear_1()
    elif key.char == '\r':
        equal()
    elif key.char == '(' or key.char == ')':
        add_brackets(key.char)
    elif key.char == '.':
        add_dot()


root = Tk()

root.title('Calculator')
w = 600
h = 700
# photo = PhotoImage(file='calculator.png')
# root.iconphoto(False, photo)
root.geometry(f'{w}x{h}+500+100')
root.config(bg='#A4F7FF')
#root.resizable(False, False)
root.bind('<Key>', press_key)

label = Label(root, text='Minecraft 2.0', bg='#A4F7FF', fg='black', font=('comic sans ms', 20, 'bold'))
label.pack()

frame = Frame(root, bg='gray')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.8)

output = Entry(frame, justify=RIGHT, bg='white', font=('Arial', 20), width=15)
output.place(relx=0.04, rely=0.04, relwidth=0.92, relheight=0.1)
output.insert(0, '0')
output['state'] = DISABLED

make_button('0').place(relx=0.04, rely=0.85, relheight=0.12, relwidth=0.16)
make_dot().place(relx=0.23, rely=0.85, relheight=0.12, relwidth=0.16)
make_equal().place(relx=0.42, rely=0.85, relheight=0.12, relwidth=0.16)
make_operation('+').place(relx=0.61, rely=0.85, relheight=0.12, relwidth=0.16)
make_operation('^').place(relx=0.80, rely=0.85, relheight=0.12, relwidth=0.16)
make_button('1').place(relx=0.04, rely=0.70, relheight=0.12, relwidth=0.16)
make_button('2').place(relx=0.23, rely=0.70, relheight=0.12, relwidth=0.16)
make_button('3').place(relx=0.42, rely=0.70, relheight=0.12, relwidth=0.16)
make_operation('-').place(relx=0.61, rely=0.70, relheight=0.12, relwidth=0.16)
make_root().place(relx=0.80, rely=0.70, relheight=0.12, relwidth=0.16)
make_button('4').place(relx=0.04, rely=0.55, relheight=0.12, relwidth=0.16)
make_button('5').place(relx=0.23, rely=0.55, relheight=0.12, relwidth=0.16)
make_button('6').place(relx=0.42, rely=0.55, relheight=0.12, relwidth=0.16)
make_operation('*').place(relx=0.61, rely=0.55, relheight=0.12, relwidth=0.16)
make_brackets('(').place(relx=0.80, rely=0.55, relheight=0.12, relwidth=0.16)
make_button('7').place(relx=0.04, rely=0.40, relheight=0.12, relwidth=0.16)
make_button('8').place(relx=0.23, rely=0.40, relheight=0.12, relwidth=0.16)
make_button('9').place(relx=0.42, rely=0.40, relheight=0.12, relwidth=0.16)
make_operation('/').place(relx=0.61, rely=0.40, relheight=0.12, relwidth=0.16)
b_clear_all = Button(frame, text='C', bg='white', font=('Arial', 35), command=clear_all, activebackground='yellow',
                     background='#FFE089')
make_brackets(')').place(relx=0.80, rely=0.40, relheight=0.12, relwidth=0.16)
b_clear_all.place(relx=0.04, rely=0.25, relheight=0.12, relwidth=0.16)
b_clear_1 = Button(frame, text='CE', bg='white', font=('Arial', 35), command=clear_1, activebackground='yellow',
                   background='#FFE089')
b_clear_1.place(relx=0.23, rely=0.25, relheight=0.12, relwidth=0.16)
b_round = Button(frame, text='%', bg='white', font=('Arial', 35), command=round_num,
                 activebackground='yellow', background='#FFE089')
b_round.place(relx=0.42, rely=0.25, relheight=0.12, relwidth=0.16)
b_secret = Button(frame, text='', bg='black', font=('Arial', 35), command=lambda: print('Not implemented yet'),
                  activebackground='yellow', background='#FFE089')
b_secret.place(relx=0.61, rely=0.25, relheight=0.12, relwidth=0.16)
b_off = Button(frame, text='off', bg='white', font=('Arial', 35), command=lambda: root.destroy(),
               activebackground='yellow', background='#FFE089')
b_off.place(relx=0.80, rely=0.25, relheight=0.12, relwidth=0.16)
root.mainloop()
