#remove punctuation and spaces, check if first and last letters are same, then its a palindrome if middle section is a plaindrome

def isPalin(s):
    def toChars(s):
        s=s.lower()
        ans=''
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans=ans+c
        return ans

    def isPal(s):
        if len(s)<=1:
            return True
        else:
            return s[0]==s[-1] and isPal(s[1:-1])
            
    return isPal(toChars(s))

print(isPalin("Able was I, ere I saw Elba"))        