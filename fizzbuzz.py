class FizzBuzz:
    def __init__(self, num):
        self.num=num
    def convert_to_fizzbuzz(self):
        if (self.num % 3 == 0):
            return "Fizz"
        return str(self.num)
        
