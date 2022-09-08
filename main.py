from array import array
from msilib import MSIDBOPEN_DIRECT
from select import select
import math

# klasa do szukania pierwszej liczby Michała
class Numbers:
    def __init__(self, array):
        self.givenArray = array
        self.start = 0
        self.middle = len(self.givenArray)//2
        self.end = len(self.givenArray) - 1

    # funkcja prywatna sprawdzająca czy numer jest liczbą pierwszą
    def __checkPrime(self, number):
        for i in range(2, number+1):
            if number % i == 0 and number != 2:
                return False
            return True
    
    # funkcja publiczna szukająca metodą binarną pierwszej liczby Michała
    def find(self):
        start = self.start
        middle = self.middle
        end = self.end
        array = self.givenArray
        check = False
        while (check == False):
            if self.__checkPrime(array[middle]) == False and self.__checkPrime(array[middle - 1]) == True:
                check = True
                print(array[middle])
            else:
                if self.__checkPrime(array[middle]) == False and self.__checkPrime(array[middle - 1]) == False:
                    end = middle
                    middle = (start + end) // 2
                else:
                    start = middle
                    middle = (start + end) // 2
                check = False

# tablica "wbita z palca"
array = [2, 3, 5, 3, 6, 8, 9, 20]

example = Numbers(array)
example.find()
