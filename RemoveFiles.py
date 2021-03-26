import os
import shutil
import time

def main():
    deleted_folders_count = 0
    deleted_files_count = 0
    path = input("Enter the path of directory to delete")
    days = 30
    seconds =  time.time() - (days*24*60*60)

if(os.path.exists(path)):
    for root_folder,folders,files in os.walk(path):
        #comparing the days
        if(seconds >= get_file_or_folder_age(root_folder)):
            #removing the folder
            remove_folder(root_folder)
            deleted_folders_count = deleted_folders_count+1

        else:
            #checking folder from the root folder
            for folder in folders:
                #folder path
                folder_path = os.path.join(root_folder,folder)
                #comparing the days
                if(seconds >= get_file_or_folder_age(root_folder)):
                    #removing the folder
                    remove_folder(root_folder)
                    deleted_folders_count = deleted_folders_count+1

            #checking the current directory files
            for file in files:
                #folder path
                file_path = os.path.join(root_folder,file)
                #comparing the days
                if(seconds >= get_file_or_folder_age(file_path)):
                    #removing the folder
                    remove_file(file_path)
                    deleted_files_count = deleted_files_count+1

                else:
                    #if the path is not  a directory
                    if(seconds >= get_file_or_folder_age(file_path)):
                    #removing the folder
                    remove_file(file_path)
                    deleted_files_count = deleted_files_count+1

else:
    print(f'"{path}" is not found')
    deleted_files_count = deleted_files_count+1

print(f"Total folders deleted: {deleted_folders_count}")
print(f"Total files deleted: {deleted_files_count}")


def remove_file(file_path):
    os.remove(file_path)

def remove_folder(root_folder):
    shutil.rmtree(root_folder)
    #folder_name = os.walk(path)

    #os.path.join(path,folder_name)

    #ctime = os.stat(path).st_ctime
    #return ctime

    #if(seconds>ctime):
        #print("Greater")
#else:
    #print("Path not found")