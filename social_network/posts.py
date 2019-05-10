from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super().__init__(text)
        super().__init__(timestamp)
        
    def __str__(self):
        pass


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text)
        self.image_url = image_url
        super().__init__(timestamp)

    def __str__(self):
        pass


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text)
        self.latitude = latitude
        self.longitude = longitude
        super().__init__(timestamp)

    def __str__(self):
        pass
