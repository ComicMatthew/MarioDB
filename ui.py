import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import subprocess
import sys
import json
from my_functions import read_config

config_values = read_config("config.json") if sys.platform.startswith(
    'win') else read_config("config_mac.json")
database_file_path = config_values.get('database_file_path', '')
usage_subtraction_file_path = config_values.get(
    'usage_subtraction_file_path', '')
done_folder_path = config_values.get('done_folder_path', '')
usage_addition_file_path = config_values.get('usage_addition_file_path', '')


def save_config():
    # Update the variables in the config module
    config_data = {
        "database_file_path": entry_database_file_path.get(),
        "usage_subtraction_file_path": entry_usage_subtraction_file_path.get(),
        "usage_addition_file_path": entry_usage_addition_file_path.get(),
        "done_folder_path": entry_done_folder_path.get()
    }

    # Write the updated configuration to the config.json file
    with open('config.json' if sys.platform.startswith(
            'win') else 'config_mac.json', 'w') as json_file:
        json.dump(config_data, json_file, indent=4)
    # show_windows_alert("Konfiguracja zmieniona", "Konfiguracja zostala zmieniona. Sprawdz czy nazwy folderow czy pliku sa poprawne")


def run_odejmowanie():
    save_config()
    run_command("./odejmowanie.py")


def run_dodawanie():
    save_config()
    run_command("./dodawanie.py")


def run_command(command):
    # Run the command and redirect stdout to the Text widget
    try:
        result = subprocess.run(
            [sys.executable, command], text=True, capture_output=True)
        log_text.insert(tk.END, result.stdout)
        log_text.insert(tk.END, result.stderr)
        log_text.see(tk.END)
    except Exception as e:
        log_text.insert(tk.END, f"Error: {e}\n")
        log_text.see(tk.END)


# Create the main window
root = tk.Tk()
root.title("Baza Danych 3000")


# Create entry widgets for each variable
label_database_file_path = tk.Label(
    root, text="Sciezka do Folderu z baza danych:")
entry_database_file_path = tk.Entry(root)
entry_database_file_path.insert(0, database_file_path)

label_usage_subtraction_file_path = tk.Label(
    root, text="Sciezka do Folderu do odejmowania:")
entry_usage_subtraction_file_path = tk.Entry(root)
entry_usage_subtraction_file_path.insert(0, usage_subtraction_file_path)

label_usage_addition_file_path = tk.Label(
    root, text="Sciezka do Folderu do dodawania:")
entry_usage_addition_file_path = tk.Entry(root)
entry_usage_addition_file_path.insert(0, usage_addition_file_path)

label_done_folder_path = tk.Label(
    root, text="Sciezka do Folderu po przetworzeniu:")
entry_done_folder_path = tk.Entry(root)
entry_done_folder_path.insert(0, done_folder_path)

# Create Text widget for logs
log_text = ScrolledText(root, wrap=tk.WORD, height=30, width=50)
log_text.grid(row=7, column=0, columnspan=2, pady=10)

# Create buttons
button_save = tk.Button(root, text="Zapisz konfiguracje", command=save_config)
button_odejmowanie = tk.Button(
    root, text="Odejmowanie", command=run_odejmowanie)
button_dodawanie = tk.Button(
    root, text="Dodawanie", command=run_dodawanie)

# Grid layout for widgets
label_database_file_path.grid(row=0, column=0, pady=5, padx=5, sticky=tk.W)
entry_database_file_path.grid(row=0, column=1, pady=5, padx=5, sticky=tk.W)

label_usage_subtraction_file_path.grid(
    row=1, column=0, pady=5, padx=5, sticky=tk.W)
entry_usage_subtraction_file_path.grid(
    row=1, column=1, pady=5, padx=5, sticky=tk.W)

label_usage_addition_file_path.grid(
    row=2, column=0, pady=5, padx=5, sticky=tk.W)
entry_usage_addition_file_path.grid(
    row=2, column=1, pady=5, padx=5, sticky=tk.W)

label_done_folder_path.grid(row=3, column=0, pady=5, padx=5, sticky=tk.W)
entry_done_folder_path.grid(row=3, column=1, pady=5, padx=5, sticky=tk.W)

button_save.grid(row=4, column=0, columnspan=2, pady=10)
button_odejmowanie.grid(row=5, column=0, columnspan=2, pady=5)
button_dodawanie.grid(row=6, column=0, columnspan=2, pady=5)

# Start the Tkinter event loop
root.mainloop()
