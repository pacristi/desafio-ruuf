import pytest
from src import main


@pytest.mark.parametrize(
    "a, b, x, y, expected",
    [
        (1, 2, 2, 4, 4),
        (1, 2, 3, 5, 7),
        (2, 2, 1, 10, 0),
        (2, 2, 3, 3, 1),
        (2, 2, 3, 4, 2),
        (2, 4, 6, 3, 1)
    ]
)
def test_main(a, b, x, y, expected):
    assert main(a, b, x, y) == expected


def test_negative_sides_error():
    with pytest.raises(ValueError):
        main(-1, 2, 3, 4)
