
def Count(s):
    vowels = ['a','e','i','o','u']
    res = {
        "Vowel":0,
        "Letter":0,
        "Space":0,
        "Number":0,
        "Word":0,
        "Line":0,
        "Special":0
    }
    for ch in s:
        ch = ch.lower()
        if ch >='a' and ch<='z':
            res["Letter"]+=1
            if ch in vowels:
                res["Vowel"]+=1
        elif ch>='0' and ch<='9':
            res["Number"]+=1
        elif ch == ' ':
            res["Space"]+=1
        elif ch == '\n':
            res["Line"]+=1
        else:
            res["Special"]+=1
    res["Word"] = len(s.split(' '))
    return res

def main():
    print("\tCOUNT IN STRING")
    while True:
        s = input("Enter a string:")
        print(f"Result: {Count(s)}")
        ch = input("Did you want to continue (Y/N):")
        if ch.lower !='y':
            break
main()
