import numpy as np  # importing numpy package
import random  # importing random numbers package
import matplotlib.pyplot as plt  # importing matplotlib package


class Car:  # creating a car class to create car objects
    def __init__(self, initial_position):  # initialising car objects with initial position
        self.position = [initial_position]

    def update(self, new_position):  # method to update position list of a car object
        self.position.append(new_position)


class Road:  # creating road class to create road objects
    # initialising road data like positions of cars and length of road
    def __init__(self, length, density):
        self.road = []  # road list
        self.cars = []  # list of car objects
        for i in range(length):  # loop to decide the positions of cars based on density
            if random.random() <= density:
                self.road.append(1)
                self.cars.append(Car(i))
            else:
                self.road.append(0)

    def iteration(self):  # method to iterate the road object once
        for i in self.cars:
            if i.position[-1] == len(self.road) - 1:
                post = 0  # next index the given car if it is at the end of the road
            else:
                # next index the given car if it is anywhere other than the end of the road
                post = i.position[-1] + 1
            if self.road[post] == 0:
                self.road[i.position[-1]] = 0
                self.road[post] = 1
                i.update(post)
            else:
                i.update(i.position[-1])

    def avg_speed(self):  # method to return average speed of the latest iteration
        if len(self.cars) == 0:  # condition if there are no cars on the road
            return 0
        else:
            moving_cars = 0
            for i in self.cars:  # loop to check how many cars have moved
                if i.position[-1] != i.position[-2]:
                    moving_cars += 1
            else:
                return moving_cars/len(self.cars)  # returning average speed


def main():  # main method
    length = int(input("Length of road: "))
    timestep = int(input("Number of iterations: "))
    density = float(input("Car Density: "))
    main_road = Road(length, density)
    time_count = [0]  # list of timestep points for plotting graphs

    # loop to iterate road the specified number of times and print average speed at each timestep
    for i in range(timestep):
        main_road.iteration()
        print("Avg speed at timestep " + str(i + 1) +
              ": " + str(main_road.avg_speed()))
        time_count.append(i + 1)

    plt.figure(1)  # plot of car position vs timestep
    plt.title("Position vs Time")
    plt.xlabel("Time")
    plt.ylabel("Position")
    for i in main_road.cars:  # loop to populate the first figure
        plt.plot(time_count, i.position)

    # creating lost of car densities to check
    car_densities = np.linspace(
        0, 1, int(input("Number of car densities to check between 0 and 1: ")))
    steady_speeds = []  # list of steady speeds for each car density

    for i in range(len(car_densities)):  # loop to find steady speed for each car density
        # creating temporary road object
        temp_road = Road(length, car_densities[i])
        avg_speed = 0  # initialising average speed variable
        while True:  # loop to check for steady speed
            for j in range(100):  # loop to iterate road a given number of times
                temp_road.iteration()
            if avg_speed == temp_road.avg_speed():
                break
            else:
                avg_speed = temp_road.avg_speed()
        steady_speeds.append(avg_speed)  # appending to steady speed list

    plt.figure(2)  # plot of steady speeds vs car densities
    plt.title("Steady Speed vs Car Density")
    plt.xlabel("Car Density")
    plt.ylabel("Steady Speed")
    plt.plot(car_densities, steady_speeds)
    plt.show()  # displaying graphs


main()  # calling the main function
