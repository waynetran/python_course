from shapes import *

def main():
  r = 3
  print("Circle")
  print("-----------------------")
  print("Circumference: {}".format(circle.circumference(r)))
  print("Area: {}".format(circle.area(r)))
  print("\n")

  s = 2
  print("Square")
  print("-----------------------")
  print("Perimeter: {}".format(square.perimeter(s)))
  print("Area: {}".format(square.area(s)))
  print("\n")

  w = 2
  l = 3
  print("Rectangle")
  print("-----------------------")
  print("Perimeter: {}".format(rectangle.perimeter(w,l)))
  print("Area: {}".format(rectangle.area(w,l)))
  print("\n")

  print("Triangle")
  print("-----------------------")
  print("Perimeter: {}".format(triangle.perimeter(2,3,4)))
  print("Area: {}".format(triangle.area(3,4)))
  print("\n")

  print("Parallelogram")
  print("-----------------------")
  print("Perimeter: {}".format(parallelogram.perimeter(2,3)))
  print("Area: {}".format(parallelogram.area(2,3)))
  print("\n")

  print("Trapezoid")
  print("-----------------------")
  print("Perimeter: {}".format(trapezoid.perimeter(2,3,4,5)))
  print("Area: {}".format(trapezoid.area(2,3,4)))
  print("\n")

if __name__ == "__main__":
    main()
