# Application of static method in Python
class MyClass:
    @staticmethod
    def my_static_method():
        return "Este é um método estático!"
    
    @classmethod
    def my_class_method(cls):
        return "Este é um método de classe!"
    
    def my_instance_method(self):
        return "Este é um método de instância!"

# Calling static method
print(MyClass.my_static_method())
    
# Calling class method
print(MyClass.my_class_method())
    
# Calling instance method
print(MyClass().my_instance_method())
