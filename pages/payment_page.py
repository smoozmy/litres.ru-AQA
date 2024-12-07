from base.base_class import Base
import allure

""" Эта страница является условным финалом клиентского пути при покупке книги на сайте litres """

class Payment_page(Base):

    # Methods

    def payment_finish(self):
        with allure.step('[payment finish] Книга приобретена'):
            self.screen()
            print('Книга куплена ✅')

