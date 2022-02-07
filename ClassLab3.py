class Book:
    def __init__(self,title,author,price):
        self.B_title = title
        self.B_author = author
        self.B_price = price
    def __str__(self):
        return 'Book 클래스로 생성된 객체'

    def getBookInfo(self):
        return self.B_title + ',' + self.B_author + ',' + str(self.B_price)

Books = []

for idx,ch in enumerate(['A','B','C','D','E']):
    Books.append(Book(ch,ch+str(idx),10 +idx))

for idx,Book in enumerate(Books):
    print(f'[객체{idx} : {Book.__str__()}')
    info = Book.getBookInfo().split(',')
    print(f'책이름: {info[0]}')
    print(f'저자: {info[1]}')
    print(f'가격 : {info[2]}')