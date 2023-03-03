import statistics

class Movie:
    all_movies = []

    def __init__(self, title):
         if type(title) == str:
           self.title = title
         else:
            raise Exception("Movie title must be a string")
         
         self.reviews = [] 
         self.reviewers = []

    # title property goes here!
    def get_title(self):
        return self._title
    
    def set_title(self, title):
        if type(title) == str and len(title) > 0:
            self._title = title
        else:
            raise Exception("TITLE CAN NOT BE EMPTY BRO")
        
    title = property(get_title, set_title)

#We will back 
    def average_rating(self):
        total = 0

        for review in self.reviews:
            total += review

        average = total / len(self.reviews)

        return average

        pass

    @classmethod
    def highest_rated(cls):
        #???????
        return cls.all_movies
    #I see your request for the highest rating and I instead offer up all movies. 
        pass
