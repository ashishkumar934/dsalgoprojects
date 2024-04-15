from typing import *
class Solution:

    @staticmethod
    def try_method1(self):
        print('THis is the method one intuation which defines why I did not choosed the following method ')
        # AS the part of this method I thought to take the mid of the string and then divide that
        # into two parts and then calculate individually in the both parts the longest palindrome after
        # checking the left+right part together.
        # But this method will not work as in this method we are considered center as only mid of the string but
        # the center of palindrome can be off string center and those cases will be missed out.

    @staticmethod
    def solution_one(self, s: str) -> int:
        n = len(s)
        _s = ''
        for ch in s:
            _s = _s + '*' + ch
        _s = _s + '*'
        _s_n = len(_s)
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


if __name__=='__main__':
    print('Calling Longest Palindromic Substring')