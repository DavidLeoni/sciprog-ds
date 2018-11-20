import unittest
from ComplexNumber_solution import *

class ComplexNumberTest(unittest.TestCase):

    """ Test cases for ComplexNumber

         Note this is a *completely* separated class from ComplexNumber and
         we declare it here just for testing purposes!
         The 'self' you see here have nothing to do with the selfs from the
         ComplexNumber methods!        
    """
        
    def test_01_init(self):
        self.assertEqual(ComplexNumber(1,2).real, 1)        
        self.assertEqual(ComplexNumber(1,2).imaginary, 2)
        
    def test_02_phase(self):
        """ 
            NOTE: we can't use assertEqual, as the result of phase() is a 
            float number which may have floating point rounding errors. So it's
            necessary to use assertAlmostEqual
            As an option with the delta you can declare the precision you require.
            For more info see Python docs: 
            https://docs.python.org/2/library/unittest.html#unittest.TestCase.assertAlmostEqual
            
            NOTE: assertEqual might still work on your machine but just DO NOT use it 
            for float numbers!!!
        """       
        self.assertAlmostEqual(ComplexNumber(0.0,1.0).phase(), math.pi / 2, delta=0.001)
        
    def test_03_str(self):        
        self.assertEqual(str(ComplexNumber(1,2)), "1 + 2i")        
        #self.assertEqual(str(ComplexNumber(1,0)), "1")
        #self.assertEqual(str(ComplexNumber(1.0,0)), "1.0")
        #self.assertEqual(str(ComplexNumber(0,1)), "i")
        #self.assertEqual(str(ComplexNumber(0,0)), "0") 

        
    def test_04_log(self):
        c = ComplexNumber(1.0,1.0)
        l = c.log(math.e)
        self.assertAlmostEqual(l.real, 0.0, delta=0.001)
        self.assertAlmostEqual(l.imaginary, c.phase(), delta=0.001)

class MagnitudeTest(unittest.TestCase):
    
    def test_01_magnitude(self):
        self.assertAlmostEqual(ComplexNumber(3.0,4.0).magnitude(),5, delta=0.001)

class EqTest(unittest.TestCase):
    def test_01_integer_equality(self):
        """
            Note all other tests depend on this test !

            We want also to test the constructor, so in c we set stuff by hand    
        """
        c = ComplexNumber(0,0)
        c.real = 1       
        c.imaginary = 2        
        self.assertEquals(c, ComplexNumber(1,2))         
        
class IscloseTest(unittest.TestCase):
    def test_01_isclose(self):
        """  Notice we use `assertTrue` because we expect `isclose` to return a `bool` value, and 
             we also test a case where we expect `False`
        """
        self.assertTrue(ComplexNumber(1.0,1.0).isclose(ComplexNumber(1.0,1.1), 0.2))        
        self.assertFalse(ComplexNumber(1.0,1.0).isclose(ComplexNumber(10.0,10.0), 0.2))        
               
class AddTest(unittest.TestCase):            
    def test_01_add_zero(self):
        self.assertEquals(ComplexNumber(1,2) + ComplexNumber(0,0), ComplexNumber(1,2));
        
    def test_02_add_numbers(self):        
        self.assertEquals(ComplexNumber(1,2) + ComplexNumber(3,4), ComplexNumber(4,6));

class RaddTest(unittest.TestCase):
     def test_01_add_scalar_right(self):        
        self.assertEquals(ComplexNumber(1,2) + 3, ComplexNumber(4,2));        

    def test_02_add_scalar_left(self):        
        self.assertEquals(3 + ComplexNumber(1,2), ComplexNumber(4,2));        

    def test_03_add_negative(self):
        self.assertEquals(ComplexNumber(-1,0) + ComplexNumber(0,-1), ComplexNumber(-1,-1));

