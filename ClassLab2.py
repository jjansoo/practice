class Member:
    def __init__(self,name,account,passwd,birthyear):
        self.m_name = name
        self.m_account = account
        self.m_passwd = passwd
        self.m_birthyear = birthyear


member1 = Member('홍진수','dkdlfjs7894','123123','961008')
member2 = Member('정재용','jaeyongism','321321','960121')
member3 = Member('김아무개','kimamugae','456456','961111')

print(f'회원1 {member1.m_name}({member1.m_account},{member1.m_passwd},{member1.m_birthyear})')
print(f'회원2 {member2.m_name}({member2.m_account},{member2.m_passwd},{member2.m_birthyear})')
print(f'회원3 {member3.m_name}({member3.m_account},{member3.m_passwd},{member3.m_birthyear})')