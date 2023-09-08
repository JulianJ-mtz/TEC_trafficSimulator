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
EstArenaBorregos = []

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
EstArenaBorregos = [
    INICIO,  # 0
    ENTRADA_BORREGOS,  # 1
    INTERSECCION_1R,  # 2
    INTERSECCION_2R,  # 3
    INTERSECCION_3R,  # 4
    INTERSECCION_4R,  # 5
    INTERSECCION_0C,  # 6
    SALIDA_BORREGOS_1,  # 7
    SALIDA_BORREGOS_2,  # 8
    SALIDA  # 9
]

# ---- ESTACIONAMIENTO ARENA BORREGOS ----
# Guarda los valores y para grabar donde tienen que ir las intersecciones
InterseccionesLY = [INTERSECCION_1L[0][1],INTERSECCION_2L[0][1],INTERSECCION_3L[0][1],INTERSECCION_4L[0][1],INTERSECCION_4L[1][1]]

x1 = INTERSECCION_4C[0][0]-1
y1 = INTERSECCION_4C[0][1] - 5.5434
x2 = x1 - 3.2294
y2 = 0
for i in range(11): #CAJONES LATERALES ARENA BOREGOS 10 - 20
    y2 = y1 + 3.9333
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    InterseccionesLY.append(y1)
    y1 -= 4.5262
#Añade todas las intersecciones que van a otros caminos
InterseccionesLY.sort()
for i in range(len(InterseccionesLY) - 1): #INTERSECCIONES DE LA ENTRADA AL ESTACIONAMIENTO 21 - 35
    #Utiliza los puntos del arreglo del inicio para crear caminos partidos por el mismo eje x
    EstArenaBorregos.append(((INTERSECCION_4C[0][0],InterseccionesLY[i]),(INTERSECCION_4C[0][0],InterseccionesLY[i+1])))

#cajones interseccion 4 discapacitados
Intersecciones4CX = [INTERSECCION_4C[0][0],INTERSECCION_4C[1][0]]
x1 = INTERSECCION_4C[1][0] - 6.1286 - 2.2776
y1 = INTERSECCION_4C[1][1] + 1
x2 = 0
y2 = y1 + 3.5840
for i in range(4): #CAJONES INTERSECCION 4 ABAJO DISCAPACITADOS ARENA BORREGOS 36-39
    x2 = x1 + 3.5255
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones4CX.append(x1)
    x1 -= 6

#cajones interseccion 4 arriba
x1 = INTERSECCION_4C[1][0] - 6.1286 - 2.2776
y1 = INTERSECCION_4C[1][1] - 1
x2 = 0
y2 = y1 - 3.5840
for i in range(6): #CAJONES INTERSECCION 4 ARRIBA ARENA BORREGOS 40-45
    x2 = x1 + 3.5255
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones4CX.append(x1)
    x1 -= 3.5255


#INTERSECCIONES 4C ARENA BORREGOS 46-55
Intersecciones4CX = list(set(Intersecciones4CX))#Remueve los duplicados
Intersecciones4CX.sort()
for i in range(len(Intersecciones4CX) - 1):
    #Utiliza los puntos del arreglo del inicio para crear caminos partidos por el mismo eje x
    EstArenaBorregos.append(((Intersecciones4CX[i],INTERSECCION_4C[0][1]),(Intersecciones4CX[i+1],INTERSECCION_4C[0][1])))



#CAJONES INTERSECCION 3 ABAJO 56-61
Intersecciones3CX = [INTERSECCION_3C[0][0],INTERSECCION_3C[1][0]]
x1 = INTERSECCION_3C[1][0] - 5.6570
y1 = INTERSECCION_3C[1][1] + 1
x2 = 0
y2 = y1 + 3.5840
for i in range(6):
    x2 = x1 - 3.5255
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones3CX.append(x1)
    x1 -= 3.5255


#CAJONES INTERSECCION 3 ARRIBA 62-68
x1 = INTERSECCION_3C[1][0] - 6.1297
y1 = INTERSECCION_3C[1][1] - 1
x2 = 0
y2 = y1 - 3.8068
for i in range(7):
    x2 = x1 - 3.7830
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones3CX.append(x1)
    x1 -= 4.5019

#INTERSECCIONES 3C 69 - 82
Intersecciones3CX = list(set(Intersecciones3CX))#Remueve los duplicados
Intersecciones3CX.sort(reverse=True)
for i in range(len(Intersecciones3CX) - 1):
    #Utiliza los puntos del arreglo del inicio para crear caminos partidos por el mismo eje x
    EstArenaBorregos.append(((Intersecciones3CX[i],INTERSECCION_3C[0][1]),(Intersecciones3CX[i+1],INTERSECCION_3C[0][1])))

