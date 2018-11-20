import math


class ComplexNumber:

    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary

    def __str__(self):
        return str(self.real) + " + " + str(self.imaginary) + "i"

    def phase(self):
        """ Returns a float which is the phase (that is, the vector angle) of the complex number 
        
            This method is something we introduce by ourselves, according to the definition:
            https://en.wikipedia.org/wiki/Complex_number#Absolute_value_and_argument
        """
        return math.atan2(self.imaginary, self.real)    
    
    def log(self, base):
        """ Returns another ComplexNumber which is the logarithm of this complex number 
            
            This method is something we introduce by ourselves, according to the definition:
            (accomodated for generic base b)
            https://en.wikipedia.org/wiki/Complex_number#Natural_logarithm
        """      
        return ComplexNumber(math.log(self.real) / math.log(base), self.phase() / math.log(base)) 
    
    
    def magnitude(self):
        """ Returns a float which is the magnitude (that is, the absolute value) of the complex number 
        
            This method is something we introduce by ourselves, according to the definition:
            https://en.wikipedia.org/wiki/Complex_number#Absolute_value_and_argument
        """
        #jupman-raise
        return math.sqrt(self.real**2 + self.imaginary**2)
        #/jupman-raise
    
    
    def __eq__(self, other): 
        # subtitute this with more precise code using the properties of the object
        return self is other
        #jupman-strip
        return self.real == other.real  and self.imaginary == other.imaginary
        #/jupman-strip
    
    def isclose(self, c, delta):
        """ Returns True if the complex number is within a delta distance from complex number c.                                
        """
        #jupman-raise
        return math.sqrt((self.real-c.real)**2 + (self.imaginary-c.imaginary)**2) < delta
        #/jupman-raise
        
    def __add__(self, other): 
        # subtitute this with more precise code using the properties of the object
        return NotImplemented
        #jupman-strip
        if isinstance(other, ComplexNumber): 
            return ComplexNumber(self.real + other.real,self.imaginary + other.imaginary)
        elif type(other) is int or type(other) is float:
            return ComplexNumber(self.real + other, self.imaginary)
        else:
            return NotImplemented
        #/jupman-strip

    def __radd__(self, other): 
        # subtitute this with more precise code using the properties of the object
        return NotImplemented
        
        #jupman-strip
        if (type(other) is int or type(other) is float):
            return ComplexNumber(self.real + other, self.imaginary)
        else:
            return NotImplemented
        #/jupman-strip
    
    def __mul__(self, other): 
        # subtitute this with more precise code using the properties of the object
        return NotImplemented
        
        #jupman-strip
        if isinstance(other, ComplexNumber): 
            return ComplexNumber(self.real * other.real - self.imaginary * other.imaginary,
                                 self.imaginary * other.real + self.real * other.imaginary)
        elif type(other) is int or type(other) is float:
            return ComplexNumber(self.real * other, self.imaginary * other)
        else:
            return NotImplemented
        #/jupman-strip
        
    def __rmul__(self, other):
        # subtitute this with more precise code using the properties of the object
        return NotImplemented
        
        #jupman-strip
        if (type(other) is int or type(other) is float):
            return ComplexNumber(self.real * other, self.imaginary * other)
        else:
            return NotImplemented
         #/jupman-strip