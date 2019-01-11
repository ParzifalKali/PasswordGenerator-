from generator import Generator

if __name__ == "__main__":

    gn = Generator()

    letters_number = input("Insert the ammount of letters that the password must have : ")

    letters_number = int(letters_number)

    gn.generate(l_number=letters_number)