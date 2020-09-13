import unittest
from collections import deque
from queue_solution import *


class CompanyTest(unittest.TestCase):

    def assertCompanyEqual(self, actual,expected):
        
        n = len(expected._employees)
        m = len(actual._employees)
        if n != m:
            raise Exception("Number of employees is wrong ! EXPECTED=%s ACTUAL=%s" % (n, m))

        for i in range(len(expected._employees)):
            ex = expected._employees[i]
            ac = actual._employees[i]
            if 'name' not in ac:
                raise Exception('%s-th Employee does not have "name"!\n: %s ' % (i, ac))
            if 'rank' not in ac:
                raise Exception('%s-th Employee does not have "rank"!\n: %s ' % (i, ac))
            if 'tasks' not in ac:
                raise Exception('%s-th Employee does not have "tasks"!\n: %s ' % (i, ac))

            if ex['name'] != ac['name']:
                raise Exception('%s-th Employee:\nEXPECTED name=%s \nACTUAL name=%s  ' 
                                 % (i, ex['name'], ac['name']))
            if ex['rank'] != ac['rank']:
                raise Exception('%s-th Employee:\nEXPECTED rank=%s \nACTUAL rank=%s  ' 
                                 % (i, ex['rank'], ac['rank']))

            if ex['tasks'] != ac['tasks']:
                raise Exception('%s-th Employee:\nEXPECTED tasks=%s \nACTUAL tasks=%s  ' 
                                 % (i, ex['tasks'], ac['tasks']))


class AddEmployeeTest(CompanyTest):
    
    def test_add_employee(self):
        c1 = Company()
        c2 = Company()
        self.assertCompanyEqual(c1,c2)

        c1.add_employee('x',9)
        c2._employees = [{'name':'x',
                          'rank':9,
                          'tasks':deque()}]
        self.assertCompanyEqual(c1,c2)
        c1.add_employee('z',2)
        c2._employees = [{'name':'x',
                          'rank':9,
                          'tasks':deque()},
                         {'name':'z',
                          'rank':2,
                          'tasks':deque()}]
        self.assertCompanyEqual(c1,c2)
        c1.add_employee('y',6)
        c2._employees = [{'name':'x',
                          'rank':9,
                          'tasks':deque()},
                         {'name':'y',
                          'rank':6,
                          'tasks':deque()},
                         {'name':'z',
                          'rank':2,
                          'tasks':deque()}]
        self.assertCompanyEqual(c1,c2)

    def test_wrong_employee(self):
        c = Company()
        c.add_employee('x',9)
        with self.assertRaises(ValueError):
            c.add_employee('x',7)
        with self.assertRaises(ValueError):
            c.add_employee('y',9)

class AddTaskTest(CompanyTest):

    def test(self):
        c1 = Company()
        c1.add_employee('x',9)
        c1.add_employee('y',6)

        with self.assertRaises(ValueError):
            c1.add_task('a',7, 'w')

        c1.add_task('a', 3, 'x')

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        c2._employees[0]['tasks'] = deque([('a',3)])

        self.assertCompanyEqual(c1, c2)

        c1.add_task('b', 5, 'x')

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        c2._employees[0]['tasks'] = deque([('a',3),('b',5)])

        self.assertCompanyEqual(c1, c2)

        c1.add_task('c', 1, 'y')

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        c2._employees[0]['tasks'] = deque([('a',3),('b',5)])
        c2._employees[1]['tasks'] = deque([('c',1)])

        self.assertCompanyEqual(c1, c2)

class WorkTest(CompanyTest):

    def test_01_empty(self):
        c1 = Company()
        c2 = Company()
        self.assertCompanyEqual(c1,c2)
        c1.work()
        self.assertCompanyEqual(c1,c2)

    def test_02_one_less(self):
        c1 = Company()
        c1.add_employee('x',9)

        c1.add_task('a',8,'x')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)

        self.assertCompanyEqual(c1,c2)


    def test_03_one_same(self):
        c1 = Company()
        c1.add_employee('x',9)

        c1.add_task('a',9,'x')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)

        self.assertCompanyEqual(c1,c2)

    def test_04_one_more(self):
        c1 = Company()
        c1.add_employee('x',9)

        c1.add_task('a',10,'x')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)

        self.assertCompanyEqual(c1,c2)



    def test_05_up_highest_1(self):
        c1 = Company()
        c1.add_employee('x',9)
        c1.add_employee('y',6)

        c1.add_task('a',9,'x')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        self.assertCompanyEqual(c1,c2)

    def test_06_up_highest_2(self):
        c1 = Company()
        c1.add_employee('x',9)
        c1.add_employee('y',6)

        c1.add_task('a',12,'x')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        self.assertCompanyEqual(c1,c2)

    def test_07_up(self):
        c1 = Company()
        c1.add_employee('x',9)
        c1.add_employee('y',6)

        c1.add_task('a',8,'x')
        c1.add_task('b',7,'y')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        c2._employees[0]['tasks'] = deque([('b',7)])
        self.assertCompanyEqual(c1,c2)


    def test_08_down_highest_1(self):
        c1 = Company()
        c1.add_employee('x',9)
        c1.add_employee('y',6)

        c1.add_task('a',8,'x')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        self.assertCompanyEqual(c1,c2)

    def test_09_down_highest_2(self):
        c1 = Company()
        c1.add_employee('x',9)
        c1.add_employee('y',6)

        c1.add_task('a',7,'x')
        self.assertEqual(c1.work(), ['a'])

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        self.assertCompanyEqual(c1,c2)

    def test_10_down(self):
        c1 = Company()
        c1.add_employee('x',9)
        c1.add_employee('y',6)

        c1.add_task('a',6,'x')
        c1.add_task('b',3,'y')
        self.assertEqual(c1.work(), ['b'])

        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('y',6)
        c2._employees[1]['tasks'] = deque([('a',6)])
        self.assertCompanyEqual(c1,c2)


    def test_11_complex(self):

        c = Company()

        c.add_employee('x',9)
        c.add_employee('z',2)
        c.add_employee('y',6)

        c.add_task('a',3,'x')
        c.add_task('b',5,'x')
        c.add_task('c',12,'x')
        c.add_task('d',1,'x')
        c.add_task('e',8,'y')
        c.add_task('f',2,'y')
        c.add_task('g',8,'y')
        c.add_task('h',10,'z')
        
        self.assertEqual(c.work(), [])
        self.assertEqual(c.work(), ['f'])
        self.assertEqual(c.work(), ['c'])
        self.assertEqual(c.work(), ['a'])
        self.assertEqual(c.work(), ['e'])
        self.assertEqual(c.work(), ['g', 'b'])
        self.assertEqual(c.work(), ['h', 'd'])
        
        c2 = Company()
        c2.add_employee('x',9)
        c2.add_employee('z',2)
        c2.add_employee('y',6)

        self.assertCompanyEqual(c,c2)
