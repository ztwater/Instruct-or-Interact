class ImageProcessor:
    def adjust_brightness(image):
        if image.mode in ('RGBA', 'LA'):
            # Convert image to RGB mode if it has an alpha channel or is in grayscale mode
            image = image.convert('RGB')
    
        enhancer = ImageEnhance.Brightness(image)
        adjusted_image = enhancer.enhance(1.5)  # Increase brightness by a factor of 1.5
    
        return adjusted_image