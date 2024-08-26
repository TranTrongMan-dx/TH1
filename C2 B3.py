class Array:
  def __init__(self, Array):
      self.Array = Array
  def TrungHang(self):
      n = len(self.Array)
      for i in range(n):
          for j in range(i + 1, n):
              if self.Array[i] == self.Array[j]:
                  return True
      return False
x = [
  [1, 2, 3],
  [4, 5, 6],
  [1, 2, 3]
]
matrix = Array(x)
if matrix.TrungHang():
  print("True")
else:
  print("False")