#CAJONES INTERSECCION 2 ABAJO 83 - 89
Intersecciones2CX = [INTERSECCION_2C[0][0],INTERSECCION_2C[1][0]]
x1 = INTERSECCION_2C[1][0] - 8.8239
y1 = INTERSECCION_2C[1][1] + 1
x2 = 0
y2 = y1 + 3.8020
for i in range(7):
    x2 = x1 + 3.0133
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones2CX.append(x1)
    x1 -= 4.1806

#CAJONES INTERSECCION 2 ARRIBA 90 - 97
x1 = INTERSECCION_2C[1][0] - 6.1297
y1 = INTERSECCION_2C[1][1] - 1
x2 = 0
y2 = y1 - 3.8020
for i in range(8):
    x2 = x1 + 3.0133
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones2CX.append(x1)
    x1 -= 4.1806

#INTERSECCION 2 98 - 113
Intersecciones2CX = list(set(Intersecciones2CX))#Remueve los duplicados
Intersecciones2CX.sort()
for i in range(len(Intersecciones2CX) - 1):
    #Utiliza los puntos del arreglo del inicio para crear caminos partidos por el mismo eje x
    EstArenaBorregos.append(((Intersecciones2CX[i],INTERSECCION_2C[0][1]),(Intersecciones2CX[i+1],INTERSECCION_2C[0][1])))

#CAJONES INTERSECCION 1 ABAJO 114-120
Intersecciones1CX = [INTERSECCION_1C[0][0],INTERSECCION_1C[1][0]]
x1 = INTERSECCION_1C[1][0] - 6.1297
y1 = INTERSECCION_1C[1][1] + 1
x2 = 0
y2 = y1 + 3.8020
for i in range(7):
    x2 = x1 - 3.0133
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones1CX.append(x1)
    x1 -= 4.1806

#CAJONES INTERSECCION 1 ARRIBA 121-127
x1 = INTERSECCION_1C[1][0] - 6.1297
y1 = INTERSECCION_1C[1][1] - 1
x2 = 0
y2 = y1 - 3.8020
for i in range(7):
    x2 = x1 - 3.0133
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones1CX.append(x1)
    x1 -= 4.1806

#INTERSECCIONES 1 128 - 135
Intersecciones1CX = list(set(Intersecciones1CX))#Remueve los duplicados
Intersecciones1CX.sort(reverse=True)
for i in range(len(Intersecciones1CX) - 1):
    #Utiliza los puntos del arreglo del inicio para crear caminos partidos por el mismo eje x
    EstArenaBorregos.append(((Intersecciones1CX[i],INTERSECCION_1C[0][1]),(Intersecciones1CX[i+1],INTERSECCION_1C[0][1])))

#CAJONES INTERSECCION 0 ARRIBA 136 - 143
Intersecciones0CX = [INTERSECCION_0C[0][0]]
x1 = INTERSECCION_0C[0][0] - 2.6964
y1 = INTERSECCION_0C[0][1] - 1
x2 = 0
y2 = y1 - 3.8020
for i in range(8):
    x2 = x1 - 3.6964
    EstArenaBorregos.append(((x1,y1),(x2,y2),1))
    Intersecciones0CX.append(x1)
    x1 -= 4
Intersecciones0CX.append(INTERSECCION_0C[1][0])

#INTERSECCION 0 144 - 152
for i in range(len(Intersecciones0CX) - 1):
    #Utiliza los puntos del arreglo del inicio para crear caminos partidos por el mismo eje x
    EstArenaBorregos.append(((Intersecciones0CX[i],INTERSECCION_0C[0][1]),(Intersecciones0CX[i+1],INTERSECCION_0C[0][1])))


