import os
import shutil

def organize_jpg_files():
    source_dir = "./source_folder"
    dest_dir = "./jpgs_destination"
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
        print(f"Created new folder: {dest_dir}")
    if not os.path.exists(source_dir):
        print(f"Error: The folder '{source_dir}' does not exist. Please create it first!")
        return
    files = os.listdir(source_dir)
    moved_count = 0
    for file_name in files:
        if file_name.lower().endswith('.jpg'):
            source_path = os.path.join(source_dir, file_name)
            dest_path = os.path.join(dest_dir, file_name)
            shutil.move(source_path, dest_path)
            print(f"Moved: {file_name}")
            moved_count += 1
    print(f"\nTask Complete! Successfully moved {moved_count} .jpg files.")

organize_jpg_files()