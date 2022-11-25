import unittest

from Palindrom import isPalindrome

class Tests(unittest.TestCase): 
  
  def passingTC1(self):
    string = "rececar"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
  
  def passingTC1(self):
    string = "likhith"
    trueResult = False
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
  def passingTC1(self):
    string = "a12421a"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
