
# from Unit_Tests import square
#
# def main():
#     test_square()
#
# def test_square():
#     # if square(2) != 4:
#     #     print("2 squared was not 4")
#     # if square(3) != 9:
#     #     print("3 squared was not 9")
#     try:
#         assert square(2) == 4
#     except AssertionError:
#         print("2 squared was not 4")
#     try:
#         assert square(3) == 9
#     except AssertionError:
#         print("3 squared was not 9")
#     try:
#         assert square(-2) == 4
#     except AssertionError:
#         print("-2 squared was not 4")
#     try:
#         assert square(-3) == 9
#     except AssertionError:
#         print("-3 squared was not 9")
#     try:
#         assert square(0) == 0
#     except AssertionError:
#         print("0 squared was not 0")
#
# if __name__ == "__main__":
#     main()
# import pytest
# from Unit_Tests import square

# def test_square():
#     assert square(2) == 4
#     assert square(3) == 9
#     assert square(-2) == 4
#     assert square(-3) == 9
#     assert  square(0) == 0

# def test_positive():
#     assert square(2) == 4
#     assert square(3) == 9
#
# def test_negative():
#     assert square(-2) == 4
#     assert square(-3) == 9
#
# def test_zero():
#     assert square(0) == 0
#
# def test_str():
#     with pytest.raises(TypeError):
#         square("cat")

##############
# test hello
#############
from Unit_Tests import hello

# def test_hello():
#     assert hello("david") == "hello, david"
#     assert hello() == "hello, world"

def test_default():
    assert hello() == "hello, world"

def test_argument():
    # assert hello("david") == "hello, david"
    for name in ["hermione", "harry", "ron"]:
        assert hello(name) == f"hello, {name}"
