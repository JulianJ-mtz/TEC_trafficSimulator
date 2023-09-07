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
            coordX1= 8.0466
            coordX2= 7.9002
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=218 and x<=248):
        if(x==218):
            coordY1= -135.9693
            coordY2= -142.1104
            coordX1= 8.0466
            coordX2= 7.9002
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
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
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
    if( x>=306 and x<=331):
        if(x==306):
            coordY1= -173.0237
            coordY2= -166.8826
            coordX1= -8.7637
            coordX2= -8.9101
        coordX1=coordX1-2.7967
        coordX2=coordX2-2.7967
        coordY1=coordY1+0.1564
        coordY2=coordY2+0.1564
        cajon_EST_MEDIO.append(((coordX1,coordY1),(coordX2,coordY2),1))
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
    EST_MEDIO_CAJONES[ 0 ],# 42
    EST_MEDIO_CAJONES[ 1 ],# 43
    EST_MEDIO_CAJONES[ 2 ],# 44
    EST_MEDIO_CAJONES[ 3 ],# 45
    EST_MEDIO_CAJONES[ 4 ],# 46
    EST_MEDIO_CAJONES[ 5 ],# 47
    EST_MEDIO_CAJONES[ 6 ],# 48
    EST_MEDIO_CAJONES[ 7 ],# 49
    EST_MEDIO_CAJONES[ 8 ],# 50
    EST_MEDIO_CAJONES[ 9 ],# 51
    EST_MEDIO_CAJONES[ 10 ],# 52
    EST_MEDIO_CAJONES[ 11 ],# 53
    EST_MEDIO_CAJONES[ 12 ],# 54
    EST_MEDIO_CAJONES[ 13 ],# 55
    EST_MEDIO_CAJONES[ 14 ],# 56
    EST_MEDIO_CAJONES[ 15 ],# 57
    EST_MEDIO_CAJONES[ 16 ],# 58
    EST_MEDIO_CAJONES[ 17 ],# 59
    EST_MEDIO_CAJONES[ 18 ],# 60
    EST_MEDIO_CAJONES[ 19 ],# 61
    EST_MEDIO_CAJONES[ 20 ],# 62
    EST_MEDIO_CAJONES[ 21 ],# 63
    EST_MEDIO_CAJONES[ 22 ],# 64
    EST_MEDIO_CAJONES[ 23 ],# 65
    EST_MEDIO_CAJONES[ 24 ],# 66
    EST_MEDIO_CAJONES[ 25 ],# 67
    EST_MEDIO_CAJONES[ 26 ],# 68
    EST_MEDIO_CAJONES[ 27 ],# 69
    EST_MEDIO_CAJONES[ 28 ],# 70
    EST_MEDIO_CAJONES[ 29 ],# 71
    EST_MEDIO_CAJONES[ 30 ],# 72
    EST_MEDIO_CAJONES[ 31 ],# 73
    EST_MEDIO_CAJONES[ 32 ],# 74
    EST_MEDIO_CAJONES[ 33 ],# 75
    EST_MEDIO_CAJONES[ 34 ],# 76
    EST_MEDIO_CAJONES[ 35 ],# 77
    EST_MEDIO_CAJONES[ 36 ],# 78
    EST_MEDIO_CAJONES[ 37 ],# 79
    EST_MEDIO_CAJONES[ 38 ],# 80
    EST_MEDIO_CAJONES[ 39 ],# 81
    EST_MEDIO_CAJONES[ 40 ],# 82
    EST_MEDIO_CAJONES[ 41 ],# 83
    EST_MEDIO_CAJONES[ 42 ],# 84
    EST_MEDIO_CAJONES[ 43 ],# 85
    EST_MEDIO_CAJONES[ 44 ],# 86
    EST_MEDIO_CAJONES[ 45 ],# 87
    EST_MEDIO_CAJONES[ 46 ],# 88
    EST_MEDIO_CAJONES[ 47 ],# 89
    EST_MEDIO_CAJONES[ 48 ],# 90
    EST_MEDIO_CAJONES[ 49 ],# 91
    EST_MEDIO_CAJONES[ 50 ],# 92
    EST_MEDIO_CAJONES[ 51 ],# 93
    EST_MEDIO_CAJONES[ 52 ],# 94
    EST_MEDIO_CAJONES[ 53 ],# 95
    EST_MEDIO_CAJONES[ 54 ],# 96
    EST_MEDIO_CAJONES[ 55 ],# 97
    EST_MEDIO_CAJONES[ 56 ],# 98
    EST_MEDIO_CAJONES[ 57 ],# 99
    EST_MEDIO_CAJONES[ 58 ],# 100
    EST_MEDIO_CAJONES[ 59 ],# 101
    EST_MEDIO_CAJONES[ 60 ],# 102
    EST_MEDIO_CAJONES[ 61 ],# 103
    EST_MEDIO_CAJONES[ 62 ],# 104
    EST_MEDIO_CAJONES[ 63 ],# 105
    EST_MEDIO_CAJONES[ 64 ],# 106
    EST_MEDIO_CAJONES[ 65 ],# 107
    EST_MEDIO_CAJONES[ 66 ],# 108
    EST_MEDIO_CAJONES[ 67 ],# 109
    EST_MEDIO_CAJONES[ 68 ],# 110
    EST_MEDIO_CAJONES[ 69 ],# 111
    EST_MEDIO_CAJONES[ 70 ],# 112
    EST_MEDIO_CAJONES[ 71 ],# 113
    EST_MEDIO_CAJONES[ 72 ],# 114
    EST_MEDIO_CAJONES[ 73 ],# 115
    EST_MEDIO_CAJONES[ 74 ],# 116
    EST_MEDIO_CAJONES[ 75 ],# 117
    EST_MEDIO_CAJONES[ 76 ],# 118
    EST_MEDIO_CAJONES[ 77 ],# 119
    EST_MEDIO_CAJONES[ 78 ],# 120
    EST_MEDIO_CAJONES[ 79 ],# 121
    EST_MEDIO_CAJONES[ 80 ],# 122
    EST_MEDIO_CAJONES[ 81 ],# 123
    EST_MEDIO_CAJONES[ 82 ],# 124
    EST_MEDIO_CAJONES[ 83 ],# 125
    EST_MEDIO_CAJONES[ 84 ],# 126
    EST_MEDIO_CAJONES[ 85 ],# 127
    EST_MEDIO_CAJONES[ 86 ],# 128
    EST_MEDIO_CAJONES[ 87 ],# 129
    EST_MEDIO_CAJONES[ 88 ],# 130
    EST_MEDIO_CAJONES[ 89 ],# 131
    EST_MEDIO_CAJONES[ 90 ],# 132
    EST_MEDIO_CAJONES[ 91 ],# 133
    EST_MEDIO_CAJONES[ 92 ],# 134
    EST_MEDIO_CAJONES[ 93 ],# 135
    EST_MEDIO_CAJONES[ 94 ],# 136
    EST_MEDIO_CAJONES[ 95 ],# 137
    EST_MEDIO_CAJONES[ 96 ],# 138
    EST_MEDIO_CAJONES[ 97 ],# 139
    EST_MEDIO_CAJONES[ 98 ],# 140
    EST_MEDIO_CAJONES[ 99 ],# 141
    EST_MEDIO_CAJONES[ 100 ],# 142
    EST_MEDIO_CAJONES[ 101 ],# 143
    EST_MEDIO_CAJONES[ 102 ],# 144
    EST_MEDIO_CAJONES[ 103 ],# 145
    EST_MEDIO_CAJONES[ 104 ],# 146
    EST_MEDIO_CAJONES[ 105 ],# 147
    EST_MEDIO_CAJONES[ 106 ],# 148
    EST_MEDIO_CAJONES[ 107 ],# 149
    EST_MEDIO_CAJONES[ 108 ],# 150
    EST_MEDIO_CAJONES[ 109 ],# 151
    EST_MEDIO_CAJONES[ 110 ],# 152
    EST_MEDIO_CAJONES[ 111 ],# 153
    EST_MEDIO_CAJONES[ 112 ],# 154
    EST_MEDIO_CAJONES[ 113 ],# 155
    EST_MEDIO_CAJONES[ 114 ],# 156
    EST_MEDIO_CAJONES[ 115 ],# 157
    EST_MEDIO_CAJONES[ 116 ],# 158
    EST_MEDIO_CAJONES[ 117 ],# 159
    EST_MEDIO_CAJONES[ 118 ],# 160
    EST_MEDIO_CAJONES[ 119 ],# 161
    EST_MEDIO_CAJONES[ 120 ],# 162
    EST_MEDIO_CAJONES[ 121 ],# 163
    EST_MEDIO_CAJONES[ 122 ],# 164
    EST_MEDIO_CAJONES[ 123 ],# 165
    EST_MEDIO_CAJONES[ 124 ],# 166
    EST_MEDIO_CAJONES[ 125 ],# 167
    EST_MEDIO_CAJONES[ 126 ],# 168
    EST_MEDIO_CAJONES[ 127 ],# 169
    EST_MEDIO_CAJONES[ 128 ],# 170
    EST_MEDIO_CAJONES[ 129 ],# 171
    EST_MEDIO_CAJONES[ 130 ],# 172
    EST_MEDIO_CAJONES[ 131 ],# 173
    EST_MEDIO_CAJONES[ 132 ],# 174
    EST_MEDIO_CAJONES[ 133 ],# 175
    EST_MEDIO_CAJONES[ 134 ],# 176
    EST_MEDIO_CAJONES[ 135 ],# 177
    EST_MEDIO_CAJONES[ 136 ],# 178
    EST_MEDIO_CAJONES[ 137 ],# 179
    EST_MEDIO_CAJONES[ 138 ],# 180
    EST_MEDIO_CAJONES[ 139 ],# 181
    EST_MEDIO_CAJONES[ 140 ],# 182
    EST_MEDIO_CAJONES[ 141 ],# 183
    EST_MEDIO_CAJONES[ 142 ],# 184
    EST_MEDIO_CAJONES[ 143 ],# 185
    EST_MEDIO_CAJONES[ 144 ],# 186
    EST_MEDIO_CAJONES[ 145 ],# 187
    EST_MEDIO_CAJONES[ 146 ],# 188
    EST_MEDIO_CAJONES[ 147 ],# 189
    EST_MEDIO_CAJONES[ 148 ],# 190
    EST_MEDIO_CAJONES[ 149 ],# 191
    EST_MEDIO_CAJONES[ 150 ],# 192
    EST_MEDIO_CAJONES[ 151 ],# 193
    EST_MEDIO_CAJONES[ 152 ],# 194
    EST_MEDIO_CAJONES[ 153 ],# 195
    EST_MEDIO_CAJONES[ 154 ],# 196
    EST_MEDIO_CAJONES[ 155 ],# 197
    EST_MEDIO_CAJONES[ 156 ],# 198
    EST_MEDIO_CAJONES[ 157 ],# 199
    EST_MEDIO_CAJONES[ 158 ],# 200
    EST_MEDIO_CAJONES[ 159 ],# 201
    EST_MEDIO_CAJONES[ 160 ],# 202
    EST_MEDIO_CAJONES[ 161 ],# 203
    EST_MEDIO_CAJONES[ 162 ],# 204
    EST_MEDIO_CAJONES[ 163 ],# 205
    EST_MEDIO_CAJONES[ 164 ],# 206
    EST_MEDIO_CAJONES[ 165 ],# 207
    EST_MEDIO_CAJONES[ 166 ],# 208
    EST_MEDIO_CAJONES[ 167 ],# 209
    EST_MEDIO_CAJONES[ 168 ],# 210
    EST_MEDIO_CAJONES[ 169 ],# 211
    EST_MEDIO_CAJONES[ 170 ],# 212
    EST_MEDIO_CAJONES[ 171 ],# 213
    EST_MEDIO_CAJONES[ 172 ],# 214
    EST_MEDIO_CAJONES[ 173 ],# 215
    EST_MEDIO_CAJONES[ 174 ],# 216
    EST_MEDIO_CAJONES[ 175 ],# 217
    EST_MEDIO_CAJONES[ 176 ],# 218
    EST_MEDIO_CAJONES[ 177 ],# 219
    EST_MEDIO_CAJONES[ 178 ],# 220
    EST_MEDIO_CAJONES[ 179 ],# 221
    EST_MEDIO_CAJONES[ 180 ],# 222
    EST_MEDIO_CAJONES[ 181 ],# 223
    EST_MEDIO_CAJONES[ 182 ],# 224
    EST_MEDIO_CAJONES[ 183 ],# 225
    EST_MEDIO_CAJONES[ 184 ],# 226
    EST_MEDIO_CAJONES[ 185 ],# 227
    EST_MEDIO_CAJONES[ 186 ],# 228
    EST_MEDIO_CAJONES[ 187 ],# 229
    EST_MEDIO_CAJONES[ 188 ],# 230
    EST_MEDIO_CAJONES[ 189 ],# 231
    EST_MEDIO_CAJONES[ 190 ],# 232
    EST_MEDIO_CAJONES[ 191 ],# 233
    EST_MEDIO_CAJONES[ 192 ],# 234
    EST_MEDIO_CAJONES[ 193 ],# 235
    EST_MEDIO_CAJONES[ 194 ],# 236
    EST_MEDIO_CAJONES[ 195 ],# 237
    EST_MEDIO_CAJONES[ 196 ],# 238
    EST_MEDIO_CAJONES[ 197 ],# 239
    EST_MEDIO_CAJONES[ 198 ],# 240
    EST_MEDIO_CAJONES[ 199 ],# 241
    EST_MEDIO_CAJONES[ 200 ],# 242
    EST_MEDIO_CAJONES[ 201 ],# 243
    EST_MEDIO_CAJONES[ 202 ],# 244
    EST_MEDIO_CAJONES[ 203 ],# 245
    EST_MEDIO_CAJONES[ 204 ],# 246
    EST_MEDIO_CAJONES[ 205 ],# 247
    EST_MEDIO_CAJONES[ 206 ],# 248
    EST_MEDIO_CAJONES[ 207 ],# 249
    EST_MEDIO_CAJONES[ 208 ],# 250
    EST_MEDIO_CAJONES[ 209 ],# 251
    EST_MEDIO_CAJONES[ 210 ],# 252
    EST_MEDIO_CAJONES[ 211 ],# 253
    EST_MEDIO_CAJONES[ 212 ],# 254
    EST_MEDIO_CAJONES[ 213 ],# 255
    EST_MEDIO_CAJONES[ 214 ],# 256
    EST_MEDIO_CAJONES[ 215 ],# 257
    EST_MEDIO_CAJONES[ 216 ],# 258
    EST_MEDIO_CAJONES[ 217 ],# 259
    EST_MEDIO_CAJONES[ 218 ],# 260
    EST_MEDIO_CAJONES[ 219 ],# 261
    EST_MEDIO_CAJONES[ 220 ],# 262
    EST_MEDIO_CAJONES[ 221 ],# 263
    EST_MEDIO_CAJONES[ 222 ],# 264
    EST_MEDIO_CAJONES[ 223 ],# 265
    EST_MEDIO_CAJONES[ 224 ],# 266
    EST_MEDIO_CAJONES[ 225 ],# 267
    EST_MEDIO_CAJONES[ 226 ],# 268
    EST_MEDIO_CAJONES[ 227 ],# 269
    EST_MEDIO_CAJONES[ 228 ],# 270
    EST_MEDIO_CAJONES[ 229 ],# 271
    EST_MEDIO_CAJONES[ 230 ],# 272
    EST_MEDIO_CAJONES[ 231 ],# 273
    EST_MEDIO_CAJONES[ 232 ],# 274
    EST_MEDIO_CAJONES[ 233 ],# 275
    EST_MEDIO_CAJONES[ 234 ],# 276
    EST_MEDIO_CAJONES[ 235 ],# 277
    EST_MEDIO_CAJONES[ 236 ],# 278
    EST_MEDIO_CAJONES[ 237 ],# 279
    EST_MEDIO_CAJONES[ 238 ],# 280
    EST_MEDIO_CAJONES[ 239 ],# 281
    EST_MEDIO_CAJONES[ 240 ],# 282
    EST_MEDIO_CAJONES[ 241 ],# 283
    EST_MEDIO_CAJONES[ 242 ],# 284
    EST_MEDIO_CAJONES[ 243 ],# 285
    EST_MEDIO_CAJONES[ 244 ],# 286
    EST_MEDIO_CAJONES[ 245 ],# 287
    EST_MEDIO_CAJONES[ 246 ],# 288
    EST_MEDIO_CAJONES[ 247 ],# 289
    EST_MEDIO_CAJONES[ 248 ],# 290
    EST_MEDIO_CAJONES[ 249 ],# 291
    EST_MEDIO_CAJONES[ 250 ],# 292
    EST_MEDIO_CAJONES[ 251 ],# 293
    EST_MEDIO_CAJONES[ 252 ],# 294
    EST_MEDIO_CAJONES[ 253 ],# 295
    EST_MEDIO_CAJONES[ 254 ],# 296
    EST_MEDIO_CAJONES[ 255 ],# 297
    EST_MEDIO_CAJONES[ 256 ],# 298
    EST_MEDIO_CAJONES[ 257 ],# 299
    EST_MEDIO_CAJONES[ 258 ],# 300
    EST_MEDIO_CAJONES[ 259 ],# 301
    EST_MEDIO_CAJONES[ 260 ],# 302
    EST_MEDIO_CAJONES[ 261 ],# 303
    EST_MEDIO_CAJONES[ 262 ],# 304
    EST_MEDIO_CAJONES[ 263 ],# 305
    EST_MEDIO_CAJONES[ 264 ],# 306
    EST_MEDIO_CAJONES[ 265 ],# 307
    EST_MEDIO_CAJONES[ 266 ],# 308
    EST_MEDIO_CAJONES[ 267 ],# 309
    EST_MEDIO_CAJONES[ 268 ],# 310
    EST_MEDIO_CAJONES[ 269 ],# 311
    EST_MEDIO_CAJONES[ 270 ],# 312
    EST_MEDIO_CAJONES[ 271 ],# 313
    EST_MEDIO_CAJONES[ 272 ],# 314
    EST_MEDIO_CAJONES[ 273 ],# 315
    EST_MEDIO_CAJONES[ 274 ],# 316
    EST_MEDIO_CAJONES[ 275 ],# 317
    EST_MEDIO_CAJONES[ 276 ],# 318
    EST_MEDIO_CAJONES[ 277 ],# 319
    EST_MEDIO_CAJONES[ 278 ],# 320
    EST_MEDIO_CAJONES[ 279 ],# 321
    EST_MEDIO_CAJONES[ 280 ],# 322
    EST_MEDIO_CAJONES[ 281 ],# 323
    EST_MEDIO_CAJONES[ 282 ],# 324
    EST_MEDIO_CAJONES[ 283 ],# 325
    EST_MEDIO_CAJONES[ 284 ],# 326
    EST_MEDIO_CAJONES[ 285 ],# 327
    EST_MEDIO_CAJONES[ 286 ],# 328
    EST_MEDIO_CAJONES[ 287 ],# 329
    EST_MEDIO_CAJONES[ 288 ],# 330
    EST_MEDIO_CAJONES[ 289 ],# 331
    EST_MEDIO_CAJONES[ 290 ],# 332
    EST_MEDIO_CAJONES[ 291 ],# 333
    EST_MEDIO_CAJONES[ 292 ],# 334
    EST_MEDIO_CAJONES[ 293 ],# 335
    EST_MEDIO_CAJONES[ 294 ],# 336
    EST_MEDIO_CAJONES[ 295 ],# 337
    EST_MEDIO_CAJONES[ 296 ],# 338
    EST_MEDIO_CAJONES[ 297 ],# 339
    EST_MEDIO_CAJONES[ 298 ],# 340
    EST_MEDIO_CAJONES[ 299 ],# 341
    EST_MEDIO_CAJONES[ 300 ],# 342
    EST_MEDIO_CAJONES[ 301 ],# 343
    EST_MEDIO_CAJONES[ 302 ],# 344
    EST_MEDIO_CAJONES[ 303 ],# 345
    EST_MEDIO_CAJONES[ 304 ],# 346
    EST_MEDIO_CAJONES[ 305 ],# 347
    EST_MEDIO_CAJONES[ 306 ],# 348
    EST_MEDIO_CAJONES[ 307 ],# 349
    EST_MEDIO_CAJONES[ 308 ],# 350
    EST_MEDIO_CAJONES[ 309 ],# 351
    EST_MEDIO_CAJONES[ 310 ],# 352
    EST_MEDIO_CAJONES[ 311 ],# 353
    EST_MEDIO_CAJONES[ 312 ],# 354
    EST_MEDIO_CAJONES[ 313 ],# 355
    EST_MEDIO_CAJONES[ 314 ],# 356
    EST_MEDIO_CAJONES[ 315 ],# 357
    EST_MEDIO_CAJONES[ 316 ],# 358
    EST_MEDIO_CAJONES[ 317 ],# 359
    EST_MEDIO_CAJONES[ 318 ],# 360
    EST_MEDIO_CAJONES[ 319 ],# 361
    EST_MEDIO_CAJONES[ 320 ],# 362
    EST_MEDIO_CAJONES[ 321 ],# 363
    EST_MEDIO_CAJONES[ 322 ],# 364
    EST_MEDIO_CAJONES[ 323 ],# 365
    EST_MEDIO_CAJONES[ 324 ],# 366
    EST_MEDIO_CAJONES[ 325 ],# 367
    EST_MEDIO_CAJONES[ 326 ],# 368
    EST_MEDIO_CAJONES[ 327 ],# 369
    EST_MEDIO_CAJONES[ 328 ],# 370
    EST_MEDIO_CAJONES[ 329 ],# 371
    EST_MEDIO_CAJONES[ 330 ],# 372
    EST_MEDIO_CAJONES[ 331 ],# 373
    EST_MEDIO_CAJONES[ 332 ],# 374
    EST_MEDIO_CAJONES[ 333 ],# 375
    EST_MEDIO_CAJONES[ 334 ],# 376
    EST_MEDIO_CAJONES[ 335 ],# 377
    EST_MEDIO_CAJONES[ 336 ],# 378
    EST_MEDIO_CAJONES[ 337 ],# 379
    EST_MEDIO_CAJONES[ 338 ],# 380
    EST_MEDIO_CAJONES[ 339 ],# 381
    EST_MEDIO_CAJONES[ 340 ],# 382
    EST_MEDIO_CAJONES[ 341 ],# 383  
    EST_MEDIO_CAJONES[ 342 ],# 384
    EST_MEDIO_CAJONES[ 343 ],# 385
    EST_MEDIO_CAJONES[ 344 ],# 386      
    EST_MEDIO_CAJONES[ 345 ],# 387
    EST_MEDIO_CAJONES[ 346 ],# 388
    EST_MEDIO_CAJONES[ 347 ],# 389      
    EST_MEDIO_CAJONES[ 348 ],# 390
    EST_MEDIO_CAJONES[ 349 ],# 391
    EST_MEDIO_CAJONES[ 350 ],# 392
    EST_MEDIO_CAJONES[ 351 ],# 393
    EST_MEDIO_CAJONES[ 352 ],# 394
    EST_MEDIO_CAJONES[ 353 ],# 395
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

