import pytest
from src.index import independentFunction, functionThatCallOther, foo
from unittest.mock import patch
import os


# Một hàm test cơ bản có dạng:
def test_independentFunction_basic():
    assert independentFunction(1) == 1


# Một hàm test sử dụng cho nhiều test case
# Dùng một hàm test nhưng cho nhiều test case khác nhau
# pytest.mark.parametrize có tác dụng truyền lần lượt các test case vào hàm test của mình
# ta sẽ truyền đối số đầu tiên là các tham số cho hàm test
# đối số thứ 2 là một mảng các test case, với mỗi test case, chương trình sẽ truyền lần lượt các giá trị vào các tham số đã ghi ở đối số thứ nhất
# Về cơ bản, hàm test sẽ chạy n lần, với n là số test case, ở đây ta có 3 test case
# Giá trị của a, expected_result sẽ lần lượt được gán bằng giá trị của từng test case và sau đó được truyền vào hàm test
@pytest.mark.parametrize(
    "a, exprected_result",
    [
        (1, 1),  # Test case 1
        (2, 2),  # Test case 2
        (3, 3),  # Test case 3
    ],
)
def test_independentFunction(a, exprected_result):
    assert independentFunction(a) == exprected_result


# hàm mock cho hàm foo
# ta sẽ thay thế giá trị trả về của hàm foo bằng giá trị mà ta truyền vào trực tiếp
# Giải thích chi tiết hơn ở bên dưới
@pytest.fixture
def mockFoo(mocker, foo_return_value):
    mocker.patch("src.index.foo", return_value=foo_return_value)


# unit test một hàm khi hàm đó có gọi một hàm khác
# ở đây ta test hàm functionThatCallOther, hàm này có gọi hàm foo
# trường hợp này bắt buộc phải sử dụng mock để đảm bảo tính độc lập của unit test, tránh việc lỗi sai của hàm foo ảnh hưởng đến hàm cần test
@pytest.mark.parametrize(
    "a, foo_return_value, exprected_result",  # a_foo là giá trị trả về của hàm foo với input là a, ta sẽ tính toán sẵn giá trị này và mock để nó thay thế cho giá trị trả về của foo thay vì tính toán bằng cách gọi hàm foo
    [
        (1, 1, 1),  # Test case 1
        (2, 2, 2),  # Test case 2
        (3, 3, 3),  # Test case 3
    ],
)
# Chú ý: mình đặt tên a_foo cho tham số thứ 2 là để trùng với a_foo trong mockFoo,
# nhằm để a_foo sẽ được truyền vào hàm mockFoo và sau đó, giá trị trả về của hàm foo khi ta
# gọi functionThatCallOther sẽ được thay thế bằng giá trị trả về của mockFoo, cũng chính là a_foo
# decorator  này là để sử dụng hàm mockFoo đã được khai báo ở trên, mục đích là để mock hàm foo
@pytest.mark.usefixtures("mockFoo")
def test_functionThatCallOther(a, exprected_result):
    assert (
        functionThatCallOther(a) == exprected_result
    )  # nếu giá trị trả về khác với expected_result thì test-runner sẽ thông báo cho ta dưới dạng lỗi

