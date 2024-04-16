from typing import *
class Solution:

    @staticmethod
    def try_method1(self):
        print('THis is the method one intuation which defines why I did not choosed the following method ')
        # AS the part of this method I thought to take the mid of the string and then divide that
        # into two parts and then calculate individually in the both parts the longest palindrome after
        # checking the left+right part together.
        # But this method will not work as in this method we are considering center as only mid of the string but
        # the center of palindrome can be off center of string and those cases will be missed out.

    @staticmethod
    def solution_one(self, s: str) -> int:
        n = len(s)
        _s = ''
        for ch in s:
            _s = _s + '*' + ch
        _s = _s + '*'
        _s_n = len(_s)

        ### easy way of doing this is -> _s_n = '*'+'*'.join(s)+'*'
        print(_s)
        mid = _s_n // 2
        longest_palindrome = ''
        for center in range(1, _s_n - 1):
            ## Side Range is the nearest end of the string
            side_range = center if center < mid else _s_n - 1 - center
            ## Palindrome Range is initialized as side range which means with current center
            ## max possible string is palindrome. If at any point both side character do not match
            ## then this palindrome range will be change to that side_range.
            palindrome_range = side_range
            while side_range > 0:
                if _s[center - side_range] != _s[center + side_range]:
                    side_range -= 1
                    palindrome_range = side_range
                    continue
                side_range -= 1
            longest_palindrome = _s[center - palindrome_range:center + palindrome_range] if len(
                _s[center - palindrome_range:center + palindrome_range]) > len(
                longest_palindrome) else longest_palindrome
        longest_palindrome = longest_palindrome.replace('*', '')
        return longest_palindrome

    @staticmethod
    def dp(self, s: str) -> int:
        n=len(s)
        dp=[[0]*n for _ in range(n)] ## Initialize the dp array with the initial value of string from i to j of length 1 as 1.

        # Here the important thing is that whenever we are implementing the string problem using the dynamic programming in the 2D array we take the length of string from
        # index i to j and then implement the solution

    @staticmethod
    def longestPalindrome(self, s: str) -> str:
        n: int = len(s)
        _s = '*' + '*'.join(s) + '*'
        n = len(_s)
        lps = [0] * n
        # print(_s)
        # print(n)
        lps[0] = 0
        lps[1] = 1
        # print(lps)
        center = 1
        center_left = 0
        center_right = 2
        for current_center in range(2, n):
            # print('-----')

            # print('current_center',current_center)
            # print('center',center)
            # print('right center',center_right)
            mirror_current_center = 2 * center - current_center
            # print('mirror index',mirror_current_center)
            if current_center + lps[mirror_current_center] < center_right:
                print('inside the if loop', lps[mirror_current_center])
                lps[current_center] = lps[mirror_current_center]
            else:
                # print('inside else loop',lps[current_center])
                i = 1
                if center_right > current_center:
                    current_right = center_right
                    lps[current_center] = center_right - current_center
                    current_left = current_center - lps[current_center]

                else:
                    current_right = current_center
                    current_left = current_center
                # print(current_right+i)
                # print(current_left-i)
                while ((current_right + i) < n) and ((current_left - i) >= 0) and (_s[current_right + i]) == (
                _s[current_left - i]):
                    print(current_right + i)
                    print(current_left - i)
                    lps[current_center] += 1
                    current_right += 1
                    current_left -= 1
                    # i+=1
                if current_right > center_right:
                    print('updated center:', current_center, ',current right:', current_right)
                    center = current_center
                    center_right = current_right
                    center_left = current_left
        # print(lps)
        max_index = 0
        max_distance = 0
        for i in range(len(lps)):
            if lps[i] > max_distance:
                max_distance = lps[i]
                max_index = i
        output = _s[max_index - max_distance:max_index + max_distance]
        # print(output)
        return output.replace('*', '')



if __name__=='__main__':
    print('Calling Longest Palindromic Substring')