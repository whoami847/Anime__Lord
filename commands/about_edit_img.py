import os

def about_edit_img(photo, dir: str):
    file_path = os.path.join(dir, f"about_image_{photo.file_id}.jpg")
    return file_path
