from curve import *
from vehicle import *
from road import *
from simulation import *
from window import *
from vehicle_generator import *
from traffic_signal import *

sim = Simulation()

# Add multiple roads

# ---- ESTACIONAMIENTO ARENA BORREGOS ----
INICIO = ((0, 0), (21.7461, -26.9761))
ENTRADA_BORREGOS = ((21.7461, -26.9761), (31.8606, -26.9761))
INTERSECCION_1L = ((31.8606, -26.9761), (31.8606, -17.9761))
INTERSECCION_2L = ((31.8606, -17.9761), (31.8606, -2.842))
INTERSECCION_3L = ((31.8606, -2.842), (31.8606, 15.1221))
INTERSECCION_4L = ((31.8606, 15.1221), (31.8606, 29.6307))
INTERSECCION_1C = ((31.8606, -17.9761), (71.7077, -17.9761))
INTERSECCION_2C = ((31.8606, -2.842), (71.7077, -2.842))
INTERSECCION_3C = ((31.8606, 15.1221), (71.7077, 15.1221))
INTERSECCION_4C = ((31.8606, 29.6307), (71.7077, 29.6307))
INTERSECCION_1R = ((71.7077, 29.6307), (71.7077, 15.1221))
INTERSECCION_2R = ((71.7077, 15.1221), (71.7077, -2.842))
INTERSECCION_3R = ((71.7077, -2.842), (71.7077, -17.9761))
INTERSECCION_4R = ((71.7077, -17.9761), (71.7077, -26.9761))
INTERSECCION_0C = ((71.7077, -26.9761), (36.78, -26.9761))
SALIDA_BORREGOS_1 = ((36.78, -26.9761), (25.9072, -35.8534))
SALIDA_BORREGOS_2 = ((25.9072, -35.8534), (7.8019, -30.3946))
SALIDA = ((7.8019, -30.3946), (-12.2373, -16.9461))
sim.create_roads([
    INICIO,  # 0
    ENTRADA_BORREGOS,  # 1
    INTERSECCION_1L,  # 2
    INTERSECCION_2L,  # 3
    INTERSECCION_3L,  # 4
    INTERSECCION_4L,  # 5
    INTERSECCION_1C,  # 6
    INTERSECCION_2C,  # 7
    INTERSECCION_3C,  # 8
    INTERSECCION_4C,  # 9
    INTERSECCION_1R,  # 10
    INTERSECCION_2R,  # 11
    INTERSECCION_3R,  # 12
    INTERSECCION_4R,  # 13
    INTERSECCION_0C,  # 14
    SALIDA_BORREGOS_1,  # 15
    SALIDA_BORREGOS_2,  # 16
    SALIDA  # 17
])

