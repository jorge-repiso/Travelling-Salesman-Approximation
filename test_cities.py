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

    assert swap_cities(b_road_map1, 0, 2) == ([("Minnesota", "Saint Paul", 44.95, -93.094),
                                              ("Delaware", "Dover", 39.161921, -75.526755),
                                              ("Kentucky", "Frankfort", 38.197274, -84.86311),
                                              ('West Virginia', 'Charleston', 38.349497, -81.633294),
                                              ('Hawaii', 'Honolulu', 21.30895, -157.826182)], pytest.approx(18.496215 + 9.386057 + 3.233401 + 78.075197 + 68.914111, 0.01))

    assert swap_cities(b_road_map2, 1, 2) == ([('Nebraska', 'Lincoln', 40.809868, -96.675345),
                                              ('Connecticut', 'Hartford', 41.767, -72.677),
                                              ('Illinois', 'Springfield', 39.78325, -89.650373),
                                              ('California', 'Sacramento', 38.555605, -121.468926),
                                              ('Rhode Island', 'Providence', 41.82355, -71.422132)], pytest.approx(24.017424 + 17.088904 + 31.842227 + 50.153375 + 25.27355, 0.01))

    assert swap_cities(b_road_map3, 1, 3) == ([('Maryland', 'Annapolis', 38.972945, -76.501157),
                                              ('South Dakota', 'Pierre', 44.367966, -100.336378),
                                              ('California', 'Sacramento', 38.555605, -121.468926),
                                              ('Nevada', 'Carson City', 39.160949, -119.753877)], pytest.approx(24.438167 + 21.917302 + 1.818745 + 43.253129, 0.01))

    assert swap_cities(b_road_map4, 0, 4) == ([('Missouri', 'Jefferson City', 38.572954, -92.189283),
                                              ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                                              ('Indiana', 'Indianapolis', 39.790942, -86.147685),
                                              ('Colorado', 'Denver', 39.7391667, -104.984167),
                                              ('Utah', 'Salt Lake City', 40.7547, -111.892622)], pytest.approx(15.407392 + 9.284429 + 18.836553 + 6.982697 + 19.823763, 0.01))

    assert swap_cities(b_road_map1, 4, 4) == ([("Kentucky", "Frankfort", 38.197274, -84.86311),
                                              ("Delaware", "Dover", 39.161921, -75.526755),
                                              ("Minnesota", "Saint Paul", 44.95, -93.094),
                                              ('West Virginia', 'Charleston', 38.349497, -81.633294),
                                              ('Hawaii', 'Honolulu', 21.30895, -157.826182)], pytest.approx(9.386057 + 18.496215 + 13.225522 + 78.075197 + 74.892091, 0.01))

    assert swap_cities(b_road_map3, 2, 0) == ([('California', 'Sacramento', 38.555605, -121.468926),
                                              ('Nevada', 'Carson City', 39.160949, -119.753877),
                                              ('Maryland', 'Annapolis', 38.972945, -76.501157),
                                              ('South Dakota', 'Pierre', 44.367966, -100.336378)], pytest.approx(1.818745 + 43.253129 + 24.438167 + 21.917302, 0.01))

    assert swap_cities(b_road_map2, 4, 0) == ([('Rhode Island', 'Providence', 41.82355, -71.422132),
                                              ('Illinois', 'Springfield', 39.78325, -89.650373),
                                              ('Connecticut', 'Hartford', 41.767, -72.677),
                                              ('California', 'Sacramento', 38.555605, -121.468926),
                                              ('Nebraska', 'Lincoln', 40.809868, -96.675345)], pytest.approx(18.342072 + 17.088904 + 48.897496 + 24.89585 + 25.27355, 0.01))

    assert swap_cities(b_road_map4, 2, 2) == ([('Utah', 'Salt Lake City', 40.7547, -111.892622),
                                              ('Pennsylvania', 'Harrisburg', 40.269789, -76.875613),
                                              ('Indiana', 'Indianapolis', 39.790942, -86.147685),
                                              ('Colorado', 'Denver', 39.7391667, -104.984167),
                                              ('Missouri', 'Jefferson City', 38.572954, -92.189283)], pytest.approx(35.020366 + 9.284429 + 18.836553 + 12.847922 + 19.823763, 0.01))

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
