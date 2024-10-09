from PIL import Image, ImageDraw, ImageFont
import string

def is_arabic(char):
    """Determine if a character is Arabic."""
    return '\u0600' <= char <= '\u06FF' or '\u0750' <= char <= '\u077F' or char == '\u200c'

def get_text_size(draw, text, font):
    draw = ImageDraw.Draw(image)
    """Helper function to get the width and height of the text using textbbox()."""
    bbox = draw.textbbox((0, 0), text, font=font)
    width = bbox[2] - bbox[0]  # bbox[2] is the right, bbox[0] is the left
    height = bbox[3] - bbox[1]  # bbox[3] is the bottom, bbox[1] is the top
    return width, height

def draw_text(image, text, arabic_font, english_font, position, arabic_align="right", english_align="left", fill : tuple | str=(0, 0, 0)):
    """Draw text on the image, switching fonts and alignments between Arabic and English text."""
    
    draw = ImageDraw.Draw(image)
    
    words: list = []
    current_font = arabic_font if is_arabic(text[0]) else english_font
    current_align = arabic_align if is_arabic(text[0]) else english_align
    current_direction = 'rtl' if is_arabic(text[0]) else 'ltr'

    for char in text:
        if (is_arabic(char) and current_font == english_font) or (not is_arabic(char) and current_font == arabic_font and char != " "  and char not in string.punctuation):
            line = ''.join(words)
            width, height = get_text_size(draw, line, current_font)

            if current_direction == 'rtl': 
                draw.text((position[0] - width, position[1]), line, font=current_font, fill=fill, align=current_align, direction=current_direction)
            else:
                draw.text((position[0] - width, position[1]), line, font=current_font, fill=fill, align=current_align, direction=current_direction)
            
            position = (position[0], position[1] + height)

            words = []
            current_font = arabic_font if is_arabic(char) else english_font
            current_align = arabic_align if is_arabic(char) else english_align
            current_direction = 'rtl' if is_arabic(char) else 'ltr'

        words.append(char)

    # Draw the last word set
    line = ''.join(words)
    width, height = get_text_size(draw, line, current_font)
    if current_direction == 'rtl':
        draw.text((position[0] - width, position[1]), line, font=current_font, fill=fill, align=current_align)
    else:
        draw.text((position[0], position[1]), line, font=current_font, fill=fill, align=current_align)


# Save the image
    image_path = "handwritten_text_image.png"
    image.save(image_path)

# Show the image
    image.show()

# Output the file path for downloading
    print(f"The image has been saved as: {image_path}")
    
arabic_font = ImageFont.truetype("danstevis.otf", 30)
english_font = ImageFont.truetype("Julia_Handwritten_2.ttf", 30)
image = Image.new('RGB', (1200, 1500), 'white')
# Text content to write in the image
text = """ابزارهای چندرسانه‌ای:
نمایش تصویر: Zoner Photo Studio، XnView، و Windows Photo Viewer.
ویرایش تصویر: GIMP، Photoshop، CorelDraw.
پخش صدا و ویدئو: Winamp، VLC Player، Windows Media Player.
ویرایش ویدئو و صدا: Adobe Premiere، Final Cut Pro، Sound Forge.
تولید موسیقی و انیمیشن: Abelton Live، Toon Boom Studio، Blender.
ویژگی‌های تصاویر دیجیتال:
پیکسل و وضوح تصویر: پیکسل کوچک‌ترین واحد تصویر و وضوح آن تعداد پیکسل‌ها است.
نسبت تصویر: مثل 16:9 و 3:2.
رنگ و عمق رنگ: RGB و CMYK، عمق رنگ یعنی تعداد بیت‌های هر پیکسل.
فشرده‌سازی: بدون اتلاف (مثل PNG) و با اتلاف (مثل JPEG).
سایر ویژگی‌ها: کیفیت تصویر، مدل‌های رنگی، نور و کنتراست."""

# Define the text position on the image
textPosition = (200, 50)

draw_text(image, text, arabic_font, english_font, position=(1000, 50), arabic_align="right", english_align="right")