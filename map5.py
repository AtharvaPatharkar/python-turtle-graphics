from turtle import *

hideturtle()
speed(0)

Screen().bgcolor('black')

def myposition(x, y):
    penup()
    goto(x - 300, (y * -1) + 365)
    pendown()


def positions():
    positions.upper_india =[(157, 473), (157, 469), (155, 464), (156, 461), (154, 457), (151, 452), (153, 449), (149, 445), (149, 440),
                            (148, 434), (148, 428), (148, 424), (146, 420), (148, 416), (148, 410), (151, 406), (147, 395), (147, 391), 
                            (149, 389), (149, 385), (146, 383), (149, 379), (146, 378), (146, 375), (144, 378), (143, 383), (144, 388),
                            (140, 394), (134, 398), (129, 399), (126, 402), (118, 402), (115, 404), (107, 399), (96, 388) , (90, 381) ,
                            (86, 376) , (82, 372) , (80, 366) , (83, 363) , (86, 363) , (89, 366) , (97, 365) , (104, 362), (108, 359),
                            (108, 356), (100, 358), (91, 361) , (82, 356) , (77, 352) , (71, 343) , (66, 341) , (69, 339) , (69, 332) , 
                            (78, 333) , (78, 327) , (82, 325) , (93, 329) , (96, 327) , (100, 332), (104, 332), (105, 329), (109, 328),
                            (116, 326), (118, 330), (122, 326), (122, 321), (116, 309), (117, 305), (112, 305), (106, 295), (108, 286),  
                            (99, 282) ,  (96, 276),  (99, 270), (106, 266), (111, 259), (122, 255), (123, 263), (128, 260), (141, 259), 
                            (143, 255), (148, 252), (148, 247), (153, 241), (159, 241), (169, 228), (168, 224), (173, 219), (180, 216), 
                            (180, 210), (186, 205), (189, 198), (191, 190), (190, 185), (199, 178), (205, 178), (204, 173), (194, 170), 
                            (194, 165), (188, 165), (185, 162), (175, 158), (177, 150), (174, 141), (177, 136), (174, 132), (174, 127), 
                            (188, 118), (183, 117), (179, 113), (178, 109), (176, 111), (170, 103), (162, 103),  (160, 95),  (167, 92),  
                            (168, 87) ,  (171, 84),  (182, 84),  (191, 80), (198, 78) , (208, 79) ,  (218, 90),  (227, 95),  (231, 98), 
                            (234, 104), (241, 106), (244, 111), (253, 109), (257, 105), (265, 101), (271, 103),  (275, 99), (283, 104), 
                            (291, 110), (291, 116), (287, 121), (287, 127), (282, 127), (282, 131), (278, 131), (274, 141), (268, 139), 
                            (266, 142), (269, 144), (266, 153), (274, 156), (274, 161), (278, 169), (269, 172), (270, 176), (266, 176), 
                            (262, 169), (260, 175), (264, 182), (265, 189), (266, 196), (270, 191), 
    ]

    positions.mid_india =    [  
                            (270, 191), (273, 195), (274, 199), (286, 203), (289, 210), (296, 211), (300, 217), (298, 222), (291, 230), 
                            (304, 251), (309, 257), (322, 262), (335, 266), (343, 270), (355, 267), (365, 270), (371, 278), (379, 281), 
                            (390, 282), (401, 285), (422, 287), (422, 277), (419, 271), (424, 261), (422, 255), (428, 255), (432, 251), 
                            (435, 257), (433, 263), (437, 267), (435, 270), (442, 276), (446, 273), (451, 278), (460, 273), (471, 274), 
                            (489, 270), (487, 262), (479, 260), (478, 253), (484, 255), (494, 252), (497, 250), (496, 246), (501, 241), 
                            (505, 242), (505, 235), (516, 233), (521, 228), (528, 220), (541, 223), (550, 214), (556, 218), (554, 224), 
                            (558, 222), (561, 228), (556, 235), (574, 237), (574, 241), (567, 251), (573, 260), (568, 260), (565, 256),
                            (557, 259), (546, 273), (540, 275), (542, 285), (539, 295), (534, 301), (537, 303), (537, 311), (535, 316), 
                            (532, 328), (524, 329), (519, 329), (519, 348), (513, 351), (516, 367), (514, 374), (509, 372), (506, 375), 
                            (504, 372), (502, 360), (500, 352), (500, 346), (498, 343), (495, 337), (489, 353), (479, 350), (480, 343), 
                            (476, 336), (478, 329), (487, 324), (491, 320), (495, 315), (494, 309), (486, 310), (465, 310), (454, 310),
                            (452, 306), (454, 300), (452, 298), (452, 292), (448, 295), (439, 290), (437, 293), (435, 294), (430, 289), 
                            (426, 297), (432, 301), (436, 301), (440, 304), (441, 310), (433, 313), (431, 318), (427, 319), (430, 326), 
                            (438, 326), (437, 336), (435, 338), (439, 342), (440, 347), (444, 350), (443, 362), (447, 370), (444, 377), 
                            (438, 374), (157, 473),
                            
   ]

    positions.lower_india = [
                            (429, 377), (426, 384), (413, 387), (414, 395), (414, 401), (408, 411), (401, 417), (390, 422), 
                            (380, 428), (372, 438), (367, 447), (357, 451), (350, 461), (342, 466), (335, 471), (330,480) ,(335,  480),
                            (340,485) , (335,490) , (330,495) ,  (325,500), (325,502) ,  (328,505), (324,507) , (330,508) , (325,510) ,
                            (320,512) , (310,517) , (305,520) ,(300,524)  , (301,526) ,(295,530)  , (290,534) , (285,536) ,(285,540)  ,
                            (282,545) , (280,550) , (278,555) ,(276,560)  , (276,565) , (276,570) , (275,575) ,  (275,580),(276,585)  ,
                            (279,590) , (275,595) , (274,600) ,(274, 604) , (272, 602),(274, 604) , (267, 614), (271, 620), (254, 623), 
                            (252, 627),  (251, 636), (243, 639),(238, 643), (229, 639), (227, 635), (223, 634), (216, 628), (213, 622),
                            (213, 615), (208, 602), (213, 605) ,(207, 596), (206, 590), (205,585) ,(204,580)  ,(203,578)   ,(202,575)  ,
                            (202,572) ,(200,570)  ,(197,567)   ,(195,565)  , (190,560),
                            (188,558) ,(185,555)  ,(180,550)   ,(177,547)  ,(177,550)  ,(175,546)  ,(173,540)   ,(171,535)  ,(169,540) ,
                            (167,534) ,(166,530)  ,  (165,526) ,(162,520)  ,(164,520)  ,(165,524)  ,(162,520)   ,(160,518)  ,(160,515) ,
                            (159,508) , (159,502) ,(159,509)   ,(158,501)  ,(158,495)  ,(159,490)  ,(158,484)   ,(158,480)  ,(159,478) ,
                            (158,475) , (157, 473),
]

    
   

