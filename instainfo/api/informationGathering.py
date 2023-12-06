from instagrapi import *

class InstagramChecker:

    def __init__(self):
        self.cl = Client()
        self.cl.login('seproject20023','se2023project' )

    def get_all_information(self, username: str):
        try:
            user_id =self.cl.user_id_from_username(username=username)

            information = {
                "biography" :self.cl.user_info(user_id).biography,
                "isPrivate" : self.cl.user_info(user_id).is_private,
                "followers" : self.cl.user_info(user_id).follower_count,
                "following" : self.cl.user_info(user_id).following_count,
                "profileUrl":self.cl.user_info(user_id).profile_pic_url,
            }
            return information
        except:
            return None


    def getNumOfFollowers(self,username : str):
        try:

            user_id =self.cl.user_id_from_username(username=username)
            return self.cl.user_info(user_id,use_cache=False).follower_count
        except:
            return None

    def getNumOfFollowing(self,username : str):
        try:

            user_id =self.cl.user_id_from_username(username=username)
            return self.cl.user_info(user_id,use_cache=False).following_count
        except:
            return None

    def get_bio(self,username : str):
        try:

            user_id =self.cl.user_id_from_username(username=username)
            return self.cl.user_info(user_id,use_cache=False).biography
        except:
            return None

    def get_profile_url(self,username: str):
        try:
            user_id = self.cl.user_id_from_username(username=username)
            return self.cl.user_info(user_id,use_cache=False).profile_pic_url
        except:
            return None