class GCD :
      def GCD(x,y):
        if y==0:
            return x
        else:
            return GCD(y,x%y)
      x = int(input("Nhập x:"))
      y = int(input("Nhập y:"))
      print("Ước số chung lớn nhất là: ")
      print(GCD(x,y))