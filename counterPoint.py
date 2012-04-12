import random

#Create Fringe list
fringe = []


def formatter():



    #Get cantus firmus from user
    def userInput():
        
        print("Enter a Cantus Firmus as notes seperated by commas")
        userInput = input('>>>')
        for note in userInput.split(","):
            cantusFirmus.append(int(note))
            
        cantusFirmus.printCantus()
#        findFirstNote(cantusFirmus.getNote(0))
        


    def inRange(cantusNote, note):
        if cantusNote + note <= 81:
            return True
        else:
            return False
        
    
    def findFirstNote(cantusNote):
       
        melodicPossibilities = [0,7,12,19,24]

        for n in melodicPossibilities:
            if inRange(cantusNote, n):
                x = Node(0, n)
                fringe.append(x)
        print(fringe)




    userInput()

    
#-------------------------------------------------------------------------------
class Problem(object):

    def __init__(self, initial, goal=None):
        """The constructor specifies the initial state, and possibly a goal
        state, if there is a unique goal.  Your subclass's constructor can add
        other arguments."""
        self.initial = initial; self.goal = goal

    def result(self, state, mvmt=None):
        self.state = state
        state = state + 1
        return state 


    def actions(self, state, interval):
        self.interval = interval
        intervals = []
        if state == 0:
            melodicPossibilities = [0,7,12,19,24]
        else:
            melodicPossibilities = [3,4,7,8,9,12]

        for n in melodicPossibilities:
            "if new node is not higher than a5 and interval is not same as last interval"
            if (n + cantusFirmus.getNote(state-1) <= 81):
                if (self.interval is not n):                   
                    intervals.append(n)
        return intervals

    def goal_test(self, node):
        """Return True if the state is a goal. The default method compares the
        state to self.goal, as specified in the constructor. Override this
        method if checking against a single self.goal is not enough."""
        if node.state >= cantusFirmus.size():
           notes = []
           for tempNode in node.path():
               notes.append(tempNode.note)
               if (notes.count(max(notes)) == 1):
                   return True
        else:
            return False

#---Counterpoint tests here
    def highest_melody_test(self):
        return True
        

#-------------------------------------------------------------------------------

