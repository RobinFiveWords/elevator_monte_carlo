## Monte Carlo simulation of stops made by an elevator

You have hundreds of people waiting to board an elevator to various floors in a hotel at the same time. The one constraint you can control is how many stops the elevator makes on each trip.

### Assumptions in these files
* Each passenger is randomly assigned to a floor, with equal likelihood for each floor.
* Passengers are selected with replacement; this slightly underestimates the number of stops and makes the result independent of the total number of passengers (and much easier to compute).
* 10 passengers per elevator and 16 destination floors; the mean is around 7.6 stops. If there are 6 elevators -- meaning less than 3 floors per elevator -- pre-sorting will save around 5 stops per trip.