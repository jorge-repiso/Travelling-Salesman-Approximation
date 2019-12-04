import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),\
                 ("Delaware", "Dover", 39.161921, -75.526755),\
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = [('Nebraska', 'Lincoln', 40.809868, -96.675345),\
                 ('Illinois', 'Springfield', 39.78325, -89.650373),\
                 ('Connecticut', 'Hartford', 41.767, -72.677),\
                 ('California', 'Sacramento', 38.555605, -121.468926)]

    road_map3 = [('South Dakota', 'Pierre', 44.367966, -100.336378),\
                 ('Maryland', 'Annapolis', 38.972945, -76.501157),\
                 ('New Jersey', 'Trenton', 40.221741, -74.756138),\
                 ('Arkansas', 'Little Rock', 34.736009, -92.331122)]

    road_map4 = [('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),\
                 ('Florida', 'Tallahassee', 30.4518, -84.27277),\
                 ('Oregon', 'Salem', 44.931109, -123.029159),\
                 ('Hawaii', 'Honolulu', 21.30895, -157.826182),\
                 ('Kansas', 'Topeka', 39.04, -95.69)]

    assert compute_total_distance(road_map1) == \
           pytest.approx(9.386 + 18.496 + 10.646, 0.01)

    assert compute_total_distance(road_map2) == \
           pytest.approx(7.099 + 17.088 + 48.897 + 24.895, 0.01)

    assert compute_total_distance(road_map3) == \
           pytest.approx(24.438 + 2.145 + 18.411 + 12.524, 0.01)

    assert compute_total_distance(road_map4) == \
           pytest.approx(12.292 + 41.372 + 42.057 + 64.616 + 18.854, 0.01)


def test_swap_cities():
    new_road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311), \
                     ("Delaware", "Dover", 39.161921, -75.526755), \
                     ("Minnesota", "Saint Paul", 44.95, -93.094), \
                     ('West Virginia', 'Charleston', 38.349497, -81.633294), \
                     ('Hawaii', 'Honolulu', 21.30895, -157.826182)]

    new_road_map2 = [('Nebraska', 'Lincoln', 40.809868, -96.675345), \
                     ('Illinois', 'Springfield', 39.78325, -89.650373), \
                     ('Connecticut', 'Hartford', 41.767, -72.677), \
                     ('California', 'Sacramento', 38.555605, -121.468926), \
                     ('Rhode Island', 'Providence', 41.82355, -71.422132)]

    pass

def test_shift_cities():
    pass


def test_find_best_cycle():
    pass


def test_print_map():
    pass
