
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

g0 = (-49.6102, -249.6164) #0
g1 = (-35.1760, -249.6164) #1
g2 = (-56.5573, -299.9513) #2
g3 = (-62.4260, -313.7672) #3
g4 = (-70.5566, -329.3894) #4
g5 = (-76.4545, -344.1823) #5
g6 = (-83.3353, -358.5668) #6
g7 = (-89.1963, -373.6187) #7
g8 = (-195.9880, -368.1862) #8
g9 = (-188.5682, -353.0461) #9
g10 = (-178.1299, -339.3147) #10
g11 = (-166.1706, -323.7149) #11
g12 = (-153.1128, -307.1783) #12
g13 = (-65.7410, -296.0271) #13
g14 = (-150.8308, -293.1035) #14
g15 = (-167.4109, -288.0571) #15
g16 = (-191.0185, -287.0861) #16
g17 = (-172.8859, -262.5026) #17
g18 = (-128.9339, -209.0373) #18
g19 = (-114.2530, -209.0373) #19
g20 = (-139.4951, -188.8469) #20
g14_15 = (-156.8524, -288.5490) # 14-15
g8_9 = (-194.6809, -361.2315) #8-9

r0_1 = (g0, g1)
r1_2 = (g1, g2)
r2_3 = (g2, g3)
r2_13 = (g2, g13)
r3_4 = (g3, g4)
r3_12 = (g3, g12)
r4_5 = (g4, g5)
r4_11 = (g4, g11)
r5_6 = (g5, g6)
r5_10 = (g5, g10)
r6_7 = (g6, g7)
r6_9 = (g6, g9)
r7_8 = (g7, g8)
r8_9_1 = (g8, g8_9)
r8_9_2 = (g8_9, g9)
r9_10 = (g9, g10)
r10_11 = (g10, g11)
r11_12 = (g11, g12)
r12_14 = (g12, g14)
r13_14 = (g13, g14)
r14_15_1 = (g14, g14_15)
r14_15_2 = (g14_15, g15)
r15_16 = (g15, g16)
r15_17 = (g15, g17)
r16_17 = (g16, g17)
r17_18 = (g17, g18)
r18_19 = (g18, g19)
r19_20 = (g19, g20)




sim.create_roads([
 r0_1,
 r1_2,
 r2_3,
 r2_13,
 r3_4,
 r3_12,
 r4_5,
 r4_11,
 r5_6,
 r5_10,
 r6_7,
 r6_9,
 r7_8,
 r8_9_1,
 r8_9_2,
 r9_10,
 r10_11,
 r11_12,
 r12_14,
 r13_14,
 r14_15_1,
 r14_15_2,
 r15_16,
 r15_17,
 r16_17,
 r17_18,
 r18_19,
 r19_20
 ])

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
