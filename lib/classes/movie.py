class Movie:
    all=[]

    def __init__(self, title):
        self.title = title
        Movie.all.append(self)
    @property
    def title(self):
        return self._title
    @title.setter
    def title(self,title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise Exception

    def reviews(self):
        from classes.review import Review
        return [review for review in Review.all if review.movie == self]
    
    def reviewers(self):
        from classes.viewer import Viewer
        return [review for review in Viewer.all if review.movie == self]
    
    def average_rating(self):
        total = sum([review.rating for review in self.reviews()])
        return total / len(self.reviews())

    @classmethod
    def highest_rated(cls):
        pass
