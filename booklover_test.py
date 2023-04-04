import unittest as u
from booklover import BookLover
from pandas import pandas as pd






class BookLoverTestSuite(u.TestCase):
    

    #def main():
    #    BLTS = BookLoverTestSuite()
    #    BLTS.test_1_add_book()
    #    BLTS.test_2_add_book()
    #    BLTS.test_3_has_read()
    #    BLTS.test_4_has_read()
    #    BLTS.test_5_num_books_read()
    #    BLTS.test_6_fav_books()


    def test_1_add_book(self):
        BL = BookLover('ekaw','elk7ed@virginia.edu','nonfiction')
        BL.add_book('Pendragon',5)
        self.assertEqual(BL.book_list[BL.book_list['book_name'] == 'Pendragon'].shape[0] , 1)
        # add a book and test if it is in `book_list`.


    def test_2_add_book(self):

        BL = BookLover('ekaw','elk7ed@virginia.edu','nonfiction')
        BL.add_book('Pendragon',5)        
        BL.add_book('Pendragon',5)
        self.assertEqual(BL.book_list[BL.book_list['book_name'] == 'Pendragon'].shape[0],1)

    # add the same book twice. Test if it's in `book_list` only once.

    def test_3_has_read(self):

        BL = BookLover('ekaw','elk7ed@virginia.edu','nonfiction')
        BL.add_book('Pendragon',5)
        self.assertTrue(BL.has_read('Pendragon'))

    

    # pass a book in the list and test if the answer is `True`.

    def test_4_has_read(self):

        BL = BookLover('ekaw','elk7ed@virginia.edu','nonfiction')    
        BL.add_book('Pendragon',5)
        self.assertFalse( BL.has_read('50 Shades of Grey'))

    # pass a book NOT in the list and use `assert False` to test the answer is `True`

    def test_5_num_books_read(self):

        BL = BookLover('ekaw','elk7ed@virginia.edu','nonfiction')
        BL.add_book('BhagavadGita', 5)
        BL.add_book('KashmirShaivism', 5)
        BL.add_book('Bible', 5)
        BL.add_book('TheKingdomOfHeavenIsWithinYou', 5)
        BL.add_book('Pendragon', 5)
        self.assertEqual(BL.num_books_read(),5)
    # add some books to the list, and test num_books matches expected.

    def test_6_fav_books(self):
        BL = BookLover('ekaw','elk7ed@virginia.edu','nonfiction')
        BL.add_book('BhagavadGita', 5)
        BL.add_book('KashmirShaivism', 5)
        BL.add_book('Bible', 5)
        BL.add_book('TheKingdomOfHeavenIsWithinYou', 5)
        BL.add_book('Pendragon', 5)
        BL.add_book('BeingMortal', 2)
        BL.add_book('GameOfThrones', 3)
        BL.add_book('50ShadesofGray', 1)
        self.assertEqual(BL.fav_books().shape[0], 5)
# add some books with ratings to the list, making sure some of them have rating > 3. 
# Your test should check that the returned books have rating  > 3


if __name__ == '__main__':
    u.main(verbosity=3)