import gdown
import os

folder_url = "https://drive.google.com/drive/folders/1fMTnPv38xRXff0DIUGzWBPE84DFSNs8A"

gdown.download_folder(folder_url, output="./", quiet=False, use_cookies=False)
print(f"Download completed. Files are saved in the folder")