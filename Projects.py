"""Control Flow And String Exercises"""

"""
Create a for loop that prints the numbers zero through ten sequentially
"""
for loop in range(11):
  print(loop)

"""
Create a for loop that prints the numbers 20 through 10 sequentially
"""
for loop in range(20, 9, -1)
  print(loop)
"""
Create a while loop that prints a string of * that grow by one each print until the string printed is 10 * together
"""
x = 2
while x <= 10:
  print(x)
  x += 1
"""
Create a string with the value "world!" in a new module and import it to this one. Once you have done that, print
the phrase "Hello world!" using the variable you imported from the new module
"""
import mymodule

mymodule.greeting("Hello ")
"""
Print the phrase "Hello World" using an f string and the imported variable you used for the previous exercise
"""
greeting_f_string = f"Hello {mymodule}
  print(greeting_f_string)
"""
Create a new string variable and give it the value of your name (example: my_name = "Eric"). Then, print a greeting 
to yourself using the string format method
"""
my_name = "Samantha"
greeting = "Hello "
print(greeting + my_name)
"""
Create a string with the following value: 'It is a lovely day today'. Write out six print statements that each print
a single word from the string using string slicing
"""
my_python_var = "My_variable_one"
for word in my_python_var.split("_"):
  for character in word:
    if character is "a":
      print('It is a lovely day today')
"""
Use that same string and print the words backwards, starting from the last word, one by one
"""
string_to_slice = "It is a lovely day today"
for letter in string_to_slice[::-1]:
    print(letter)
"""
Create two number variables called num_one and num_two, and assign them any value that is a whole number between 1 
and 100. Then create an if/else statement that prints True if num_one divided by num_two is a whole number, or False
if the numbers divided make a fraction. If you get True back change the numbers to try and get False, and vice versa
"""
num_one = 20
num_two = 30
if num_one / num_two == int:
  print("This is a true statement")
else:
  print("This is not a true statement")
 #found a false statement, not true statement yet....
"""
Create a loop that prints the numbers one through five a total of five times. It also needs to tell you which 
iteration of counting the loop is currently on 
"""
for loop in range(1, 6, 1):
  print(loop)
  
string_to_slice = "1, 2, 3, 4, 5,"
print(string_to_slice)[0:6]

      

