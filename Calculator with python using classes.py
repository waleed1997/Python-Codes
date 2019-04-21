import math
class calculator():

    def __init__(self):
        self.answer=0

    def addition(self,op1,op2):
        self.answer = op1 + op2
        return self.answer

    def subtraction(self,op1,op2):
        self.answer=op1-op2
        return self.answer

    def multiplication(self,op1,op2):
        self.answer=op1*op2
        return self.answer

    def division(self,op1,op2):
        self.answer=op1/op2
        return self.answer

    def square_root(self,op1):
        self.answer=math.sqrt(op1)
        return self.answer

    def cos_func(self,op1):
        self.answer=math.cos(op1)
        return self.answer

    def sin_func(self,op1):
        self.answer=math.sin(op1)
        return self.answer
    def power(self,op1,op2):
        self.answer=math.pow(op1,op2)
        return self.answer


operation=calculator()
print("CALCULATOR MADE BY MUHAMMAD WALEED USMAN\n")
print("Operand dictionary: \n"
      "+ for addition\n"
      "- for subtraction\n"
      "x for multiplication\n"
      "/ for division\n"
      "s for sine function\n"
      "c for sine function\n"
      "p for power\n"
      "[ for square root\n"
      "= for result\n"
      "0 for clearall\n"
      "q for exit\n")
a=float((input("Enter the first number: ")))

while True:
    opcode = input()
    if opcode=='+':
        b = float(input(str(a)+" + "))
        a=operation.addition(a,b)
    elif opcode=='-':
        b = float(input(str(a)+" - "))
        a=operation.subtraction(a,b)
    elif opcode=='/':
        b = float(input(str(a)+" / "))
        a=operation.division(a,b)
    elif opcode=='x':
        b = float(input(str(a)+" x "))
        a=operation.multiplication(a,b)
    elif opcode=='[':
        print("sqrt("+str(a)+")")
        a=operation.square_root(a)
    elif opcode=='s':
        print("SIN(" + str(a) + ")")
        a=operation.sin_func(a)
    elif opcode=='c':
        print("COS(" + str(a) + ")")
        a=operation.cos_func(a)
    elif opcode=='p':
        b = float(input(str(a)+" p "))
        a=operation.power(a,b)
    elif opcode=='=':
        print("Answer: ",a)
    elif opcode=='0':
        print("Cleared")
        a = float((input("Enter the first number: ")))
    elif opcode=='q':
        #print("Answer: ",a)
        exit()