class CantusFirmus(object):
    
    def __init__(self, x):
        self.name = x
        self.cantusFirmus = []
        self.minorSecond = None
        self.majorSecond = None
        self.minorThird = None
        self.majorThird = None
        self.perfectFourth = None
        self.augmentedFourth = None
        self.minorSixth = None
        self.majorSixth = None
        self.minorSeventh = None
        self.majorSeventh = None

    def append(self, note):
        self.cantusFirmus.append(int(note))

    def setCantus(self, cantusFirmus):
        self.cantusFirmus = cantusFirmus   

    def printCantus(self):
        print(self.cantusFirmus)

    def getNote(self, i):
        return self.cantusFirmus[i]

    def size(self):
        return len(self.cantusFirmus)

    def find_qualities(self):
        self.tonic = self.cantusFirmus[-1]
        self.snd = self.cantusFirmus[-2]
        
        #Find minor Third
        for i in range(-21, 16, 12):
            if ((self.tonic + i) in self.cantusFirmus):
                self.minorThird = True
        #Find major Third
        for i in range(-20, 17, 12):
            if ((self.tonic + i) in self.cantusFirmus):
                self.majorThird = True

        # If minor Third Exists
        if self.minorThird:
            # find m2
            for i in range(-23, 14, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.minorSecond = True
            # find M2
            for i in range(-22, 15, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.majorSecond = True
            self.find_seventh()
            self.find_sixth()

        # If major Third Exists
        if self.majorThird:
            # find P4
            for i in range(-19, 18, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.perfectFourth = True
            # find +4
            for i in range(-18, 19, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.augmentedFourth = True
            self.find_seventh()
            self.find_sixth()

    def find_seventh(self):
        # find m7
        for i in range(-14, 23, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.minorSeventh = True
        # find m7
        for i in range(-13, 24, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.majorSeventh = True

    def find_sixth(self):
        # find m6
        for i in range(-16, 21, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.minorSixth = True
        # find m6
        for i in range(-15, 22, 12):
                if ((self.tonic + i) in self.cantusFirmus):
                    self.majorSixth = True

    def find_mode(self):
        self.modes = ['ionian', 'lydian', 'mixolydian', 'phrygian', 'minor', 'dorian', 'aeolian']
        if self.minorThird:
            self.modes.remove('ionian')
            self.modes.remove('lydian')
            self.modes.remove('mixolydian')
            if self.minorSecond:
                self.modes.remove('minor')
                self.modes.remove('dorian')
                self.modes.remove('aeolian')
            elif self.majorSecond:
                self.modes.remove('phrygian')
            elif self.minorSeventh:
                self.modes.remove('minor')
                ww
                if self.majorSixth:
                    self.modes.remove('dorian')
    
        elif self.majorThird: 
            self.modes.remove('dorian')
            self.modes.remove('phrygian')
            self.modes.remove('aeolian')
            self.modes.remove('minor')
            if self.perfectFourth:
                self.modes.remove('lydian')
                if self.majorSeventh:
                    self.modes.remove('mixolydian')
                elif self.minorSeventh:
                    self.modes.remove('ionian')
            elif self.augmentedFourth:
                self.modes.remove('ionian')
                self.modes.remove('mixolydian')
            elif self.minorSeventh:
                self.modes.remove('ionian')
                self.modes.remove('lydian')

        

#-------------------------------------------------------------------------------

class Node(object):
    
    def __init__(self, state, interval=0, parent=None):
        self.state = state
        self.parent = parent
        self.interval = interval
        if (state == 0):
            self.cantus = 0
            self.note = 0
        else:
            self.cantus = cantusFirmus.getNote(self.state-1)
            self.note = cantusFirmus.getNote(self.state-1) + interval

        if parent:
            self.depth = parent.depth + 1
        else:
            self.depth = 0

    def __repr__(self):
        return "<node " + repr(self.state) + "," + repr(self.cantus) + "," + repr(self.note) + "," + repr(self.interval) + ">"

    def expand(self, problem):
        "List the nodes reachable in one step from this node."
        return [self.child_node(problem, action)
            for action in problem.actions(self.state, self.interval)]

    def child_node(self, problem, action):
        "Fig. 3.10"
        next = problem.result(self.state)
        return Node(next, action, self)

    def path(self):
        "Return a list of nodes forming the path from the root to this node."
        node, path_back = self, []
        while node:
            path_back.append(node)
            node = node.parent
        return list(reversed(path_back))

    def nodeNotes(self):
        return (repr(self.cantus) + " " + repr(self.note))
        



#______________________________________________________________________________
# Uninformed Search algorithms



def tree_search(problem, frontier):
    """Search through the successors of a problem to find a goal.
    The argument frontier should be an empty queue.
    Don't worry about repeated paths to a state. [Fig. 3.7]"""
    frontier.append(Node(problem.initial))
    while frontier:
        node = frontier.pop()
        if problem.goal_test(node):
            return node
        print(node)
        frontier.extend(node.expand(problem))
    return None



def breadth_first_tree_search(problem):
    "Search the shallowest nodes in the search tree first."
    return tree_search(problem, FIFOQueue())


def depth_first_tree_search(problem):
    "Search the deepest nodes in the search tree first."
    return tree_search(problem, Stack())

def print_one():
    x = Frontier()
    z = tree_search1(problem,x)
    for x in z.path(): print(x)

#-------------------------------------------------------------------------------

class Queue:
    """Queue is an abstract class/interface. There are three types:
        Stack(): A Last In First Out Queue.
        FIFOQueue(): A First In First Out Queue.
        PriorityQueue(order, f): Queue in sorted order (default min-first).
    Each type supports the following methods and functions:
        q.append(item)  -- add an item to the queue
        q.extend(items) -- equivalent to: for item in items: q.append(item)
        q.pop()         -- return the top item from the queue
        len(q)          -- number of items in q (also q.__len())
        item in q       -- does q contain item?
    Note that isinstance(Stack(), Queue) is false, because we implement stacks
    as lists.  If Python ever gets interfaces, Queue will be an interface."""

    def __init__(self):
        abstract

    def extend(self, items):
        for item in items: self.append(item)

def Stack():
    """Return an empty list, suitable as a Last-In-First-Out Queue."""
    return []

class FIFOQueue(Queue):
    """A First-In-First-Out Queue."""
    def __init__(self):
        self.A = []; self.start = 0
    def append(self, item):
        self.A.append(item)
    def __len__(self):
        return len(self.A) - self.start
    def extend(self, items):
        self.A.extend(items)
    def pop(self):
        e = self.A[self.start]
        self.start += 1
        if self.start > 5 and self.start > len(self.A)/2:
            self.A = self.A[self.start:]
            self.start = 0
        return e
    def __contains__(self, item):
        return item in self.A[self.start:]


class PriorityQueue(Queue):
    """A queue in which the minimum (or maximum) element (as determined by f and
    order) is returned first. If order is min, the item with minimum f(x) is
    returned first; if order is max, then it is the item with maximum f(x).
    Also supports dict-like lookup."""
    def __init__(self, order=min, f=lambda x: x):
        update(self, A=[], order=order, f=f)
    def append(self, item):
        bisect.insort(self.A, (self.f(item), item))
    def __len__(self):
        return len(self.A)
    def pop(self):
        if self.order == min:
            return self.A.pop(0)[1]
        else:
            return self.A.pop()[1]

    def __getitem__(self, key):
        for _, item in self.A:
            if item == key:
                return item
    def __delitem__(self, key):
        for i, (value, item) in enumerate(self.A):
            if item == key:
                self.A.pop(i)
                return



#Create CantusfFirmus Object
cantusFirmus = CantusFirmus('x')
problem = Problem(0)
formatter()
