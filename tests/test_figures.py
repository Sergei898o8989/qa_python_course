import pytest
from src.Triangle import Triangle
from src.Circle import Circle
from src.Square import Square
from src.Rectangle import Rectangle


def test_triangle_valid_sides():
    t = Triangle(3, 4, 5)
    assert t.area == pytest.approx(6, rel=1e-2)
    assert t.perimeter == 12


def test_triangle_invalid_sides():
    with pytest.raises(ValueError):
        t = Triangle(1, 1, 10)


def test_triangle_impossible_sides():
    with pytest.raises(ValueError):
        t = Triangle(2, 3, 12)


def test_rectangle():
    r = Rectangle(3, 4)
    assert r.area == 12
    assert r.perimeter == 14


def test_rectangle_zero_dimension():
    with pytest.raises(ValueError):
        r = Rectangle(0, 4)


def test_square():
    s = Square(5)
    assert s.area == 25
    assert s.perimeter == 20


def test_square_zero_dimension():
    with pytest.raises(ValueError):
        s = Square(0)


def test_circle():
    c = Circle(3)
    assert c.area == pytest.approx(28.26, rel=1e-2)
    assert c.perimeter == pytest.approx(18.84, rel=1e-2)


def test_circle_zero_radius():
    with pytest.raises(ValueError):
        c = Circle(0)


def test_add_area():
    t = Triangle(3, 4, 5)
    s = Square(5)
    r = Rectangle(3, 4)
    c = Circle(3)
    assert t.add_area(s) == pytest.approx(31, rel=1e-2)
    assert r.add_area(c) == pytest.approx(40.26, rel=1e-2)


def test_add_area_exception():
    t = Triangle(3, 4, 5)
    with pytest.raises(ValueError):
        t.add_area(3)
