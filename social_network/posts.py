from datetime import datetime

# Please remove the comments and 
# create these classes as it corresponds:
# (your tests will fail if you don't comment out these classes)

class Post(object):
    def __init__(self, text, timestamp=None):
        self.text = text
        self.timestamp = timestamp
        self.user = None

    def set_user(self, user):
        self.user = user


class TextPost(Post):  # Inherit properly
    def __init__(self, text, timestamp=None):
        super().__init__(text, timestamp)
        
    def __str__(self):
        return '@{user}: "{text}"\n\t{timestamp}'.format(user=self.user,text=self.text,timestamp=self.timestamp.strftime('%A, %b %d, %Y'))


class PicturePost(Post):  # Inherit properly
    def __init__(self, text, image_url, timestamp=None):
        super().__init__(text, timestamp)
        self.image_url = image_url

    def __str__(self):
        return '@{user}: "{text}"\n\t{image_url}\n\t{timestamp}'.format(user=self.user,text=self.text,image_url=self.image_url,timestamp=self.timestamp.strftime('%A, %b %d, %Y'))


class CheckInPost(Post):  # Inherit properly
    def __init__(self, text, latitude, longitude, timestamp=None):
        super().__init__(text, timestamp)
        self.latitude = latitude
        self.longitude = longitude

    def __str__(self):
        return '@{user_fname} Checked In: "{text}"\n\t{latitude}, {longitude}\n\t{timestamp}'.format(user_fname=self.user.first_name,text=self.text,latitude=self.latitude,longitude=self.longitude,timestamp=self.timestamp.strftime('%A, %b %d, %Y'))
