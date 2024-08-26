class Array:
  def __init__(self, Array):
      self.Array = Array
  def TamGiacTren(self):
      n = len(self.Array)
      for i in range(n):
          for j in range(i + 1, n):
              if self.Array[i][j] != 0:
                  return False
      return True
x = [
  [1, 2, 3],
  [0, 4, 5],
  [0, 0, 6]
]
matrix = Array(x)
if matrix.TamGiacTren():
  print("True")
else:
  print("False")
