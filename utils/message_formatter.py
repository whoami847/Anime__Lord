import os
import random

class MessageFormatter:
    @staticmethod
    def format_message(message, image_dir=None):
        if image_dir and os.path.exists(image_dir):
            images = [os.path.join(image_dir, f) for f in os.listdir(image_dir) if f.endswith(('.jpg', '.png'))]
            image = random.choice(images) if images else None
        else:
            image = None
        return message, image
