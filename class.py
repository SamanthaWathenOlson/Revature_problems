"""These exercises are designed to familiarize you with classes and the ways you can utilize them"""

"""
Create a class whose objects have string, int, and boolean fields when instantiated
"""
class_MySpecialClass:
  

def __init__(self, my_string_var: str, my_integer_var: int, my_boolean: str_boolean)
  self.my_string_variable = my_string_variable
  self.my_integer_variable = my_integer_variable
  self.my_boolean = my_boolean
  
"""
Create a class that has a string, int, and boolean class field
"""
class SecondClass:
  def __init__(self, MySpecialClass):
    self.MySpecialClass = MySpecialClass
    print("")
    

"""
Create a class whose objects have two int fields and create a single method for each field that
returns its value
"""

class ThirdClass:
  a = 45
  b = 30
  
  def __init__(self, string_one: int, integer_two:int):
    self.string_one = string_one
    self.integer_two = integer_two
  
 integer_two = a + b

print(integer_two)
"""
Create a class whose objects have two string fields and a method to get the value of each field. Create a method
that performs string concatenation on the two fields and prints the result to the terminal. You may not directly
access the fields for the method that performs the string concatenation
"""
class FourthClass:
  
  @fourthmethod
  def my_fourth_method(sefl, input_one, input_two):
    
  class ClassRed(FourthClass):
      def my_fourth_method(self, input_one, input_two):
        return str(input_one) + str(input_two)
  
  object_h = ClassRed()
  object_f = ClassRed()
  
  print(object_h.my_fourth_method()
  print(object_f.my_fourth_method()

"""
Create an abstract class that has an int field called object_count that is set at zero. Then create a class that 
inherits from the abstract class and increases the value of object_count by one whenever the class is instantiated
"""


"""
Create an abstract class with an abstract method. Create a second class that inherits from the abstract class that
implements the abstract method. The implemented method must print a message to the terminal
"""
