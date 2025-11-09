class Computation:
    def __init__(self):
        print("Computation object created!")

    def Factorial(self, n):
        fact = 1
        for i in range(1, n + 1):
            fact *= i
        return fact

    def naturalSum(self, n):
        return n * (n + 1) // 2

    def testPrime(self, n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True


    def testPrims(self, a, b):
        def gcd(x, y):
            while y:
                x, y = y, x % y
            return x
        return gcd(a, b) == 1

    def tableMult(self, n):
        print(f"Multiplication table of {n}:")
        for i in range(1, 11):
            print(f"{n} x {i} = {n * i}")

 
    def allTablesMult(self):
        for i in range(1, 10):
            print("-" * 20)
            self.tableMult(i)

    def listDiv(n):
        Ldiv = []
        for i in range(1, n + 1):
            if n % i == 0:
                Ldiv.append(i)
        return Ldiv

    def listDivPrim(self, n):
        Ldiv = self.listDiv(n)
        LdivPrim = [x for x in Ldiv if self.testPrime(x)]
        return LdivPrim

if __name__ == "__main__":
    calc = Computation()

    print("Factorial of 5:", calc.Factorial(5))
    print("Sum of first 10 natural numbers:", calc.naturalSum(10))
    print("Is 13 prime?", calc.testPrime(13))
    print("Are 4 and 9 prime to each other?", calc.testPrims(4, 9))

    calc.tableMult(7)
    calc.allTablesMult()

    print("Divisors of 28:", Computation.listDiv(28))
    print("Prime divisors of 28:", calc.listDivPrim(28))
