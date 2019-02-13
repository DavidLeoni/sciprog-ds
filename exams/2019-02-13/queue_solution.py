
from collections import deque

DEBUG_ON = True

def debug(msg):
    if DEBUG_ON:
        print("DEBUG: %s" % msg)

class Company:

    def __init__(self):
        self._employees = []   # a list of dictionaries


    def __str__(self):
        """
            name  rank  tasks
              x    9:    []
              y    6:    []
              z    2:    []
        """
        import textwrap

        f = '  %-6s%-6s%-6s'
        s = textwrap.dedent("""
                                Company:
                                """ + f % ("name","rank","tasks") + "\n")

        for i in range(len(self._employees)):
            e = self._employees[i]
            s +=  f % (e['name'], e['rank'], str(e['tasks'])) + "\n"

        return s
    
    def __repr__(self):
        return self.__str__()


    def add_employee(self, name, rank):
        """
            Adds employee with name and rank to the company, maintaining 
            the _employees list sorted by rank (higher rank comes first)

            Represent the employee as a dictionary with keys 'name', 'rank' 
            and 'tasks' (a Python deque)

            - here we don't mind about complexity, feel free to use a linear scan and .insert 
            - If an employee of the same rank already exists, raise ValueError
            - if an employee of the same name already exists, raise ValueError
        """   
        #jupman-raise

        for e in self._employees:
            if e['name'] == name:
                raise ValueError("There is already an employee with same name ! %s" % e)

        i = 0
        while i < len(self._employees):
            e = self._employees[i]
            r = e['rank']
            if rank == r:
                raise ValueError("There is already an employee with same rank ! %s" % e)
            elif rank > r:
                break
            i += 1
        newe = {
            'name':name,
            'rank':rank,
            'tasks':deque()
        }
        self._employees.insert(i,newe)
        #/jupman-raise

    def add_task(self, task_name, task_rank, employee_name):
        """ Append the task as a (name, rank) tuple to the tasks of 
            given employee

            - If employee does not exist, raise ValueError
        """
        #jupman-raise
        es = self._employees
        for i in range(len(es)):
            if es[i]['name'] == employee_name:
                es[i]['tasks'].append((task_name,task_rank))
                return
        raise ValueError("Couldn't find employee %s " % employee_name)
        #/jupman-raise

    def work(self):
        """ Performs a work step and RETURN a list of performed task names.

            For each employee, dequeue its current task from the left and:
            - if the task rank is greater than the rank of the
            current employee, append the task to his supervisor queue 
            (the highest ranking employee must execute the task)
            - if the task rank is lower or equal to the rank of the
            next lower ranking employee, append the task to that employee queue
            - otherwise, add the task name to the list of
              performed tasks to return
        """
        #jupman-raise
        ret = []
        i = 0
        es = self._employees
        for i in range(len(es)):
            e = es[i]
            if len(e['tasks']) > 0:
                task = e['tasks'].popleft()
                  
                if i > 0 and task[1] > es[i]['rank']:
                    debug("Employee %s gives task %s to employee %s" % (e['name'], task, es[i-1]['name']))
                    es[i-1]['tasks'].append(task)
                elif i+1 < len(es) and task[1] <= es[i+1]['rank']:
                    debug("Employee %s gives task %s to employee %s" % (e['name'], task, es[i+1]['name']))
                    es[i+1]['tasks'].append(task)
                else:
                    debug("Employee %s executes task %s" % (e['name'],task))
                    ret.append(task[0])      
        debug('Total performed work this step: %s' % ret)              
        return ret
        #/jupman-raise
