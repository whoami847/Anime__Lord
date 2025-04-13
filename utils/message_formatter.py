from .font_formatter import FontFormatter
from .image_handler import ImageHandler

class MessageFormatter:
    @staticmethod
    def format_message(text: str, image_dir: str = None, style: str = "small_caps") -> tuple:
        """Format message with text style and optional image."""
        formatted_text = FontFormatter.format_text(text, style)
        image = ImageHandler.get_random_image(image_dir) if image_dir else None
        return formatted_text, image

    @staticmethod
    def create_template(text: str, placeholders: dict, style: str = "small_caps") -> str:
        """Create a formatted message from a template."""
        for key, value in placeholders.items():
            text = text.replace(f"{{{key}}}", str(value))
        return FontFormatter.format_text(text, style)
