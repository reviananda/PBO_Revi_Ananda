print(len("polymorphism"))
print(len([0, 1, 2]))

class jerman :
    def ibukota(self) :
        print("Berlin adalah ibukota negara Jerman")

class jepang :
    def ibukota(self) :
        print("Tokyo adalah ibukota negara Jepang")

negara1 = jerman()
negara2 = jepang()

for country in (negara1, negara2) :
    country.ibukota()