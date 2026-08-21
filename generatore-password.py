import random
import string
import tkinter as tk
from tkinter import messagebox


def genera_password_logica(lunghezza):
    caratteri = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(caratteri) for i in range(lunghezza))
    return password

def esegui_generazione():
    try:
        stringa_lunghezza = entry_lunghezza.get()
        lunghezza = int(stringa_lunghezza)

        if lunghezza < 4:
            messagebox.showwarning("Attenzione, la password deve avere almeno 4 caratteri")
            return
        nuova_password = genera_password_logica(lunghezza)

        entry_risultato.config(state="normal")
        entry_risultato.delete(0, tk.END)
        entry_risultato.insert(0, nuova_password)
        entry_risultato.config(state="readonly")

    except ValueError:
        messagebox.showerror("Errore Input", "Devi inserire un numero valido")

window = tk.Tk()
window.title("Generatore-Password")
window.geometry("400x250")

lbl_istruzione = tk.Label(window, text="Lunghezza Password:", font=("Arial", 12))
lbl_istruzione.pack(pady=10)

entry_lunghezza = tk.Entry(window, font=("Arial", 12), width=10)
entry_lunghezza.insert(0, "12")
entry_lunghezza.pack()

btn_genera = tk.Button(window, text="Genera Password", command=esegui_generazione, font=("Arial", 11, "bold"))
btn_genera.pack(pady=20)

lbl_risultato = tk.Label(window, text="Password Generata:", font=("Arial", 10))
lbl_risultato.pack()

entry_risultato = tk.Entry(window, font=("Consolas", 12), width=30, state="readonly", fg="blue")
entry_risultato.pack(pady=5)

window.mainloop()



    