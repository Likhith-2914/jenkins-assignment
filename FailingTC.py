#!/usr/bin/python3
import unittest

from Palindrome import isPalindrome

class Tests(unittest.TestCase): 
  
  def testcasefailing1(self):
    string = "madam"
    trueResult = False
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
  
  def testcasefailing2(self):
    string = "software-engineering"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
  def testcasefailing3(self):
    string = ""
    trueResult = False
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)

if __name__ == '__main__':
    unittest.main()
