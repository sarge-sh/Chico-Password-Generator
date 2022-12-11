import random


class PWD_string:
    def __init__(self, length=0):
        if length == 0:
            self.length = 12
        else:
            self.length = length;

    def __int__(self):
        return int(self.length)

    def lettersUP(self, choice = ''):
        letters_up = []
        if choice.upper() == 'ALL':
            for i in range(ord('A'), ord('Z')+1):
                letters_up.append(chr(i))
        else:
            for i in range(self.length):
                letters_up.append(chr(random.randint(ord('A'), ord('Z'))))

        return letters_up

    def lettersLOW(self, choice = ''):
        letters_low = []
        if choice.upper() == 'ALL':
            for i in range(ord('a'), ord('z')+1):
                letters_low.append(chr(i))
        else:
            for i in range(self.length):
                letters_low.append(chr(random.randint(ord('a'), ord('z'))))

        return letters_low

    def numbers(self, choice = ''):
        nums = []
        if choice.upper() == 'ALL':
            for i in range(0,10):
                nums.append(str(i))
        else:
            for i in range(self.length):
                nums.append(str(random.randint(0, 9)))

        return nums

    def special(self, choice=''):      # 33-47, 58-64, 91-96
        spec = []
        spec_out = []
        for i in list(range(33, 47)) + list(range(58, 64)) + list(range(91, 96)) + list(range(123, 126)):
            spec.append(chr(i))
        if choice.upper() == 'ALL':
            return spec
        else:
            for i in range(self.length):
                spec_out.append(spec[random.randint(0, len(spec)-1)])
        return spec_out
