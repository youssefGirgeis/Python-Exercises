#Welcome. In this kata, you are asked to square every digit of a number.
#For example, if we run 9119 through the function, 811181 will come out.
#Note: The function accepts an integer and returns an integer



def square_digits(num):

	nums = str(num)
	result = ''

	for digit in nums:

		digit_int = int(digit)**2
		result += str(digit_int)
	
	return int(result)

print(square_digits(9119))