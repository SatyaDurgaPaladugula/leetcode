class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        l=[]
        for i in s:
           if i.isupper() or i.islower():
              l.append(i)
        l.reverse()
        letter_index = 0
        r=[]
        for i in s:
            if i.isupper() or i.islower():
                r.append(l[letter_index])
                letter_index += 1
            else:
                r.append(i)

        return ''.join(r)
