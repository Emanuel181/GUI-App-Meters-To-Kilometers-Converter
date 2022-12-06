import tkinter as tk
from tkinter import ttk
import tkinter.font as font
import windows


windows.set_dpi()


def convert_meters_to_kilometers(*args):

    if len(meters.get()) == 0:
        meters_show_dynamic.set('Enter a value')
    else:
        try:
            float(meters.get())
        except ValueError:
            meters_show_dynamic.set('Decimal or float numbers are allowed only!')
        else:
            meters_show_dynamic.set(str(float(meters.get()) * 0.001) + ' Km')


root = tk.Tk()
root.title("Meters to Kilometers converter")
font.nametofont('TkDefaultFont').configure(size=15)
root.geometry('600x400')


meters = tk.StringVar()
meters.set('')
meters_show_dynamic = tk.StringVar(value=' ')


main = ttk.Frame(padding=(20, 15))
main.grid(row=0, column=0)


label = ttk.Label(main, text='Meters: ')
entry_meters = ttk.Entry(main, width=12, textvariable=meters, font=15)
km_label = ttk.Label(main, text='Labels: ')
km_display = ttk.Label(main, text='Kilometers display here', textvariable=meters_show_dynamic)
calculate_button = ttk.Button(main, text='Calculate', padding=(0, 0, 0, 5), command=convert_meters_to_kilometers)
quit_button = ttk.Button(main, text='Close application', command=root.destroy)

label.grid(row=0, column=0, pady=15)
km_label.grid(row=1, column=0, sticky='W', pady=15)
entry_meters.grid(row=0, column=1, sticky='EW')
km_display.grid(row=1, column=1, sticky='EW')
calculate_button.grid(row=2, column=0, columnspan=2, sticky='EW')
quit_button.grid(row=3, column=0, columnspan=2, sticky='EW')

for child in main.winfo_children():
    child.grid_configure(pady=15)

root.columnconfigure(0, weight=1)


root.bind('<Return>', convert_meters_to_kilometers)
root.bind('<KP_Enter>', convert_meters_to_kilometers)


root.mainloop()
