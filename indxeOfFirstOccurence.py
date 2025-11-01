def strStr( haystack, needle):
        if needle in haystack:
            return haystack.index(needle)
        return -1
print(strStr("Hello","ll"))