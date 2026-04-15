

# 11-m
class Talaba:
    def __init__(self, ism, yosh, kurs, faqulted):
        self.ism = ism
        self.yosh = yosh
        self.kurs = kurs
        self.faqulted = faqulted

t1 = Talaba("Ali", 20, 2, "IT")
print(t1.ism)
print(t1.yosh)
print(t1.kurs)
print(t1.faqulted)

t2 = Talaba("Vali", 22, 3, "Iqtisod")
print(t2.ism)
print(t2.yosh)
print(t2.kurs)
print(t2.faqulted)


# 12-m
class Kitob:
    def __init__(self, nomi, muallif, janr, narx):
        self.nomi = nomi
        self.muallif = muallif
        self.janr = janr
        self.narx = narx


k1 = Kitob("O‘tkan kunlar", "Abdulla Qodiriy", "roman", 50000)
print(k1.nomi)
print(k1.muallif)
print(k1.janr)
print(k1.narx)

k2 = Kitob("Alkimyogar", "Paulo Coelho", "fantastika", 40000)
print(k2.nomi)
print(k2.muallif)
print(k2.janr)
print(k2.narx)


# 13-m
class Telefon:
    def __init__(self, madel, rang, xotira, narx):
        self.madel = madel
        self.rang = rang
        self.xotira = xotira
        self.narx = narx

t1 = Telefon("iPhone 13", "qora", "128GB", 1200)
print(t1.madel)
print(t1.rang)
print(t1.xotira)
print(t1.narx)

t2 = Telefon("Samsung S21", "oq", "256GB", 950)
print(t2.madel)
print(t2.rang)
print(t2.xotira)
print(t2.narx)


# 14-m
class Mashina:
    def __init__(self, marka, rang, yili, narx):
        self.marka = marka
        self.rang = rang
        self.yili = yili
        self.narx = narx

m1 = Mashina("Cobalt", "oq", 2022, 12000)
print(m1.marka)
print(m1.rang)
print(m1.yili)
print(m1.narx)

m2 = Mashina("Cobalt", "oq", 2022, 12000)
print(m2.marka)
print(m2.rang)
print(m2.yili)
print(m2.narx)


# 15-m
class Xodim:
    def __init__(self, ism, yosh, lavozim, maosh):
        self.ism = ism
        self.yosh = yosh
        self.lavoz = lavozim
        self.maosh = maosh

x1 = Xodim("Ali", 25, "Backend developer", 2000)
print(x1.ism)
print(x1.yosh)
print(x1.lavoz)
print(x1.maosh)


x2 = Xodim("Vali", 30, "Team lead", 3000)
print(x2.ism)
print(x2.yosh)
print(x2.lavoz)
print(x2.maosh)
