# Learn Python

Read Allen Downey's [Think Python](http://www.greenteapress.com/thinkpython/) for getting up to speed with Python 2.7 and computer science topics. It's completely available online, or you can buy a physical copy if you would like.

<a href="http://www.greenteapress.com/thinkpython/"><img src="img/think_python.png" style="width: 100px;" target="_blank"></a>

For quick and easy interactive practice with Python, many people enjoy [Codecademy's Python track](http://www.codecademy.com/en/tracks/python). There's also [Learn Python The Hard Way](http://learnpythonthehardway.org/book/) and [The Python Tutorial](https://docs.python.org/2/tutorial/).

---

###Q1. Lists &amp; Tuples

How are Python lists and tuples similar and different? Which will work as keys in dictionaries? Why?

Tuples are fixed size in nature whereas lists are dynamic. In other words, a tuple is immutable whereas a list is mutable.

* You can't add elements to a tuple. Tuples have no append or extend method.
* You can't remove elements from a tuple. Tuples have no remove or pop method.
* You can find elements in a tuple, since this doesn’t change the tuple.
* You can also use the in operator to check if an element exists in the tuple.
* Tuples are faster than lists. If you're defining a constant set of values and all you're ever going to do with it is iterate through it, use a tuple instead of a list.
* It makes your code safer if you “write-protect” data that does not need to be changed. Using a tuple instead of a list is like having an implied assert statement that this data is constant, and that special thought (and a specific function) is required to override that.

Some tuples can be used as dictionary keys (specifically, tuples that contain immutable values like strings, numbers, and other tuples). Lists can never be used as dictionary keys, because lists are not immutable.

---

###Q2. Lists &amp; Sets

How are Python lists and sets similar and different? Give examples of using both. How does performance compare between lists and sets for finding an element. Why?

1. Sets can't contain duplicates.
2, Sets are unordered.
3. In order to find an element in a set, a hash lookup is used (which is why sets are unordered). This makes __contains__ (in operator) a lot more efficient for sets than lists.
4. Sets can only contain hashable items (see #3). If you try: set(([1],[2])) you'll get a TypeError.
5. In practical applications, lists are very nice to sort and have order while sets are nice to use when you don't want duplicates and don't care about order.

Performance depends on what you are intending to do with it. Sets are significantly faster when it comes to determining if an object is present in the set, but are slower than lists when it comes to iterating over their contents.

`x in s` would be faster in a set
`for x in s` would be faster in a list

Sets are implemented using hash tables. Whenever you add an object to a set, the position within the memory of the set object is determined using the hash of the object to be added. When testing for membership, all that needs to be done is basically to look if the object is at the position determined by its hash, so the speed of this operation does not depend on the size of the set. For lists, in contrast, the whole list needs to be searched, which will become slower as the list grows.


---

###Q3. Lambda Function

Describe Python's `lambda`. What is it, and what is it used for? Give at least one example, including an example of using a `lambda` in the `key` argument to `sorted`.

A lambda is an anonymous function (i.e. function that is not bound to a name) defined at runtime. To generalize, a lambda function is a function that takes any number of arguments (including optional arguments) and returns the value of a single expression. lambda functions can not contain commands, and they can not contain more than one expression. Don't try to squeeze too much into a lambda function; if you need something more complex, define a normal function instead and make it as long as you want.

`a = sorted(a, key=lambda x: x.modified, reverse=True)`

---

###Q4. List Comprehension, Map &amp; Filter

Explain list comprehensions. Give examples and show equivalents with `map` and `filter`. How do their capabilities compare? Also demonstrate set comprehensions and dictionary comprehensions.

>> REPLACE THIS TEXT WITH YOUR RESPONSE

---

###Complete the following problems by editing the files below:

###Q5. Datetime
Use Python to compute days between start and stop date.   
a.  

```
date_start = '01-02-2013'    
date_stop = '07-28-2015'
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

b.  
```
date_start = '12312013'  
date_stop = '05282015'  
```

>> REPLACE THIS TEXT WITH YOUR RESPONSE (answer will be in number of days)

c.  
```
date_start = '15-Jan-1994'      
date_stop = '14-Jul-2015'  
```

936 days, 23:00:00

512 days, 23:00:00

7849 days, 23:00:00

Place code in this file: [q5_datetime.py](python/q5_datetime.py)

---

###Q6. Strings
Edit the 7 functions in [q6_strings.py](python/q6_strings.py)

---

###Q7. Lists
Edit the 5 functions in [q7_lists.py](python/q7_lists.py)

---

###Q8. Parsing
Edit the 3 functions in [q8_parsing.py](python/q8_parsing.py)





