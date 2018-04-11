from random import randint
from math import floor

class Puzzle:
    # Creating rings: inner to outer
    arr1 =  [13, 0, 3, 0, 3, 0, 6, 0,10, 0,10, 0,10, 0, 6, 0]

    arr2 = [[10, 2, 6,10, 4, 1, 5, 5, 4, 8, 6, 3, 1, 6,10, 6],
            [22, 0, 2, 0,17, 0,15, 0,14, 0, 5, 0,10, 0, 2, 0]]

    arr3 = [[11,27,14, 5, 5, 7, 8,24, 8, 3, 6,15,22, 6, 1, 1],
            [16, 0,17, 0, 2, 0, 2, 0,10, 0,15, 0, 6, 0, 9, 0]]

    arr4 = [[ 9, 7, 3,12,24,10, 9,22, 9, 5,10, 5, 1,24, 2,10],
            [11,27,10,19,10,13,10, 2,15,23,19, 3, 2, 3,27,20]]

    # Creates a new random puzzle, if default set to False
    def __init__(self, default=False):
        if not default:
        	# Creates random values
            for i in range(16):
                a = randint(2,floor(40*0.6))
                b = randint(2,floor((40-a)*0.6))
                c = randint(2,floor((40-a-b)*0.6))
                d = 40-a-b-c
                self.iterSingle(i,4,[d,c,b,a])
            
            # Creates random values for those numbers under another number
            self.push(1)
            self.push(3)
            for i in range(16):
                if i % 2 == 0:
                    arr2[0][i] = randint(2,20)
                    arr4[0][i] = randint(2,20)
                else:
                    arr3[0][i] = randint(2,20)
            
            for n in range(1,5):
                # Shuffles the puzzle
                rand = randint(1,16)
                self.push(n, rand)

    # Selects rings
    def select(self, n):
        switch = {
            1: self.arr1,
            2: self.arr2,
            3: self.arr3,
            4: self.arr4
        }
        return switch.get(n)

    # Pushes a selected ring to the left by number of counts
    def push(self, n, count=1):
        arr = self.select(n)
        if n == 1:
            temp = arr[:count]
            del arr[:count]
            arr += temp
        else:
            temp = [arr[0][:count], arr[1][:count]]
            del arr[0][:count]
            del arr[1][:count]
            arr[0] += temp[0]
            arr[1] += temp[1]
        return arr

    # Returns the sum of a selected row i, starting from a selected ring n (defaults to outer ring)
    # If array of numbers is passed into argument, function replaces the number from outer to inner
    ### replace=[6,5,2,27] -> 6 goes to 1st (inner) ring, 27 goes to 4th (outer) ring
    def iterSingle(self, i=0, n=4, replace=[]):
        arr = self.select(n)
        # Innermost circle
        if n == 1:
            if replace:
                arr[i] = replace.pop(0)
                return 0
            else:
                data = arr[i]
                return data if data else self.arr2[0][i]

        # Outer three circles
        data = arr[1][i]
        if not data:
            if replace:
                self.select(n+1)[0][i] = replace.pop()
                return self.iterSingle(i,n-1,replace)
            else:
                data = self.select(n+1)[0][i]
        else:
            if replace:
                arr[1][i] = replace.pop()
                return self.iterSingle(i, n-1, replace)
        return data + self.iterSingle(i, n-1)

    # Prints the values of the rings
    def printP(self):
        puzzle = [
            self.arr1,
            self.arr2[1],
            self.arr3[1],
            self.arr4[1]
        ]
        for i in range(3):
            for j in range(16):
                if puzzle[i][j] == 0:
                    puzzle[i][j] = self.select(i+2)[0][j]

        print("From inner to outer:")
        for arr in puzzle:
            print(arr)

    # Finds the answer, including how many counts it takes
    def findAns(self):
        priCount = 0
        secCount = 0
        while True:
            if self.iterSingle(0) == 40:
                check = 0
                for i in range(1,16):
                    if not self.iterSingle(i) == 40:
                        break
                    else: check += 1
                if check == 15:
                    self.printP()
                    print("It took %d counts" % priCount)
                    return 0

            self.push(1)
            priCount += 1
            if priCount % 16 == 0:
                self.push(2)
                secCount += 1
                if secCount % 16 == 0:
                    self.push(3)
