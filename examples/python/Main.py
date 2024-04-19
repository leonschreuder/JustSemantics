
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

    # classes and its functions
    # ------------------------------------------------------------
    class_instance = AClass("some string")  # classes are bold blue
    class_instance.class_function(regular_variable) # so are class functions
    print(class_instance.class_field)  # fields are pink


class AClass:
    class_field = 'value'

    def __init__(self, constructor_arg):
        self.constructor_arg = constructor_arg

    def class_function(self, function_argument):
        pass