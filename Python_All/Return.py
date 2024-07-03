class abc:
    def __init__char(self,s):
        self.s=s
    def missingCharacters(self):
        # Write your code here
        s=v
        removedNum = " "
        removedLet = " "
        removed = removedLet + removedNum

        num = "0123456789"
        letter = "abcdefghijklmnopqrstuvwxyz"
        for i in s:
         if i not in num:
            removedNum = removedNum+i
        for i in s:
         if i not in letter:
             removedLet = removedLet+i
        print(removed)

v = input("Enter a string")
p1=abc()
ans = abc.missingCharacters(v)
print(ans)