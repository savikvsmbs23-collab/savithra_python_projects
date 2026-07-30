class Book:
    def __init__(self, title, author, genre):
        self.title = title
        self.author = author
        self.genre = genre
        self.available = True

    def get_details(self):
        return f"Title: {self.title} | Author: {self.author} | Genre: {self.genre}: Available: {self.available}"
