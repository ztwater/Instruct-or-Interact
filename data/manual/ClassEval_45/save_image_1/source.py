class ImageProcessor:
    def save_image(image, path):
        if image is not None:
            image.save(path)
            print("Image saved successfully!")
        else:
            print("No image has been opened.")