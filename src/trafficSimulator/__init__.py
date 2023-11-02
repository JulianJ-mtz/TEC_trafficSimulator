from curve import *
from vehicle import *
from road import *
from simulation import *
from window import *
from vehicle_generator import *
from traffic_signal import *

sim = Simulation()

#Bajo
p0 = (0,0)
p1 = (27,-28)
p2 = (29,-19)
p3 = (31,-9)
p4 = (30,5)
p5 = (32,22)
p6 = (34,36)
p7 = (70,36)
p8 = (70,21)
p9 = (70,7) 
p10 = (71,-9)
p11 = (71,-18)
#Medio
p12 = (18,-42)
p13 = (11,-60)
p14 = (7,-79)
p15 = (7,-97)
p16 = (5,-116)
p17 = (4,-136)
p18 = (-2,-155)
p19 = (-13,-172)
p20 = (-90,-168)
p21 = (-89,-150)
p22 = (-87,-130)
p23 = (-81,-112) 
p24 = (-67,-93)
p25 = (-53,-75)
p26 = (-40,-57)
p27 = (-27,-39)
#Nuevo
p28 = (-27,-191) 
p29 = (-46,-206)
p30 = (-54,-218)
p31 = (-65,-245)
p32 = (-68,-264)
p33 = (-69,-281)
p34 = (-153,-276)
p35 = (-150,-259)
p36 = (-138,-241)
p37 = (-116,-211)
#Arriba
p38 = (-36,-247)
p39 = (-54,-296)
p40 = (-60,-307)
p41 = (-65,-317)
p42 = (-69,-326)
p43 = (-73,-336)
p44 = (-78,-346)
p45 = (-82,-356)
p46 = (-87,-366)
p47 = (-90,-376)
p48 = (-205,-371)
p49 = (-203,-361) 
p50 = (-196,-351)
p51 = (-192,-341)
p52 = (-184,-331)
p53 = (-177,-322)
p54 = (-170,-312)
p55 = (-162,-302)
#salida
p56 = (-169,-286)
p57 = (-193,-285)
p58 = (-174,-260)
p59 = (-132,-205)
p60 = (-113,-202)
p61 = (-90,-182)
p00 = (-141,-187)

    


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

#Inicio


#Abajo

p0_1 = [((p0),(p1))] #0
caminos.append(p0_1)

p1_2 = [((p1),(p2))] #1
caminos.append(p1_2)

p1_12 = [((p1),(p12))] #2
caminos.append(p1_12)

p2_3 = [((p2),(p3))] #3
caminos.append(p2_3)

p3_4 = extension(p3,p4,4,0) #4-7
caminos.append(p3_4)

p4_5 = extension(p4,p5,4,0) #8-11
caminos.append(p4_5)

p5_6 = extension(p5,p6,3,0) #12-14
caminos.append(p5_6)

p6_7 = extension(p6,p7,6,0) #15-20
caminos.append(p6_7)

p7_8 = extension(p7,p8,1,0) #21
caminos.append(p7_8)

p8_9 = extension(p8,p9,1,0) #22
caminos.append(p8_9)

p9_10 = extension(p9,p10,1,0) #23
caminos.append(p9_10)

p10_11 = extension(p10,p11,1,0) #24
caminos.append(p10_11)

p11_2 = extension(p11,p2,8,0) #25-32 
caminos.append(p11_2)

p8_5 = extension(p8,p5,7,0) #33-39
caminos.append(p8_5)

p4_9 = extension(p4,p9,8,0) #40-47
caminos.append(p4_9)

p10_3 = extension(p10,p3,7,0) #48-54
caminos.append(p10_3)


#Medio

p12_13 = extension(p12,p13,1,0) #55
caminos.append(p12_13)

p13_14 = extension(p13,p14,1,0) #56
caminos.append(p13_14)

p14_15 = extension(p14,p15,1,0) #57
caminos.append(p14_15)

p15_16 = extension(p15,p16,1,0) #58
caminos.append(p15_16)

p16_17 = extension(p16,p17,1,0) #59
caminos.append(p16_17)

p17_18 = extension(p17,p18,1,0) #60
caminos.append(p17_18)

p18_19 = extension(p18,p19,1,0) #61
caminos.append(p18_19)

p19_20 = extension(p19,p20,25,0) #62-86
caminos.append(p19_20)

p20_21 = extension(p20,p21,1,0) #87
caminos.append(p20_21)

p21_22 = extension(p21,p22,1,0) #88
caminos.append(p21_22)