def color_fill(coordinates, co = (0, 0, 0)):
    color(co)
    p_x, p_y = coordinates[0]
    myposition(p_x, p_y)
    fillcolor(co)
    begin_fill()
    t = 0
    for i in coordinates[1:]:
        x, y = i
        if t:
            myposition(x, y)
            t = 0
            begin_fill()
            continue

        if x == -1 and y == -1:
            t = 1
            end_fill()
            continue
        else:
            goto(x - 300, (y * -1) + 365)
    end_fill()


def draw(coordinates, mode = 1, co = (0, 0, 0), thickness = 1):
    co = (co[0] / 255, co[1] / 255, co[2] / 255)
    color(co)

    if mode:
        width(thickness)
        p_x, p_y = coordinates[0]
        myposition(p_x, p_y)
        t = 0
        for i in coordinates[1:]:
            x, y = i
            if t:
                myposition(x, y)
                t = 0
                continue

            if x == -1 and y == -1:
                t = 1
                continue
            else:
                goto(x - 300, (y * -1) + 365)
    else:
        color_fill(coordinates, co)


def files():
    positions()
    draw(positions.upper_india, co = (255, 167, 31), mode = 0)
    draw(positions.mid_india, co = (255,255,255), mode = 0)
    draw(positions.lower_india, co = (1, 174, 59 ), mode = 0)

  
files()





def draw_circle(radius):
    penup()
    goto(-10, -radius+20)
    pendown()
    circle(radius)
    penup()
    goto(-10, 20)
    pendown()

def draw_spoke(length):
    penup()
    goto(-10, 20)
    pendown()
    forward(length)
    penup()
    goto(-10, 20)
    pendown()

def draw_ashoka_chakra():
  
    pensize(5)
    color("blue")

    # Draw the outer circle of the Ashoka Chakra
    draw_circle(75)

    # Draw the 24 spokes
    for _ in range(24):
        draw_spoke(75)
        right(360 / 24)

    hideturtle()

if __name__ == "__main__":
    setup(width=500, height=500)
    title("Ashoka Chakra")
    draw_ashoka_chakra()
  

done()