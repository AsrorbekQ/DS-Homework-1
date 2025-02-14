def typeBasedTransformer(**kwargs):

    func_return = {}
    for i, t in kwargs.items():
        if isinstance(t, (int, float)):
            func_return[i] = t ** 2
        elif isinstance(t, str):
            func_return[i] = t[::-1]
        elif isinstance(t, bool):
            func_return[i] = not t
        elif isinstance(t, (list, tuple)):
            func_return[i] = t[::-1]
        elif isinstance(t, dict):
            func_return[i] = {v: k for k, v in t.items()}
        else:
            func_return[i] = t

    return func_return

print(typeBasedTransformer(
    number=4,
    text="Hello",
    boolean=True,
    my_list=[1, 2, 3],
    my_dict={"a": 1, "b": 2}
))

