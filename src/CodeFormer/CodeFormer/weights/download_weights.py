import gdown
import os

folder_url = "https://drive.google.com/drive/folders/106x5rlMz8XFjNMqfXByQxzsVKlNmoDtd"

gdown.download_folder(folder_url, output="./", quiet=False, use_cookies=False)
print(f"Download completed. Files are saved in the folder")