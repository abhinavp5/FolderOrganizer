import os 
import shutil

path = input("Enter the Absolute Path of the file you want to clean:")
files = os.listdir(path)
parent = os.path.abspath(os.path.join(path, os.pardir))
file_extensions = []

def find_index(list,element):
    try:
        return list.index(element)
    except ValueError:
        return -1

for file in files:
    #directory
    if(os.path.isdir(os.path.abspath(file))):
        if find_index(file_extensions,"folders")==-1:
            file_extensions.append("folders")
            dirname = "folders"
            os.mkrdir(dirname)
            old_name = os.path.abspath(file)
            new_name = os.path.join(parent,dirname,file)
            os.rename(old_name,new_name)
        else:
            old_name = os.path.abspath(file)
            new_name = os.path.join(parent,dirname,file)
            os.rename(old_name,new_name)
    #file
    else:
        delim_index = file.rfind(".")##index of period
        if (delim_index!=-1):
            extension = file[delim_index: ] #extesnsion is the file extension
        #searching for the extension in the list
        value = find_index(file_extensions,extension)       
        if(value==-1):#if it was equal to -1
            file_extensions.append(extension)
            dirname = extension[1:] + "files"
            new_dir = os.path.join(path,dirname)
            try:
                os.mkdir(new_dir)
            except FileExistsError:
                print(file," exists")
                continue
            old_name = os.path.abspath(path)
            old_name = os.path.join(old_name,file)
            new_name = os.path.join(path,dirname)
            new_name = os.path.join(new_name,file)
            shutil.move(old_name,new_name)
        else:#if its not equal to -1
            dirname = extension[1:] + "files"
            old_name = os.path.abspath(path)
            old_name = os.path.join(old_name,file)
            new_name = os.path.join(path,dirname)
            new_name = os.path.join(new_name,file)
            shutil.move(old_name,new_name)


    

    


