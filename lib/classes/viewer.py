class Viewer:
    all = []
    def __init__(self, username):
        self.username = username
        Viewer.all.append(self)
    @property
    def username(self):
        return self._username
    @username.setter
    def username(self,username):
        if isinstance(username, str) and 6 <= len(username) <= 16:
            self._username = username
        else:
            raise Exception

    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.viewer == self]
    
    def reviewed_movies(self):
        pass

    def has_reviewed_movie(self, movie):
        pass
