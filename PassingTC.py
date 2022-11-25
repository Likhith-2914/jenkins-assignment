#!/usr/bin/python3
import unittest

from Palindrome import isPalindrome

class Tests(unittest.TestCase): 
  
  def testcasepassing1(self):
    string = "racecar"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
  
  def testcasepassing2(self):
    string = "likhith"
    trueResult = False
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
  def testcasepassing3(self):
    string = "a12421a"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
if __name__ == '__main__':
    unittest.main()
