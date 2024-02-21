import os

def create_if_not_exist(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

def move(folder_name, files):
    for file in files:
        os.replace(file, os.path.join(folder_name, file))

files = os.listdir()
files.remove("main.py")

create_if_not_exist('Images')
create_if_not_exist('Docs')
create_if_not_exist('Media')
create_if_not_exist('Others')

doc_exts = [".txt", ".docx", ".doc", ".pdf", ".xlsx", ".ppt"]
img_exts = [".png", ".img", ".jpg", ".jpeg"]
media_exts = [".mp4", ".mp3", ".avi", ".flv", ".mpeg"]

images = [file for file in files if os.path.splitext(file)[1].lower() in img_exts]
docs = [file for file in files if os.path.splitext(file)[1].lower() in doc_exts]
medias = [file for file in files if os.path.splitext(file)[1].lower() in media_exts]
others = [file for file in files if os.path.isfile(file) and os.path.splitext(file)[1].lower() not in (media_exts + doc_exts + img_exts)]

move("Images", images)
move("Docs", docs)
move("Media", medias)
move("Others", others)
