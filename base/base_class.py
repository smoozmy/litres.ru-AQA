class Base():

    def __init__(self, driver):
        self.driver = driver

    """ Получение текущего URL """

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f'Текущий url - {get_url}')

    """ Проверка текста """

    def assert_word(self, word, result):
        value_word = word.text
        assert value_word == result
        print('Текстовое значение соответствует ✅')