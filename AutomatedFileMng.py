#import required Modules
import os
import shutil

#dirs
download_dir = '/Users/ivanroy/Downloads'
music_dir = '/Users/ivanroy/Downloads/Music'
video_dir = '/Users/ivanroy/Downloads/Videos'
zip_dir = '/Users/ivanroy/Downloads/Zips'
img_dir = '/Users/ivanroy/Downloads/Images'
doc_dir = '/Users/ivanroy/Downloads/Docs'


#ext arrays
music_arr = ["mp3","wav"]
img_arr = ["jpg","png","jpeg","webp","heic","gif","svg"]
zip_arr = ["zip",]
vid_arr = ["mov","mp4"]
doc_arr = ["txt","docx","pdf","xlsx","xlsm"]

#function to move files

def move_func(root_file,target_folder):
    shutil.move(root_file,target_folder)



#function to check the ext and move file from download to target folder
def ext_check(ext_in,filepath):
    ext_in = ext_in.lower()
    if ext_in in music_arr: move_func(filepath,music_dir)
    if ext_in in img_arr: move_func(filepath,img_dir)
    if ext_in in zip_arr: move_func(filepath,zip_dir)
    if ext_in in vid_arr: move_func(filepath,video_dir)
    if ext_in in doc_arr: move_func(filepath,doc_dir)
    



def main_function(print_txt):
    print(print_txt)
    for filename in os.listdir(download_dir):
        f = os.path.join(download_dir,filename)
        if os.path.isfile(f):
            ext = f.split('.')[-1]
            ext_check(ext,f)


#creating infinite loop
i = 0
while i <= 10:
    main_function("Listening")