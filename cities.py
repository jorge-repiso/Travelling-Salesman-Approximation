import random
import math


class City:
    def __init__(self, state, name, latitude, longitude):
        self.state = state
        self.name = name
        self.latitude = latitude
        self.longitude = longitude


def read_cities(file_name):
    with open(file_name) as road_map:
        road_map = [tuple(element.rstrip().split("\t")) for element in road_map]
        return road_map


def print_cities(road_map):
    c = "City"
    s = "State"
    lat = "Latitude"
    long = "Longitude"
    header = f'{c:^15}|{s:^15}|{lat:^15}|{long:^15}'

    print(f'{"-" * len(header)}')
    print(f'{header}')
    print(f'{"-" * len(header)}')
    for item in road_map:
        print(f'{item[1]:<15} {item[0]:<15} {item[2][:5]:^15} {item[3][:6]:^15}')


def compute_total_distance(road_map):
    distance = 0
    count = 1

    for city in road_map:
        p1 = city[2]
        p2 = city[3]
        if city != road_map[-1]:
            q1 = road_map[count][2]
            q2 = road_map[count][3]
        else:
            q1 = road_map[0][2]
            q2 = road_map[0][3]
        distance = distance + math.sqrt(((p1-q1) ** 2) + ((p2-q2) ** 2))
        count += 1
    return distance


def euclidean_distance(coord_a, coord_b):
    return math.sqrt(math.pow(coord_a[0] - coord_b[0], 2) + math.pow(coord_a[1] - coord_b[1], 2))


def swap_cities(road_map, index1, index2):
    """
    Take the city at location `index` in the `road_map`, and the 
    city at location `index2`, swap their positions in the `road_map`, 
    compute the new total distance, and return the tuple 

        (new_road_map, new_total_distance)

    Allow for the possibility that `index1=index2`,
    and handle this case correctly.
    """



def shift_cities(road_map):
    """
    For every index i in the `road_map`, the city at the position i moves
    to the position i+1. The city at the last position moves to the position
    0. Return the new road map.
    """
    pass

def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    pass

def print_map(road_map):
    """
    Prints, in an easily understandable format, the cities and 
    their connections, along with the cost for each connection 
    and the total cost.
    """
    pass

def main():
    """
    Reads in, and prints out, the city data, then creates the "best"
    cycle and prints it out.
    """
    pass

if __name__ == "__main__": #keep this in
    main()