p22_23 = extension(p22,p23,1,0) #89
caminos.append(p22_23)

p23_24 = extension(p23,p24,1,0) #90
caminos.append(p23_24)

p24_25 = extension(p24,p25,1,0) #91
caminos.append(p24_25)

p25_26 = extension(p25,p26,1,0) #92
caminos.append(p25_26)

p26_27 = extension(p26,p27,1,0) #93
caminos.append(p26_27)

p27_12 = extension(p27,p12,12,0) #94-105
caminos.append(p27_12)

p13_26 = extension(p13,p26,16,0) #106-121
caminos.append(p13_26)

p25_14 = extension(p25,p14,21,0) #122-142
caminos.append(p25_14)

p15_24 = extension(p15,p24,25,0) #143-167
caminos.append(p15_24)

p23_16 = extension(p23,p16,29,0) #168-196
caminos.append(p23_16)

p17_22 = extension(p17,p22,31,0) #197-227
caminos.append(p17_22)

p21_18 = extension(p21,p18,30,0) #228-257
caminos.append(p21_18)

#Nuevo

p19_28 = extension(p19,p28,1,0) #258
caminos.append(p19_28)

p20_61 = extension(p20,p61,1,0) #259
caminos.append(p20_61)

p28_61 = extension(p28,p61,18,0) #260-277 
caminos.append(p28_61)

p61_60 = extension(p61,p60,1,0) #278
caminos.append(p61_60)

p28_29 = extension(p28,p29,1,0) #279
caminos.append(p28_29)

p29_30 = extension(p29,p30,1,0) #280
caminos.append(p29_30)

p29_60 = extension(p29,p60,1,0) #281
caminos.append(p29_60)

p30_37 = extension(p30,p37,18,0) #282-299
caminos.append(p30_37)

p30_31 = extension(p30,p31,1,0) #300
caminos.append(p30_31)

p31_32 = extension(p31,p32,1,0) #301
caminos.append(p31_32)

p32_33 = extension(p32,p33,1,0) #302
caminos.append(p32_33)

p33_34 = extension(p33,p34,27,0) #303-329
caminos.append(p33_34)

p34_35 = extension(p34,p35,1,0) #330
caminos.append(p34_35)

p35_36 = extension(p35,p36,13,0) #331-343
caminos.append(p35_36)

p32_35 = extension(p32,p35,28,0) #344-371
caminos.append(p32_35)

p31_36 = extension(p31,p36,24,0) #372-395
caminos.append(p31_36)

p36_37 = extension(p36,p37,1,0) #396
caminos.append(p36_37)

p37_60 = extension(p37,p60,1,0) #397
caminos.append(p37_60)

#Terraceria

p31_38 = extension(p31,p38,5,0) #398-402
caminos.append(p31_38)

p38_39 = extension(p38,p39,18,0) #403-420
caminos.append(p38_39)

p39_40 = extension(p39,p40,4,0) #421-424
caminos.append(p39_40)

p40_41 = extension(p40,p41,3,0) #425-427
caminos.append(p40_41)

p41_42 = extension(p41,p42,3,0) #428-430
caminos.append(p41_42)

p42_43 = extension(p42,p43,3,0) #431-433
caminos.append(p42_43)

p43_44 = extension(p43,p44,3,0) #434-436
caminos.append(p43_44)

p44_45 = extension(p44,p45,4,0) #437-440
caminos.append(p44_45)

p45_46 = extension(p45,p46,3,0) #441-443
caminos.append(p45_46)

p46_47 = extension(p46,p47,1,0) #444
caminos.append(p46_47)

p47_48 = extension(p47,p48,33,0) #445-477
caminos.append(p47_48)

 

 
p48_49 = extension(p48,p49,1,0) #478
caminos.append(p48_49)

p49_46 = extension(p49,p46,35,0) #479-513
caminos.append(p49_46)

p45_50 = extension(p45,p50,35,0) #514-548
caminos.append(p45_50)

p51_44 = extension(p51,p44,35,0) #549-583
caminos.append(p51_44)

p43_52 = extension(p43,p52,35,0) #584-618
caminos.append(p43_52)

p53_42 = extension(p53,p42,31,0) #619-649
caminos.append(p53_42)

p41_54 = extension(p41,p54,31,0) #650-680
caminos.append(p41_54)

p55_40 = extension(p55,p40,30,0) #681-710
caminos.append(p55_40)

p39_56 = extension(p39,p56,34,0) #711-744
caminos.append(p39_56)

