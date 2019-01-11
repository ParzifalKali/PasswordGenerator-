import random


class Generator():

    def __init__(self):
        self.self = self

    def generate(self, l_number = 20, all_included = True):

        l_number = int(l_number)

        ###################################

        letters = []
        letters_str = "qwertyuiopasdfghjklzxcvbnm"

        for letter in letters_str:

            letters.append(letter)

        ###################################

        symbols = []
        symbols_str = "±!@#$%ˆˆ*()_+{}:""<>?,./;''[]=-§|"

        for symbol in symbols_str:

            symbols.append(symbol)

        ###################################

        numbers = []
        numbers_str = "1234567890"

        for number in numbers_str:

            numbers.append(number)

        ###################################

        if all_included:

            all_chr = []

            for le in letters:

                all_chr.append(le)

            for sy in symbols:

                all_chr.append(sy)

            for nu in numbers:

                all_chr.append(nu)

            #print(all_chr)

            #all_chr.append(letters)
            #all_chr.append(symbols)
            #all_chr.append(numbers)


            passw = []

            for i in range(0, l_number):

                l = random.choice(all_chr)
                passw.append(l)

            #print(passw)

            complete_pasw = "".join(map(str, passw))

            print(f"Your super secure password is : \n{complete_pasw}")

        elif all_included == False:

            print("I am sorry but this mode is not aviable now")


#Generator().generate(l_number=5, all_included=False) # or it can be false