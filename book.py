import shelve
from tools import message_output

class Book:
    @staticmethod
    def add_book(book_id: str, title: str, author: str, year: int, status: str):
        with shelve.open('bookDB', 'c') as file:
            file[book_id] = [title, author, year, status]
            return file[book_id]

    def input_add_book(self):
        '''Добавляет книгу. Запрашивает название, автора, год от пользователя.'''
        try:
            with shelve.open('bookDB') as file:
                keys = list(file.keys())
                last_id = keys[-1]

                book_id = str(int(last_id) + 1)

            title = input('Enter title: ')
            assert title
            author = input('Enter author: ')
            assert author
            year = input('Enter year: ')
            assert year

            status = 'в наличии'

            res = self.add_book(book_id, title, author, int(year), status)
            message_output(f'The book added successfully: {res}')

        except AssertionError:
            message_output('You cannot enter an empty line')
        except ValueError:
            message_output('The year must be a number')


    @staticmethod
    def find_book(choice: int, sign: str):
        books_res = []
        with shelve.open('bookDB', 'r') as file:
            for value in file.values():
                if sign == value[(choice - 1)]:
                    books_res.append(value)

        return books_res

    def input_find_book(self):
        '''Поиск книги по названию, автору, году'''
        try:
            print('What to look for?:')
            print('1 - Title')
            print('2 - Author')
            print('3 - Year')
            choice = int(input('Enter status: '))
            assert 1 <= choice <= 3

            sign = input('Enter: ')

            books = self.find_book(choice, sign)

            if books:
                input(books)
            else:
                message_output('There are no such books')

        except ValueError:
            message_output('You cannot enter an empty line')
        except AssertionError:
            message_output('There in no such option')


    @staticmethod
    def read_all_books():
        '''Выводит все книги'''
        with shelve.open('bookDB') as file:
            for key in file.keys():
                print(key, file[key])

    @staticmethod
    def update_book(book_id: str, status: str):
        with shelve.open('bookDB') as file:
            book = file[book_id]
            book[3] = status
            file[book_id] = book
            return file[book_id]

    def input_update_book(self):
        '''Обновляет статус книги по id'''
        try:
            book_id = input('Enter id: ')

            print('Statues:')
            print('1 - в наличие')
            print('2 - выдана')
            status_id = input('Enter status: ')

            assert 1 <= int(status_id) <= 2

            status_all = {
                '1': 'в наличие',
                '2': 'выдана',
            }
            status = status_all[status_id]

            res = self.update_book(book_id, status)
            message_output(f'The book updated successfully: {res}')

        except KeyError:
            message_output('There is no such book')
        except ValueError:
            message_output('You cannot enter an empty line')
        except AssertionError:
            message_output('There is on such option')

    @staticmethod
    def delete_book(book_id: str):
        with shelve.open('bookDB') as file:
            state = file.pop(book_id, 'NotFound')
            return state

    def input_delete_book(self):
        '''Удаляет книгу по id'''
        try:
            book_id = input('Enter id: ')

            res = self.delete_book(book_id)
            assert res != 'NotFound'

            message_output(f'The book deleted successfully:  {res}')

        except AssertionError:
            message_output('There is no such book')
        except ValueError:
            message_output('You cannot enter an empty line')
