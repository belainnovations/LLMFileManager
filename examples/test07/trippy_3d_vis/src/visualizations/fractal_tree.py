import math
from OpenGL.GL import *
from OpenGL.GLU import *

class FractalTreeVis:
    def __init__(self):
        self.angle = 0
        self.color_shift = 0

    def update(self, beat_intensity):
        self.angle += 0.02 + beat_intensity * 0.1
        self.color_shift += 0.01

    def render(self):
        glPushMatrix()
        glTranslatef(0, -0.5, -1)
        self.draw_tree(0.3, 10, self.angle)
        glPopMatrix()

    def draw_tree(self, length, depth, angle):
        if depth == 0:
            return

        r = (math.sin(self.color_shift) + 1) / 2
        g = (math.sin(self.color_shift + 2) + 1) / 2
        b = (math.sin(self.color_shift + 4) + 1) / 2
        glColor3f(r, g, b)

        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, length, 0)
        glEnd()

        glPushMatrix()
        glTranslatef(0, length, 0)

        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        self.draw_tree(length * 0.8, depth - 1, angle)
        glPopMatrix()

        glPushMatrix()
        glRotatef(-angle, 0, 0, 1)
        self.draw_tree(length * 0.8, depth - 1, angle)
        glPopMatrix()

        glPopMatrix()
    def __init__(self):
        self.angle = 0

    def update(self):
        self.angle += 0.02

    def render(self):
        glPushMatrix()
        glTranslatef(0, -0.5, -1)
        self.draw_tree(0.3, 10, self.angle)
        glPopMatrix()

    def draw_tree(self, length, depth, angle):
        if depth == 0:
            return

        glColor3f(0.1, 0.8, 0.1)
        glBegin(GL_LINES)
        glVertex3f(0, 0, 0)
        glVertex3f(0, length, 0)
        glEnd()

        glPushMatrix()
        glTranslatef(0, length, 0)

        glPushMatrix()
        glRotatef(angle, 0, 0, 1)
        self.draw_tree(length * 0.8, depth - 1, angle)
        glPopMatrix()

        glPushMatrix()
        glRotatef(-angle, 0, 0, 1)
        self.draw_tree(length * 0.8, depth - 1, angle)
        glPopMatrix()

        glPopMatrix()