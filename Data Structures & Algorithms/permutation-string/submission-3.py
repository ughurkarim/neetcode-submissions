class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        l = 0
        length1 = len(s1)
        hashS1 = {}
        seen = {}

        for i in range(97, 123):
            hashS1[chr(i)] = 0
            seen[chr(i)] = 0
            
        for char in s1:
            hashS1[char] += 1

        for r in range(length1):
            seen[s2[r]] += 1

        if seen == hashS1:
            return True

        for r in range(len(s1), len(s2)):
            seen[s2[r]] += 1
            seen[s2[l]] -= 1

            l+=1

            if seen == hashS1:
                return True

   
        return False






        