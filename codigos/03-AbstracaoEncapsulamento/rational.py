import math

class RationalNumber:
    def __init__(self, numerador=1, denominador=1):
        self.num = numerador
        self.den = denominador

    def adicionar(self, racional):
        novo = RationalNumber()
        if self.den == racional.den:
            num = self.num + racional.num
            novo.num = num
            novo.den = self.den
        else:
            mmc = math.lcm(self.den, racional.den)
            num = ((mmc / self.den) * self.num) + ((mmc / racional.den) * racional.num)
            novo.num = num
            novo.den = mmc

        return novo

    def subtrair(self, racional):
            novo = RationalNumber()
            if self.den == racional.den:
                num = self.num - racional.num
                novo.num = num
                novo.den = self.den
            else:
                mmc = math.lcm(self.den, racional.den)
                num = ((mmc / self.den) * self.num) - ((mmc / racional.den) * racional.num)
                novo.num = num
                novo.den = mmc
    
            return novo

    def multiplicar(self, racional):
         novo = RationalNumber()
         novo.num = self.num * racional.num
         novo.den = self.den * racional.den
         return novo


    def dividir(self, racional):
        novo = RationalNumber()
        novo.num = self.num * racional.den
        novo.den = self.den * racional.num
        return novo

    def imprimir(self):
        print(f"{self.num}/{self.den}")

    def imprimirFloat(self):
        print(self.num / self.den)



if __name__ == "__main__":
    r1 = RationalNumber(3,4)
    r2 = RationalNumber(2,4)
    r3 = r1.adicionar(r2)
    r3.imprimir()
    r3.imprimirFloat()

    r1 = RationalNumber(3,4)
    r2 = RationalNumber(2,4)
    r3 = r1.subtrair(r2)
    r3.imprimir()
    r3.imprimirFloat()

    r1 = RationalNumber(3,4)
    r2 = RationalNumber(2,4)
    r3 = r1.multiplicar(r2)
    r3.imprimir()
    r3.imprimirFloat()

    r1 = RationalNumber(3,4)
    r2 = RationalNumber(2,4)
    r3 = r1.dividir(r2)
    r3.imprimir()
    r3.imprimirFloat()