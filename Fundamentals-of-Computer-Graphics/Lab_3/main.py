import sys
import math
import numpy as np
from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *


R = 2.0
H = 3.0
K = R / H
EPS = 1e-9

PLANE_Z = -6.0
GRID_N = 80
SPAN = 3.0

points_near = []
points_far = []


def intersect_cone(origin, direction):

    ox, oy, oz = origin
    dx, dy, dz = direction

    a = dx * dx + dz * dz - K * K * dy * dy
    b = 2.0 * (ox * dx + oz * dz - K * K * (oy - H) * dy)
    c = ox * ox + oz * oz - K * K * (oy - H) ** 2

    ts = []


    if abs(a) < EPS:
        if abs(b) < EPS:
            return ts
        t = -c / b
        if t > EPS:
            ts.append(t)
    else:
        disc = b * b - 4.0 * a * c
        if disc < -EPS:
            return ts
        if abs(disc) <= EPS:
            disc = 0.0
            t = -b / (2.0 * a)
            if t > EPS:
                ts.append(t)
        else:
            sq = math.sqrt(disc)
            t1 = (-b - sq) / (2.0 * a)
            t2 = (-b + sq) / (2.0 * a)
            for t in (t1, t2):
                if t > EPS:
                    ts.append(t)


    result = []
    for t in ts:
        y = oy + t * dy
        if -EPS <= y <= H + EPS:
            result.append(t)
    return result


def cast_rays():
    global points_near, points_far
    points_near, points_far = [], []

    step = 2.0 * SPAN / (GRID_N - 1)
    direction = (0.0, 0.0, 1.0)

    for i in range(GRID_N):
        for j in range(GRID_N):
            x = -SPAN + i * step
            y = -SPAN + j * step
            origin = (x, y, PLANE_Z)

            ts = intersect_cone(origin, direction)
            if not ts:
                continue

            ts.sort()
            t_near = ts[0]
            p_near = (x, y, PLANE_Z + t_near)
            points_near.append(p_near)

            if len(ts) > 1 and (ts[1] - ts[0]) > 1e-4:
                t_far = ts[1]
                p_far = (x, y, PLANE_Z + t_far)
                points_far.append(p_far)


def init():
    glClearColor(0.05, 0.05, 0.08, 1.0)
    glEnable(GL_DEPTH_TEST)
    glPointSize(2.5)


def draw_points(pts, color):
    glColor3f(*color)
    glBegin(GL_POINTS)
    for p in pts:
        glVertex3f(*p)
    glEnd()


def display():
    glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
    glLoadIdentity()

    gluLookAt(8.0, 6.0, 12.0,
              0.0, 1.5, 0.0,
              0.0, 1.0, 0.0)

    draw_points(points_near, (1.0, 0.85, 0.2))
    draw_points(points_far, (0.2, 0.45, 1.0))

    glBegin(GL_LINES)
    glColor3f(0.6, 0.0, 0.0); glVertex3f(0, 0, 0); glVertex3f(4, 0, 0)
    glColor3f(0.0, 0.6, 0.0); glVertex3f(0, 0, 0); glVertex3f(0, 4, 0)
    glColor3f(0.0, 0.0, 0.6); glVertex3f(0, 0, 0); glVertex3f(0, 0, 4)
    glEnd()

    glutSwapBuffers()


def reshape(w, h):
    if h == 0:
        h = 1
    glViewport(0, 0, w, h)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    gluPerspective(45.0, w / h, 0.1, 100.0)
    glMatrixMode(GL_MODELVIEW)


def main():
    print("Строим точки методом ray casting...")
    cast_rays()
    print(f"Точек на ближней поверхности: {len(points_near)}")
    print(f"Точек на дальней поверхности: {len(points_far)}")

    glutInit(sys.argv)
    glutInitDisplayMode(GLUT_DOUBLE | GLUT_RGB | GLUT_DEPTH)
    glutInitWindowSize(900, 700)
    glutCreateWindow(b"Ray Casting: cone point cloud")
    init()
    glutDisplayFunc(display)
    glutReshapeFunc(reshape)
    glutMainLoop()


if __name__ == "__main__":
    main()