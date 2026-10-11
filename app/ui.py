import tkinter as tk
from tkinter import messagebox
from tkinter.scrolledtext import ScrolledText

from app.config import load_config, save_config
from app.excel_service import process_addition, process_subtraction


def build_ui():
    config = load_config()

    root = tk.Tk()
    root.title("Baza Danych 3000")

    fields = {
        "database_file_path": "Sciezka do bazy danych",
        "usage_subtraction_file_path": "Folder do odejmowania",
        "usage_addition_file_path": "Folder do dodawania",
        "done_folder_path": "Folder po przetworzeniu",
        "usage_worksheet": "Nazwa arkusza zrodlowego",
        "usage_workdatasheet": "Nazwa arkusza bazy danych",
        "substraction_start_row": "Numer wiersza odejmowania",
        "addition_start_row": "Numer wiersza dodawania",
        "database_start_row": "Numer wiersza bazy danych",
    }

    entries = {}
    row = 0
    for key, label in fields.items():
        tk.Label(root, text=label).grid(row=row, column=0, padx=5, pady=5, sticky="w")
        entry = tk.Entry(root, width=60)
        entry.insert(0, str(config.get(key, "")))
        entry.grid(row=row, column=1, padx=5, pady=5)
        entries[key] = entry
        row += 1

    log = ScrolledText(root, wrap=tk.WORD, width=80, height=18)
    log.grid(row=row, column=0, columnspan=2, padx=10, pady=10)

    def run_processor(kind):
        data = {key: entry.get() for key, entry in entries.items()}
        save_config(data)
        try:
            if kind == "subtract":
                result = process_subtraction()
            else:
                result = process_addition()

            log.insert(tk.END, f"{result.get('summary', 'Operacja zakończona.')}\n")
            for item in result.get("audit", []):
                log.insert(tk.END, f"- {item.get('message', 'Brak szczegółów.')}\n")

            if result.get("missing"):
                log.insert(tk.END, "Brakujące rekordy: " + ", ".join(str(item) for item in result["missing"]) + "\n")

            log.see(tk.END)
            messagebox.showinfo("Sukces", "Operacja zakończona pomyślnie.")
        except Exception as exc:  # pragma: no cover - UI path only
            log.insert(tk.END, f"Błąd: {exc}\n")
            log.see(tk.END)
            messagebox.showerror("Błąd", str(exc))

    btn_row = row + 1
    tk.Button(root, text="Odejmowanie", command=lambda: run_processor("subtract")).grid(row=btn_row, column=0, padx=5, pady=5, sticky="ew")
    tk.Button(root, text="Dodawanie", command=lambda: run_processor("add")).grid(row=btn_row, column=1, padx=5, pady=5, sticky="ew")
    tk.Button(root, text="Wyczyść log", command=lambda: log.delete("1.0", tk.END)).grid(row=btn_row + 1, column=0, columnspan=2, padx=5, pady=(0, 5), sticky="ew")

    root.mainloop()


def main():
    build_ui()


if __name__ == "__main__":
    main()
