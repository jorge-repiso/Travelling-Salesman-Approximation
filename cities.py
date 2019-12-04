def read_cities(file_name):
    with open(file_name) as road_map:
        road_map = [tuple(element.rstrip().split("\t")) for element in road_map]
        print(road_map)
        return road_map

read_cities('city-data.txt')
def print_cities(road_map):

    for item in road_map:
        subindex_a = item[2].find(".") + 3
        subindex_b = item[3].find(".") + 3
        print(item[0], item[1], item[2][:subindex_a], item[3][:subindex_b])


def compute_total_distance(road_map):

    from math import sqrt
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
        distance = distance + sqrt(((p1-q1) ** 2) + ((p2-q2) ** 2))
        count += 1

    print(distance)
    return(distance)


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
