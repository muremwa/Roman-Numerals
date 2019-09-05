# Roman numeral converter for integers in python
__it does upto 3999 because I never found the character set for 5000, 10000, 50000...you get the idea__
Help if you can

## Usage
1. Import the class from wherever it is
```python 
	>>> # I will import from the file directly
	>>> from int_roman import IntRoman
```
1. Create an instance of the class 'IntRoman'
```python
	>>> ir = IntRoman()
```
1. Use the to_roman method to convert to a roman number
```python
	>>> # the return value is a roman numeral equivalent string
	>>> ir.to_roman(4)
	'IV'
```
1. Additionaly, you might want to convert a whole list. Use the to_roman_list method
```python
	>>> # returns a list of strings with equilvalent roman numerals to the input string at the same index
	>>> nums = [4, 63, 963, 623]
	>>> ir.to_roman_list(nums)
	['IV', 'LXIII', 'CMLXIII', 'DCXXIII']
```

### Please help add support from number __4000 to infinity (at least a million)__