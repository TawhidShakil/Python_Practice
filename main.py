# n = int(input("Enter the number: "))
# reverse = 0
# while n!=0:
#     r = n%10
#     reverse = reverse*10+r
#     n = n//10
# print(reverse)

##fibonacci seris
# def fibo(n):
#     if n<=0:
#         return []
#     if n==1:
#         return [0]
#     fibo_seris = [0, 1]
#     for i in range(2, n):
#         fibo_seris.append(fibo_seris[i-1] + fibo_seris[i-2])

#     return fibo_seris

# n = int(input("Enter the number: "))
# fiboSeris = fibo(n)
# print(f"Fibonacci Seris: {fiboSeris}")
#Reverse the number
n = int(input("Enter the number: "))
temp = n
rev = 0
while temp!=0:
    r = temp%10
    rev = rev*10+r
    temp = temp//10 
if rev == n:
    print("YEs")
else:
    print("NO")
# print(f"The reverse number is: {reverse}")
#Sum of Digit
# n = int(input("Enter the number: "))
# sum = 0

# while n!=0:
#     r = n%10
#     sum+= r
#     n = n//10
# print(sum)
#Factorial Number
# def factorial(n):
#     if n==1:
#         return n
#     return n*factorial(n-1)

# n = int(input("Enter the number: "))
# fact = factorial(n)
# print(f"Factorial is: {fact}")
#Nth of Sum
# def nthOfSum(n):
#     if n==1:
#         return n
#     return n+nthOfSum(n-1)

# n = int(input("Enter the number: "))
# sum = nthOfSum(n)
# print(f"Sum is: {sum}")
#Sum of Even number from 1 to Nth


