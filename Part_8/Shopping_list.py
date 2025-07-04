class Book:
    def __init__(self,name, author, genre, year):
        self.name = name
        self.author = author
        self.genre = genre
        self.year = year

    def name(self):
        return self.name
    def author(self):
        return self.author
    def year(self):
        return self.year
    def genre(self):
        return self.genre
    

python = Book("Fluent Python", "Luciano Ramalho", "programming", 2015)
everest = Book("High Adventure", "Edmund Hillary", "autobiography", 1956)

print(f"{python.author}: {python.name} ({python.year})")
print(f"The genre of the book {everest.name} is {everest.genre}")