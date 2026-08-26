class Complex:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def adicionar(self, complex):
        real = self.real + complex.real
        imag = self.imag + complex.imag
        novo = Complex(real, imag)
        return novo

    def subtrair(self, complex):
            real = self.real - complex.real
            imag = self.imag - complex.imag
            novo = Complex(real, imag)
            return novo

    def imprimir(self):
         print(f"({self.real}, {self.imag})")

if __name__ == "__main__":
     c1 = Complex(1,1)
     #c1.imprimir()
     c2 = Complex(2,3)
     #c2.imprimir()

     c3 = c1.adicionar(c2)
     c3.imprimir()

     c4 = c2.subtrair(c1)
     #c4.imprimir()






    