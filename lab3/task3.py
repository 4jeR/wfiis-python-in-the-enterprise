#Matrix. 


#Write a class that can represent any 4𝑥4 real matrix. 
#Include two functions to calculate the sum and dot product of two matrices. 
#Next, write a program that imports this library module and use it to perform calculations.
# You CAN'T use numpy.
#Examples:
#
# matrix_1 = Matrix(4.,5.,6.,7.)
# matrix_2 = Matrix(2.,2.,2.,1.)
#
# matrix_3 = matrix_2 @ matrix_1
# matrix_4 = matrix_2 + matrix_1
# matrix_4 = 6 + matrix_1
# matrix_4 = matrix_1 + 6
#
# expand your solution to include other operations like
# - subtraction 
# - inversion
# - string representation 
#
#Try to expand your implementation as best as you can. 
#Think of as many features as you can, and try implementing them.
#Make intelligent use of pythons syntactic sugar (overloading, iterators, generators, etc)
#Most of all: CREATE GOOD, RELIABLE, READABLE CODE.
#The goal of this task is for you to SHOW YOUR BEST python programming skills.
#Impress everyone with your skills, show off with your code.
#
#Your program must be runnable with command "python task.py".
#Show some usecases of your library in the code (print some things)
#Delete these comments before commit!
#
#Good luck.



class Matrix:
    def __init__(self, a0=0, a1=0, a2=0, a3=0):
        self.a0 = a0
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3


    def __str__(self):
        return f'''Matrix:
            {self.a0} {self.a1}
            {self.a2} {self.a3}
        '''

    def __add__(self, other_matrix):
        if isinstance(other_matrix, Matrix):
            m = Matrix(self.a0, self.a1, self.a2, self.a3)
            m.a0 += other_matrix.a0
            m.a1 += other_matrix.a1
            m.a2 += other_matrix.a2
            m.a3 += other_matrix.a3
            return m
        else:
            m = Matrix(self.a0, self.a1, self.a2, self.a3)
            m.a0 += other_matrix
            m.a1 += other_matrix
            m.a2 += other_matrix
            m.a3 += other_matrix
            return m


    def __sub__(self, other_matrix):
        m = Matrix(self.a0, self.a1, self.a2, self.a3)
        m.a0 -= other_matrix.a0
        m.a1 -= other_matrix.a1
        m.a2 -= other_matrix.a2
        m.a3 -= other_matrix.a3
        return m

    
    def __mul__(self, other_matrix):
        m = Matrix(self.a0, self.a1, self.a2, self.a3)
        s = 0
        s += m.a0 * other_matrix.a0
        s += m.a1 * other_matrix.a1
        s += m.a2 * other_matrix.a2
        s += m.a3 * other_matrix.a3
        return s
    

def main():
    matrix_1 = Matrix(4.,5.,6.,7.)
    print(matrix_1)

    matrix_2 = Matrix(2.,2.,2.,1.)
    print(matrix_2)

    matrix_3 = matrix_2 * matrix_1
    print(f'Dot product is: {matrix_3}')

    matrix_4 = matrix_2 + matrix_1
    print(matrix_4)

    matrix_4 = matrix_1 + 6
    print(matrix_4)



if __name__ == '__main__':
    main()
        
