class Neper:
  def calculate_factorial(num):
      if num == 0:
          return 1
      factorial = 1
      for i in range(1, num + 1):
          factorial *= i
      return factorial
  def neper_sum(n):
      sum = 0
      for k in range(n + 1):
          sum += 1 / Neper.calculate_factorial(k)
      return sum
n = int(input("Nhập n : "))
print("Tổng của a0 + a1 + ... + an là:", Neper.neper_sum(n))
