class Member:
    def __init__(self, name, member_id, borrowed_books):
        self.name = name
        self.member_id = member_id
        self.borrowed_books = borrowed_books
    def get_profile(self):
        return f"Name: {self.name} | Member_ID: {self.member_id} | Borrowed_books: {self.borrowed_books}"
