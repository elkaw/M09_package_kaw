import pandas as pd
class BookLover:
    name = None
    email = None
    fav_genre = None
    num_books = None
    book_list = None

    def __init__(self,name, email, fav_genre, num_books = 0, book_list = pd.DataFrame({'book_name':[], 'book_rating':[]})):
        self.name = name
        self.email = email
        self.book_list = book_list

    def add_book(self, book_name, rating):
        """
            This function takes a `book name` (string) and `rating` (integer from 0 to 5)
            It tries to add the book to `book_list`. See hint below on how to pass a new book to the dataframe.
            Only add a book to the person’s `book_list` if that book doesn’t already exist.
            It is sufficient to match on `book_name`.
            If it does exist, tell the user.
        """

        new_book = pd.DataFrame({
            'book_name': [book_name],
            'book_rating': [rating]
        })
        if self.book_list[self.book_list['book_name'] == book_name].shape[0] >0:
            print("Book already exists, please add another book")
        else:
            self.book_list = pd.concat([self.book_list, new_book], ignore_index=True)





    def has_read(self, book_name):
        """
            This function takes `book_name` (string) as input and determines if the person has read the book.
            That is, if that `book name` is in `book_list`.
            Again, it is sufficient to match on `book_name`.
            The method should return `True` if the person has read the book, `False` otherwise.
        """
        if self.book_list[self.book_list['book_name'] == book_name].shape[0] > 0:
            return True
        else:
            return False





    def num_books_read(self):
        """
        This function takes no parameters and just returns the total number of books the person has read.
        """
        return self.book_list['book_name'].shape[0]


    def fav_books(self):
        """
            This function takes no parameters and returns the filtered dataframe of the person’s most favorite books.
            Books in this list should have a rating > 3.
        """
        return self.book_list[self.book_list['book_rating']>3]