# ---- ESTACIONAMIENTO MEDIO ----
ENTRADA_EST_MEDIO = ((31.8606, -26.9761), (25.7451, -42.7844))
EST_MEDIO_B1 = ((-12.3963, -39.9349),(-19.9238, -39.1975))
EST_MEDIO_B2 = ((25.7451, -41.8117),(21.1641, -41.8117))
EST_MEDIO_L1 = ((-17.9238, -39.1975),(-31.9968, -57.6005))
EST_MEDIO_R1 = ((25.7451, -42.7844), (18.7474, -60.7765))
EST_MEDIO_INTERSECCION1_1 = ((18.7474, -59.7765), (12.7740, -59.6201))
EST_MEDIO_INTERSECCION1_2 = ((-29.1765, -57.1177), (-31.9968, -56.7765))
EST_MEDIO_L2 = ((-31.9968, -57.6005),(-46.1621, -76.3309))
EST_MEDIO_R2 = ((18.7474, -60.7765), (14.8199, -79.5145))
EST_MEDIO_INTERSECCION2_1 = ((14.8199, -79.5145), (15.5707, -79.5145))
EST_MEDIO_INTERSECCION2_2 = ((-43.1600, -76.2301), (-46.1621, -76.3309))
EST_MEDIO_L3 = ((-46.1621, -76.3309),(-59.7169, -94.2937))
EST_MEDIO_R3 = ((14.8199, -79.5145), (13.4589, -98.2519))
EST_MEDIO_INTERSECCION3_1 = ((13.4589, -98.2519), (11.7707, -98.2519))
EST_MEDIO_INTERSECCION3_2 = ((-58.1468, -94.3419), (-59.7169, -94.2937))
EST_MEDIO_L4 = ((-59.7169, -94.2937),(-73.6444, -112.51092))
EST_MEDIO_R4 = ((13.4589, -98.2519), (12.0715, -117.39122))
EST_MEDIO_INTERSECCION4_1 = ((12.0715, -117.39122), (10.5707, -117.39122))
EST_MEDIO_INTERSECCION4_2 = ((-67.7369, -113.01202), (-73.6444, -112.51092))
EST_MEDIO_L5 = ((-73.6444, -112.51092),(-80.1746, -131.3942))
EST_MEDIO_R5 = ((12.0715, -117.39122), (10.6169, -135.9693))
EST_MEDIO_INTERSECCION5_1 = ((10.6169, -135.9693), (8.8466, -135.9693))
EST_MEDIO_INTERSECCION5_2 = ((-77.8511, -131.1209), (-80.1746, -131.3942))
EST_MEDIO_L6 = ((-80.1746, -131.3942),(-81.5118, -150.2121))
EST_MEDIO_R6 = ((10.6169, -135.9693), (7.59559, -155.39970))
EST_MEDIO_INTERSECCION6_1 = ((7.59559, -155.39970), (5.3963, -155.3997))
EST_MEDIO_INTERSECCION6_2 = ((-67.3179, -151.3333), (-81.5118, -150.2121))
EST_MEDIO_R7 = ((7.59559, -155.39970), (9.3492, -153.5104))
EST_MEDIO_L7 = ((-81.5118, -150.2121),(-82.8175, -168.5878))
EST_MEDIO_R8 = ((9.3492, -153.5104), (-8.7637, -173.0237))
EST_MEDIO_T1 = ((-8.7637, -173.0237), (-9.7637, -173.0237))
EST_MEDIO_T2 = ((-81.47790000000002, -168.95730000000023), (-82.8175, -168.5878))

# ---- CAJONES:ESTACIONAMIENTO MEDIO ----
coordX1=0
coordX2=0
coordY1=0
coordY2=0
cajon_EST_MEDIO=[]
estacion_MEDIO_CAMINO_B=[]
for x in range(354):
    if (x<=11):
        if(x==0):
            coordX1=21.1641
            coordX2=21.0177
            coordY1=-41.8117
            coordY2=-35.6706
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1)))#11
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
            coordY1= -59.6201
            coordY2= -59.6201 - 6.1411 
            coordX1= 15.5707
            coordX2= 15.4243
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1)))#27
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
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1))) #48
    if( x>=89 and x<=109):
        if(x==89):
            coordY1= -98.2519
            coordY2= -92.1108
            coordX1= 11.5707
            coordX2= 11.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=110 and x<=134):
        if(x==110):
            coordY1= -98.2519
            coordY2= -104.393
            coordX1= 11.7707
            coordX2= 11.6243
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1)))#73
    if( x>=135 and x<=159):
        if(x==135):
            coordY1= -117.39122
            coordY2= -111.25012
            coordX1= 10.5707
            coordX2= 10.4243
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=160 and x<=188):
        if(x==160):
            coordY1= -117.39122
            coordY2= -123.53232
            coordX1= 10.5707
            coordX2= 10.4243
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1)))#102
    if( x>=189 and x<=217):
        if(x==189):
            coordY1= -135.9693
            coordY2= -129.8282
            coordX1= 8.8466
            coordX2= 8.7002
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=218 and x<=248):
        if(x==218):
            coordY1= -135.9693
            coordY2= -142.1104
            coordX1= 8.8466
            coordX2= 8.7002
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1)))#133
    if( x>=249 and x<=279):
        if(x==249):
            coordY1= -155.39970
            coordY2= -149.2586
            coordX1= 5.3963
            coordX2= 5.2499
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=280 and x<=305):
        if(x==280):
            coordY1= -155.39970
            coordY2= -161.5408
            coordX1= 5.3963
            coordX2= 5.2499
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1)))#159
    if( x>=306 and x<=331):
        if(x==306):
            coordY1= -173.0237
            coordY2= -166.8826
            coordX1= -8.7637
            coordX2= -8.9101
        oldCoordX1=coordX1
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        oldCoordY1=coordY1
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
        estacion_MEDIO_CAMINO_B.append(((oldCoordX1,oldCoordY1),(coordX1,coordY1)))#185
    if( x>=332 and x<=354):
        if(x==332):
            coordY1= -173.0237
            coordY2= -179.1648
            coordX1= -18.9381
            coordX2= -19.0845
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))


    
EST_MEDIO_CAJONES=tuple(cajon_EST_MEDIO)
EST_MEDIO_CAMINO=tuple(estacion_MEDIO_CAMINO_B)


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
res1 = 93.25 - 28.96
divX = res1 / 10
res2 = 196.92 - 191.87
divY = res2 / 10
HORIZONTAL_SECCIONADA_1 = []
for inter in range(0, 10):
    if (inter == 0 and inter <= 10):
        xi = -28.96
        yi = -195.92
        xf = xi - divX
        yf = yi + divY
    HORIZONTAL_SECCIONADA_1.append(((xi, yi),(xf, yf)))
    xi -= divX
    xf -= divX
    yi += divY
    yf += divY 
    