# ---- ESTACIONAMIENTO MEDIO ----
ENTRADA_EST_MEDIO = ((31.8606, -26.9761), (25.7451, -42.7844))
EST_MEDIO_B = ((-19.9238, -39.1975), (25.7451, -42.7844))
EST_MEDIO_L1 = ((-31.9968, -57.6005), (-17.9238, -39.1975))
EST_MEDIO_R1 = ((25.7451, -42.7844), (18.7474, -60.7765))
EST_MEDIO_INTERSECCION1 = ((18.7474, -60.7765), (-31.9968, -57.6005))
EST_MEDIO_L2 = ((-46.1621, -76.3309), (-31.9968, -57.6005))
EST_MEDIO_R2 = ((18.7474, -60.7765), (14.8199, -79.5145))
EST_MEDIO_INTERSECCION2 = ((14.8199, -79.5145), (-46.1621, -76.3309))
EST_MEDIO_L3 = ((-59.7169, -94.2937), (-46.1621, -76.3309))
EST_MEDIO_R3 = ((14.8199, -79.5145), (13.4589, -98.2519))
EST_MEDIO_INTERSECCION3 = ((13.4589, -98.2519), (-59.7169, -94.2937))
EST_MEDIO_L4 = ((-73.6444, -112.51092), (-59.7169, -94.2937))
EST_MEDIO_R4 = ((13.4589, -98.2519), (12.0715, -117.39122))
EST_MEDIO_INTERSECCION4 = ((12.0715, -117.39122), (-73.6444, -112.51092))
EST_MEDIO_L5 = ((-80.1746, -131.3942), (-73.6444, -112.51092))
EST_MEDIO_R5 = ((12.0715, -117.39122), (10.6169, -135.9693))
EST_MEDIO_INTERSECCION5 = ((10.6169, -135.9693), (-80.1746, -131.3942))
EST_MEDIO_L6 = ((-81.5118, -150.2121), (-80.1746, -131.3942))
EST_MEDIO_R6 = ((10.6169, -135.9693), (7.59559, -155.39970))
EST_MEDIO_INTERSECCION6 = ((7.59559, -155.39970), (-81.5118, -150.2121))
EST_MEDIO_R7 = ((7.59559, -155.39970), (9.3492, -153.5104))
EST_MEDIO_L7 = ((-82.8175, -168.5878), (-81.5118, -150.2121))
EST_MEDIO_R8 = ((9.3492, -153.5104), (-8.7637, -173.0237))
EST_MEDIO_T = ((-8.7637, -173.0237), (-82.8175, -168.5878))
# ---- CAJONES:ESTACIONAMIENTO MEDIO ----
coordX1=0
coordX2=0
coordY1=0
coordY2=0
cajon_EST_MEDIO=[]
for x in range(354):
    if (x<=11):
        if(x==0):
            coordX1=-12.3963
            coordX2=-12.5427
            coordY1=-39.9349
            coordY2=-33.7938
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        coordX1=coordX1+2.7967
        coordX2=coordX2+2.7967
        coordY1=coordY1-0.1564
        coordY2=coordY2-0.1564
    if( x>=12 and x<=22):
        if(x==12):
            coordY1= -33.7938 - 6.1411
            coordY2= -39.9349 - 6.1411
            coordX1= -12.3963
            coordX2= -12.5427
        coordX1=coordX1+2.7967
        coordX2=coordX2+2.7967
        coordY1=coordY1-0.1564
        coordY2=coordY2-0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=23 and x<=35):
        if(x==23):
            coordY1= -59.6201
            coordY2= -46.076 - 6.1411
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=36 and x<=51 ):
        if(x==36):
            coordY1= -60.7765 - 6.1411
            coordY2= -52.2171 - 6.1411
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=52 and x<=67):
        if(x==52):
            coordY1= -79.5145 
            coordY2= -73.3734
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=68 and x<=88):
        if(x==68):
            coordY1= -79.5145 
            coordY2= -85.6556
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=89 and x<=109):
        if(x==89):
            coordY1= -98.2519
            coordY2= -92.1108
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=110 and x<=134):
        if(x==110):
            coordY1= -98.2519
            coordY2= -104.393
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=135 and x<=159):
        if(x==135):
            coordY1= -117.39122
            coordY2= -111.25012
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=160 and x<=188):
        if(x==160):
            coordY1= -117.39122
            coordY2= -123.53232
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=189 and x<=217):
        if(x==189):
            coordY1= -135.9693
            coordY2= -129.8282
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=218 and x<=248):
        if(x==218):
            coordY1= -135.9693
            coordY2= -142.1104
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=249 and x<=279):
        if(x==249):
            coordY1= -155.39970
            coordY2= -149.2586
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=280 and x<=305):
        if(x==280):
            coordY1= -155.39970
            coordY2= -161.5408
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=306 and x<=331):
        if(x==306):
            coordY1= -173.0237
            coordY2= -166.8826
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=332 and x<=354):
        if(x==332):
            coordY1= -173.0237
            coordY2= -179.1648
            coordX1= 15.5707
            coordX2= 15.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))


    
EST_MEDIO_CAJONES=tuple(cajon_EST_MEDIO)
print(EST_MEDIO_CAJONES)
sim.create_roads([
    ENTRADA_EST_MEDIO,  # 18
    EST_MEDIO_B,  # 19
    EST_MEDIO_L1,  # 20
    EST_MEDIO_R1,  # 21
    EST_MEDIO_INTERSECCION1,  # 22
    EST_MEDIO_L2,  # 23
    EST_MEDIO_R2,  # 24
    EST_MEDIO_INTERSECCION2,  # 25
    EST_MEDIO_L3,  # 26
    EST_MEDIO_R3,  # 27
    EST_MEDIO_INTERSECCION3,  # 28
    EST_MEDIO_L4,  # 29
    EST_MEDIO_R4,  # 30
    EST_MEDIO_INTERSECCION4,  # 31
    EST_MEDIO_L5,  # 32
    EST_MEDIO_R5,  # 33
    EST_MEDIO_INTERSECCION5,  # 34
    EST_MEDIO_L6,  # 35
    EST_MEDIO_R6,  # 36
    EST_MEDIO_INTERSECCION6,  # 37
    EST_MEDIO_R7,  # 38
    EST_MEDIO_L7,  # 39
    EST_MEDIO_R8,  # 40
    EST_MEDIO_T,  # 41
   
])

