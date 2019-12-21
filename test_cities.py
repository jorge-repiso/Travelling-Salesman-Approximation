import pytest
from cities import *


def test_compute_total_distance():
    road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                 ("Delaware", "Dover", 39.161921, -75.526755),
                 ("Minnesota", "Saint Paul", 44.95, -93.094)]

    road_map2 = [('Nebraska', 'Lincoln', 40.809868, -96.675345),
                 ('Illinois', 'Springfield', 39.78325, -89.650373),
                 ('Connecticut', 'Hartford', 41.767, -72.677),
                 ('California', 'Sacramento', 38.555605, -121.468926)]

    road_map3 = [('South Dakota', 'Pierre', 44.367966, -100.336378),
                 ('Maryland', 'Annapolis', 38.972945, -76.501157),
                 ('New Jersey', 'Trenton', 40.221741, -74.756138),
                 ('Arkansas', 'Little Rock', 34.736009, -92.331122)]

    road_map4 = [('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                 ('Florida', 'Tallahassee', 30.4518, -84.27277),
                 ('Oregon', 'Salem', 44.931109, -123.029159),
                 ('Hawaii', 'Honolulu', 21.30895, -157.826182),
                 ('Kansas', 'Topeka', 39.04, -95.69)]

    assert compute_total_distance(road_map1) == pytest.approx(9.386 + 18.496 + 10.646, 0.01)

    assert compute_total_distance(road_map2) == pytest.approx(7.099 + 17.088 + 48.897 + 24.895, 0.01)

    assert compute_total_distance(road_map3) == pytest.approx(24.438 + 2.145 + 18.411 + 12.524, 0.01)

    assert compute_total_distance(road_map4) == pytest.approx(12.292 + 41.372 + 42.057 + 64.616 + 18.854, 0.01)


def test_swap_cities():
    b_road_map1 = [("Kentucky", "Frankfort", 38.197274, -84.86311),
                   ("Delaware", "Dover", 39.161921, -75.526755),
                   ("Minnesota", "Saint Paul", 44.95, -93.094),
                   ('West Virginia', 'Charleston', 38.349497, -81.633294),
                   ('Hawaii', 'Honolulu', 21.30895, -157.826182)]

    b_road_map2 = [('Nebraska', 'Lincoln', 40.809868, -96.675345),
                   ('Illinois', 'Springfield', 39.78325, -89.650373),
                   ('Connecticut', 'Hartford', 41.767, -72.677),
                   ('California', 'Sacramento', 38.555605, -121.468926),
                   ('Rhode Island', 'Providence', 41.82355, -71.422132)]

    b_road_map3 = [('Maryland', 'Annapolis', 38.972945, -76.501157),
                   ('Nevada', 'Carson City', 39.160949, -119.753877),
                   ('California', 'Sacramento', 38.555605, -121.468926),
                   ('South Dakota', 'Pierre', 44.367966, -100.336378)]

    b_road_map4 = [('Utah', 'Salt Lake City', 40.7547, -111.892622),
                   ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                   ('Indiana', 'Indianapolis', 39.790942, -86.147685),
                   ('Colorado', 'Denver', 39.7391667, -104.984167),
                   ('Missouri', 'Jefferson City', 38.572954, -92.189283)]

    pass

def test_shift_cities():
    c_road_map1 = [('Idaho', 'Boise', 43.613739, -116.237651),
                   ('California', 'Sacramento', 38.555605, -121.468926),
                   ('Rhode Island', 'Providence', 41.82355, -71.422132),
                   ('Utah', 'Salt Lake City', 40.7547, -111.892622),
                   ('Alaska', 'Juneau', 58.301935, -134.41974)]

    c_road_map2 = [('Georgia', 'Atlanta', 33.76, -84.39),
                   ('New York', 'Albany', 42.659829, -73.781339),
                   ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                   ('New Hampshire', 'Concord', 43.220093, -71.549127),
                   ('Arkansas', 'Little Rock', 34.736009, -92.331122)]

    c_road_map3 = [('Tennessee', 'Nashville', 36.165, -86.784),
                   ('New Mexico', 'Santa Fe', 35.667231, -105.964575),
                   ('Illinois', 'Springfield', 39.78325, -89.650373),
                   ('Nevada', 'Carson City', 39.160949, -119.753877),
                   ('Wyoming', 'Cheyenne', 41.145548, -104.802042)]

    c_road_map4 = [('Montana', 'Helana', 46.595805, -112.027031),
                   ('Michigan', 'Lansing', 42.7335, -84.5467),
                   ('Florida', 'Tallahassee', 30.4518, -84.27277),
                   ('Oregon', 'Salem', 44.931109, -123.029159),
                   ('Wisconsin', 'Madison', 43.074722, -89.384444)]

    assert shift_cities(c_road_map1) == [('Alaska', 'Juneau', 58.301935, -134.41974),
                                              ('Idaho', 'Boise', 43.613739, -116.237651),
                                              ('California', 'Sacramento', 38.555605, -121.468926),
                                              ('Rhode Island', 'Providence', 41.82355, -71.422132),
                                              ('Utah', 'Salt Lake City', 40.7547, -111.892622)]

    assert shift_cities(c_road_map2) == [('Arkansas', 'Little Rock', 34.736009, -92.331122),
                                              ('Georgia', 'Atlanta', 33.76, -84.39),
                                              ('New York', 'Albany', 42.659829, -73.781339),
                                              ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                                              ('New Hampshire', 'Concord', 43.220093, -71.549127)]

    assert shift_cities(c_road_map3) == [('Wyoming', 'Cheyenne', 41.145548, -104.802042),
                                              ('Tennessee', 'Nashville', 36.165, -86.784),
                                              ('New Mexico', 'Santa Fe', 35.667231, -105.964575),
                                              ('Illinois', 'Springfield', 39.78325, -89.650373),
                                              ('Nevada', 'Carson City', 39.160949, -119.753877)]

    assert shift_cities(c_road_map4) == [('Wisconsin', 'Madison', 43.074722, -89.384444),
                                              ('Montana', 'Helana', 46.595805, -112.027031),
                                              ('Michigan', 'Lansing', 42.7335, -84.5467),
                                              ('Florida', 'Tallahassee', 30.4518, -84.27277),
                                              ('Oregon', 'Salem', 44.931109, -123.029159)]

def test_find_best_cycle():
    pass


def test_print_map():
    pass