NUEVO_HORIZONTAL_1 = tuple(HORIZONTAL_SECCIONADA_1)
    
h2_1 = (-40.82, -208.18)
h2_2 = (-104.71, -203.76)
h3_1 = (-46.08, -212.96)
h3_2 = (-114.25, -208.69)

h4_1 = (-55.18, -221.65)
h4_2 = (-113.92, -218.92)
resX4 = 113.92 - 55.18
divX4 = resX4 / 10
resY4 = 221.65 - 218.92
divY4 = resY4 / 10
HORIZONTAL_SECCIONADA_4 = []
for inter in range(0, 10):
    if (inter == 0 and inter <= 10):
        xi = -55.18
        yi = -221.65
        xf = xi - divX4
        yf = yi + divY4
    HORIZONTAL_SECCIONADA_4.append(((xi, yi),(xf, yf)))
    xi -= divX4
    xf -= divX4
    yi += divY4
    yf += divY4
NUEVO_HORIZONTAL_4 = tuple(HORIZONTAL_SECCIONADA_4)

h5_1 = (-67.29, -250.20)
h5_2 = (-136.68, -246.70)
resX5 = 136.68 - 67.29
divX5 = resX5 / 25
resY5 = 250.20 - 246.70
divY5 = resY5 / 25
HORIZONTAL_SECCIONADA_5 = []
for inter in range(0, 25):
    if (inter == 0 and inter <= 25):
        xi = -67.29
        yi = -250.20
        xf = xi - divX5
        yf = yi + divY5
    HORIZONTAL_SECCIONADA_5.append(((xi, yi),(xf, yf)))
    xi -= divX5
    xf -= divX5
    yi += divY5
    yf += divY5
NUEVO_HORIZONTAL_5 = tuple(HORIZONTAL_SECCIONADA_5)

h6_1 = (-67.99, -268.79)
h6_2 = (-152.39, -265.03)
resX6 = 152.39 - 67.99
divX6 = resX6 / 28
resY6 = 268.79 - 265.03
divY6 = resY6 / 28
HORIZONTAL_SECCIONADA_6 = []
for inter in range(0, 28):
    if (inter == 0 and inter <= 28):
        xi = -67.99
        yi = -268.79
        xf = xi - divX6
        yf = yi + divY6
    HORIZONTAL_SECCIONADA_6.append(((xi, yi),(xf, yf)))
    xi -= divX6
    xf -= divX6
    yi += divY6
    yf += divY6
NUEVO_HORIZONTAL_6 = tuple(HORIZONTAL_SECCIONADA_6)

h7_1 = (-68.69, -285.74)
h7_2 = (-151.02, -282.50)
resX7 = 151.02 - 68.69
divX7 = resX7 / 28
resY7 = 285.74 - 282.50
divY7 = resY7 / 28
HORIZONTAL_SECCIONADA_7 = []
for inter in range(0, 28):
    if (inter == 0 and inter <= 28):
        xi = -68.69
        yi = -285.74
        xf = xi - divX7
        yf = yi + divY7
    HORIZONTAL_SECCIONADA_7.append(((xi, yi),(xf, yf)))
    xi -= divX7
    xf -= divX7
    yi += divY7
    yf += divY7
NUEVO_HORIZONTAL_7 = tuple(HORIZONTAL_SECCIONADA_7)

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

# CAJONES
xi = 0
yi = 0
xf = 0 
yf = 0
indexCajonNuevos = 0
cajon_EST_NUEVO = []
for x in range(194):
    if (x <= 13):
        if (x == 0):
            xi = -84.96
            yi = -191.84
            xf = -85.48
            yf = -201.12
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.2
        yi -= 0.2
    if (x >= 14 and x <= 31):
        if(x == 14):
            xi = -81.50
            yi = -192.16
            xf = -81.07
            yf = -185.07
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.2
        yi -= 0.2
    if (x >= 32 and x <= 49):
        if (x == 32):
            xi = -110.26
            yi = -218.33
            xf = -110.72
            yf = -226.97
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.11
        yi -= 0.11
    if (x >= 50 and x <= 67):
        if (x == 50):
            xi = -104.54
            yi = -218.83
            xf = -104.15
            yf = -212.57
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.11
        yi -= 0.11
    if (x >= 68 and x <= 91):
        if (x == 68):
            xi = -134.83
            yi = -247.72
            xf = -135.30
            yf = -255.35
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.11
        yi -= 0.11
    if (x >= 92 and x <= 112):
        if (x == 92):
            xi = -126.73
            yi = -248.10
            xf = -126.44
            yf = -239.81
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.11
        yi -= 0.11
    if (x >= 113 and x < 141):
        if (x == 113):
            xi = -148.38
            yi = -265.84
            xf = -148.83
            yf = -272.20
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.11
        yi -= 0.11
    if (x >= 142 and x < 166):
        if (x == 142):
            xi = -138.44
            yi = -266.28
            xf = -138.02
            yf = -258.51
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.11
        yi -= 0.11
    if (x >= 167 and x <= 194):
        if (x == 167):
            xi = -147.18
            yi = -283.33
            xf = -146.78
            yf = -276.06
        cajon_EST_NUEVO.append(((xi, yi),(xf, yf), 1))
        xi += 2.8
        xf += 2.8
        yf -= 0.11
        yi -= 0.11

