
from curve import *
from vehicle import *
from road import *
from simulation import *
from window import *
from vehicle_generator import *
from traffic_signal import *

sim = Simulation()

# # Add multiple roads

## ---- ESTACIONAMIENTO ARENA BORREGOS ----
sim.create_roads([
    ((0,0),(20,-20)), #Entrada                                                 0
    ((20,-20),(40,-20)), #Inicio de estacionamiento staff                      1
    ((40,-20),(40,0)), #Lineas de la izquierda ((40,-20),(40,80))              2
    ((40,0),(40,20)), #Inter 1                                                 3
    ((40,20),(40,40)), #Inter 2                                                4
    ((40,40),(40,60)), #Inter 3                                                5
    ((40,60),(40,80)), #Inter 4                                                6
    ((40,20),(120,20)), #Espacio est 1                                         7
    ((40,40),(120,40)), #                                                      8
    ((40,60),(120,60)), #                                                      9                 
    ((40,80),(120,80)), #linea de abajo                                        10
    ((120,80),(120,60)), #Lineas de la derecha                                 11
    ((120,60),(120,40)), #Inters derecha                                       12
    ((120,40),(120,20)), #                                                     13
    ((120,20),(120,0)), #                                                      14
    ((120,0),(120,-20)), #                                                     15
    ((120,-20),(40,-24)), #                                                    16
    ((40,-24),(20,-24)), #Final es                                             17
    ((20,-24),(0,-10)) #Salida                                                 18
])

## ---- ESTACIONAMIENTO MEDIO ----
# sim.create_roads([

# ])

## ---- ESTACIONAMIENTO NUEVO ----
# sim.create_roads([

# ])

## ---- ESTACIONAMIENTO TERRACERIA ----
# sim.create_roads([

# ])

sim.create_gen({
    'vehicle_rate': 60,
    'vehicles': [
        [1, {"path": [0,1,2,3,4,5,6,10,11,12,13,14,15,16,17,18]}],
        [0, {"path": [0,1,2,3,7,14,15,16,17,18]}],
        [0, {"path": [0,1,2,3,4,8,13,14,15,16,17,18]}],
        [0, {"path": [0,1,2,3,4,5,9,12,13,14,15,16,17,18]}],
    ]
})

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)
