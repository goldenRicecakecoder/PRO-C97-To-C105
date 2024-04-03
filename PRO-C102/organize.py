import os
import shutil


from_dir = "C:/Users/hepzi/Downloads"  
to_dir = "C:/Users/hepzi/Downloads/lelel"  


list_of_files = os.listdir(from_dir)


print("List of files in the source path:")
for file_name in list_of_files:
    print(file_name)


for file_name in list_of_files:

    name, extension = os.path.splitext(file_name)

   
    if extension == '' or extension.lower() not in ['.txt', '.doc', '.docx', '.pdf']:
        continue  
 
    path1 = from_dir + '/' + file_name
    path2 = to_dir + '/' + "Document_Files"
    path3 = to_dir + '/' + "Document_Files" + '/' + file_name


    if os.path.exists(path2):
        print(f"Moving {file_name} to {path3}")
        shutil.move(path1, path3)
    else:
        os.makedirs(path2)
        print(f"Moving {file_name} to {path3}")
        shutil.move(path1, path3)
