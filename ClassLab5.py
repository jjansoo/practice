class Account:
  def __init__(self, accountNo, ownerName, balance):
      # 클래스 내부에서 사용할 변수 초기화
      # self.변수이름
      self.accountNo = accountNo
      self.ownerName = ownerName
      self.balance = balance

  def deposit(self, amount):
      # 입금한다
      # 잔액 = 기존잔액 + 입금한금액
      # self.balance += amount
      self.balance += amount

  def withdraw(self, amount):
      # 출금한다
      # 만약, 기존잔액 < 출금할금액 -> 출금 못함
      if self.balance < amount:
         return 0

      # 잔액 = 기존잔액 - 출금할금액
      self.balance -= amount

def printAccount(obj):
   print("계좌번호 : " + obj.accountNo)
   print("예금주   : " + obj.ownerName)
   print("잔액     : " + str(obj.balance))
   print()


# 객체 생성
obj1 = Account("111-222-33333", "홍진수", 50000)
obj2 = Account("222-333-44444", "정재용", 100000)

obj1.deposit(100000)
printAccount(obj1)

obj2.withdraw(30000)
printAccount(obj2)