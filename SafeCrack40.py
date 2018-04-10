class Puzzle:
    #Creating rings: inner to outer
    arr1 =  [13, 0, 3, 0, 3, 0, 6, 0,10, 0,10, 0,10, 0, 6, 0]

    arr2 = [[10, 2, 6,10, 4, 1, 5, 5, 4, 8, 6, 3, 1, 6,10, 6],
            [22, 0, 2, 0,17, 0,15, 0,14, 0, 5, 0,10, 0, 2, 0]]

    arr3 = [[11,27,14, 5, 5, 7, 8,24, 8, 3, 6,15,22, 6, 1, 1],
            [16, 0,17, 0, 2, 0, 2, 0,10, 0,15, 0, 6, 0, 9, 0]]

    arr4 = [[ 9, 7, 3,12,24,10, 9,22, 9, 5,10, 5, 1,24, 2,10],
            [11,27,10,19,10,13,10, 2,15,23,19, 3, 2, 3,27,20]]

    def select(self, n):
        switch = {
            1: self.arr1,
            2: self.arr2,
            3: self.arr3,
            4: self.arr4
        }
        return switch.get(n,0)

    def push(self, n):
        arr = self.select(n)
        if n == 1:
            temp = arr[0]
            for i in range(len(arr)-1):
                arr[i] = arr[i+1]
            arr[-1] = temp

        else:
            temp = [arr[0][0], arr[1][0]]
            for i in range(len(arr[0])-1):
                arr[0][i] = arr[0][i+1]
                arr[1][i] = arr[1][i+1]
            arr[0][-1] = temp[0]
            arr[1][-1] = temp[1]
        return arr

    def sumSingle(self, i=0, n=0):
        arr = self.select(n)
        if n == 1:
            data = arr[i]
            return data if data else self.arr2[0][i]

        data = arr[1][i]
        if not data:
            data = self.select(n+1)[0][i]
        return data + self.sumSingle(i, n-1)

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

        print "From inner to outer:"
        for arr in puzzle:
            print arr

        def findAns(self):
            priCount = 0
            secCount = 0
            while True:
                if self.sumSingle(0) == 40:
                    check = 0
                    for i in range(1,16):
                        if not self.sumSingle(i) == 40:
                            break
                        else: check += 1
                    if check == 15:
                        self.printP()
                        print "It took %d counts" % priCount
                        return 0

                self.push(1)
                priCount += 1
                if priCount % 16 == 0:
                    self.push(2)
                    secCount += 1
                    if secCount % 16 == 0:
                        self.push(3)
