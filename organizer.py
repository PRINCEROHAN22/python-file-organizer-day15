import os
import shutil

# 📁 Folder to organize
folder_path = "D:/projects/to_organize"

# 📦 Folder categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png"],
    "Documents": [".pdf", ".docx", ".txt"],
    "Videos": [".mp4", ".mov"],
    "Music": [".mp3", ".wav"],
    "Others": []
}

# 🚀 Organizer logic
def organize_folder(path):
    for file in os.listdir(path):
        file_path = os.path.join(path, file)
        if os.path.isfile(file_path):
            moved = False
            for category, extensions in file_types.items():
                if any(file.endswith(ext) for ext in extensions):
                    dest_folder = os.path.join(path, category)
                    os.makedirs(dest_folder, exist_ok=True)
                    shutil.move(file_path, os.path.join(dest_folder, file))
                    moved = True
                    break
            if not moved:
                dest_folder = os.path.join(path, "Others")
                os.makedirs(dest_folder, exist_ok=True)
                shutil.move(file_path, os.path.join(dest_folder, file))

# 🏁 Run the organizer
organize_folder(folder_path)
