import unittest

from Palindrom import isPalindrome

class Tests(unittest.TestCase): 
  
  def failingTC1(self):
    string = "madam"
    trueResult = False
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
  
  def failingTC1(self):
    string = "software-engineering"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
  def failingTC1(self):
    string = ""
    trueResult = False
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
