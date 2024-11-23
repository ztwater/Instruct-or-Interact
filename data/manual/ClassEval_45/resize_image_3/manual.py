### Method Description:
    def resize_image(self, width, height):
        """
        Risize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        >>> processor.load_image('test.jpg')
        >>> processor.resize_image(300, 300)
        >>> processor.image.width
        300
        >>> processor.image.height
        300
        """

### Solution Code:
    def resize_image(self, width, height):
        if self.image:
            self.image = self.image.resize((width, height))

### Source Code:
    def resize_image(image):
        if image.mode == 'RGB':
            width, height = image.size
            if width > 1000 or height > 1000:
                image = image.resize((width // 2, height // 2))
        return image

### Predicted Code:
    def resize_image(self, width, height):
        """
        Resize the image if image has opened.
        :param width: int, the target width of image
        :param height: int, the target height of image
        """
        if self.image.mode == 'RGB':
            width, height = self.image.size
            if width > 1000 or height > 1000:
                self.image = self.image.resize((width // 2, height // 2))
        self.image.width = width
        self.image.height = height

### Adaptation:
Total number: 25
### Raw Output:
```python
def resize_image(self, width, height):
    """
    Resize the image if image has opened.
    :param width: int, the target width of image
    :param height: int, the target height of image
    """
    if self.image.mode == 'RGB':
        width, height = self.image.size
        if width > 1000 or height > 1000:
            self.image = self.image.resize((width // 2, height // 2))
    self.image.width = width
    self.image.height = height
```

### Test Code:
class ImageProcessorTestResizeImage(unittest.TestCase):
    def setUp(self):
        self.processor = ImageProcessor()
        self.image_path = os.path.join(os.path.dirname(__file__), "test.png")
        image = Image.new("RGB", (100, 100), (255, 255, 255))
        image.save(self.image_path)

    def tearDown(self):
        self.processor.image.close()

    def test_resize_image(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(30, 15)
        self.assertEqual(self.processor.image.size, (30, 15))

    def test_resize_image_2(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(30, 15)
        self.assertEqual(self.processor.image.mode, "RGB")

    def test_resize_image_3(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(30, 15)
        self.assertEqual(self.processor.image.format, None)

    def test_resize_image_4(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(40, 20)
        self.assertEqual(self.processor.image.mode, "RGB")

    def test_resize_image_5(self):
        self.processor.load_image(self.image_path)
        self.processor.resize_image(50, 25)
        self.assertEqual(self.processor.image.format, None)

### Test Output:
# 5 errors, 0 failures in 5 runs.
# errors:
#     NameError:
#         test_resize_image: name 'os' is not defined
#         test_resize_image_2: name 'os' is not defined
#         test_resize_image_3: name 'os' is not defined
#         test_resize_image_4: name 'os' is not defined
#         test_resize_image_5: name 'os' is not defined
# failures:


### Dependencies:
# lib_dependencies: 
# field_dependencies: self.image
# method_dependencies: 


