from OpenGL.GL import *
from OpenGL.GLU import *
from visualizations.goa_trance import GoaTranceVis
from visualizations.fractal_tree import FractalTreeVis
from visualizations.psychedelic_sphere import PsychedelicSphereVis
import random
import time
import math

class SceneManager:
    def __init__(self):
        self.visualizations = [
            GoaTranceVis(),
            FractalTreeVis(),
            PsychedelicSphereVis()
        ]
        self.current_vis = 0
        self.next_vis = 0
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)
        self.beat_intensity = 0
        self.beat_speed = random.uniform(0.1, 0.3)
        self.global_intensity = 1.0
        self.transition_progress = 1.0

    def update(self):
        self.beat_intensity = (math.sin(time.time() * self.beat_speed) + 1) / 2
        self.visualizations[self.current_vis].update(self.beat_intensity * self.global_intensity)
        self.visualizations[self.next_vis].update(self.beat_intensity * self.global_intensity)

        current_time = time.time()
        if current_time - self.last_switch_time > self.switch_interval:
            self.start_transition()

        if self.transition_progress < 1.0:
            self.transition_progress += 0.02
            if self.transition_progress >= 1.0:
                self.current_vis = self.next_vis

    def render(self):
        glEnable(GL_BLEND)
        glBlendFunc(GL_SRC_ALPHA, GL_ONE_MINUS_SRC_ALPHA)

        # Render current visualization
        glPushMatrix()
        glColor4f(1, 1, 1, 1 - self.transition_progress)
        self.visualizations[self.current_vis].render()
        glPopMatrix()

        # Render next visualization (if transitioning)
        if self.transition_progress < 1.0:
            glPushMatrix()
            glColor4f(1, 1, 1, self.transition_progress)
            self.visualizations[self.next_vis].render()
            glPopMatrix()

        glDisable(GL_BLEND)

    def start_transition(self):
        self.next_vis = (self.current_vis + 1) % len(self.visualizations)
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)
        self.beat_speed = random.uniform(0.1, 0.3)
        self.transition_progress = 0.0

    def increase_intensity(self):
        self.global_intensity = min(2.0, self.global_intensity + 0.1)

    def decrease_intensity(self):
        self.global_intensity = max(0.1, self.global_intensity - 0.1)
    def __init__(self):
        self.visualizations = [
            GoaTranceVis(),
            FractalTreeVis(),
            PsychedelicSphereVis()
        ]
        self.current_vis = 0
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)
        self.beat_intensity = 0
        self.beat_speed = random.uniform(0.1, 0.3)
        self.global_intensity = 1.0
        self.transition_progress = 1.0

    def update(self):
        self.beat_intensity = (math.sin(time.time() * self.beat_speed) + 1) / 2
        self.visualizations[self.current_vis].update(self.beat_intensity * self.global_intensity)

        current_time = time.time()
        if current_time - self.last_switch_time > self.switch_interval:
            self.switch_visualization()

        if self.transition_progress < 1.0:
            self.transition_progress += 0.05

    def render(self):
        glPushMatrix()
        glScalef(self.transition_progress, self.transition_progress, self.transition_progress)

        # Apply global color shift based on beat
        glColorMask(self.beat_intensity, 1 - self.beat_intensity, self.beat_intensity, 1)

        self.visualizations[self.current_vis].render()
        glPopMatrix()

    def switch_visualization(self):
        self.current_vis = (self.current_vis + 1) % len(self.visualizations)
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)
        self.beat_speed = random.uniform(0.1, 0.3)
        self.transition_progress = 0.1

    def increase_intensity(self):
        self.global_intensity = min(2.0, self.global_intensity + 0.1)

    def decrease_intensity(self):
        self.global_intensity = max(0.1, self.global_intensity - 0.1)
    def __init__(self):
        self.visualizations = [
            GoaTranceVis(),
            FractalTreeVis(),
            PsychedelicSphereVis()
        ]
        self.current_vis = 0
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)
        self.beat_intensity = 0
        self.beat_speed = random.uniform(0.1, 0.3)

    def update(self):
        self.beat_intensity = (math.sin(time.time() * self.beat_speed) + 1) / 2
        self.visualizations[self.current_vis].update(self.beat_intensity)

        current_time = time.time()
        if current_time - self.last_switch_time > self.switch_interval:
            self.switch_visualization()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()

        # Apply global color shift based on beat
        glColorMask(self.beat_intensity, 1 - self.beat_intensity, self.beat_intensity, 1)

        self.visualizations[self.current_vis].render()

    def switch_visualization(self):
        self.current_vis = (self.current_vis + 1) % len(self.visualizations)
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)
        self.beat_speed = random.uniform(0.1, 0.3)
    def __init__(self):
        self.visualizations = [
            GoaTranceVis(),
            FractalTreeVis(),
            PsychedelicSphereVis()
        ]
        self.current_vis = 0
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)  # Switch every 5-15 seconds

    def update(self):
        self.visualizations[self.current_vis].update()

        # Check if it's time to switch visualizations
        current_time = time.time()
        if current_time - self.last_switch_time > self.switch_interval:
            self.switch_visualization()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.visualizations[self.current_vis].render()

    def switch_visualization(self):
        self.current_vis = (self.current_vis + 1) % len(self.visualizations)
        self.last_switch_time = time.time()
        self.switch_interval = random.uniform(5, 15)  # Set a new random interval
    def __init__(self):
        self.visualizations = [GoaTranceVis()]
        self.current_vis = 0

    def update(self):
        self.visualizations[self.current_vis].update()

    def render(self):
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glLoadIdentity()
        self.visualizations[self.current_vis].render()