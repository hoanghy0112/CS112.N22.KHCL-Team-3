
# Hàm này không gọi hàm nào khác
def independentFunction(a):
    return (a)

# Hàm này gọi hàm foo nên khi test bằng unit test cần phải mock
def functionThatCallOther(a):
    result = foo(a)
    return result


def foo(a):
    return a 