import sys
sys.path.append('/opt/mycroft/skills/iRobotSkill')

from os.path import dirname

import create_python2
import time


try:
    open('grid.txt', 'r')
    lines = open('grid.txt', 'r').readlines()
    w = lines[0]
    h = lines[1]
    ct = lines[2]
    a =lines[3]
    #lines[3] = gt # get goToTile from user
    gt = getGoToTile

except IOError:
    # file grid.txt does not exist since we are starting from scratch
    # initial starting point of 0
    ct = 0
    # initial angle of 0
    a = 0
    # get grid size and tile to go to
    w = getWidth
    h = getHeight
    gt = getGoToTile


def grid(w, h, ct, gt, a):
    width = w
    height = h
    #tile = t
    currentTile = ct
    goToTile = gt
    angle = a

    maxTile = width * height
    # get coordinates of current and goTo tiles
    currentRow = (currentTile - 1) // w
    currentCol = (currentTile - 1) % w

    goToTileRow = (goToTile - 1) // w
    goToTileCol = (goToTile - 1) % w

    currentRowCoord = currentRow + 0.5
    currentColCoord = currentCol + 0.5

    goToTileRowCoord = goToTileRow + 0.5
    goToTileColCoord = goToTileCol + 0.5

    # calculate travel distance
    if goToTileRowCoord > currentRowCoord:
        xDistance = goToTileRowCoord - currentRowCoord
    elif goToTileColCoord < currentRowCoord:
        xDistance = currentRowCoord - goToTileRowCoord

    if goToTileColCoord > currentColCoord:
        yDistance = goToTileColCoord - currentColCoord
    elif goToTileColCoord < currentColCoord:
        yDistance = currentColCoord - goToTileColCoord

    # convert x and y Distances to real world distances
    xMovement = xDistance * 300
    yMovement = yDistance * 300

    # put robot in center of tile
    #hCoord = row + 0.5
    #vCoord = col + 0.5

    # set starting from coordinate (0,0), upper right hand corner of grid
    #startHCoord = 0
    #startVCoord = 0

    # set real world distances of coordinates in milimeters, current size of
    # tile is 300mmx300mm, will change as needed
    #hCoordRW = hCoord * 300
    #vCoordRW = vCoord * 300

    # check for edges
    if row == 0:
        isRowEdge = "yes"
        rowEdge = "top"
    elif row == (h - 1):
        isRowEdge = "yes"
        rowEdge = "bottom"
    else:
        isRowEdge = "no"
        rowLocation = "middle"

    if col == 0:
        isColEdge = "yes"
        colEdge = "Left"
    elif col == (w - 1):
        isColEdge = "yes"
        colEdge = "Right"
    else:
        isColEdge = "no"
        colLocation = "middle"

    if ((rowEdge == "top") & (colEdge == "left")):
        isCorner = "yes"
        corner = "upperLeft"
    elif ((rowEdge == "top") & (colEdge == "right")):
        isCorner = "yes"
        corner = "upperRight"
    elif ((rowEdge == "bottom") & (colEdge == "left")):
        isCorner = "yes"
        corner = "bottomLeft"
    elif ((rowEdge == "bottom") & (colEdge == "right")):
        isCorner = "yes"
        corner = "bottomRight"
    else:
        isCorner = "no"

    # get current angle while accounting for value of angle while angle >= 360
    #while angle >= 360:
    #    # make angle a more managable value
    #    angle = angle - 360

    # make negative angles more managable
    #while angle < 0:
    #    angle = angle + 360


    # movement to next tile based on current tile
    # NOTE: since robot is only programmed to go forward
    # there are only two angles to program for rotating
    # both angles point outside of the grid
    # TODO check if manually setting angle makes more sense than performing math
    # on it
    if isCorner == "yes":
        if corner == "upperLeft":
            if angle == 180:
                if currentRowCoord == goToTileRowCoord:
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                elif currentColCoord == goToTileColCoord:
                    robot.go(0, 45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle + 180
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
                else:
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 0
                    robot.go(yMovement, 0)
                    robot.sleep(1)
                    robot.stop()
            elif angle == 270:
                if currentRowCoord == goToTileRowCoord:
                    robot.go(0, -45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle - 180
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                elif currentColCoord == goToTileColCoord:
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
                else:
                    robot.go(0, -45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle - 180
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 0
                    robot.go(yMovement, 0)
                    robot.sleep(1)
                    robot.stop()
        elif corner == "upperRight":
            if angle == 90:
                if currentRowCoord == goToTileRowCoord:
                    robot.go(0, -45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle - 180
                    angle = 270
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                elif currentColCoord == goToTileColCoord:
                    robot.go(0, -45)
                    time.sleep(2)
                    #angle = angle - 90
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
                else:
                    robot.go(0, -45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle - 180
                    angle = 270
                    robot.stop()
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
            elif angle == 180:
                if currentRowCoord == goToTileRowCoord:
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 270
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                elif currentColCoord == goToTileColCoord:
                    robot.go(0, -45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle - 180
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop
                else:
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 270
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop()
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
        elif corner == "bottomLeft":
            if ((angle == 0) | (angle == 360)):
                if (currentRowCoord == goToTileRowCoord):
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop
                elif (currentColCoord == goToTileColCoord):
                    robot.go(0, 45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle + 180
                    angle = 180
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop
                else:
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 180
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
            elif angle == 270:
                if (currentRowCoord == goToTileRowCoord):
                    robot.go(0, -45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle - 180
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop
                elif (currentColCoord == goToTileColCoord):
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop
                else:
                    robot.go(0, 45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle + 180
                    angle = 90
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 180
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
        elif corner == "bottomRight":
            if ((angle == 0) | (angle == 360)):
                if (currentRowCoord == goToTileRowCoord):
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 270
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop
                elif (currentColCoord == goToTileColCoord):
                    robot.go(0, 90)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 180
                    angle = 180
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop
                else:
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 270
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 180
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
            elif angle == 90:
                if (currentRowCoord == goToTileRowCoord):
                    robot.go(0, 45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle + 180
                    angle = 270
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.stop
                elif (currentColCoord == goToTileColCoord):
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle + 90
                    angle = 180
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop
                else:
                    robot.go(0, 45)
                    time.sleep(4)
                    robot.stop()
                    #angle = angle + 180
                    angle = 270
                    robot.go(xMovement, 0)
                    time.sleep(1)
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    #angle = angle - 90
                    angle = 180
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
    elif isCorner == "no":
        if isRowEdge == "yes":
                if currentRowCoord == goToTileRowCoord:
                    if currentColCoord > goToTileColCoord:
                        if angle == 90:
                            robot.go(0, -45)
                            time.sleep(4)
                            robot.stop()
                            angle == 270
                            robot.go(xMovement, 0)
                        elif 180:
                            robot.go(0, 45)
                            time.sleep(2)
                            angle = 270
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 270:
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
                    if currentColCoord < goToTileColCoord:
                        if angle == 90:
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 180:
                            robot.go(0, -45)
                            time.sleep(2)
                            robot.stop()
                            angle = 90
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
                    if currentColCoord == goToTileColCoord:
                        # since all the coordinates are the same, don't move
                        pass
                elif currentColCoord == goToTileColCoord:
                    if angle == 90:
                        robot.go(0, -45)
                        time.sleep(2)
                        robot.stop()
                        angle = 0
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 180:
                        robot.go(0, -45)
                        time.sleep(4)
                        robot.stop()
                        angle = 0
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 270:
                        robot.go(0, 45)
                        time.sleep(2)
                        robot.stop()
                        angle = 0
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                else:
                    if currentRowCoord > goToTileRowCoord:
                        if angle == 90:
                            robot.go(0, -45)
                            time.sleep(2)
                            robot.stop()
                            angle = 0
                            robot.go(yMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 180:
                            robot.go(0, -45)
                            time.sleep(4)
                            robot.stop()
                            angle = 0
                            robot.go(yMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 270:
                            robot.go(0, 45)
                            time.sleep(2)
                            robot.stop()
                            angle = 0
                            robot.go(yMovement, 0)
                            time.sleep(1)
                            robot.stop
                    elif currentRowCoord < goToTileRowCoord:
                        if angle == 0:
                            robot.go(0, -45)
                            time.sleep(4)
                            robot.stop()
                            angle = 180
                            robot.go(yMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 90:
                            robot.go(0, 45)
                            time.sleep(2)
                            robot.stop()
                            angle = 180
                            robot.go(yMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 270:
                            robot.go(0, -45)
                            time.sleep(2)
                            robot.stop()
                            angle = 180
                            robot.go(yMovement, 0)
                            time.sleep(1)
                            robot.stop()
                    if currentColCoord > goToTileColCoord:
                        if angle == 90:
                            robot.go(0, -45)
                            time.sleep(4)
                            robot.stop()
                            angle == 270
                            robot.go(xMovement, 0)
                        elif 180:
                            robot.go(0, 45)
                            time.sleep(2)
                            angle = 270
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 0:
                            robot.go(0, -45)
                            time.sleep(2)
                            robot.stop()
                            angle = 270
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
                    elif currentColCoord < goToTileColCoord:
                        if angle == 0:
                            robot.go(0, 45)
                            time.sleep(2)
                            robot.stop()
                            angle = 90
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
                        elif angle == 180:
                            robot.go(0, -45)
                            time.sleep(2)
                            robot.stop()
                            angle = 90
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop
                        elif angle == 270:
                            robot.go(0, 45)
                            time.sleep(4)
                            robot.stop()
                            angle = 90
                            robot.go(xMovement, 0)
                            time.sleep(1)
                            robot.stop()
        elif isColEdge == "yes":
            if currentColCoord == goToTileColCoord:
                if currentRowCoord > goToTileRowCoord:
                    if angle == 270:
                        robot.go(0, -45)
                        time.sleep(4)
                        robot.stop()
                        angle == 90
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif 0:
                        robot.go(0, 45)
                        time.sleep(2)
                        robot.stop()
                        angle == 90
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 180:
                        robot.go(0, 45)
                        time.sleep(2)
                        robot.stop()
                        angle == 90
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                if currentRowCoord < goToTileRowCoord:
                    if angle == 90:
                        robot.go(0, -45)
                        time.sleep(4)
                        robot.stop()
                        angle == 270
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 180:
                        robot.go(0, -45)
                        time.sleep(2)
                        robot.stop()
                        angle == 270
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 0:
                        robot.go(0, -45)
                        time.sleep(2)
                        robot.stop()
                        angle == 270
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                if currentRowCoord == goToTileRowCoord:
                    # since all the coordinates are the same, don't move
                    pass
            elif currentRowCoord == goToTileRowCoord:
                if angle == 90:
                    robot.go(0, -45)
                    time.sleep(2)
                    robot.stop()
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
                elif angle == 180:
                    robot.go(0, -45)
                    time.sleep(4)
                    robot.stop()
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
                elif angle == 270:
                    robot.go(0, 45)
                    time.sleep(2)
                    robot.stop()
                    angle = 0
                    robot.go(yMovement, 0)
                    time.sleep(1)
                    robot.stop()
            else:
                if currentColCoord > goToTileColCoord:
                    if angle == 90:
                        robot.go(0, -45)
                        time.sleep(2)
                        robot.stop()
                        angle = 0
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 180:
                        robot.go(0, -45)
                        time.sleep(4)
                        robot.stop()
                        angle = 0
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 270:
                        robot.go(0, 45)
                        time.sleep(2)
                        robot.stop()
                        angle = 0
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                elif currentColCoord < goToTileColCoord:
                    if angle == 0:
                        robot.go(0, -45)
                        time.sleep(4)
                        robot.stop()
                        angle = 180
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 90:
                        robot.go(0, 45)
                        time.sleep(2)
                        robot.stop()
                        angle = 180
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 270:
                        robot.go(0, -45)
                        time.sleep(2)
                        robot.stop()
                        angle = 180
                        robot.go(yMovement, 0)
                        time.sleep(1)
                        robot.stop()
                if currentRowCoord > goToTileRowCoord:
                    if angle == 90:
                        robot.go(0, -45)
                        time.sleep(4)
                        robot.stop()
                        angle == 270
                        robot.go(xMovement, 0)
                    elif 180:
                        robot.go(0, 45)
                        time.sleep(2)
                        angle = 270
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 0:
                        robot.go(0, -45)
                        time.sleep(2)
                        robot.stop()
                        angle = 270
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                elif currentRowCoord < goToTileRowCoord:
                    if angle == 0:
                        robot.go(0, 45)
                        time.sleep(2)
                        robot.stop()
                        angle = 90
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()
                    elif angle == 180:
                        robot.go(0, -45)
                        time.sleep(2)
                        robot.stop()
                        angle = 90
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop
                    elif angle == 270:
                        robot.go(0, 45)
                        time.sleep(4)
                        robot.stop()
                        angle = 90
                        robot.go(xMovement, 0)
                        time.sleep(1)
                        robot.stop()



    # move robot vertically
    #vTime = vCoord / 150
    #robot.go(150, 0)
    #time.sleep(vTime)
    #robot.stop()

    # move robot horizontally
    #robot.go(0, 45)
    # for every angle change made, update the current angle
    # turning clockwise increases angle while going counterclockwise reduces it
    #angle = angle + 90
    #time.sleep(2)
    #robot.stop()
    #hTime = hCoord / 150
    #robot.go(150, 0)
    #time.sleep(hTime)
    #robot.stop()


    #psuedocode for handling edges and corners
    # if at bottom row:
    #    if current angle is 0 or multiple of 360:
    #       if at leftbottom:
    #           rotate right or 180 degrees
    #           move toward desired tile
    #       elif at rightbottom:
    #           rotate left or 180 degrees
    #           move toward desired tile
    #       elif at middle bottom:
    #           rotate left, right or 180 degrees based on desired tile
    # if at top row:
    #   if current angle is 180 or multiple of 180:
    #       if at top left:
    #           rotate right or 180 degrees
    #       elif at top right:
    #           rotate left or 180 degrees
    #       elif at top middle:
    #           rotate left, right or 180 degrees based on desired tile
    # elif at left column middle:
    #   if current angle is 90 or multiple of 90:
    #       rotate, left, right, or 180 based on desired tile
    # elif at right column middle:
    #   if current angle is 270 or multiple of 270:
    #       rotate left, right, or 180 degrees
