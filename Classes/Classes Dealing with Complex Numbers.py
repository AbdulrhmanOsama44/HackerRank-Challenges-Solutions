class Complex(object):
    def __init__(self, real, imaginary):
        
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, no):
        
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        
        a, b, c, d = self.real, self.imaginary, no.real, no.imaginary
        return Complex(a * c - b * d, a * d + b * c)

    def __truediv__(self, no):
        
        a, b, c, d = self.real, self.imaginary, no.real, no.imaginary
        nom = Complex(a, b) * Complex(c, -1 * d)
        denom = (Complex(c, d) * Complex(c, -1 * d)).real
        return Complex(nom.real / denom, nom.imaginary / denom)

    def mod(self):
        
        return Complex(math.sqrt(self.real ** 2 + self.imaginary ** 2), 0)

    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result