#!/usr/bin/env python3
import math

# Funktion 'zeichnet' Dreieck aus drei übergebenen Punkten

def vertex(one, two, three):
    file.write('facet normal 0.0 0.0 0.0\n')
    file.write('outer loop\n')
    file.write('vertex ' + one + '\n')
    file.write('vertex ' + two + '\n')
    file.write('vertex ' + three + '\n')
    file.write('endloop\n')
    file.write('endfacet\n')

# 'Zeichnet' Quader
# in den for-Schleifen werden die gegenüberliegenden Seiten 'gezeichnet'

def quader(length, width, height):
    for i in range(2):
        height = str(height)
        length = str(length)
        width = str(width)
        z = ('0.0' if i == 0 else height)
        vertex('0.0 0.0 ' + z, length + ' 0.0 ' + z, '0.0 ' + width + ' ' + z)
        vertex(length + ' ' + width + ' ' + z, length + ' 0.0 ' + z, '0.0 ' + width + ' ' + z)
        x = ('0.0' if i == 0 else length)
        vertex(x + ' 0.0 0.0', x + ' ' + width + ' 0.0', x + ' 0.0 ' + height)
        vertex(x + ' ' + width + ' ' + height, x + ' ' + width + ' 0.0', x + ' 0.0 ' + height)
        y = ('0.0' if i == 0 else width)
        vertex('0.0 ' + y + ' 0.0', length + ' ' + y + ' 0.0', '0.0 ' + y + ' ' + height)
        vertex(length + ' ' + y + ' ' + height, length + ' ' + y + ' 0.0', '0.0 ' + y + ' ' + height)
    
# 'Zeichnet' Zylinder
# zuerst Berechnung, welchen Winkel die einzelnen Segmente haben
# Berechnung erstes Segment
# dann jeweils Spiegelung des Punktes am neu berechneten Punkt für die restlichen Segmente

def cylinder(corners):
    Px = 1.0
    Py = 0.0
    angle = 360 / corners
    Qx = round((Px * math.cos(angle * math.pi / 180) + Py * math.sin(angle * math.pi / 180))/math.sqrt(Px * Px + Py * Py), 5)
    Qy = round((Py * math.cos(angle * math.pi / 180) + Px * math.sin(angle * math.pi / 180))/math.sqrt(Px * Px + Py * Py), 5)
    for z in range(2) :
        vertex(str(Px) + ' ' + str(Py) + ' ' + str(z), str(Qx) + ' ' + str(Qy) + ' ' + str(z), '0.0 0.0 ' + str(z))
        if z == 0:
            vertex(str(Px) + ' ' + str(Py) + ' ' + str(z), str(Qx) + ' ' + str(Qy) + ' ' + str(z), str(Px) + ' ' + str(Py) + ' ' + str(1))
        else:
            vertex(str(Px) + ' ' + str(Py) + ' ' + str(z), str(Qx) + ' ' + str(Qy) + ' ' + str(z), str(Qx) + ' ' + str(Qy) + ' ' + str(0))
        for i in range(corners - 1) :
            t = ( Qx * Px + Qy * Py ) / (Qx * Qx + Qy * Qy)
            Sx = t * Qx
            Sy = t * Qy
            Rx = Px + 2*(Sx - Px)
            Ry = Py + 2*(Sy - Py)
            vertex(str(Qx) + ' ' + str(Qy) + ' ' + str(z), str(Rx) + ' ' + str(Ry) + ' ' + str(z), '0.0 0.0 ' + str(z))
            if z == 0:
                vertex(str(Qx) + ' ' + str(Qy) + ' ' + str(z), str(Rx) + ' ' + str(Ry) + ' ' + str(z), str(Qx) + ' ' + str(Qy) + ' ' + str(1))
            else:
                vertex(str(Qx) + ' ' + str(Qy) + ' ' + str(z), str(Rx) + ' ' + str(Ry) + ' ' + str(z), str(Rx) + ' ' + str(Ry) + ' ' + str(0))
            Px = Qx
            Py = Qy
            Qx = Rx
            Qy = Ry

eingabe = input('Welcher Körper soll erzeugt werden? (Zylinder / Quader) ')
if eingabe == 'Zylinder':
    ecken = input('Wie viele Ecken soll die Grundfläche haben? (> 2) ')
    ecken = int(ecken)
    file = open('Alexander_Vollrath_Zylinder.stl', 'w')
    file.write('solid cylinder\n')
    cylinder(ecken)
    file.write('endsolid')
    file.close()
    print('Erstellung erfolgreich')
elif eingabe == 'Quader':
    length = input('Länge? ')
    length = float(length)
    width = input('Breite? ')
    width = float(width)
    height = input('Höhe? ')
    height = float(height)
    file = open('Alexander_Vollrath_Zylinder.stl', 'w')
    file.write('solid cylinder\n')
    quader(length, width, height)
    file.write('endsolid')
    file.close()
    print('Erstellung erfolgreich')
else:
    print('Falsche Eingabe')
