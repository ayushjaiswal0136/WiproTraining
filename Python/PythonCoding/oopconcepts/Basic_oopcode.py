class Movie:
    def __init__(self,name,genre):
        self.name = name
        self.genre = genre

    def show(self):
        print("Name:",self.name)
        print("Genre:",self.genre)


#Object Creation
m1 = Movie("Prometheus", "Sci-Fi")

#Calling
m1.show()