import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from PIL import Image

def distance(city1, city2):
    return np.linalg.norm(np.array(city1) - np.array(city2))

def nearest_neighbor_algorithm(cities):
    n = len(cities)
    unvisited_cities = set(range(1, n))
    current_city = 0
    tour = [current_city]

    while unvisited_cities:
        nearest_city = min(unvisited_cities, key=lambda city: distance(cities[current_city], cities[city]))
        tour.append(nearest_city)
        unvisited_cities.remove(nearest_city)
        current_city = nearest_city

    tour.append(tour[0])

    return tour

def plot_tsp_animation(cities_coordinates, map_path):
    fig, ax = plt.subplots(figsize=(10, 8))
    ax.set_title('TSP Optimization - Nearest Neighbor Algorithm')

    # Load India map image
    india_map = Image.open(map_path)
    india_extent = [0, india_map.width, 0, india_map.height]
    ax.imshow(india_map, extent=india_extent, alpha=0.5)

    city_names = [
        'Delhi',
        'Mumbai',
        'Bangalore',
        'Kolkata',
        'Jodhpur',
        'Rameswaram',
        'Pune',
        'Varanasi',
        'Hyderabad',
        'Visakhapatnam'
    ]

    def update(frame):
        ax.clear()
        ax.set_title(f"India: {frame + 1} City's")

        current_tour = nearest_neighbor_algorithm(cities_coordinates[:frame + 2])

        # Plot India map image
        ax.imshow(india_map, extent=india_extent, alpha=0.5)

        # Plot cities
        cities_x, cities_y = zip(*cities_coordinates)
        ax.scatter(cities_x, cities_y, color='red', label='Cities')

        # Plot tour
        tour_x = [cities_coordinates[i][0] for i in current_tour]
        tour_y = [cities_coordinates[i][1] for i in current_tour]
        ax.plot(tour_x, tour_y, linestyle='-', marker='o', color='blue', label='Current Tour')

        # Display city names next to their markers
        for i, (x, y) in enumerate(cities_coordinates):
            ax.text(x, y, city_names[i], fontsize=8, ha='center', va='center')

        ax.legend()

    ani = FuncAnimation(fig, update, frames=len(cities_coordinates)-1, repeat=False, interval=1000)
    plt.show()

# Example usage
if __name__ == "__main__":
    # Coordinates of cities in India
    cities_coordinates = [
        (703.6, 1979.5),  # Delhi
        (355.4, 1193.0),  # Mumbai
        (719.4, 676.5),  # Bangalore
        (1556.0, 1497.4),  # Kolkata
        (393.2, 1790.6),  # Jodhpur
        (851.8, 365.1),  # Rameswaram
        (429.4, 1147.3),  # Pune
        (1138.0, 1705.4),   # Varanasi
        (786.0, 1034.0),   # Hyderabad
        (1166.3, 1072.4),   # Visakhapatnam
    ]

    # Local path to the map image (replace with the actual path)
    india_map_path = r'C:\Users\91876\Desktop\CODING\Python\Discrite Mathem,atics PROJECT\India_Map.jpg'

    # Define city names
    city_names = [
        'Delhi',
        'Mumbai',
        'Bangalore',
        'Kolkata',
        'Jodhpur',
        'Rameswaram',
        'Pune',
        'Varanasi',
        'Hyderabad',
        'Visakhapatnam'
    ]

    plot_tsp_animation(cities_coordinates, india_map_path)

    # Find the optimized tour using the Nearest Neighbor Algorithm
    optimized_tour_indices = nearest_neighbor_algorithm(cities_coordinates)

    # Map indices to city names
    optimized_tour = [city_names[i] for i in optimized_tour_indices]

    # Print the optimized tour
    print("Optimized Tour:", optimized_tour)