#194 paths
EST_NUEVO_CAJONES = tuple(cajon_EST_NUEVO)

#Nuevo paths

neo_paths = []

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
NUEVO_VERTICAL_14 = (v14_2, v14_1)
NUEVO_VERTICAL_15 = (v15_2, v15_1)

NUEVO_HORIZONTAL_2 = (h2_1, h2_2) 
NUEVO_HORIZONTAL_3 = (h3_1, h3_2)

NUEVO_SALIDAS_1 = (s1_1, s1_2)
NUEVO_SALIDAS_2 = (s2_1, s2_2)
NUEVO_ENTRADA_1 = (e1_1, e1_2)
NUEVO_ENTRADA_2 = (e2_1, e2_2)
NUEVO_ENTRADA_3 = (e3_1, e3_2)

#22 roads
neo_paths.append(NUEVO_VERTICAL_1)
neo_paths.append(NUEVO_VERTICAL_2)
neo_paths.append(NUEVO_VERTICAL_3)
neo_paths.append(NUEVO_VERTICAL_4)
neo_paths.append(NUEVO_VERTICAL_5)
neo_paths.append(NUEVO_VERTICAL_6)
neo_paths.append(NUEVO_VERTICAL_7)
neo_paths.append(NUEVO_VERTICAL_8)
neo_paths.append(NUEVO_VERTICAL_9)
neo_paths.append(NUEVO_VERTICAL_10)
neo_paths.append(NUEVO_VERTICAL_11)
neo_paths.append(NUEVO_VERTICAL_12)
neo_paths.append(NUEVO_VERTICAL_13)
neo_paths.append(NUEVO_VERTICAL_14)
neo_paths.append(NUEVO_VERTICAL_15)
neo_paths.append(NUEVO_HORIZONTAL_2)
neo_paths.append(NUEVO_HORIZONTAL_3)
neo_paths.append(NUEVO_SALIDAS_1)
neo_paths.append(NUEVO_SALIDAS_2)
neo_paths.append(NUEVO_ENTRADA_1)
neo_paths.append(NUEVO_ENTRADA_2)
neo_paths.append(NUEVO_ENTRADA_3)
    
## ---- ESTACIONAMIENTO TERRACERIA ----

g0 = (-49.6102, -249.6164) #0
g1 = (-33.7784, -247.4305) #1
g2 = (-17.3714, -248.4225) #2
g3 = (-47.0759, -314.1266) #3
g4 = (-54, -329.9062) #4
g5 = (-60.0554, -344.8489) #5
g6 = (-67.1610, -359.8162) #6
g7 = (-73.1061, -374.8023) #7
g8 = (-195.9880, -368.1862) #8
g9 = (-188.5682, -353.0461) #9
g10 = (-178.1299, -339.3147) #10
g11 = (-166.1706, -323.7149) #11
g12 = (-153.1128, -307.1783) #12
g13 = (-54.3620, -296.4803) #13
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
r1_13 = (g1, g13)
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

#dir 0 up
#dir 1 down
#dir 2 left
#dir 3 right

def extension(inicio, final, divider, dir):
    xi = inicio[0]
    yi = inicio[1]
    xf = final[0]
    yf = final[1]
    division = []
    stepx = (xf-xi)/divider
    stepy = (yf-yi)/divider
    for i in range(divider):
        xp = xi
        yp = yi
        #up
        if dir == 0:
            xi += stepx
            yi += stepy
        #down
        elif dir == 1:
            xi += stepx
            yi -= stepy
        #left
        elif dir == 2:
            xi += stepx
            yi += stepy
        #right
        else:
            xi += stepx
            yi += stepy
        division.append(((xp, yp),(xi, yi))) 
    return division

caminos =[]

#VERTICALES

#2-3 26r 18l
p2_3 = extension(g2,g3,26,0)
caminos.append(p2_3)

#3-4 6r
p3_4 = extension(g3,g4,6,0)
caminos.append(p3_4)

#4-5 6r
p4_5 = extension(g4,g5,6,0)
caminos.append(p4_5)

#5-6 6r
p5_6 = extension(g5,g6,6,0)
caminos.append(p5_6)

#6-7 5r
p6_7 = extension(g6,g7,5,0)
caminos.append(p6_7)

