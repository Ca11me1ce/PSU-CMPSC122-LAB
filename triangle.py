class Rectangle():
    def __init__(s, length, width):
        s.l = length
        s.w= width
    def perimeter(s):
        rec_peri=2*s.l+2*s.w
        return rec_peri
    def area(s):
        rec_area=s.l*s.w
        return rec_area
    
#############################
#                           #
#   test case, do not copy  #
#                           #
#############################
a=Rectangle(2, 5)
print(a.perimeter())
print(a.area())
