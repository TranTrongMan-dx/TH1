class Array:
  def __init__(self, Array):
      self.Array = Array
  def NhomHang(self):
      n = len(self.Array)
      nhom = {} 
      for i in range(n):
          for j in range(i + 1, n):
              if self.Array[i] == self.Array[j]:
                  if i in nhom:
                      nhom[i].append(j)
                  else:
                      nhom[i] = [i, j]
      for key, value in nhom.items():
          print("Nhom {}: {}".format(key + 1, ", ".join(str(idx + 1) for idx in value)))
x = [
  [1, 2, 3],
  [4, 5, 6],
  [1, 2, 3]
]
matrix = Array(x)
matrix.NhomHang()
