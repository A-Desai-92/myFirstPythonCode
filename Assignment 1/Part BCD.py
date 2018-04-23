
"""
@author: Astha Desai
@date:   23/04/2018
@rev:    1
@lang:   Python 
@deps:   <None>
@desc:   Assignment 1b, 1c and 1d
"""

def partB():
    print('Part B - Add, Subtract or Multiply two numbers')
    
    #Define Functions
    def add(num1, num2):
      ans = num1 + num2
      return ans
    def subtract(num1, num2):
      ans = num1 - num2
      return ans
    def multiply(num1, num2):
      ans = num1 * num2
      return ans  
      
    #Numbers and function input by user
    num1 = input('Enter first number: ')
    num2 = input('Enter second number: ')
    func1 = raw_input("Enter Add,Subtract or Multiply: ")
    
    #Function Execution
    if func1 in ["add", "Add", "+"]:
      ans = add(num1, num2)
      print(ans)
    if func1 in ["subtract", "Subtract", "-"]:
      ans = subtract(num1, num2)
      print(ans)
    if func1 in ["multiply", "Multiply", "*"]:
      ans = multiply(num1, num2)
      print(ans)
    
partB ()

def main():
  while(True):
    again = raw_input("Sweet! Would you like to try again? ")
    
    if again.lower().startswith("y"):
      partB()
    
    elif again.lower().startswith("n"):
      print("See you later!")
      exit()
    
main ()
