import tkinter as tk
import subprocess
import sys
import config


def save_config():
    # Update the variables in the config module
    config.database_file_path = entry_database_file_path.get()
    config.usage_subtraction_file_path = entry_usage_subtraction_file_path.get()
    config.usage_addition_file_path = entry_usage_addition_file_path.get()
    config.done_folder_path = entry_done_folder_path.get()
    # Optionally, you can save the changes to the config file here


def run_odejmowanie():
    save_config()
    subprocess.run([sys.executable, "./odejmowanie.py"])


def run_dodawanie():
    save_config()
    subprocess.run([sys.executable, "./dodawanie.py"])


# Create the main window
root = tk.Tk()
root.title("Configuration UI")

# Create entry widgets for each variable
label_database_file_path = tk.Label(root, text="Database File Path:")
entry_database_file_path = tk.Entry(root)
entry_database_file_path.insert(0, config.database_file_path)

label_usage_subtraction_file_path = tk.Label(
    root, text="Usage Subtraction File Path:")
entry_usage_subtraction_file_path = tk.Entry(root)
entry_usage_subtraction_file_path.insert(0, config.usage_subtraction_file_path)

label_usage_addition_file_path = tk.Label(
    root, text="Usage Addition File Path:")
entry_usage_addition_file_path = tk.Entry(root)
entry_usage_addition_file_path.insert(0, config.usage_addition_file_path)

label_done_folder_path = tk.Label(root, text="Done Folder Path:")
entry_done_folder_path = tk.Entry(root)
entry_done_folder_path.insert(0, config.done_folder_path)

# Create buttons
button_save = tk.Button(root, text="Save Configuration", command=save_config)
button_odejmowanie = tk.Button(
    root, text="Run odejmowanie.py", command=run_odejmowanie)
button_dodawanie = tk.Button(
    root, text="Run dodawanie.py", command=run_dodawanie)

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
