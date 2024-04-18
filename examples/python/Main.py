
def main():
    x = len('abc')
    print(x)
    other = 'value'
    # variables
    # ------------------------------------------------------------
    # green for local variables. Strings are also green but don't pop at you as much
    regular_variable = 'value'
    print(regular_variable)
    # unused ones are gray
    unused = "value"
    # added underline for mutable ones

    # classes and its functions
    # ------------------------------------------------------------
    class_instance = AClass()  # classes are bold blue
    # classInstance.classFunction(regularVariable) // so are class functions
    #     classInstance.classField // fields are pink
    # classInstance.mutableClassField = mutableVariable // mutable fields underlined like the variables


class AClass:
    class_field = 'value'

# @decorator(param=1)
# def f(x):
#     """
#     Syntax Highlighting Demo
#     @param x Parameter
#
#     Semantic highlighting:
#     Generated spectrum to pick colors for local variables and parameters:
#      Color#1 SC1.1 SC1.2 SC1.3 SC1.4 Color#2 SC2.1 SC2.2 SC2.3 SC2.4 Color#3
#      Color#3 SC3.1 SC3.2 SC3.3 SC3.4 Color#4 SC4.1 SC4.2 SC4.3 SC4.4 Color#5
#     """
#
#     def nested_func(y):
#         print(y + 1)
#
#     s = ("Test", 2+3, {'a': 'b'}, f'{x!s:{"^10"}}')   # Comment
#     f(s[0].lower())
#     nested_func(42)
#
# class Foo:
#     tags: List[str]
#
#     def __init__(self: Foo):
#         byte_string: bytes = b'newline:\n also newline:\x0a'
#         text_string = u"Cyrillic Я is \u042f. Oops: \u042g"
#         self.make_sense(whatever=1)
#
#     def make_sense[T](self, whatever: T):
#         self.sense = whatever
#
# x = len('abc')
# type my_int< = int
# print(f.__doc__)