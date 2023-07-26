import os
import shutil

audio = ('.mp3', '.flac', '.wav')
video = ('.mp4', '.mov')
img = ('.jpg', '.jpeg', '.png', '.svg', '.gif')
docs = ('.doc', '.docx', '.pdf', '.rtf', '.txt')

def FileOrganiser(fileFolder, destinationFolder):
    categories = ['Video', 'Audio', 'Images', 'Docs', 'Others']
    for category in categories:
        folderPath = os.path.join(destinationFolder, category)
        os.makedirs(folderPath, exist_ok=True)

    with os.scandir(fileFolder) as entries:
        for entry in entries:
            if entry.is_file():
                file = entry.name
                filename, ext = os.path.splitext(file)
                ext = ext.lower()

                if ext in video:
                    dest = os.path.join(destinationFolder, 'Video')
                elif ext in audio:
                    dest = os.path.join(destinationFolder, 'Audio')
                elif ext in img:
                    dest = os.path.join(destinationFolder, 'Images')
                elif ext in docs:
                    dest = os.path.join(destinationFolder, 'Docs')
                else:
                    dest = os.path.join(destinationFolder, 'Others')

                shutil.move(os.path.join(fileFolder, file), os.path.join(dest, file))

filePath = input("Enter File Path: ").strip()
destinationPath = input("Enter Destination Folder Path: ").strip()
FileOrganiser(filePath, destinationPath)
