#String Reversal function:

def reverse(text):
    lst = []
    count = 1
    for i in range(0,len(text)):
        lst.append(text[len(text)-count])
        count += 1
    lst = ''.join(lst)
    return lst

text= str(input("Enter the string: "))
print (reverse(text))