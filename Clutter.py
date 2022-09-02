# This is the python clutter used by the users who want to make their directories systematic and clean
"""
This programme is not here because it can damage my files systematic arrangement so i prefer it to run in virtual environment name as clutter.
If you want to run this file in your computer then please go to the virtual environment projects and lets see the work
"""

import os

def make_Dir(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def Cleaner(File_type, folderName):
    folder = []
    Data = [file for file in files if os.path.splitext(file)[1].lower() in File_type]
    folder.append(Data)
    for file in folder:
        os.replace(file, f"{folderName}/{file}")

if __name__ == '__main__':

    DocExts = ['.docx', '.doc', '.html', '.htm', '.odt', '.pdf', '.xls', '.xlsx', '.ods', '.ppt', '.pptx', '.txt']
    ImgExts = ['.jpg', '.jpeg', '.png', '.tif', '.tiff', '.bmp', '.gif', '.eps', '.raw', '.cr2', '.nef', '.orf', '.sr2', '.wepb', '.psd', '.bmp', '.heif', '.indd', '.ai', '.eps']
    MediaExts = ['.mp4', '.mp3', '.flv']

    files = os.listdir()
    files.remove('main.py')
    print(files)

    make_Dir('Images')
    make_Dir('Docs')
    make_Dir('Medias')
    make_Dir('Others')

    Cleaner(DocExts, 'Docs')
    Cleaner(ImgExts, 'Images')
    Cleaner(MediaExts, 'Medias')

    others = []
    for file in files:
        ext = os.path.splitext(file)[1].lower()
        if (ext not in DocExts) and (ext not in ImgExts) and (ext not in MediaExts) and os.path.isfile(file):
            others.append(ext)
    Cleaner(MediaExts, 'Others')
    