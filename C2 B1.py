class Array:
  def __init__(self, Array):
      self.Array = Array
  def DoiXung(self):
      n = len(self.Array)
      for i in range(n):
          for j in range(n):
              if self.Array[i][j] != self.Array[j][i]:
                  return False
      return True
x = [
  [1, 2, 3],
  [2, 4, 7],
  [3, 5, 6]
]
matrix = Array(x)
if matrix.DoiXung():
  print("True")
else:
  print("False")
