from tkinter import *
#import openpyxl
from tkinter import messagebox

mas_1 = []
mas_dat = []
mas_date = []
mas_zac = []
mas_fio = []
mas_group = []
mas_disc = []
mas_num = []

f = open('zhurnal.txt', 'r', encoding='utf-8')
mas = []
mas_of_date = []

for word in f:
    print(word)
f.close()
root = Tk()

root.geometry('500x400+300+300')

# labels

data_label = Label(root, text="дата")
data_label.grid(row=0, column=0, pady=10)

zach_label = Label(root, text="Номер зачетки")
zach_label.grid(row=1, column=0, pady=10)

fio_label = Label(root, text="ФИО")
fio_label.grid(row=2, column=0, pady=10)

group_label = Label(root, text="Группа")
group_label.grid(row=3, column=0, pady=10)

disc_label = Label(root, text="Дисциплина")
disc_label.grid(row=4, column=0, pady=10)

num_label = Label(root, text="Номер пары")
num_label.grid(row=5, column=0, pady=10)

# entries

data_entry = Entry(root, width=40)
data_entry.grid(row=0, column=1, pady=10)

zach_entry = Entry(root, width=40)
zach_entry.grid(row=1, column=1, pady=10)

fio_entry = Entry(root, width=40)
fio_entry.grid(row=2, column=1, pady=10)

group_entry = Entry(root, width=40)
group_entry.grid(row=3, column=1, pady=10)

disc_entry = Entry(root, width=40)
disc_entry.grid(row=4, column=1, pady=10)

num_entry = Entry(root, width=40)
num_entry.grid(row=5, column=1, pady=10)


# Buttons

def print_win():


    file_p = open('zhurnal.txt', 'r', encoding='utf-8')
    for i in file_p:
        mas_1.append(str(i).replace('\n', ''))
    print(mas_1)

    for i in range(0, len(mas_1), 6):
        mas_dat.append(mas_1[i])

    for i in range(1, len(mas_1), 6):
        mas_zac.append(mas_1[i])

    for i in range(2, len(mas_1), 6):
        mas_fio.append(mas_1[i])

    for i in range(3, len(mas_1), 6):
        mas_group.append(mas_1[i])

    for i in range(4, len(mas_1), 6):
        mas_disc.append(mas_1[i])

    for i in range(5, len(mas_1), 6):
        mas_num.append(mas_1[i])

    print(mas_dat)
    print(mas_zac)
    print(mas_fio)
    print(mas_group)
    print(mas_disc)
    print(mas_num)

    file_p.close()

    file_pr = open('pechat.txt', 'w', encoding='utf-8')
    for i in range(len(mas_dat)):
        file_pr.write(mas_dat[i] + " ")
        file_pr.write(mas_zac[i] + " ")
        file_pr.write(mas_fio[i] + " ")
        file_pr.write(mas_group[i] + " ")
        file_pr.write(mas_disc[i] + " ")
        file_pr.write(mas_num[i] + "\n")

print_button = Button(root, text="Отпечатать файл", width=15, command=print_win)
print_button.grid(row=0, column=2, padx=20)


def add_date():
    data = data_entry.get()
    st = data + "\n"
    with open('date.txt', 'a', encoding='utf-8') as file:
        file.write(st)
    messagebox.showinfo("ok", "sucsessfull")

add_date_button = Button(root, text="Отпечатать даты", width=15, command=add_date)
add_date_button.grid(row=4, column=2, padx=20)

"""
def xl_add():
    wb = openpyxl.load_workbook(filename='date.xlsx')
    sheet = wb['test']
    val = sheet['A1'].value
    print(val)
    fil = open('zhurnal.txt', 'r', encoding='utf-8')
    for i in fil:
        mas.append(str(i).replace('\n', ''))
    print(mas)

    print(len(mas))

    for j in range(0, len(mas), 6):
        mas_of_date.append(mas[j])

    print(mas_of_date)

    ws = wb.active
    ws.append(mas_of_date)
    wb.save('date.xlsx')

    fil.close()
    mas.clear()
    mas_of_date.clear()

    messagebox.showinfo("ok", "sucsessfull")


ex_button = Button(root, text="Date excel", width=15, command=xl_add)
ex_button.grid(row=1, column=2, padx=20)
"""    

def add():
    data = data_entry.get()
    zach = zach_entry.get()
    fio = fio_entry.get()
    group = group_entry.get()
    disc = disc_entry.get()
    num = num_entry.get()
    st = "\n" + data + "\n" + zach + "\n" + fio + "\n" + group + "\n" + disc + "\n" + num

    with open('zhurnal.txt', 'a', encoding='utf-8') as file:
        file.write(st)
    messagebox.showinfo("ok", "sucsessfull")


add_button = Button(root, text="Добавить запись", width=15, command=add)
add_button.grid(row=2, column=2)

root.mainloop()
