def sumOfDigits(n):
  total = 0
  for digit in str(n):
    total += int(digit)
  return total

#test case
if __name__ == "__main__":
  n = int(input("Enter a number: "))
    print(f"Sum of digits: {sum_digits(n)}")
