import os
import random
from functools import lru_cache
import logging

logger = logging.getLogger(__name__)

class ImageHandler:
    SUPPORTED_EXTENSIONS = ('.jpg', '.png', '.jpeg', '.gif')

    @staticmethod
    @lru_cache(maxsize=128)
    def get_image_list(directory: str) -> list:
        """Get cached list of images from directory."""
        if not os.path.exists(directory):
            logger.warning(f"Directory not found: {directory}")
            return []
        images = [f for f in os.listdir(directory) if f.lower().endswith(ImageHandler.SUPPORTED_EXTENSIONS)]
        return images

    @staticmethod
    def get_random_image(directory: str) -> str:
        """Select a random image with validation."""
        images = ImageHandler.get_image_list(directory)
        if not images:
            logger.error(f"No valid images found in {directory}")
            return None
        selected_image = os.path.join(directory, random.choice(images))
        if os.path.getsize(selected_image) > 0:  # Check for empty files
            return selected_image
        logger.warning(f"Selected image is empty: {selected_image}")
        return None
