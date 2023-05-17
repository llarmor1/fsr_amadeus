from instagrapi.types import StoryMention



class StoryManager:
    def __init__(self, client):
        self.client = client



    def post_story(self, story, user_mentions=[]):

        if user_mentions == []:
            return self.client.photo_upload_to_story(story)
        else:
            usr_list = []
            for user in user_mentions:
                try:
                    usr = self.client.user_info_by_username(user)
                    usr_list.append(StoryMention(user=usr, x=0.5, y=0.5, width=0.5, height=0.125))

                except:
                    print(f"User '{user}' not found!\n")
                    
            return self.client.photo_upload_to_story(story, mentions=usr_list)
    
    def like_story(self):
        pass

    def unlike_story(self):
        pass
        