p56_57 = extension(p56,p57,8,0) #745-752
caminos.append(p56_57)

p56_58 = extension(p56,p58,1,0) #753
caminos.append(p56_58)

p57_58 = extension(p57,p58,11,0) #754-764
caminos.append(p57_58)

p58_59 = extension(p58,p59,23,0) #765-787
caminos.append(p58_59)

p59_60 = extension(p59,p60,1,0) #788
caminos.append(p59_60)

#path izquierdo

p50_51 = extension(p50,p51,1,0) #789
caminos.append(p50_51)

p52_53 = extension(p52,p53,1,0) #790
caminos.append(p52_53)

p54_55 = extension(p54,p55,1,0) #791
caminos.append(p54_55)

#Salida arriba

p47_46 = extension(p47,p46,1,0) #792
caminos.append(p47_46)

p46_45 = extension(p46,p45,1,0) #793
caminos.append(p46_45)

p45_44 = extension(p45,p44,1,0) #794
caminos.append(p45_44)

p44_43 = extension(p44,p43,1,0) #795
caminos.append(p44_43)

p43_42 = extension(p43,p42,1,0) #796
caminos.append(p43_42)

p42_41 = extension(p42,p41,1,0) #797
caminos.append(p42_41)

p41_40 = extension(p41,p40,1,0) #798
caminos.append(p41_40) 

p40_39 = extension(p40,p39,1,0) #799
caminos.append(p40_39)


#Final

p60_00 = extension(p60,p00,1,0) #800
caminos.append(p60_00)




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


#c2_3_l = cajonear(p2_3, 18,0,1)
#c2_3_r = cajonear(p2_3, 26, 1, 0)
#estacionamientos.append(c2_3_l)
#estacionamientos.append(c2_3_r)



#------------------------------------------------
#CAMINOS 0-800 
# index 0-800
print('CAMINOS')
#CAMINOS ARRIBA
for camino in caminos:
     for i in range(0, len(camino)):
        sim.create_roads([camino[i]])

#---------------------------------------------------
#CAJONES ARRIBA
# index 801 - 0000
print('CAJONES')
for spot in estacionamientos:
     for i in range(0, len(spot)):
        sim.create_roads([spot[i]])
        # print(i)




extra = [0] #No le hagan caso a este 
#Path arena 0
pathArena0 = [0,1,21,20]
for i in range(22,27):
    pathArena0.append(i)
for i in range(98,114):
    pathArena0.append(i)
pathArena0.append(4)
pathArena0.append(5)
for i in range(144,153):
    pathArena0.append(i)
for i in range(7,10):
    pathArena0.append(i)
#Path arena 1
pathArena1 = [0,1,21,22,23,19]
for i in range(24,27):
    pathArena1.append(i)
for i in range(98,114):
    pathArena1.append(i)
pathArena1.append(4)
pathArena1.append(5)
for i in range(144,153):
    pathArena1.append(i)
for i in range(7,10):
    pathArena1.append(i)
#Path arena 2
pathArena2 = [0,1,21,22,23,24,25,17,26]
for i in range(98,114):
    pathArena2.append(i)
pathArena1.append(4)
pathArena1.append(5)
for i in range(144,153):
    pathArena2.append(i)
for i in range(7,10):
    pathArena2.append(i)
#Path arena 3
pathArena3 = [0,1,21,22,23,24,25,26,98,97]
for i in range(99,114):
    pathArena3.append(i)
pathArena3.append(4)
pathArena3.append(5)
for i in range(144,153):
    pathArena3.append(i)
for i in range(7,10):
    pathArena3.append(i)
#path arena 4
pathArena4 = [0,1,21,22,23,24,25,26]
for i in range(98,114):
    pathArena4.append(i)
pathArena4.append(4)
pathArena4.append(128)
pathArena4.append(121)
for i in range(129,136):
    pathArena4.append(i)
for i in range(23,27):
    pathArena4.append(i)
for i in range(98,114):
    pathArena4.append(i)
pathArena4.append(4)
pathArena4.append(5)
for i in range(144,153):
    pathArena4.append(i)
for i in range(7,10):
    pathArena4.append(i)
#Path arena 5
pathArena5 = [0,1,21,22,23,24,25,26,27,28,15]
for i in range(29,36):
    pathArena5.append(i)
for i in range(46,56):
    pathArena5.append(i)
for i in range(2,6):
    pathArena5.append(i)
for i in range(144,153):
    pathArena5.append(i)
