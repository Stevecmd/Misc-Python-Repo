#Method 1
def isAnagram(s:str, t:str):
    if(sorted(s) == sorted(t)):
        print ("true")
    else:
        print ("false")
        
s = input("What is the first word? ").lower()
t = input("What is the second word? ").lower()
isAnagram(s, t)

#Method 2
#def is Anagram(s, t):
#    return Counter(s) == Counter(t)

#Method 3
#def is Anagram(s, t):
#    return sorted(s) == sorted(t)