# ---- ESTACIONAMIENTO NUEVO ----
# VERTICALES DERECHA
v1_1 = (-8.7637, -173.0237)
v1_2 = (-28.96, -196.92)
v2_1 = (-28.96, -196.92)
v2_2 = (-40.82, -208.18)
v3_1 = (-40.82, -208.18)
v3_2 = (-46.08, -212.96)
v4_1 = (-46.08, -212.96)
v4_2 = (-55.18, -221.65)
v5_1 = (-55.18, -221.65)
v5_2 = (-67.29, -250.20)
v6_1 = (-67.29, -250.20)
v6_2 = (-68, -268.79)
v7_1 = (-68, -268.79)
v7_2 = (-68.69, -285.74)

# VERTICALES IZQUIERDA
v8_1 = (-151.02, -282.50)
v8_2 = (-156.64, -276.12)
v9_1 = (-156.64, -276.12)
v9_2 = (-152.39, -265.03)
v10_1 = (-152.39, -265.03)
v10_2 = (-136.68, -246.70)
v11_1 = (-136.68, -246.70)
v11_2 = (-113.92, -218.92)
v12_1 = (-113.92, -218.92)
v12_2 = (-108.55, -208.87)
v13_1 = (-108.55, -208.87)
v13_2 = (-104.71, -203.76)
v14_1 = (-104.71, -203.76)
v14_2 = (-93.25, -191.87)
v15_1 = (-93.25, -191.87)
v15_2 = (-82.8175, -168.5878)

# HORIZONTALES
h1_1 = (-28.96, -196.92)
h1_2 = (-93.25, -191.87)
h2_1 = (-40.82, -208.18)
h2_2 = (-104.71, -203.76)
h3_1 = (-46.08, -212.96)
h3_2 = (-114.2530, -208.69)
h4_1 = (-55.18, -221.65)
h4_2 = (-113.92, -218.92)
h5_1 = (-67.29, -250.20)
h5_2 = (-136.68, -246.70)
h6_1 = (-67.99, -268.79)
h6_2 = (-152.39, -265.03)
h7_1 = (-68.69, -285.74)
h7_2 = (-151.02, -282.50)

# SALIDA
s1_1 = (-113.92, -218.92)
s1_2 = (-114.2530, -209.69)
s2_1 = (-67.29, -250.20)
s2_2 = (-49.6102, -249.6164)

# ENTRADA
e1_1 = (-130.31, -178.62)
e1_2 = (-111.90, -193.64)
e2_1 = (-111.90, -193.64)
e2_2 = (-104.71, -203.76)
e3_1 = (-111.90, -193.64)
e3_2 = (-93.25, -191.87)

NUEVO_VERTICAL_1 = (v1_1, v1_2)
NUEVO_VERTICAL_2 = (v2_1, v2_2)
NUEVO_VERTICAL_3 = (v3_1, v3_2)
NUEVO_VERTICAL_4 = (v4_1, v4_2)
NUEVO_VERTICAL_5 = (v5_1, v5_2)
NUEVO_VERTICAL_6 = (v6_1, v6_2)
NUEVO_VERTICAL_7 = (v7_1, v7_2)

NUEVO_VERTICAL_8 = (v8_1, v8_2)
NUEVO_VERTICAL_9 = (v9_1, v9_2)
NUEVO_VERTICAL_10 = (v10_1, v10_2)
NUEVO_VERTICAL_11 = (v11_1, v11_2)
NUEVO_VERTICAL_12 = (v12_1, v12_2)
NUEVO_VERTICAL_13 = (v13_1, v13_2)
NUEVO_VERTICAL_14 = (v14_1, v14_2)
NUEVO_VERTICAL_15 = (v15_1, v15_2)

NUEVO_HORIZONTAL_1 = (h1_1, h1_2)
NUEVO_HORIZONTAL_2 = (h2_1, h2_2)
NUEVO_HORIZONTAL_3 = (h3_1, h3_2)
NUEVO_HORIZONTAL_4 = (h4_1, h4_2)
NUEVO_HORIZONTAL_5 = (h5_1, h5_2)
NUEVO_HORIZONTAL_6 = (h6_1, h6_2)
NUEVO_HORIZONTAL_7 = (h7_1, h7_2)

NUEVO_SALIDAS_1 = (s1_1, s1_2)
NUEVO_SALIDAS_2 = (s2_1, s2_2)
NUEVO_ENTRADA_1 = (e1_1, e1_2)
NUEVO_ENTRADA_2 = (e2_1, e2_2)
NUEVO_ENTRADA_3 = (e3_1, e3_2)

