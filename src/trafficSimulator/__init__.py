
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
INICIO = ((0,0),(21.7461,-26.9761))
ENTRADA_BORREGOS = ((21.7461,-26.9761),(31.8606,-26.9761))
INTERSECCION_1L = ((31.8606,-26.9761),(31.8606,-17.9761))
INTERSECCION_2L = ((31.8606,-17.9761),(31.8606,-2.842))
INTERSECCION_3L = ((31.8606,-2.842),(31.8606,15.1221))
INTERSECCION_4L = ((31.8606,15.1221),(31.8606,29.6307))
INTERSECCION_1C = ((31.8606,-17.9761),(71.7077,-17.9761))
INTERSECCION_2C = ((31.8606,-2.842),(71.7077,-2.842))
INTERSECCION_3C = ((31.8606,15.1221),(71.7077,15.1221))
INTERSECCION_4C = ((31.8606,29.6307),(71.7077,29.6307))
INTERSECCION_1R = ((71.7077,29.6307),(71.7077,15.1221))
INTERSECCION_2R = ((71.7077,15.1221),(71.7077,-2.842))
INTERSECCION_3R = ((71.7077,-2.842),(71.7077,-17.9761))
INTERSECCION_4R = ((71.7077,-17.9761),(71.7077,-26.9761))
INTERSECCION_0C = ((71.7077,-26.9761),(36.78,-26.9761))
SALIDA_BORREGOS_1 = ((36.78,-26.9761),(25.9072,-35.8534))
SALIDA_BORREGOS_2 = ((25.9072,-35.8534),(7.8019,-30.3946))
SALIDA = ((7.8019,-30.3946),(-12.2373,-16.9461))
sim.create_roads([
    INICIO, #0
    ENTRADA_BORREGOS, #1
    INTERSECCION_1L, #2
    INTERSECCION_2L, #3
    INTERSECCION_3L, #4
    INTERSECCION_4L, #5
    INTERSECCION_1C, #6
    INTERSECCION_2C, #7
    INTERSECCION_3C, #8
    INTERSECCION_4C, #9
    INTERSECCION_1R, #10
    INTERSECCION_2R, #11
    INTERSECCION_3R, #12
    INTERSECCION_4R, #13
    INTERSECCION_0C, #14
    SALIDA_BORREGOS_1, #15
    SALIDA_BORREGOS_2, #16
    SALIDA #17
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
    'vehicle_rate': 30,
    'vehicles': [
        [1, {"path": [0,1,2,3,4,5,9,10,11,12,13,14,15,16,17]}],
        [1, {"path": [0,1,2,6,13,14,15,16,17]}],
        [1, {"path": [0,1,2,3,7,12,13,14,15,16,17]}],
        [1, {"path": [0,1,2,3,4,8,11,12,13,14,15,16,17]}],
        [1, {"path": [0,1,2,3,4,5,9,10,11,12,13,14,15,16,17]}],
    ]
})

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)
