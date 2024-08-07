import math
import random
from OpenGL.GL import *
from OpenGL.GLU import *

class GoaTranceVis:
    def __init__(self):
        self.rotation = 0
        self.particles = [(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0.5, 2)) for _ in range(5000)]
        self.time = 0

    def update(self, beat_intensity):
        self.rotation += 1 + beat_intensity * 5
        self.time += 0.05 * beat_intensity

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)

        # Render particles
        glPointSize(3)
        glBegin(GL_POINTS)
        for i, (x, y, z, speed) in enumerate(self.particles):
            r = (math.sin(self.time * speed + i * 0.1) + 1) / 2
            g = (math.cos(self.time * speed + i * 0.1) + 1) / 2
            b = (math.sin(self.time * 2 * speed + i * 0.1) + 1) / 2
            glColor3f(r, g, b)

            new_x = x * math.cos(self.time * speed) - z * math.sin(self.time * speed)
            new_z = x * math.sin(self.time * speed) + z * math.cos(self.time * speed)
            new_y = y * math.cos(self.time * speed * 0.5)
            glVertex3f(new_x, new_y, new_z)
        glEnd()

        # Render multiple rotating cones
        for i in range(3):
            glPushMatrix()
            glRotatef(self.rotation * (i + 1) * 0.5, 0, 1, 0)
            glTranslatef(0.5 * (i + 1), 0, 0)
            self.render_cone(0.2, 0.5, 20, i)
            glPopMatrix()

        # Render central sphere
        self.render_sphere(0.3, 20, 20)

        glPopMatrix()

    def render_cone(self, radius, height, slices, offset):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 0, 0)  # Red tip
        glVertex3f(0, height, 0)
        for i in range(slices + 1):
            theta = (i / slices) * 2 * math.pi
            x = radius * math.cos(theta)
            z = radius * math.sin(theta)
            r = (math.sin(self.time + offset + i * 0.1) + 1) / 2
            g = (math.cos(self.time + offset + i * 0.1) + 1) / 2
            b = (math.sin(self.time * 2 + offset + i * 0.1) + 1) / 2
            glColor3f(r, g, b)
            glVertex3f(x, 0, z)
        glEnd()

    def render_sphere(self, radius, slices, stacks):
        for i in range(stacks):
            lat0 = math.pi * (-0.5 + (i - 1) / stacks)
            z0 = math.sin(lat0)
            zr0 = math.cos(lat0)

            lat1 = math.pi * (-0.5 + i / stacks)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(slices + 1):
                lng = 2 * math.pi * (j - 1) / slices
                x = math.cos(lng)
                y = math.sin(lng)

                r = (math.sin(self.time + i * 0.1 + j * 0.05) + 1) / 2
                g = (math.cos(self.time + i * 0.1 + j * 0.05) + 1) / 2
                b = (math.sin(self.time * 2 + i * 0.1 + j * 0.05) + 1) / 2
                glColor3f(r, g, b)

                glVertex3f(radius * x * zr0, radius * y * zr0, radius * z0)
                glVertex3f(radius * x * zr1, radius * y * zr1, radius * z1)
            glEnd()
    def __init__(self):
        self.rotation = 0
        self.particles = [(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0.5, 2)) for _ in range(5000)]
        self.time = 0

    def update(self, beat_intensity):
        self.rotation += 1 + beat_intensity * 5
        self.time += 0.05 * beat_intensity

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)

        # Render particles
        glPointSize(3)
        glBegin(GL_POINTS)
        for i, (x, y, z, speed) in enumerate(self.particles):
            r = (math.sin(self.time * speed + i * 0.1) + 1) / 2
            g = (math.cos(self.time * speed + i * 0.1) + 1) / 2
            b = (math.sin(self.time * 2 * speed + i * 0.1) + 1) / 2
            glColor3f(r, g, b)

            new_x = x * math.cos(self.time * speed) - z * math.sin(self.time * speed)
            new_z = x * math.sin(self.time * speed) + z * math.cos(self.time * speed)
            new_y = y * math.cos(self.time * speed * 0.5)
            glVertex3f(new_x, new_y, new_z)
        glEnd()

        # Render multiple rotating cones
        for i in range(3):
            glPushMatrix()
            glRotatef(self.rotation * (i + 1) * 0.5, 0, 1, 0)
            glTranslatef(0.5 * (i + 1), 0, 0)
            self.render_cone(0.2, 0.5, 20, i)
            glPopMatrix()

        # Render central sphere
        self.render_sphere(0.3, 20, 20)

        glPopMatrix()

    def render_cone(self, radius, height, slices, offset):
        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1, 0, 0)  # Red tip
        glVertex3f(0, height, 0)
        for i in range(slices + 1):
            theta = (i / slices) * 2 * math.pi
            x = radius * math.cos(theta)
            z = radius * math.sin(theta)
            r = (math.sin(self.time + offset + i * 0.1) + 1) / 2
            g = (math.cos(self.time + offset + i * 0.1) + 1) / 2
            b = (math.sin(self.time * 2 + offset + i * 0.1) + 1) / 2
            glColor3f(r, g, b)
            glVertex3f(x, 0, z)
        glEnd()

    def render_sphere(self, radius, slices, stacks):
        for i in range(stacks):
            lat0 = math.pi * (-0.5 + (i - 1) / stacks)
            z0 = math.sin(lat0)
            zr0 = math.cos(lat0)

            lat1 = math.pi * (-0.5 + i / stacks)
            z1 = math.sin(lat1)
            zr1 = math.cos(lat1)

            glBegin(GL_QUAD_STRIP)
            for j in range(slices + 1):
                lng = 2 * math.pi * (j - 1) / slices
                x = math.cos(lng)
                y = math.sin(lng)

                r = (math.sin(self.time + i * 0.1 + j * 0.05) + 1) / 2
                g = (math.cos(self.time + i * 0.1 + j * 0.05) + 1) / 2
                b = (math.sin(self.time * 2 + i * 0.1 + j * 0.05) + 1) / 2
                glColor3f(r, g, b)

                glVertex3f(radius * x * zr0, radius * y * zr0, radius * z0)
                glVertex3f(radius * x * zr1, radius * y * zr1, radius * z1)
            glEnd()
    def __init__(self):
        self.rotation = 0
        self.particles = [(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0.5, 2)) for _ in range(5000)]
        self.time = 0

    def update(self, beat_intensity):
        self.rotation += 1 + beat_intensity * 5
        self.time += 0.05 * beat_intensity

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)

        glPointSize(3)
        glBegin(GL_POINTS)
        for i, (x, y, z, speed) in enumerate(self.particles):
            r = (math.sin(self.time * speed + i * 0.1) + 1) / 2
            g = (math.cos(self.time * speed + i * 0.1) + 1) / 2
            b = (math.sin(self.time * 2 * speed + i * 0.1) + 1) / 2
            glColor3f(r, g, b)

            new_x = x * math.cos(self.time * speed) - z * math.sin(self.time * speed)
            new_z = x * math.sin(self.time * speed) + z * math.cos(self.time * speed)
            new_y = y * math.cos(self.time * speed * 0.5)
            glVertex3f(new_x, new_y, new_z)
        glEnd()

        glPopMatrix()
    def __init__(self):
        self.rotation = 0
        self.particles = [(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(0, 1)) for _ in range(2000)]
        self.time = 0

    def update(self, beat_intensity):
        self.rotation += 2 * beat_intensity
        self.time += 0.05 * beat_intensity

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)

        glPointSize(2 + 3 * math.sin(self.time))
        glBegin(GL_POINTS)
        for i, (x, y, z, speed) in enumerate(self.particles):
            r = (math.sin(self.time + i * 0.1) + 1) / 2
            g = (math.cos(self.time + i * 0.1) + 1) / 2
            b = (math.sin(self.time * 2 + i * 0.1) + 1) / 2
            glColor3f(r, g, b)

            new_x = x * math.cos(self.time * speed) - z * math.sin(self.time * speed)
            new_z = x * math.sin(self.time * speed) + z * math.cos(self.time * speed)
            glVertex3f(new_x, y, new_z)
        glEnd()

        glBegin(GL_TRIANGLES)
        for i in range(20):
            angle = i / 20 * 2 * math.pi
            r = (math.sin(self.time + i * 0.5) + 1) / 2
            g = (math.cos(self.time + i * 0.5) + 1) / 2
            b = (math.sin(self.time * 2 + i * 0.5) + 1) / 2
            glColor3f(r, g, b)
            glVertex3f(math.sin(angle) * (1 + 0.3 * math.sin(self.time)), math.cos(angle) * (1 + 0.3 * math.sin(self.time)), -1)
            glVertex3f(math.sin(angle + 0.3) * (1 + 0.3 * math.cos(self.time)), math.cos(angle + 0.3) * (1 + 0.3 * math.cos(self.time)), -1)
            glVertex3f(0, 0, 1 + 0.5 * math.sin(self.time))
        glEnd()
        glPopMatrix()
    def __init__(self):
        self.rotation = 0
        self.particles = [(random.uniform(-1, 1), random.uniform(-1, 1), random.uniform(-1, 1)) for _ in range(1000)]

    def update(self, beat_intensity):
        self.rotation += 1 + beat_intensity * 5

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)

        glBegin(GL_POINTS)
        for i, (x, y, z) in enumerate(self.particles):
            glColor3f(math.sin(i * 0.01), math.cos(i * 0.01), math.sin(i * 0.02))
            glVertex3f(x, y, z)
        glEnd()

        glBegin(GL_TRIANGLES)
        for i in range(20):
            angle = i / 20 * 2 * math.pi
            glColor3f(math.sin(angle), math.cos(angle), 0.5)
            glVertex3f(math.sin(angle), math.cos(angle), -1)
            glVertex3f(math.sin(angle + 0.3), math.cos(angle + 0.3), -1)
            glVertex3f(0, 0, 1)
        glEnd()
        glPopMatrix()
    def __init__(self):
        self.rotation = 0

    def update(self):
        self.rotation += 1

    def render(self):
        glPushMatrix()
        glRotatef(self.rotation, 0, 1, 0)
        glBegin(GL_TRIANGLES)
        for i in range(20):
            angle = i / 20 * 2 * math.pi
            glColor3f(math.sin(angle), math.cos(angle), 0.5)
            glVertex3f(math.sin(angle), math.cos(angle), -1)
            glVertex3f(math.sin(angle + 0.3), math.cos(angle + 0.3), -1)
            glVertex3f(0, 0, 1)
        glEnd()
        glPopMatrix()