try:
x = 5 / 0
except ZeroDivisionError as e:
# `e` is the exception object
print("Got a divide by zero! The exception was:", e)
# handle exceptional case
x = 0
finally:
print "The END"
   
