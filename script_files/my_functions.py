import os
import ctypes

def show_windows_alert(title, message):
    ctypes.windll.user32.MessageBoxW(0, message, title, 1)


def get_used_file(usage_path):
        
    todo_folder_path = os.path.join(usage_path)
    todo_files = [f for f in os.listdir(todo_folder_path) if f.endswith(".xlsx")]
    if not todo_files:
        error_message = f"W Folderze {todo_folder_path} nie ma zadnego pliku do przetworzenia!"
        show_windows_alert("Brak Pliku", error_message)
        print(error_message)       
    else:
        todo_file_name = todo_files[0]
        todo_file_path = os.path.join(todo_folder_path, todo_file_name)
        return todo_file_path, todo_file_name
    