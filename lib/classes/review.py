
class Review:
    all = []
    def __init__(self, viewer, movie, rating):
        from classes.movie import Movie
        from classes.viewer import Viewer
        if isinstance(movie, Movie) and isinstance(viewer, Viewer):
            self.viewer = viewer
            self.movie = movie
            self.rating = rating
            Review.all.append(self)
        else:
            raise Exception
    @property
    def rating(self):
        return self._rating
    @rating.setter
    def rating(self,rating):
        if isinstance(rating, int) and 1<= (rating) <= 5:
            self._rating = rating
        else:
            raise Exception
    
    
    