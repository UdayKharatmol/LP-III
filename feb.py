def fibonacci_iterative(n):
	if n<=1:
		return n
	a,b = 0,1
	for i in range(2,n+1):
		a,b=b,a+b
		return b

def fibonacci_recursion(n):
	if n<=1:
		return n
	return fibonacci_recursion (n-1)+ fibonacci_recursion(n-2)
	
def calculate_fibonacci():
	try:
		n=int(input("Enter a number to calculate fibonacci: "))
		if n<0:
			print("Please Enter a positive integer !")
			return
			
		print("Choose method:\n1.Iterative\n2.Recursive")
		choice = int(input("Enter 1 or 2: "))
		
		if choice ==1:
			result = fibonacci_iterative(n)
			print(f"Iterative Fibonacci of {n}:{result}")
		elif choice ==2:
			result = fibonacci_recursion(n)
			print(f"Recursive Fibonacci of {n}:{result}")
		else:
			print("Invalid choice !!!")
			
	except ValueError:
		print("Invalid Input!!!")

calculate_fibonacci()