#1-13 17r 16l
p1_13 = extension(g1,g13,17,0)
caminos.append(p1_13)

#8-9 7l
p8_9 = extension(g8,g9,7,0)
caminos.append(p8_9)

#9-10 5l
p9_10 = extension(g9,g10,5,0)
caminos.append(p9_10)

#10-11 7l
p10_11 = extension(g10,g11,7,0)
caminos.append(p10_11)

#11-12 8l
p11_12 = extension(g11,g12,8,0)
caminos.append(p11_12)

#15-17 3r ??

#16-17 12l
p16_17 = extension(g16,g17,12,0)
caminos.append(p16_17)

#17-18 25l 13r
p17_18 = extension(g17,g18,25,0)
caminos.append(p17_18)

#HORIZONTALES 

#0-1 5d
p0_1 = extension(g0,g1,5,0)
caminos.append(p0_1)

#1-2 5d
p1_2 = extension(g1,g2,5,0)
caminos.append(p1_2)

#13-14 36u 12d(para)
p13_14 = extension(g13,g14,36,0)
caminos.append(p13_14)

#3-12 36d 35u
p3_12 = extension(g3,g12,36,0)
caminos.append(p3_12)

#4-11 36d 36u
p4_11 = extension(g4,g11,36,0)
caminos.append(p4_11)

#5-10 38d 38u
p5_10 = extension(g5,g10,38,0)
caminos.append(p5_10)

#6-9 39d 41u
p6_9 = extension(g6,g9,41,0)
caminos.append(p6_9)

#7-8 42d 41u
p7_8 = extension(g7,g8,42,0)
caminos.append(p7_8)

#14-15 4u
p14_15 = extension(g14,g15,4,0)
caminos.append(p14_15)

#15-16 8u
p15_16 = extension(g15,g16,8,0)
caminos.append(p15_16)


#----------------------
#ESTACIONAMIENTOS
estacionamientos =[]

def cajonear(ruta, n, dir, skip):
    i = 0
    extra = skip
    cajones = []
    while i < n + extra:
        xi = ruta[i][0][0] 
        yi = ruta[i][0][1]
        xf = ruta[i][1][0] 
        yf = ruta[i][1][1]
        dx = xf - xi
        dy = yf - yi
        ndx = dy*2
        ndy = dx*2
        nidx = dy/3
        nidy = dx/3
        if dir == 0:
            xn = xf + ndx
            xni = xf + nidx
            #xf += 1.5
            yn = yf - ndy
            yni = yf - nidy
          
        elif dir == 1:
            xn = xf - ndx
            xni = xf - nidx
            #xf -= 1.5
            yn = yf + ndy
            yni = yf + nidy
        #cajones.append(((xf,yf),(xn,yn)))
        if skip <= 0:
             cajones.append(((xni,yni),(xn,yn)))

        i += 1
        skip -= 1
         
    return cajones


c2_3_l = cajonear(p2_3, 18,0,1)
c2_3_r = cajonear(p2_3, 26, 1, 0)
estacionamientos.append(c2_3_l)
estacionamientos.append(c2_3_r)

c3_4 = cajonear(p3_4, 6,1,0)
estacionamientos.append(c3_4)

c4_5 = cajonear(p4_5, 6,1,0)
estacionamientos.append(c4_5)

c5_6 = cajonear(p5_6, 6,1,0)
estacionamientos.append(c5_6)

c6_7 = cajonear(p6_7, 5,1,0)
estacionamientos.append(c6_7)

c1_13_r = cajonear(p1_13, 17,1,0)
c1_13_l = cajonear(p1_13, 16,0,0)
estacionamientos.append(c1_13_r)
estacionamientos.append(c1_13_l)

c8_9 = cajonear(p8_9, 7,1,0)
estacionamientos.append(c8_9)

c9_10 = cajonear(p9_10, 5,1,0)
estacionamientos.append(c9_10)

c10_11 = cajonear(p10_11, 7,1,0)
estacionamientos.append(c10_11)

c11_12 = cajonear(p11_12, 8,1,0)
estacionamientos.append(c11_12)

c16_17 = cajonear(p16_17, 12,1,0)
estacionamientos.append(c16_17)

c17_18_r =cajonear(p17_18, 13, 0, 10)
c17_18_l =cajonear(p17_18, 25, 1,0)
estacionamientos.append(c17_18_r)
estacionamientos.append(c17_18_l)

#hori

c0_1 = cajonear(p0_1, 5,1,0)
estacionamientos.append(c0_1)

c1_2 = cajonear(p1_2, 5,1,0)
estacionamientos.append(c1_2)

c13_14_d = cajonear(p13_14, 12,0,0)
c13_14_u = cajonear(p13_14, 36,1,0)
estacionamientos.append(c13_14_d)
estacionamientos.append(c13_14_u)

c3_12_d = cajonear(p3_12, 36,0,0)
c3_12_u = cajonear(p3_12, 35,1,0)
estacionamientos.append(c3_12_d)
estacionamientos.append(c3_12_u)

