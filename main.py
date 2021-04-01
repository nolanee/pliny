from book_files import Pliny_books
from list_occurrences import list_greek

lists_storage = []
for book in Pliny_books:
    lists_storage.append(list_greek(book))

passage_list = ""
for li in lists_storage:
    passage_list += ', '.join(li)
    passage_list += '\n'

file = open("results.txt", 'w')
file.write(passage_list)
file.close