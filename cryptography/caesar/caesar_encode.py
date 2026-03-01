upper = "ABCDEFGHIJKLMNOPQRXTUVWXYZ"
lower = "abcdefghijklmnopqrxtuvwxyz"
n = len(upper)

def caesar_input():
    
    key = int(input("Enter Shift value:"))
    string = input("Enter strings:")
    
    print("key = {}\nstring={}".format(key,string))

    return key,string

def caesar(key,string):
    new_upper = upper
    new_lower = lower
    new_string = ""

    for idx in range(n):
        if idx < n-key:        
            new_upper = upper[key:] + upper[:key]
        else:
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
    print("This is a Caesar Cipher encoding machine!")
    key, string = caesar_input()
    new_string =  caesar(key,string)
    print("new string = {}".format(new_string))













        
    

