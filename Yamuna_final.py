import heapq

def dijkstra(graph, start):
    distances = {vertex: float('inf') for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    previous_vertices = {vertex: None for vertex in graph}
    
    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)
        if current_distance > distances[current_vertex]:
            continue
        
        for neighbor, (distance_weight, population_weight) in graph[current_vertex].items():
            distance = distance_weight
            population = population_weight
            #print(neighbor)
            #combined_weight = distance + distances[current_vertex]
            combined_weight = ((distance*weights['distance']) + (population*weights['population']) + distances[current_vertex])

            
            if combined_weight < distances[neighbor]:
                distances[neighbor] = combined_weight
                heapq.heappush(priority_queue, (combined_weight, neighbor))
                previous_vertices[neighbor] = current_vertex
    
    return previous_vertices, distances

def get_shortest_path(previous_vertices, target):
    path = []
    while target is not None:
        path.insert(0, target)
        target = previous_vertices[target]
    return path

def find_shortest_path(graph, start_node, end_node):
    previous_vertices, distances = dijkstra(graph, start_node)
    shortest_path = get_shortest_path(previous_vertices, end_node)
    shortest_distance = distances[end_node]
    
    population_sum = 0
    for i in range(len(shortest_path) - 1):
        current_node = shortest_path[i]
        next_node = shortest_path[i + 1]
        _, population_weight = graph[current_node][next_node]
        population_sum += population_weight
    
    return shortest_path, shortest_distance, population_sum

graph = {
    1: {2: (283.22, 0)},
    2: {1: (283.22, 0), 4: (385.25, 0.1), 26: (288.13, 0.1)},
    3: {26: (106.19, 0.3)},
    4: {2: (385.25, 0.1)},
    5: {26: (176.46, 0.4)},
    6: {25: (544.34, 0.1), 26: (453.97, 0.1)},
    7: {27: (149.62, 0.6)},
    8: {38: (52.42, 0.1)},
    9: {45: (75, 0.6)},
    10: {45: (73.46, 0)},
    11: {36: (321.92, 0)},
    12: {35: (436.32, 1)},
    13: {34: (534.22, 0.8)},
    14: {34: (351.10, 0.8)},
    15: {33: (151.38, 0)},
    16: {30: (672.11, 0)},
    17: {32: (191, 0.2), 33: (210.43, 0.2)},
    18: {39: (403, 0)},
    19: {41: (82.16, 0.5)},
    20: {41: (110, 0.5)},
    21: {44: (66.80, 0)},
    22: {44: (217.50, 0)},
    23: {29: (306.50, 0)},
    24: {28: (96.30, 0)},
    25: {6: (544.34, 0.1), 27: (413.08, 0), 28: (126.30, 0), 44: (440, 0)},
    26: {2: (288.13, 0.1), 5: (176.46, 0.4), 6: (453.97, 0.1), 3: (106.19, 0.3)},
    27: {7: (149.62, 0.6), 25: (413.08, 0), 38: (270.54, 0)},
    28: {24: (96.30, 0), 25: (126.30, 0), 29: (136.50, 0)},
    29: {23: (306.50, 0), 28: (136.50, 0), 43: (417.67, 1), 42: (250, 0)},
    30: {16: (672.11, 0), 43: (96.10, 1)},
    31: {33: (450, 1), 32: (137.92, 1), 35: (202.67, 1)},
    32: {17: (191, 0.2), 31: (137.92, 1), 33: (450, 0), 34: (221.82, 0.8), 40: (925.30, 1)},
    33: {15: (151.38, 0), 17: (210.43, 0.2), 32: (450, 0), 39: (450, 1)},
    34: {14: (351.10, 0.8), 13: (534.22, 0.8), 32: (221.82, 0.8)},
    35: {12: (436.32, 1), 31: (202.67, 1), 36: (383.56, 1)},
    36: {11: (321.92, 0), 35: (383.56, 1), 37: (172.68, 0)},
    37: {36: (230.47, 0), 45: (210.61, 0)},
    38: {8: (52.42, 0.1), 27: (270.54, 0), 45: (188.75, 0)},
    39: {18: (403, 0), 40: (231.81, 0), 33: (450, 1)},
    40: {41: (216, 0.5), 42: (360, 1), 32: (925.30, 1), 39 :(231.81, 0)},
    41: {19: (82.16, 0.5), 20: (110, 0.5), 40: (216, 0.5)},
    42: {29: (250, 0), 40: (360, 1), 44: (138.6, 0)},
    43: {30: (96.10, 1), 29: (417.67, 1)},
    44: {21: (66.80, 0), 22: (217.50, 0), 25: (440, 0), 42: (138.6, 0)},
    45: {37: (210.61, 0), 38: (188.75, 0), 9: (75, 0.6), 10: (73.46, 0)}
}

start_node = 2
end_nodes = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45]
weights = {'distance': 0.7, 'population': 0.3}
print(weights['distance'])
print(weights['population'])

for end_node in end_nodes:
    shortest_path, shortest_distance, population_sum = find_shortest_path(graph, start_node, end_node)
    print(f"Shortest path from {start_node} to {end_node}: {shortest_path}")
    print(f"Total distance: {shortest_distance:.2f}")
    print(f"Total population sum: {population_sum:.2f}")
    print()
