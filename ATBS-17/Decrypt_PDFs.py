#my job is to undo what PDF_Madness does

import pypdf, os

def decrypto(folder, password, decrypted_folder):
    for folder_name, subfolders, filenames in os.walk(folder):
        print(f'Scanning: {folder_name}')
        for filename in filenames:
            if filename.endswith('.pdf'):
                print (f'PDF Found, decrypting: {filename}')
                reader = pypdf.PdfReader(f'{folder_name}/{filename}')
                print(f'{filename} encryption status is {reader.is_encrypted}')
                
                if 'NOT_DECRYPTED' in reader.decrypt(password).name:
                    print(f'your passsword: {password} was wrong')
                    return print(f'remove from folder and try program again')
                else:
                    print(f'Password correct')
                    writer = pypdf.PdfWriter()
                    writer.append(reader)
                    print(f'Saving decrypted files to {decrypted_folder}')
                    with open(f'{decrypted_folder}/{filename[:-4]}_DECRYPTED.pdf', 'wb') as file:
                        writer.write(file)
    print(f'done')




path_input = input(f'Please provide folder path where I will decrypt files:\n')
password_input = input(f'Please provide password to unlock the files (this will be used on all of them):\n')
decrypted_input = input(f'Please provide folder path where files will be saved:\n')
decrypto(path_input, password_input, decrypted_input)