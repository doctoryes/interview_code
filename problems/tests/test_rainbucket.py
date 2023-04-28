
import pytest
import rainbucket

def test_rainfall_empty():
    r = []
    z = rainbucket.maximum_rain(r)
    assert(z == (None, None))

@pytest.mark.parametrize(
    "forecast,expected",
    [
        [
            [(10, 5), (2, 4), (6, 5), (9, 2), (3, 1), (2, 8), (4, 4)], (1, 5)
        ],
        [
            [(100, 1), (10, 5), (2, 4), (6, 5), (9, 2), (3, 1), (2, 8), (4, 4)], (1, 6)
        ],
    ]
)
def test_rainfall_initial_positive(forecast, expected):
    z = rainbucket.maximum_rain(forecast)
    assert(z == expected)

@pytest.mark.parametrize(
    "forecast,expected",
    [
        [
            [(10, 50), (2, 4), (6, 5), (9, 2), (3, 1), (2, 8), (4, 4)], (3, 5)
        ],
        [
            [(2, 4), (6, 5), (9, 2), (3, 1), (2, 8), (4, 4)], (2, 4)
        ],
    ]
)
def test_rainfall_initial_negative(forecast, expected):
    z = rainbucket.maximum_rain(forecast)
    assert(z == expected)

@pytest.mark.parametrize(
    "forecast,expected",
    [
        [
            [(1, 8)], (None, None)
        ],
        [
            [(5, 6), (1, 8)], (None, None)
        ],
        [
            [(5, 10), (5, 6), (1, 8)], (None, None)
        ],
    ]
)
def test_rainfall_all_negative(forecast, expected):
    z = rainbucket.maximum_rain(forecast)
    assert(z == expected)

@pytest.mark.parametrize(
    "forecast,expected",
    [
        [
            [(8, 1)], (1, 1)
        ],
        [
            [(6, 5), (8, 1)], (1, 2)
        ],
        [
            [(10, 5), (6, 5), (8, 1)], (1, 3)
        ],
    ]
)
def test_rainfall_all_positive(forecast, expected):
    z = rainbucket.maximum_rain(forecast)
    assert(z == expected)

