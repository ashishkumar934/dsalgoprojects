class Solution:
    #### This is the Solution by me Whose time complexity ->
    def lengthOfLongestSubstring(self, s: str) -> int:
        ll=[0]*256
        max_length=0
        i,j=0,0
        while j<len(s):
            print(max_length)
            if ll[ord(s[j])-1]==1:
                while ord(s[j])!=ord(s[i]):
                    ll[ord(s[i])-1]=0
                    i+=1
                ll[ord(s[i])-1]=0
                i+=1
            ll[ord(s[j])-1]=1
            max_length=max(max_length,j-i+1)
            j+=1
        return max_length

    #### Another way of solution is using the dictionary in python where we will keep track of the charater visited at which position
    # class Solution:
    #     def lengthOfLongestSubstring(self, s: str) -> int:
    #         ls = ""
    #         l, r = 0, 0
    #         ci = {}
    # 
    #         while r < len(s):
    #             c = s[r]
    #             if c not in ci:
    #                 ci[c] = r
    #             else:
    #                 if ci[c] + 1 > l:
    #                     l = ci[c] + 1
    #                 ci[c] = r
    #
    #             if len(ls) < r - l + 1:
    #                 ls = s[l:r + 1]
    #
    #             r += 1
    #
    #         if len(ls) < r - l:
    #             ls = s[l:r]
    #
    #         return len(ls)


if __name__ == "__main__":
    print(__name__)
    print(dir())
    print(vars())
    print(ord('2'))
    print(chr(34))