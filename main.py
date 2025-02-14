from task1 import kwargsAcceptFun
from task2 import typeBasedTransformer

print("Task 1:")
kwargsAcceptFun(name="Sanjar", age=20, city="Tashkent")
print('''
*************
      ''')

print("Task 2:")
print(typeBasedTransformer(
    number=4,
    text="Hello",
    boolean=True,
    my_list=[1, 2, 3],
    my_dict={"a": 1, "b": 2}
))

