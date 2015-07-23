
class Fibonacci:

    def __contains__(self,n):
        iterator = 0
        while True:
            fib_number = self.number_at(iterator)
            if fib_number == n:
                return True
            elif fib_number >= n:
                return False
            else:
                iterator += 1

    def number_at(self,n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.number_at(n-1) + self.number_at(n-2)

    def k_numbers(self,k):
        k_numbers = []
        iterator = 1

        while iterator < k:
            k_numbers.append(self.number_at(iterator))
            iterator += 1

        return k_numbers

    def k_even_numbers(self,k):
        k_odd_numbers = []
        iterator = 0

        for number in self.k_numbers(k):
            if number % 2 == 0:
                k_odd_numbers.append(number)

        return k_odd_numbers

    def k_odd_numbers(self,k):
        k_odd_numbers = self.k_numbers(k)

        for number in self.k_even_numbers(k):
            k_odd_numbers.remove(number)

        return k_odd_numbers

    def sum_k_numbers(self,k):
        return sum(self.k_numbers(k))

fib = Fibonacci()

if fib.__contains__(7):
    print 'Encontrador'
else:
    print 'No encontrado'

print fib.number_at(6)
print 'Los 7 primeros numeros de la serie de Fibonacci son ', fib.k_numbers(7)
print 'Y la suma de estos es ', fib.sum_k_numbers(7)

print 'Los 10 primeros numeros pares son ', fib.k_even_numbers(7)
print 'Los 10 primeros impares son ', fib.k_odd_numbers(7)
