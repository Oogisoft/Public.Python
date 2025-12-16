import pypdf, os
from pathlib import Path

def encrypto_check(folder):
    for folder_name, subfolders, filenames in os.walk(folder):
        for filename in filenames:
            if filename.endswith('.pdf'):              
                reader = pypdf.PdfReader(f'{folder_name}/{filename}')
                if reader.is_encrypted == True:
                    print(f'{filename} is hella encrypted dawg')

def encrypto(folder, password, encrypted_folder, delete_answer):
    def save_files(encrypted_folder, filename): #will reuse multiple times
        with open(f'{encrypted_folder}/{filename[:-4]}_ENCRYPTED.pdf', 'wb') as file:
            writer.write(file)
            print(f'{filename}, encrypted') #everything works
    for folder_name, subfolders, filenames in os.walk(folder):
        print(f'Scanning: {folder_name}')
        for filename in filenames:
            if filename.lower().endswith('.pdf'): #making case insensitive with .lower()
                print (f'PDF Found, encrypting: {filename}')
                writer = pypdf.PdfWriter()
                writer.append(f'{folder_name}/{filename}')
                writer.encrypt(password, algorithm='AES-256')
                #delete old files in original file path
                if 'Y' in delete_answer.upper():
                    os.unlink(f'{folder_name}/{filename}')
                    print(f'deleted {filename}')
                    save_files(encrypted_folder, filename)
                else:
                    save_files(encrypted_folder, filename)

    #have the program attempt to read and decrypt the new file 
    #to ensure that it was encrypted correctly.
    encrypto_check(encrypted_folder)
    return print(f'done')

path_input = input('I will encrypt all PDFs in this folder path:\n')
password_input = input('I will put this password on all of them:\n')
encrypted_input = input('Tell me the folder path where you want this saved:\n')
delete_old_input = input('Do you want to delete the old files? (type Y or N):\n')
encrypto(path_input, password_input, encrypted_input, delete_old_input)
