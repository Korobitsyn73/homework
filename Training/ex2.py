from book import Book


library = [
    Book('Идиот', 'Достоевский'),
    Book("Мастер и Маргарита", 'Булгаков'),
    Book('Каштанка', 'Чехов')]

for book in library:
    print(f'{book.title} - {book.author}')
