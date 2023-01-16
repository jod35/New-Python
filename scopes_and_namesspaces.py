def test_function():
    test=1

    print("Test in localscope of function",test)

test_function()

test = 4

print("Test in global scope",test)


def outer():
    test = 1

    def inner():
        test =2
        print(f"Inner: {test}")

    inner()

    print(f"Outer {test}")

test = 0 
outer()
print("Global: ",test)