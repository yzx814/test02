class Matrix:
    def __call__(self,date):
        self.date=date

    def __call__(self,other):
        a_row = len(self.date)
        a_col = len(self.date[0])

        b_row = len(self.date)
        b_col = len(self.date[0])


        if a_row != b_row and a_col != b_col :
            return "形状不同，不能相加"


        for row in rang(a_row) :
            for col in rang(a_col) :
                self.date[row][col] += other.date[row][col]


            return self
    def __str__(self):
            return str(self.date)

if __name__ == '__main__':
        a = Matrix([1, 48])
        b = Matrix([1,1])
print( a+b )

''' a = Matrix([[1, 29][56, 458]])
        b = Matrix([[1, 31, 29][56, 45, 48]])
        这样是错误的TypeError: list indices must be integers or slices, not tuple
        列表索引必须是整数或切片，而不是元组     a = Matrix([[1, 31, 29],[6, 45, 48]])
                                            b = Matrix([[1, 31, 29],[6, 45, 48]]) '''
