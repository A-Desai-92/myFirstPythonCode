"""
@author: Astha Desai
@date:   23/04/2018
@rev:    1
@lang:   Python
@deps:   <None>
@desc:   Assignment 1a
"""

print('Welcome to Astha\'s Calculator')
print('Part A - Add two numbers')
print('The sum is %.1f' %(float(input('Enter first number: '))+float(input('Enter second number: '))))

def main():
  while(True):
    again = raw_input("Sweet! Would you like to try again? ")
    
    if again.lower().startswith("y"):
      partB()
    
    elif again.lower().startswith("n"):
      print("See you later!")
      exit()
    
main ()