c4_11_d = cajonear(p4_11, 36,0,0)
c4_11_u = cajonear(p4_11, 36,1,0)
estacionamientos.append(c4_11_d)
estacionamientos.append(c4_11_u)

c5_10_d = cajonear(p5_10, 38,0,0)
c5_10_u = cajonear(p5_10, 38,1,0)
estacionamientos.append(c5_10_d)
estacionamientos.append(c5_10_u)

c6_9_d = cajonear(p6_9, 39,0,0)
c6_9_u = cajonear(p6_9, 41,1,0)
estacionamientos.append(c6_9_d)
estacionamientos.append(c6_9_u)

c7_8_d = cajonear(p7_8, 42,0,0)
c7_8_u = cajonear(p7_8, 41,1,0)
estacionamientos.append(c7_8_d)
estacionamientos.append(c7_8_u)

c14_15 = cajonear(p14_15, 4,1,0)
estacionamientos.append(c14_15)

c15_16 = cajonear(p15_16, 8,1,0)
estacionamientos.append(c15_16)

#------------------------------------------------------
#ESTACIONAMIENTOS SUBIDA

#Caminos

inter = (31.8606, -26.9761)
s1 = (36.7870, -38.9865)
s2 = (110.0329, -54.3665)
s3 = (208.3744, -48.1776)
inicio_s = extension(inter,s1,1,0)
caminos.append(inicio_s)
ps1_2 = extension(s1,s2,28,0)
ps2_3 = extension(s2,s3,29,0)
caminos.append(ps1_2)
caminos.append(ps2_3)

#Estacionamientos 

cs1_2 = cajonear(ps1_2, 28,1,0)

cs2_3 = cajonear(ps2_3, 29,1,0)

estacionamientos.append(cs1_2)
estacionamientos.append(cs2_3)


#----------------------------------------------------

# Arena borregos index 0 - 153
for i in range (0, len(EstArenaBorregos)):
    sim.create_roads([EstArenaBorregos[i]])
    # print(i)

# Estacionamiento medio index 154 - 185
sim.create_roads([
    ENTRADA_EST_MEDIO,  # 154
    EST_MEDIO_B1,  # 155
    EST_MEDIO_B2,  # 156
    EST_MEDIO_L1,  # 157
    EST_MEDIO_R1,  # 158
    EST_MEDIO_INTERSECCION1_1,  # 159
    EST_MEDIO_INTERSECCION1_2,  # 160
    EST_MEDIO_L2,  # 161
    EST_MEDIO_R2,  # 162
    EST_MEDIO_INTERSECCION2_1,  # 163
    EST_MEDIO_INTERSECCION2_2,  # 164
    EST_MEDIO_L3,  # 165
    EST_MEDIO_R3,  # 166
    EST_MEDIO_INTERSECCION3_1,  # 167
    EST_MEDIO_INTERSECCION3_2,  # 168
    EST_MEDIO_L4,  # 169
    EST_MEDIO_R4,  # 170
    EST_MEDIO_INTERSECCION4_1,  # 171
    EST_MEDIO_INTERSECCION4_2,  # 172
    EST_MEDIO_L5,  # 173
    EST_MEDIO_R5,  # 174
    EST_MEDIO_INTERSECCION5_1,  # 175
    EST_MEDIO_INTERSECCION5_2,  # 176
    EST_MEDIO_L6,  # 177
    EST_MEDIO_R6,  # 178
    EST_MEDIO_INTERSECCION6_1,  # 179
    EST_MEDIO_INTERSECCION6_2,  # 180
    EST_MEDIO_R7,  # 181
    EST_MEDIO_L7,  # 182
    EST_MEDIO_R8,  # 183
    EST_MEDIO_T1,  # 184
    EST_MEDIO_T2,  # 185
])

# indix desde 186 - 371
for i in range(0, len(EST_MEDIO_CAMINO)):
    sim.create_roads([EST_MEDIO_CAMINO[i]])#(186-197):EST_MEDIO_B_ABAJO/(198-213):EST_MEDIO_B_ARRIBA/(214-371):EST_MEDIO_T_ARRIBA
    # print(i)

# index desde 372 - 725
for i in range(0, len(EST_MEDIO_CAJONES)):
    sim.create_roads([EST_MEDIO_CAJONES[i]])
    # print(i)

# Verticales y estrada est nuevo 726 - 745
sim.create_roads([
    NUEVO_VERTICAL_1,   # 726
    NUEVO_VERTICAL_2,   # 727
    NUEVO_VERTICAL_3,   # 728
    NUEVO_VERTICAL_4,   # 729
    NUEVO_VERTICAL_5,   # 730
    NUEVO_VERTICAL_6,   # 731
    NUEVO_VERTICAL_7,   # 732
    NUEVO_VERTICAL_8,   # 733
    NUEVO_VERTICAL_9,   # 734
    NUEVO_VERTICAL_10,  # 735
    NUEVO_VERTICAL_11,  # 736
    NUEVO_VERTICAL_12,  # 737
    NUEVO_VERTICAL_13,  # 738
    NUEVO_VERTICAL_14,  # 739
    NUEVO_VERTICAL_15,  # 740
    NUEVO_SALIDAS_1,    # 741
    NUEVO_SALIDAS_2,    # 742
    NUEVO_ENTRADA_1,    # 743
    NUEVO_ENTRADA_2,    # 744
    NUEVO_ENTRADA_3     # 745
])