for i in range(7,10):
    pathArena5.append(i)
#Path arena 6
pathArena6 = [0,1,21,22,23,24,25,26,27,28,29,30,13]
for i in range(31,36):
    pathArena6.append(i)
for i in range(46,56):
    pathArena6.append(i)
for i in range(2,6):
    pathArena6.append(i)
for i in range(144,153):
    pathArena6.append(i)
for i in range(7,10):
    pathArena6.append(i)
#path arena 7
pathArena7 = [0,1,21,22,23,24,25,26,27,28,29,30,31,32,12]
for i in range(33,36):
    pathArena7.append(i)
for i in range(46,56):
    pathArena7.append(i)
for i in range(2,6):
    pathArena7.append(i)
for i in range(144,153):
    pathArena7.append(i)
for i in range(7,10):
    pathArena7.append(i)
#Path arena 8
pathArena8 = [0,1,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,46,39]
for i in range(47,56):
    pathArena8.append(i)
for i in range(2,6):
    pathArena8.append(i)
for i in range(144,153):
    pathArena8.append(i)
for i in range(7,10):
    pathArena8.append(i)
#Path arena 9
pathArena9 = [0,1,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,46,47,45]
for i in range(48,56):
    pathArena9.append(i)
for i in range(2,6):
    pathArena9.append(i)
for i in range(144,153):
    pathArena9.append(i)
for i in range(7,10):
    pathArena9.append(i)

def crear_lista_entrada(numero, horizotal):
    entrada_nueva = [0, 1, 153, 157, 161, 165, 169, 173, 177, 180, 182] 
    for i in range(725, 732 ):
        entrada_nueva.append(i)
    for i in range(821, (848 - horizotal)):
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
for i in range (0, 19):
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
    entradaNuevo11 = crear_lista_entrada(24, i)
    entradaNuevo12 = crear_lista_entrada(25, i)
    entradaNuevo13 = crear_lista_entrada(26, i)
    entradaNuevo14 = crear_lista_entrada(27, i)
    entradaNuevo15 = crear_lista_entrada(28, i)
    entradaNuevo16 = crear_lista_entrada(29, i)
    entradaNuevo17 = crear_lista_entrada(30, i)
    entradaNuevo18 = crear_lista_entrada(31, i)
    entradaNuevo19 = crear_lista_entrada(32, i)
    entradaNuevo20 = crear_lista_entrada(33, i)

#Listas

#abajo

l0_1 = [0]
l1_2 = [1]
l1_12 = [2]
l2_3 = [3]
l3_4 = [i for i in range(4,7)]
l4_5 = [i for i in range(8,11)]
l5_6 = [i for i in range(12,14)]
l6_7 = [i for i in range(15,20)]
l7_8 = [21]
l8_9 = [22]
l9_10 = [23]
l10_11 = [24]
l11_2 = [i for i in range(25,32)]

l8_5 = [i for i in range(33,39)]

l4_9 = [i for i in range(40,47)]

l10_3 = [i for i in range(48,54)]

#medio

l12_13 = [55]

l13_14 = [56]

l14_15 = [57]

l15_16 = [58]

l16_17 = [59]

l17_18 = [60]

l18_19 = [61]

l19_20 = [i for i in range(62,86)]

l20_21 = [87]

l21_22 = [88]

l22_23 = [89]

l23_24 = [90]

l24_25 = [91]

l25_26 = [92]

l26_27 = [93]

l27_12 = [i for i in range(94,105)]

l13_26 = [i for i in range(106,121)]

l25_14 = [i for i in range(122,142)]

l15_24 = [i for i in range(143,167)]

l23_16 = [i for i in range(168,196)]

l17_22 = [i for i in range(197,227)]

l21_18 = [i for i in range(228,257)]

#Nuevo

l19_28 = [258]

l20_61 = [259]

l28_61 = [i for i in range(260,277)]

l61_60 = [278]

l28_29 = [279]

l29_30 = [280]

l29_60 = [281]

l30_37 = [i for i in range(282,299)]

l30_31 = [300]

l31_32 = [301]

l32_33 = [302]

l33_34 = [i for i in range(303,329)]

l34_35 = [330]

l35_36 = [i for i in range(331,343)]

l32_35 = [i for i in range(344,371)]

l31_36 = [i for i in range(372,395)]

l36_37 = [396]

l37_60 = [397]

#Terraceria

l31_38 = [i for i in range(398,402)]

l38_39 = [i for i in range(403,420)]

