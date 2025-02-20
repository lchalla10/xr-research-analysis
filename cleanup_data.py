import os
import re

def cleanup_folder(folder_path):
    file_groups = {}
    pattern = re.compile(r"(.+?)_(\d+)$")  # Matches filename_number

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)
        if os.path.isfile(file_path):
            match = pattern.match(os.path.splitext(file)[0])
            if match:
                base_name, _ = match.groups()
                if base_name not in file_groups:
                    file_groups[base_name] = []
                file_groups[base_name].append(file_path)

    for base_name, files in file_groups.items():
        if len(files) > 1:
            largest_file = max(files, key=os.path.getsize)  # Find the largest file
            for file in files:
                if file != largest_file:
                    os.remove(file)  # Delete smaller versions
            
            new_name = f"{base_name}_1{os.path.splitext(largest_file)[1]}"
            new_path = os.path.join(folder_path, new_name)
            os.rename(largest_file, new_path)  # Rename to filename_1
            print(f"Kept {new_name}, deleted others.")

def process_all_folders(root_folder):
    for main_folder in os.listdir(root_folder):
        main_folder_path = os.path.join(root_folder, main_folder)
        if os.path.isdir(main_folder_path) and main_folder.isdigit():
            for sub_folder in ["controller", "hand"]:
                sub_folder_path = os.path.join(main_folder_path, sub_folder)
                if os.path.isdir(sub_folder_path):
                    for numbered_folder in os.listdir(sub_folder_path):
                        numbered_folder_path = os.path.join(sub_folder_path, numbered_folder)
                        if os.path.isdir(numbered_folder_path) and numbered_folder.isdigit():
                            cleanup_folder(numbered_folder_path)

if __name__ == "__main__":
    root_folder = r"data/"  # Change this to your target root folder
    process_all_folders(root_folder)
