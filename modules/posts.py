import main



class PostManager:
    def __init__(self, client):
        self.client = client




    def post_image(self, photo, comment): # In development
        return self.client.photo_upload(photo, comment)
    