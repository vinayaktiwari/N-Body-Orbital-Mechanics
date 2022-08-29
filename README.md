# N-Body-Orbital-Mechanics
Simulation to see how various celestial bodies interact following Newtonian and Euler laws
# Problem Statement 
This assignment asks you to build a simple simulation of N-body orbital mechanics.  It might sound sophisticated, but the actual mechanics of the system should be very, very simple: 2-dimensions, and only model gravitational force between the objects. 

# Project structure
THis project has a body.py for calculating the forces between the bodies, and utilised matplotlib for 3D animation. It inputs the number of planets with a fixed mass, location and velocity and outputs a matplotlib simulation that shows the bodies interacting with each other following newton's gravitational laws.

# Setup
To run this project in your system, follow the steps below

`Step1:` `$ git clone https://github.com/vinayaktiwari/N-Body-Orbital-Mechanics.git`
`Step2:` `$ pip install -r requirements.txt`
`Step3:` `$ python3 main.py --num_planets 3`
parameter **num_bodies** takes integer value from 1 to 6
