import os
import shutil

# -- File types supported -- #

image = ['.jpeg', '.jpg', '.png', '.jfif']
adobe = ['.ai', '.ps']
text = ['.txt']
apps = ['.py', '.cs', '.cpp', '.jar', '.java', '.exe']
zip_file = ['.zip']

image_name = 'Images'
adobe_name = 'Adobe Files'
text_name = "Text Files"
app_name = "Apps"
zip_name = "Zipped Files"


# -- Function to create folders for sorting -- #
# This function creates folders associated with the file types
# and assigns the type to it

def folders(old, new):
    print(f'folder: {old}')
    print(f'destination: {new}')

    image_folder = new + f'\\{image_name}\\'
    adobe_folder = new + f'\\{adobe_name}\\'
    text_folder = new + f'\\{text_name}\\'
    app_folder = new + f'\\{app_name}\\'
    zip_folder = new + f'\\{zip_name}\\'

    for file in os.listdir(old):
        os.chdir(old)
        ext = os.path.splitext(file)
        print(ext[1])

        if ext[1] in image:
            if not os.path.exists(image_folder):
                os.chdir(new)
                os.mkdir(image_name)
                continue

        elif ext[1] in adobe:
            if not os.path.exists(adobe_folder):
                os.chdir(new)
                os.mkdir(adobe_name)
                continue

        elif ext[1] in text:
            if not os.path.exists(text_folder):
                os.chdir(new)
                os.mkdir(text_name)
                continue

        elif ext[1] in apps:
            if not os.path.exists(app_folder):
                os.chdir(new)
                os.mkdir(app_name)
                continue

        elif ext[1] in zip_file:
            if not os.path.exists(zip_folder):
                os.chdir(new)
                os.mkdir(zip_name)
                continue


# -- Sorting Function -- #
# Loops through the original folder and moves files
# to their respective folders

def sorting(old, new):
    print(f'folder: {old}')
    print(f'destination: {new}')

    image_folder = new + f'\\{image_name}\\'
    adobe_folder = new + f'\\{adobe_name}\\'
    text_folder = new + f'\\{text_name}\\'
    app_folder = new + f'\\{app_name}\\'
    zip_folder = new + f'\\{zip_name}\\'

    for file in os.listdir(old):

        os.chdir(old)
        ext = os.path.splitext(file)
        print(ext[1])

        if ext[1] in image:
            if os.path.exists(image_folder):
                shutil.move(file, image_folder)
                continue

        elif ext[1] in adobe:
            if os.path.exists(adobe_folder):
                shutil.move(file, adobe_folder)
                continue

        elif ext[1] in text:
            if os.path.exists(text_folder):
                shutil.move(file, text_folder)
                continue

        elif ext[1] in apps:
            if os.path.exists(app_folder):
                shutil.move(file, app_folder)
                continue

        elif ext[1] in zip_file:
            if not os.path.exists(app_folder):
                shutil.move(file, zip_folder)
                continue

