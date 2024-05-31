import os
import shutil
from_dir="C:/Users/Rafik/Desktop/Proj 102/Downloads"
to_dir="C:/Users/Rafik/Desktop/Proj 102"
list_of_files=os.listdir(from_dir)


for file_name in list_of_files:
    name,extention=os.path.splitext(file_name)
    print(name)
    print(extention)
    if extention=='':
        continue 
    if extention in  ['.txt','.doc', '.docx', '.pdf']:
        path1 = from_dir + '/' + file_name
        path2 = to_dir + '/' + "doc_file"
        path3 = to_dir + '/' + "doc_file" + '/' + file_name
        if os.path.exists(path2):
            print("moving...",file_name)
            shutil.move(path1,path3)
        else:
            os.makedirs(path2)
            print("moving...", file_name)
            shutil.move(path1,path3)
