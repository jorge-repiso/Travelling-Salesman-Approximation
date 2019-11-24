import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311), \
                 ("Delaware", "Dover", 39.161921, -75.526755), \
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = [('Nebraska', 'Lincoln', 40.809868, -96.675345), \
                 ('Illinois', 'Springfield', 39.78325, -89.650373), \
                 ('Connecticut', 'Hartford', 41.767, -72.677), \
                 ('California', 'Sacramento', 38.555605, -121.468926)]

    road_map3 = [('South Dakota', 'Pierre', 44.367966, -100.336378)]

    road_map4 = []

    assert compute_total_distance(road_map1) == \
           pytest.approx(9.386 + 18.496 + 10.646, 0.01)

    assert compute_total_distance(road_map2) == \
           pytest.approx(7.099 + 17.088 + 48.897 + 24.895, 0.01)

    assert compute_total_distance(road_map3) == \
           pytest.raises(Exception)



def test_swap_cities():
    pass


def test_shift_cities():
    pass


def test_find_best_cycle():
    pass


def test_print_map():
    pass
