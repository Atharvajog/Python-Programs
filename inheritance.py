# class A:
#     def __init__(self):
#         print("Constructor of A")
#     def feature(self):
#         print("A feature")
# class B:
#     def __init__(self):
#         print("Contructor of B")
#     def feature(self):
#         print("B feature")
#
# class C(B,A):
#     def __init__(self):
#         super().__init__()
#         A.__init__(self)
#
#     def method(self):
#         print("C method")
#
# obj=C()
# obj.feature()
class A:
    def __init__(self):
        print("Constructor of A")

    def feature(self):
        print("A feature")


class B:
    def __init__(self):
        print("Constructor of B")

    def feature(self):
        print("B feature")


class C(B, A):
    def __init__(self):
        super().__init__()  # Call constructor of class B
        A.__init__(self)  # Call constructor of class A

    def method(self):
        print("C method")


obj = C()  # Create an instance of class C
obj.feature()  # This will call the feature method of class A
A.feature(C)
