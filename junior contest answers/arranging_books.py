book_shelf = input()
swaps = 0
books = []
for letter in book_shelf:
    books.append(letter)
while True:    
    count = 0
    for book in books:
        try:
            if book == 'L' and books[count-1] == 'S':
                books[count] = books[count-1]
                books[count-1] = book
                swaps += 1
            elif book == 'L' and books[count+1] == 'S':
                books[count] = books[count+1]
                books[count+1] = book
                swaps += 1
            count += 1
        except:
            print(swaps, books); exit()

            
