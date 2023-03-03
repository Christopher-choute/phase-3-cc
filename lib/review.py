from movie import Movie
from viewer import Viewer
class Review:
    
    def __init__(self, viewer, movie, rating):
        self.viewer = viewer
        self.movie = movie
        self.rating = rating

        # self.add_review_to_movie()
        # self.add_review_to_viewer()
        # self.add_movie_to_viewer()
        pass

    # rating property goes here!
    @property
    def rating(self):
        return self._rating

    @rating.setter
    def rating(self, rating):
        if type(rating) == int and 1 <= rating <= 5:  
            self._rating = rating
        else:
            raise Exception("Rating must be between 1 and 5")
    # viewer property goes here!
    @property
    def viewer(self):
        return self._viewer
    
    @viewer.setter
    def viewer(self, viewer):
        if isinstance(viewer, Viewer):
            self._viewer = viewer
        else:
            raise Exception("Viewer must be an instance of Viewer")
    # movie property goes here!
    @property
    def movie(self):
        return self._movie
    
    @movie.setter
    def movie(self, movie):
        if isinstance(movie, Movie):
            self._movie = movie
        else:
            raise Exception("Movie must be an instance of Movie")
        

    # def add_review_to_viewer():
    #     self.viewer.reviews.append(self)

    # def add_review_to_movie():
    #     self.movie.reviews.append(self)

    # def add_movie_to_viewer():
    #     self.movie.viewers.append(self)


#I Think somewhere in the code above is causing additional code to fail. No good