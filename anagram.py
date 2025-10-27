def anagram(s,t):
    if(len(s)!=len(t)):
        return False
    else:
        return sorted(s)==sorted(t) 
s="listen"
t="silent" 
print(anagram(s,t))