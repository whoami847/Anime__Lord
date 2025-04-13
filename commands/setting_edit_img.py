import os

def setting_edit_img(photo, dir: str):
    file_path = os.path.join(dir, f"settings_image_{photo.file_id}.jpg")
    return file_path
