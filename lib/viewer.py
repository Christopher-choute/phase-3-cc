class Viewer:
    
    def __init__(self, username):
        if type(username) == str:
            self.username = username
        else:
            raise Exception("Username must be a string!")

    # username property goes here!
    def get_username(self):
        return self._username
    
    def set_username(self, username):
        if type(username) == str and len(username) > 6 and len(username) < 16:
            self._username = username
        else:
            raise Exception("Username must be between 6 and 16 characters long!")

    viewer = property(get_username, set_username)
# We'll be back 
    def reviewed_movie(self, movie):
        # if movie in self.reviewed_movies:
        #     return True
        # else:
        #     return False
        pass

    def rate_movie(self, movie, rating):
         from review import Review
         Review(self, movie, rating)

