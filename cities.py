import copy
import math
import random


def read_cities(file_name):
    with open(file_name) as road_map:
        road_map = [tuple(element.rstrip().split("\t")) for element in road_map]
        return road_map


def print_cities(road_map):
    header = f'{"City":^15}|{"State":^15}|{"Latitude":^15}|{"Longitude":^15}'

    print(f'{"-" * len(header)}')
    print(f'{header}')
    print(f'{"-" * len(header)}')
    for item in road_map:
        print(f'{item[1]:<15} {item[0]:<15} {item[2][:5]:^15} {item[3][:6]:^15}')


def compute_total_distance(road_map):
    distance = 0
    count = 1

    for city in road_map:
        lat1 = float(city[2])
        long1 = float(city[3])
        if city != road_map[-1]:
            lat2 = float(road_map[count][2])
            long2 = float(road_map[count][3])
        else:
            lat2 = float(road_map[0][2])
            long2 = float(road_map[0][3])
        distance = distance + math.sqrt(math.pow((lat1 - lat2), 2) + math.pow((long1 - long2), 2))
        count += 1

    return distance


def swap_cities(road_map, index1, index2):
    new_road_map = copy.deepcopy(road_map)
    new_road_map[index1], new_road_map[index2] = new_road_map[index2], new_road_map[index1]
    return new_road_map, compute_total_distance(new_road_map)


def shift_cities(road_map):
    new_road_map = copy.deepcopy(road_map)
    last_element = new_road_map.pop()
    new_road_map.insert(0, last_element)

    return new_road_map


def find_best_cycle(road_map):
    """
    Using a combination of `swap_cities` and `shift_cities`, 
    try `10000` swaps/shifts, and each time keep the best cycle found so far. 
    After `10000` swaps/shifts, return the best cycle found so far.
    Use randomly generated indices for swapping.
    """
    best_cycle = road_map, compute_total_distance(road_map)

    for i in range(10000):
        random_value1 = random.randint(0, len(road_map)-1)
        random_value2 = random.randint(0, len(road_map)-1)

        new_map = shift_cities(best_cycle[0])
        new_map = swap_cities(new_map, random_value1, random_value2)

        if new_map[1] < best_cycle[1]:
            best_cycle = new_map

    return best_cycle


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
    find_best_cycle(read_cities('city-data.txt'))

if __name__ == "__main__":  # keep this in
    main()
