import tkinter as tk
import subprocess
import sys


def run_odejmowanie():
    subprocess.run([sys.executable, "./odejmowanie.py"])


def run_dodawanie():
    subprocess.run([sys.executable, "./dodawanie.py"])


# Create the main window
root = tk.Tk()
root.title("Simple UI")

# Create buttons
button_odejmowanie = tk.Button(
    root, text="Run odejmowanie.py", command=run_odejmowanie)
button_dodawanie = tk.Button(
    root, text="Run dodawanie.py", command=run_dodawanie)

# Pack buttons into the window
button_odejmowanie.pack(pady=10)
button_dodawanie.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
