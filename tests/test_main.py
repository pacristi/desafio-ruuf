import pytest


def main(a, b, x, y):
    if a > x and b > x or a > y and b > y:
        return 0
    return (x * y) // (a * b)


@pytest.mark.parametrize(
    "a, b, x, y, expected",
    [
        (1, 2, 2, 4, 4),
        (1, 2, 3, 5, 7),
        (2, 2, 1, 10, 0)
    ]
)
def test_main(a, b, x, y, expected):
    assert main(a, b, x, y) == expected
