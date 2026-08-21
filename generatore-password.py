import random
import string
import tkinter as tk
from tkinter import messagebox


def genera_password():
    try:
        lunghezza = int(entry_lunghezza.get())
        if lunghezza <= 0:
            messagebox.showerror(
                "Errore", "La lunghezza deve essere maggiore di 0!"
            )
            return
    except ValueError:
        messagebox.showerror(
            "Errore", "Inserisci un numero valido per la lunghezza!"
        )
        return

    # Costruzione dinamica del pool di caratteri in base alle checkbox
    caratteri = ""
    if var_minuscole.get():
        caratteri += string.ascii_lowercase
    if var_maiuscole.get():
        caratteri += string.ascii_uppercase
    if var_numeri.get():
        caratteri += string.digits
    if var_simboli.get():
        caratteri += string.punctuation

    # Verifica se è stato selezionato almeno un set di caratteri
    if not caratteri:
        messagebox.showwarning(
            "Attenzione", "Seleziona almeno un tipo di carattere!"
        )
        return

    # Generazione casuale della password
    password = "".join(random.choice(caratteri) for _ in range(lunghezza))

    # Mostra il risultato nel campo di testo
    entry_risultato.config(state="normal")
    entry_risultato.delete(0, tk.END)
    entry_risultato.insert(0, password)
    entry_risultato.config(state="readonly")


def copia_password():
    pwd = entry_risultato.get()
    if pwd:
        finestra.clipboard_clear()
        finestra.clipboard_append(pwd)
        messagebox.showinfo("Copiato", "Password copiata negli appunti! 📋")
    else:
        messagebox.showwarning("Attenzione", "Nessuna password da copiare!")


# Creazione della finestra principale
finestra = tk.Tk()
finestra.title("Generatore di Password Sicure")
finestra.geometry("380x380")
finestra.resizable(False, False)

# Titolo principale
lbl_titolo = tk.Label(
    finestra, text="Generatore di Password", font=("Arial", 14, "bold")
)
lbl_titolo.pack(pady=10)

# Selezione della lunghezza
frame_lunghezza = tk.Frame(finestra)
frame_lunghezza.pack(pady=5)
lbl_lunghezza = tk.Label(
    frame_lunghezza, text="Lunghezza password:", font=("Arial", 10)
)
lbl_lunghezza.pack(side=tk.LEFT, padx=5)
entry_lunghezza = tk.Entry(frame_lunghezza, width=5, font=("Arial", 10))
entry_lunghezza.insert(0, "12")
entry_lunghezza.pack(side=tk.LEFT)

# Riquadro Opzioni (Checkbox)
frame_opzioni = tk.LabelFrame(
    finestra,
    text=" Personalizzazione Caratteri ",
    font=("Arial", 10, "bold"),
    padx=10,
    pady=10,
)
frame_opzioni.pack(pady=10, padx=20, fill="both", expand=True)

var_minuscole = tk.BooleanVar(value=True)
var_maiuscole = tk.BooleanVar(value=True)
var_numeri = tk.BooleanVar(value=True)
var_simboli = tk.BooleanVar(value=True)

chk_minuscole = tk.Checkbutton(
    frame_opzioni,
    text="Minuscole (a-z)",
    variable=var_minuscole,
    font=("Arial", 10),
)
chk_minuscole.pack(anchor="w")

chk_maiuscole = tk.Checkbutton(
    frame_opzioni,
    text="Maiuscole (A-Z)",
    variable=var_maiuscole,
    font=("Arial", 10),
)
chk_maiuscole.pack(anchor="w")

chk_numeri = tk.Checkbutton(
    frame_opzioni, text="Numeri (0-9)", variable=var_numeri, font=("Arial", 10)
)
chk_numeri.pack(anchor="w")

chk_simboli = tk.Checkbutton(
    frame_opzioni,
    text="Simboli (!@#$...)",
    variable=var_simboli,
    font=("Arial", 10),
)
chk_simboli.pack(anchor="w")

# Pulsante Genera
btn_genera = tk.Button(
    finestra,
    text="Genera Password",
    command=genera_password,
    bg="#2196F3",
    fg="white",
    font=("Arial", 10, "bold"),
    padx=10,
)
btn_genera.pack(pady=5)

# Campo Risultato + Pulsante Copia
frame_risultato = tk.Frame(finestra)
frame_risultato.pack(pady=10)

entry_risultato = tk.Entry(
    frame_risultato, width=22, font=("Arial", 11), state="readonly"
)
entry_risultato.pack(side=tk.LEFT, padx=5)

btn_copia = tk.Button(
    frame_risultato, text="Copia 📋", command=copia_password, font=("Arial", 9)
)
btn_copia.pack(side=tk.LEFT)

# Riconoscimento tasto Invio per generare
finestra.bind("<Return>", lambda event: genera_password())

finestra.mainloop()



    