# index 746 a 755
for i in range(0, len(NUEVO_HORIZONTAL_1)):
    sim.create_roads([NUEVO_HORIZONTAL_1[i]])
    # print(i)

sim.create_roads([
    NUEVO_HORIZONTAL_2,  # 756
    NUEVO_HORIZONTAL_3  # 757
])

# index 758 a 767
for i in range(0, len(NUEVO_HORIZONTAL_4)):
    sim.create_roads([NUEVO_HORIZONTAL_4[i]])
    # print(i)

# index 768 a 792
for i in range(0, len(NUEVO_HORIZONTAL_5)):
    sim.create_roads([NUEVO_HORIZONTAL_5[i]])
    # print(i)

# index 793 a 820 
for i in range(0, len(NUEVO_HORIZONTAL_6)):
    sim.create_roads([NUEVO_HORIZONTAL_6[i]])
    # print(i)

# index 821,  848
for i in range(0, len(NUEVO_HORIZONTAL_7)):
    sim.create_roads([NUEVO_HORIZONTAL_7[i]])
    # print(i)

# CAJONES
# index 849 a 1040
for i in range (0, len(EST_NUEVO_CAJONES)):
    sim.create_roads([EST_NUEVO_CAJONES[i]])


#------------------------------------------------
#CAMINOS ARRIBA 
# index 1041 - 1479
print('CAMINOS')
#CAMINOS ARRIBA
for camino in caminos:
     for i in range(0, len(camino)):
        sim.create_roads([camino[i]])

#---------------------------------------------------
#CAJONES ARRIBA
# index 1480 - 2165
print('CAJONES')
for spot in estacionamientos:
     for i in range(0, len(spot)):
        sim.create_roads([spot[i]])
        # print(i)


sim.create_roads([
    r12_14,     # 2166
    r15_17,     # 2167
    r18_19,     # 2168
    r19_20      # 2169
])

test = []

for i in range(152):
    test.append(i)

# -------------------------------------------------------
#       total de cajones 625 + 191 + 353 + 71 = 1240
# -------------------------------------------------------
def crear_lista_entrada(numero, horizotal):
    entrada_nueva = [0, 1, 153, 157, 161, 165, 169, 173, 177, 180, 182] 
    for i in range(725, 732 ):
        entrada_nueva.append(i)
    for i in range(821, 848 - horizotal):
        entrada_nueva.append(i)
    entrada_nueva.append(1000 + numero)  # Agregar el número proporcionado al final
    for i in range ((848 - horizotal), 848):
        entrada_nueva.append(i)
    for i in range(733, 736):
        entrada_nueva.append(i)
    entrada_nueva.append(740)
    entrada_nueva.append(2168)
    return entrada_nueva

# Llamar a la función para crear las listas
for i in range (1, 10):
    entradaNuevo1 = crear_lista_entrada(14 , i)
    entradaNuevo2 = crear_lista_entrada(15, i)
    entradaNuevo3 = crear_lista_entrada(16, i)
    entradaNuevo4 = crear_lista_entrada(17, i)
    entradaNuevo5 = crear_lista_entrada(18, i)
    entradaNuevo6 = crear_lista_entrada(19, i)
    entradaNuevo7 = crear_lista_entrada(20, i)
    entradaNuevo8 = crear_lista_entrada(21, i)
    entradaNuevo9 = crear_lista_entrada(22, i)
    entradaNuevo10 = crear_lista_entrada(23, i)


# Paths
path = [
#[1, {"path": [0, 1, 2, 3, 4, 5, 9, 10, 11, 12, 13, 14, 15, 16, 17]}],#1
    [1, {"path": entradaNuevo1, "cajon_index":1014}],#3
    [2, {"path": entradaNuevo2, "cajon_index":1015}],#3
    [3, {"path": entradaNuevo3, "cajon_index":1016}],#3
    [4, {"path": entradaNuevo4, "cajon_index":1017}],#3
    [5, {"path": entradaNuevo5, "cajon_index":1018}],#3
    [6, {"path": entradaNuevo6, "cajon_index":1019}],#3
    [7, {"path": entradaNuevo7, "cajon_index":1020}],#3
    [8, {"path": entradaNuevo8, "cajon_index":1021}],#3
    [9, {"path": entradaNuevo9, "cajon_index":1022}],#3
    [10, {"path": entradaNuevo10, "cajon_index":1023}],#3
]
sim.create_gen({
    'vehicle_rate': 10,
    'vehicles': path
})

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)
