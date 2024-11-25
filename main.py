from tools import line, clear_console, message_output, func_with_clear_console
from book import Book
def app():
    while True:
        line()
        print('Library')
        line()
        print('What do you do?')
        print('1 - Add book')
        print('2 - Find book')
        print('3 - Watch all books')
        print('4 - Update book')
        print('5 - Delete book')
        print('6 - Exit')
        choice_number = input('Enter a number: ')

        book = Book()
        if choice_number == '1':
            func_with_clear_console(book.input_add_book)
        elif choice_number == '2':
            func_with_clear_console(book.input_find_book)
        elif choice_number == '3':
            func_with_clear_console(Book.read_all_books, stop_clear=True)
        elif choice_number == '4':
            func_with_clear_console(book.input_update_book)
        elif choice_number == '5':
            func_with_clear_console(book.input_delete_book)
        elif choice_number == '6':
            break
        else:
            message_output('There is no such option')


if __name__ == '__main__':
    clear_console()
    app()