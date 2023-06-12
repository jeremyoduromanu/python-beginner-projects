rom_numerals = ["","I","II","III","IV","V","VI", "VII", "VIII", "IX", "X"]

def roman_numeral():
    user_num = int(input("Enter a number between 1 and 10: "))
    
    if user_num in range(1,10):
        result_rom_num = rom_numerals[user_num]
        print("The roman numeral for your number is: " + result_rom_num)
    else:
        print("Enter a number between 1 and 10 only")

roman_numeral()
    