sim.create_roads([
    NUEVO_VERTICAL_1, #42
    NUEVO_VERTICAL_2, #43
    NUEVO_VERTICAL_3, #44
    NUEVO_VERTICAL_4, #45
    NUEVO_VERTICAL_5, #46
    NUEVO_VERTICAL_6, #47
    NUEVO_VERTICAL_7, #48
    NUEVO_VERTICAL_8, #49
    NUEVO_VERTICAL_9, #50
    NUEVO_VERTICAL_10,#51
    NUEVO_VERTICAL_11,#52
    NUEVO_VERTICAL_12,#53
    NUEVO_VERTICAL_13,#54
    NUEVO_VERTICAL_14,#55
    NUEVO_VERTICAL_15,#56
    NUEVO_HORIZONTAL_1,#57
    NUEVO_HORIZONTAL_2,#58
    NUEVO_HORIZONTAL_3,#59
    NUEVO_HORIZONTAL_4,#60
    NUEVO_HORIZONTAL_5,#61
    NUEVO_HORIZONTAL_6,#62
    NUEVO_HORIZONTAL_7,#63
    NUEVO_SALIDAS_1,#64
    NUEVO_SALIDAS_2,#65
    NUEVO_ENTRADA_1,#66
    NUEVO_ENTRADA_2,#67
    NUEVO_ENTRADA_3#68
])



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
    r0_1, #69
    r1_2, #70
    r2_3, #71
    r2_13, #72
    r3_4, #73
    r3_12, #74
    r4_5, #75
    r4_11, #76
    r5_6, #77
    r5_10, #78
    r6_7, #79
    r6_9, #80
    r7_8, #81
    r8_9_1, #82
    r8_9_2, #83
    r9_10, #84
    r10_11, #85
    r11_12, #86
    r12_14, #87
    r13_14, #88
    r14_15_1, #89
    r14_15_2, #90
    r15_16, #91
    r15_17, #92
    r16_17, #93
    r17_18, #94
    r18_19, #95
    r19_20 #96
])

sim.create_roads([

    #Cajones Javier

    EST_MEDIO_CAJONES[0], #97
    EST_MEDIO_CAJONES[1], #98
    EST_MEDIO_CAJONES[2], #99
    EST_MEDIO_CAJONES[3], #100
    EST_MEDIO_CAJONES[4], #101
    EST_MEDIO_CAJONES[5], #102
    EST_MEDIO_CAJONES[6], #103
    EST_MEDIO_CAJONES[7], #104
    EST_MEDIO_CAJONES[8], #105
    EST_MEDIO_CAJONES[9], #106
    EST_MEDIO_CAJONES[10], #107
    EST_MEDIO_CAJONES[11], #108
    EST_MEDIO_CAJONES[12], #109
    EST_MEDIO_CAJONES[13], #110
    EST_MEDIO_CAJONES[14], #111
    EST_MEDIO_CAJONES[15], #112
    EST_MEDIO_CAJONES[16], #113
    EST_MEDIO_CAJONES[17], #114
    EST_MEDIO_CAJONES[18], #115
    EST_MEDIO_CAJONES[19], #116
    EST_MEDIO_CAJONES[20], #117
    EST_MEDIO_CAJONES[21], #118
    EST_MEDIO_CAJONES[22], #119
    EST_MEDIO_CAJONES[23], #120

    #Julian

    #Santiago

    #Gustavo
])



# Paths
path = [
[1, {"path": [0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17]}],#1
[1, {"path": [0, 1, 2, 6, 13, 14, 15, 16, 17]}],#2
[1, {"path": [0, 1, 2, 3, 7, 12, 13, 14, 15, 16, 17]}],#3
[1, {"path": [0, 1, 2, 3, 4, 8, 11, 12, 13, 14, 15, 16, 17]}],#4
[1, {"path": [0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17]}],#5
[1, {"path": [0, 1, 18, 21, 24, 27, 30, 33, 36, 38, 40, 41, 39, 35, 32, 29, 26, 23, 20, 19, 52]}],#6
[1, {"path": [0, 1, 18, 21, 22, 20, 19, 42]}],#7
[1, {"path": [0, 1, 18, 21, 24, 25, 23, 20, 19, 43]}],#8
[1, {"path": [0, 1, 18, 21, 24, 27, 28, 26, 23, 20, 19, 44]}],#9
[1, {"path": [0, 1, 18, 21, 24, 27, 30, 31, 29, 26, 23, 20, 19, 45]}],#10
[1, {"path": [0, 1, 18, 21, 24, 27, 30, 33, 34, 32, 31, 29, 26, 23, 20, 19, 46]}],#11
[1, {"path": [0, 1, 18, 21, 24, 27, 30, 33, 36, 37, 35, 32, 31, 29, 26, 23, 20, 19, 47]}],#12
]
sim.create_gen({
    'vehicle_rate': 10,
    'vehicles': path
})

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)

