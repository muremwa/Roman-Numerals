Roman numeral converter for integers in Python
It does upto 3999 because I never found the character set for 5000, 10000, 50000...you get the idea Help if you can

Usage
Import the class from wherever it is
	>>> # I will import from the file directly
	>>> from int_roman import IntRoman
Create an instance of the class 'IntRoman'
	>>> ir = IntRoman()
Use the to_roman method to convert to a roman number
	>>> # the return value is a roman numeral equivalent string
	>>> ir.to_roman(4)
	'IV'
Additionaly, you might want to convert a whole list. Use the to_roman_list method
	>>> # returns a list of strings with equilvalent roman numerals to the input string at the same index
	>>> nums = [4, 63, 963, 623]
	>>> ir.to_roman_list(nums)
	['IV', 'LXIII', 'CMLXIII', 'DCXXIII']
For additional support or to check available methods use the dir() function
	>>> dir(ir)
Please help add support from number 4000 to infinity (at least a million)