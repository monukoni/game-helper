import tkinter as tk

x = 1800
y = 894
x_size = 128
y_size = 128


def update():
    frame = sleep
    window.geometry(f'{x_size}x{y_size}+{x}+{y}')
    label.configure(image=frame)


window = tk.Tk()

sleep = tk.PhotoImage(file='cat128.png', format='png')

# window configuration
window.config(highlightbackground='grey')
label = tk.Label(window, bd=0, bg='grey')
window.overrideredirect(True)
window.wm_attributes('-topmost', 1)
window.wm_attributes('-transparentcolor', 'grey')
label.pack()
window.after(1, update)
window.mainloop()