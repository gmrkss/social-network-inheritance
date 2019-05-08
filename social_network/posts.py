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


# class TextPost(...):  # Inherit properly
#     def __init__(self, text, timestamp=None):
#         pass
#
#     def __str__(self):
#         pass


# class PicturePost(...):  # Inherit properly
#     def __init__(self, text, image_url, timestamp=None):
#         pass
#
#     def __str__(self):
#         pass


# class CheckInPost(...):  # Inherit properly
#     def __init__(self, text, latitude, longitude, timestamp=None):
#         pass
#
#     def __str__(self):
#         pass