l39_40 = [i for i in range(421,424)]

l40_41 = [i for i in range(425,427)]

l41_42 = [i for i in range(428,430)]

l42_43 = [i for i in range(431,433)]

l43_44 = [i for i in range(434,436)]

l44_45 = [i for i in range(437,440)]

l45_46 = [i for i in range(441,443)]

l46_47 = [444]

l47_48 = [i for i in range(445,477)]

l48_49 = [478]

l49_46 = [i for i in range(479,513)]

l45_50 = [i for i in range(514,548)]

l51_44 = [i for i in range(549,583)]

l43_52 = [i for i in range(584,618)]

l53_42 = [i for i in range(619,649)]

l41_54 = [i for i in range(650,680)]

l55_40 = [i for i in range(681,710)]

l39_56 = [i for i in range(711,744)]

l56_57 = [i for i in range(745,752)]

l56_58 = [753]

l57_58 = [i for i in range(754,764)]

l58_59 = [i for i in range(765,787)]

l59_60 = [788]

l50_51 = [789]

l52_53 = [790]

l54_55 = [791]

l47_46 = [792]

l46_45 = [793]

l45_44 = [794]

l44_43 = [795]

l43_42 = [796]

l42_41 = [797]

l41_40 = [798]

l40_39 = [799]

l60_00 = [800]


#paths

# abajo

l1 = l0_1 + l1_2 + l2_3 + l3_4 + l4_5 + l5_6 + l6_7 + l7_8 + l8_9 + l9_10 + l10_11 + l11_2

l2 = l0_1 + l1_2 + l2_3 + l3_4 + l4_5 + l5_6 + l6_7 + l7_8 + l8_5

l3 = l0_1 + l1_2 + l2_3 + l3_4 + l4_9 + l9_10 + l10_11 + l11_2

l4 = l0_1 + l1_2 + l2_3 + l3_4 + l4_5 + l5_6 + l6_7 + l7_8 + l8_9 + l9_10 + l10_3

# medio

l5 = l0_1 + l1_12 + l12_13 + l13_26 + l26_27 + l27_12 + l12_13 + l13_14 + l14_15 + l15_16 + l16_17 + l17_18 + l18_19 + l19_28 + l28_29 + l29_60 + l60_00

l6 = l0_1 + l1_12 + l12_13 + l13_14 + l14_15 + l15_24 + l24_25 + l25_14 + l14_15 + l15_16 + l16_17 + l17_18 + l18_19 + l19_28 + l28_29 + l29_60 + l60_00

l7 = l0_1 + l1_12 + l12_13 + l13_14 + l14_15 + l15_16 + l16_17 + l17_22 + l22_23 + l23_16 + l16_17 + l17_18 + l18_19 + l19_28 + l28_29 + l29_60 + l60_00

l8 = l0_1 + l1_12 + l12_13 + l13_14 + l14_15 + l15_16 + l16_17 + l17_18 + l18_19 + l19_20 + l20_21 + l21_18 + l18_19 + l19_28 + l28_29 + l29_60 + l60_00


# Paths
path = [
    
    
    [1, {"path": l2, "cajon_index": 20}],
    [1, {"path": l2, "cajon_index": 20}],
    [1, {"path": l2, "cajon_index": 20}],
    [1, {"path": l3, "cajon_index": 20}],
    [1, {"path": l3, "cajon_index": 20}],
    [1, {"path": l4, "cajon_index": 20}],
    [1, {"path": l4, "cajon_index": 20}],
    [1, {"path": l4, "cajon_index": 20}],
    [1, {"path": l5, "cajon_index": 20}],
    [1, {"path": l5, "cajon_index": 20}],
    [1, {"path": l5, "cajon_index": 20}],
    [1, {"path": l6, "cajon_index": 20}],
    [1, {"path": l6, "cajon_index": 20}],
    [1, {"path": l6, "cajon_index": 20}],
    [1, {"path": l7, "cajon_index": 20}],
    [1, {"path": l7, "cajon_index": 20}],
    [1, {"path": l8, "cajon_index": 20}],
    [1, {"path": l8, "cajon_index": 20}],
    [1, {"path": l8, "cajon_index": 20}],
    [1, {"path": l8, "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],
    [1, {"path": [i for i in range(398,800)], "cajon_index": 20}],

    
    
]
sim.create_gen({
    'vehicle_rate': 20,
    'vehicles': path
})

# Start simulation
win = Window(sim)
win.zoom = 10
win.run(steps_per_update=5)
