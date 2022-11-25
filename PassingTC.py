#!/usr/bin/python3
import unittest

from Palindrom import isPalindrome

class Tests(unittest.TestCase): 
  
  def testcasepassing1(self):
    string = "rececar"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
  
  def testcasepassing2(self):
    string = "likhith"
    trueResult = False
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
  def testpassing3(self):
    string = "a12421a"
    trueResult = True
    testResult = isPalindrome(string)
    self.assertEqual(testResult, trueResult)
    
