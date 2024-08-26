#Viết phương thức Fibonacci( ) như sau - Dãy số Fibonacci bậc 1 gồm các số F0, F1, F2, F3, F4, F5, F6, ... là dãy 0, 1, 1, 2, 3, 5, 8,
...- Nhập vào số nguyên n ≥ 0.- Phương thức trả về một số nguyên là số Fn theo hai cách: dùng giải thuật đệ qui và dùng
giải thuật không đệ qui.- Gợi ý thuật đệ qui: F0 = 0, F1 = 1, Fn = Fn-1 + Fn-2
 thuật không đệ qui: dùng ba biến a, b, c để lưu ba số Fibonacci kế tiếp nhau.
  
class Fibonacci:

  def recursive_fibonacci(n):
    if n <= 1:
      return n
    else:
      return Fibonacci.recursive_fibonacci(
          n - 1) + Fibonacci.recursive_fibonacci(n - 2)

  def interative_fibonacci(n):
    if n == 0:
      return n
    elif n == 1:
      return n
    else:
      a, b, c = 0, 1, 1
      for i in range(2, n):
        a, b, c = b, c, a + b + c
      return c


n = int(input("Nhập số n : "))
print("Recursive Fibonacci: ", Fibonacci.recursive_fibonacci(n))
print("Interative Fibonacci: ", Fibonacci.interative_fibonacci(n))
