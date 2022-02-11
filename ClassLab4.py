class GoodStock:
    # init 클래스 내부에서 사용할 변수 초기화
    def __init__(self,code,num):
        #상품 수량
        self.goodsCode = code
        #재고 수량
        self.stockNum = num

    #재고 수량을 계산 함수
    def addStock(self,amount): # stockNum--> 기존재고 + 추가재고
        # stockNum = stockNum + amount
        self.stockNum += amount

#input() 특징 : 리턴값 타입 = String
code = input("상품 코드 입력 : ")
num = int(input("상품 수량 입력 :"))

#객체 생성 방법
#변수(객체) =Goodstock()
obj = GoodStock(code,num)

amount = int(input("추가 수량 입력:"))
obj.addStock(amount)

print("재고 수량 :",obj.stockNum)


#깃허브 연습
