from base.base_class import Base

""" Эта страница является условным финалом клиентского пути при покупке книги на сайте litres """

class Payment_page(Base):

    # Methods

    def payment_finish(self):
        self.screen()
        print('Книга куплена ✅')

