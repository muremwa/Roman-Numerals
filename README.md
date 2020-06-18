## Roman numeral converter for integers in Python
It does upto 3999 because I never found the character set for 5000, 10000, 50000...you get the idea Help if you can

### Usage
1. Import the class from wherever it is
```python
	>>> # I will import from the file directly
	>>> from int_roman import IntRoman
```

2. Create an instance of the class 'IntRoman'
```python
	>>> ir = IntRoman()
```

3. Use the to_roman method to convert to a roman number
```python
	>>> # the return value is a roman numeral equivalent string
	>>> ir.to_roman(4)
	# 'IV'
```

4. Additionally, you might want to convert a whole list. Use the to_roman_list method
```python
	>>> # returns an iterable of strings with equivalent roman numerals to the input string at the same index
	>>> nums = [4, 63, 963, 623]
	>>> ir.to_roman_list(nums)
	# ['IV', 'LXIII', 'CMLXIII', 'DCXXIII']
	>>> # it returns the same type it was fed
	>>> nums = (4, 63, 963, 623)
	>>> ir.to_roman_list(nums)
	# ('IV', 'LXIII', 'CMLXIII', 'DCXXIII')
	# The order of the results when a set is input may differ from the input
```

5. For additional support or to check available methods use the dir() function
```python
	>>> dir(ir)
```
__Please help add support from number 4000 to infinity (at least a million)__