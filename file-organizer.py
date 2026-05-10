print("Welcome to the basic file organizer program") #added an intro cause why not 

import os #importing the os library 
import shutil #importing the shutil library for file organizing

path = "" #path where the folder is 

files = os.listdir(path)
print(files)
for file in files: #The code with how are we supposed to move the files to the folders created 
   
    src = os.path.join(path,file)
  
    if file.endswith(".jpg"): #for jpg files
        dst_folder = os.path.join(path,"Pic")
        os.makedirs(dst_folder,exist_ok=True)
        shutil.move(src,dst_folder)
   
    elif file.endswith(".mp3"): #for mp3 files
        dst_folder = os.path.join(path,"Music")
        os.makedirs(dst_folder,exist_ok=True)
        shutil.move(src,dst_folder)

    elif file.endswith(".pdf"): #for pdf 
        dst_folder = os.path.join(path,"Doc")
        os.makedirs(dst_folder,exist_ok=True)
        shutil.move(src,dst_folder)

#Gonna improve it later to make an even better version 