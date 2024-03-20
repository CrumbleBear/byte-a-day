import os
import shutil
import datetime

def MDTSF(): #"move_downloads_to_single_folder"
    
    downloads_dir = os.path.expanduser('~/Downloads')
    target_dir = os.path.expanduser('~/Desktop/ARCDownloads')

    if os.path.exists(downloads_dir) and os.listdir(downloads_dir):

        if not os.path.exists(target_dir):
            os.makedirs(target_dir)

        current_date = datetime.datetime.now().strftime('%Y-%m-%d')

        folder_name = os.path.join(target_dir, f'Downloads_{current_date}')

        os.makedirs(folder_name)

        for item in os.listdir(downloads_dir):
            item_path = os.path.join(downloads_dir, item)
            if os.path.isfile(item_path):
                shutil.move(item_path, folder_name)
            elif os.path.isdir(item_path):
                shutil.move(item_path, folder_name)

        print("Downloads moved successfully to", folder_name)
    else:
        print("No downloads to move.")

print('Sorting Downloads...')
MDTSF()
