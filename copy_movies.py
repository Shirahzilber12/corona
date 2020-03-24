from shutil import copy
import glob


dst = 'C:\\Users\\This_user\\Pictures\\New folder\\video'
source_folder = "C:\\Users\\This_user\\Pictures\\Camera backup"
files = glob.glob(source_folder + '/**/*.mp4', recursive=True)
for i in files:
    copy(i, dst)
