#day2
import os
import shutil

# Define the folders dictionary with default directory paths
folders = {
    'Docs': ['.txt', '.doc', '.docx', '.pdf', '.xls', '.xlsx', '.ppt', '.pptx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.svg'],
    'Videos': ['.mp4', '.mov', '.avi', '.mkv', '.wmv', '.flv', '.webm'],
    'Apps': ['.exe', '.app', '.apk', '.bat', '.com', '.jar', '.deb', '.pkg', '.cmd'],
    'Apple': ['.pages', '.key', '.numbers', '.ipynb', '.m4a', '.aiff', '.caf'],
    'CAD': ['.dwg', '.dxf', '.igs', '.stp', '.step', '.stl'],
    'Audio': ['.mp3', '.wav', '.flac', '.aac', '.ogg', '.wma'],
    'Arcives': ['.zip', '.rar', '.7z', '.tar', '.gz', '.bz2', '.xz'],
    'ISO': ['.iso', '.bin', '.cue', '.img', '.nrg', '.dmg', '.vhd', '.vmdk'],
    'WEB': ['.html', '.htm', '.php', '.asp', '.aspx', '.jsp', '.css', '.js', '.xml'],
    'Script': ['.py', '.sh', '.bash', '.ps1', '.rb', '.pl', '.lua', '.js']
}

# Function to ensure directory existence or create it
def ensure_directory(path):
    if not os.path.exists(path):
        os.makedirs(path)

# Function to move files to their respective directories
def organize_files(source_dir, folders):
    print("Starting file organization...")
    num_files_processed = 0
    for file in os.listdir(source_dir):
        if os.path.isfile(os.path.join(source_dir, file)):
            file_extension = os.path.splitext(file)[1].lower()
            for folder, extensions in folders.items():
                if file_extension in extensions:
                    destination_dir = os.path.join(source_dir, folder)
                    ensure_directory(destination_dir)
                    shutil.move(os.path.join(source_dir, file), destination_dir)
                    print(f'Moved {file} to {destination_dir}')
                    num_files_processed += 1
                    break
    print(f"File organization completed. {num_files_processed} files processed.")

# Test the function with the source directory
source_directory = input("Enter the directory path to organize: ")
organize_files(source_directory, folders)
