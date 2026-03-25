import string

upper = string.ascii_uppercase
lower = string.ascii_lowercase

def UI():
    print("This is a Caesar encryption machine.\n" \
    "if you give me a key and plain text, we'll show the Ciphertext.")

def PLATIN_INPUT():
    key = int(input("Enter Shift value:"))
    M = input("Enter any strings:")

    return key,M

def CAESAR_ENC(key,string):
    new_upper = upper
    new_lower = lower
    new_string = ""

    #key shift에 따른 알파벳 재 정렬
    for idx in range(26):
        if idx < 26-key:
            new_upper = upper[key:] + upper[:key]
            new_lower = lower[key:] + lower[:key]

    for char in string:
        idx = 0
        flag = True
        while flag:
            if char == upper[idx]:
                new_string += new_upper[idx]
                flag = False
            elif char == lower[idx]:
                new_string += new_lower[idx]
                flag = False
            else:
                idx +=1

    return new_string

if __name__ == "__main__":
    UI()
    key,string = PLATIN_INPUT()
    Ciphertext = CAESAR_ENC(key,string)
    print("Ciphertext = {}".format(Ciphertext))