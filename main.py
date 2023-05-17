from instagrapi import Client
import config

from modules.stories import StoryManager
from modules.posts import PostManager


modules = {"StoryManager": StoryManager,
           "PostManager": PostManager}



class IgClient:
    def __init__(self, account_username, account_password, modules):
        self.account_username = account_username
        self.account_password = account_password
        self.cl = Client()
        self.story_manager = modules['StoryManager'](self.cl)

    def login(self):
        self.cl.login(self.account_username, self.account_password)

    def command(self):
        cmd = input("\n[1] Stories\n").split()[0]
        if cmd.isdigit():
            if int(cmd) == 1:
                storie_selection = input("\n[1] Upload storie\n").split()[0]
                if int(storie_selection) == 1:
                    path = input("Path: ")
                    mentions = input("Mentions (Optional): ").split()
                    self.story_manager.post_story(path, mentions)
                    print("Done!")

    
if __name__ == '__main__':
    igclient = IgClient(config.account_username, config.account_password, modules=modules)
    try:
        igclient.login()
    except (RuntimeError, TypeError, NameError):
        print(RuntimeError+"\n"+TypeError+"\n"+NameError)
    
    igclient.command()
    




