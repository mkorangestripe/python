# Sets the python path before running the shell:
# PYTHONPATH=./src ipython


# Convert between chr and int (integer ordinal):
ord('A') # 65
chr(65) # A
# Convert between hex and int
int(0x41) # 65
hex(65) # 0x41
# Convert between bin and int
int(0b1000001) # 65
bin(65) # 0b1000001
# Convert between oct and int
int(0101) # 65
oct(65) # 0101

# Multiple assignment:
a, b = 9, 2

# Return a list of valid attributes for the object:
dir(list)

# Use a global variable in a function:
global num



# Reversed
for i in reversed(xrange(1,11)):
    print i,
# 10 9 8 7 6 5 4 3 2 1



# Generators, Yield:

# Generators are iterators, but can only be iterated over once.
generator1 = (x**2 for x in range(10))
for i in generator1: print i,
# 0 1 4 9 16 25 36 49 64 81
for i in generator1: print i,
# Nothing is printed

# Yield:
# Yield returns a generator.
# Unlike a list, the cubes generator doesn't store any of these items in memory,
# rather the cubed values are computed at runtime, returned, and forgotten.
def cube_numbers(nums):
    for i in nums:
        yield(i**3)

cubes = cube_numbers([1, 2, 3, 4, 5])
next(cubes) # 1
next(cubes) # 8
next(cubes) # 27



# try, except statements
while True:
    try:
        x = int(raw_input("Please enter a number: "))
        break
    except ValueError:
        print "Not a valid number.  Try again..."

# Try, except statement with else and finally.
import sys
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except IOError:
        print 'cannot open', arg
    else:
        print arg, 'has', len(f.readlines()), 'lines'
        f.close()
    finally:
        print "executing finally clause"



# continue
# The continue statement continues to the next iteration of the loop.
# This can reduce the need for additional control statements (if/elif/else),
# further nesting, and make code easier to read.

for (bucket_name, endpoint) in buckets_and_endpoints.items():
   #CODE BLOCK REMOVED

   if self.unwhitelist:
       self.delete_ip_whitelist(bucket_name)
       continue

   bucket = endpoint_connections[endpoint].get_bucket(bucket_name)
   if bucket.name != bucket_name:
       log_line = {'timestamp': time.time(),
                   'account': account_id,
                   'req_bucket': bucket_name,
                   'rx_bucket': bucket.name,
                   'message': 'Bucket names do not match. Skipping'}
       logger.info(json.dumps(log_line))
       continue

   #CODE BLOCK REMOVED


# copy
# Python creates a new object when the contents of a shallow copy are changed.
# The comparisons are value comparisons.
import copy
b = {1: [1,2,3]}

# Reference assignment (same object, same sub-objects)
a = b
id(a) # 4340438192
id(b) # 4340438192
id(a[1]) # 4340522520
id(b[1]) # 4340522520
a == b # True

# Shallow copy (new object, same sub-objects)
a = b.copy()
id(a) # 4340575600
id(b) # 4340438192
id(a[1]) # 4340522520
id(b[1]) # 4340522520
a == b # True
# This creates a new sub-object under 'a'.
a[1] = [4, 5, 6]
id(a[1]) # 4369444592
id(b[1]) # 4340522520
a == b # False
b[1] = [4, 5, 6]
a == b # True

# Deep copy (new object, new sub-objects)
a = copy.deepcopy(b)
a == b # True
id(a) # 4340489584
id(b) # 4340438192
id(a[1]) # 4340168608
id(b[1]) # 4340522520
a == b # True



# Raise a runtime error:
raise RuntimeError('test for validate_request_parameters debug log')



# args and kwargs
# Both allow you to pass a variable number of arguments to a function.
# **kwargs allows you to pass keyworded variable length of arguments to a function.

def test_var_args(f_arg, *argv):
    print("first normal arg:", f_arg)
    for arg in argv:
        print("another arg through *argv:", arg)

test_var_args('yasoob', 'python', 'eggs', 'test')
# ('first normal arg:', 'yasoob')
# ('another arg through *argv:', 'python')
# ('another arg through *argv:', 'eggs')
# ('another arg through *argv:', 'test')

def greet_me(**kwargs):
    for key, value in kwargs.items():
        print("{0} = {1}".format(key, value))

greet_me(name="yasoob")
# name = yasoob
