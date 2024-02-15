
import os

def clear_folder(folder_path):
    if not os.path.exists(folder_path):
        raise f"The folder '{folder_path}' does not exist."
    
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path,item)

        if os.path.isfile(item_path):
            os.remove(item_path)
            print(f"Deleted file: {item_path}")

        elif os.path.isdir(item_path):
            clear_folder(item_path)
            os.rmdir(item_path)
            print(f"Deleted directory: {item_path}")