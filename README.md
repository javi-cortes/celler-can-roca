<!-- ABOUT THE PROJECT -->
## About The Project
`Celler can roca` is one of the best restaurant in the world.

This script automates the booking to the waiting list of the restaurant.

Can Roca usually has the full year booked up and by the end of each month they release the following month
from the next year. So its kinda difficult to get a reservation.

This script automatically adds your reservation to the waiting list of the whole year and whenever someone cancels their
booking you'll be notified by email.

The software that can roca uses for reservation is the same for Diverxo and other famous restaurants.
This script allows you to select between can roca and diverxo but feel free to change/add more [here](https://github.com/javi-cortes/celler-can-roca/blob/f4f114b0de2b692704ccb3e5c92342cd70b475b0/can_roca.py#L36)


List of all the restaurants: https://www.covermanager.com/software-para/restaurantes

So far is booking for Thursday - Friday - Saturday (Lunch / Dinner)
(You can change this at [this line](https://github.com/javi-cortes/celler-can-roca/blob/a127515d9420b8a2050b498c4cc809135a4d4905/can_roca.py#L51))

<!-- GETTING STARTED -->
## Getting Started
***
You can use docker and/or Makefile to run the project.
### Prerequisites
In order to run the project you will need the following:
* [docker](https://docs.docker.com/engine/install/)
* [GNU Make](https://www.gnu.org/software/make/)

## How to run the script
***
1.
```
make run
```
2. Will prompt some info about your booking, name, email, etc.
