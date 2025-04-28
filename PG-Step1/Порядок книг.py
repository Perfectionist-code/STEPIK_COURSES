def deleting_initials(book_lst):
    new_book_lst = []
    for word_lst in book_lst:
        del word_lst[1]
        word_str = ' '.join(word_lst)
        new_book_lst.append(word_str)
    return new_book_lst


number = int(input())
books = [input().split() for _ in range(number)]
new_book_lst = deleting_initials(books)
print(('NO', 'YES')[new_book_lst == sorted(new_book_lst)])