def reverseString(r):
  reversed_str = ""
  for i in range(len(s) - 1, -1, -1):
        reversed_str += r[i]
    return reversed_str

if __name__ == "__main__":
  r = input("Enter a string: ")
    print("Reversed string: ", reverse_string(r))

