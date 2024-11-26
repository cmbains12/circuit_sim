# drawing.py

import pygame
import math
import pygame_menu
from component import Component
from conductor import Conductor
from resistor import Resistor
from capacitor import Capacitor
from inductor import Inductor
from battery import Battery
from ground import Ground
from switch import Switch
from voltage_source import VoltageSource
from current_source import CurrentSource
from diode import Diode
from transistor import Transistor
from signal_generator import SignalGenerator
from oscilloscope import Oscilloscope
from multimeter import Multimeter
from ammeter import Ammeter
from voltmeter import Voltmeter
from wattmeter import Wattmeter
from fuse import Fuse
from circuit_breaker import CircuitBreaker
from transformer import Transformer
from motor import Motor

class Drawing:
    def __init__(self, width, height):
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Electrical Circuit Simulation Program")
        self.running = True
        self.start_pos = None
        self.drawing = False
        self.components = []  # List to store all component instances
        self.undone_components = []  # List to store undone component instances
        self.component_id = 0  # Counter for component IDs

        self.screen.fill((255, 255, 255))  # Fill the screen with white

    def distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
    
    # Create the menu
        self.menu = pygame_menu.Menu('Select Component', width, 40, theme=pygame_menu.themes.THEME_DARK)
        self.menu.add_button('Conductor', self.select_conductor)
        self.menu.add_button('Resistor', self.select_resistor)
        self.menu.add_button('Capacitor', self.select_capacitor)
        self.menu.add_button('Inductor', self.select_inductor)
        self.menu.add_button('Transistor', self.select_transistor)
        self.menu.add_button('Diode', self.select_diode)
        self.menu.add_button('Battery', self.select_battery)
        self.menu.add_button('Ground', self.select_ground)
        self.menu.add_button('Switch', self.select_switch)
        self.menu.add_button('Voltage Source', self.select_voltage_source)
        self.menu.add_button('Current Source', self.select_current_source)
        #self.menu.add_button('Signal Generator', self.select_signal_generator)
        #self.menu.add_button('Oscilloscope', self.select_oscilloscope)
        #self.menu.add_button('Multimeter', self.select_multimeter)
        #self.menu.add_button('Ammeter', self.select_ammeter)
        #self.menu.add_button('Voltmeter', self.select_voltmeter)
        #self.menu.add_button('Wattmeter', self.select_wattmeter)
        #self.menu.add_button('Fuse', self.select_fuse)
        #self.menu.add_button('Circuit Breaker', self.select_circuit_breaker)
        #self.menu.add_button('Transformer', self.select_transformer)
        #self.menu.add_button('Motor', self.select_motor)
        self.menu.add_button('Exit', pygame_menu.events.EXIT)
        self.menu.mainloop(self.screen)




    def draw_components(self):
        """Draw all components on the screen."""
        self.screen.fill((255, 255, 255))  # Clear the screen
        for component in self.components:
            if isinstance(component, Conductor):
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
            elif isinstance(component, Resistor):
                mid_point = ((component.start_point[0] + component.end_point[0]) // 2,
                             (component.start_point[1] + component.end_point[1]) // 2)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, mid_point, 2)
                pygame.draw.line(self.screen, (0, 0, 0), mid_point, component.end_point, 2)
            elif isinstance(component, Capacitor):
                mid_point = ((component.start_point[0] + component.end_point[0]) // 2,
                             (component.start_point[1] + component.end_point[1]) // 2)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, mid_point, 2)
                pygame.draw.line(self.screen, (0, 0, 0), mid_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), mid_point, 5)
            elif isinstance(component, Inductor):
                mid_point = ((component.start_point[0] + component.end_point[0]) // 2,
                             (component.start_point[1] + component.end_point[1]) // 2)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, mid_point, 2)
                pygame.draw.line(self.screen, (0, 0, 0), mid_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), mid_point, 5)
                pygame.draw.circle(self.screen, (0, 0, 0), mid_point, 10, 2)
            elif isinstance(component, Battery):
                # Example drawing for a battery (you can customize this)
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(component.start_point[0], component.start_point[1], 10, 20))
                pygame.draw.rect(self.screen, (0, 0, 0), pygame.Rect(component.end_point[0] - 10, component.end_point[1], 10, 20))
                pygame.draw.line(self.screen, (0, 0, 0), (component.start_point[0] + 5, component.start_point[1]),
                                 (component.end_point[0] - 5, component.end_point[1]), 2)
            elif isinstance(component, Ground):
                # Example drawing for a ground (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
            elif isinstance(component, Switch):
                # Example drawing for a switch (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 10, 2)
            elif isinstance(component, VoltageSource):
                # Example drawing for a voltage source (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
            elif isinstance(component, CurrentSource):
                # Example drawing for a current source (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
            elif isinstance(component, Diode):
                # Example drawing for a diode (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.polygon(self.screen, (0, 0, 0), [(component.end_point[0] - 5, component.end_point[1] - 5),
                                                             (component.end_point[0] + 5, component.end_point[1] - 5),
                                                             (component.end_point[0], component.end_point[1] + 5)])
            elif isinstance(component, Transistor):
                # Example drawing for a transistor (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.circle(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1]), 5)
                pygame.draw.circle(self.screen, (0, 0, 0), (component.end_point[0] + 5, component.end_point[1]), 5)
                pygame.draw.polygon(self.screen, (0, 0, 0), [(component.end_point[0] - 5, component.end_point[1] - 5),
                                                             (component.end_point[0] + 5, component.end_point[1] - 5),
                                                             (component.end_point[0], component.end_point[1] + 5)])
            elif isinstance(component, SignalGenerator):
                # Example drawing for a signal generator (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Oscilloscope):
                # Example drawing for an oscilloscope (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Multimeter):
                # Example drawing for a multimeter (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Ammeter):
                # Example drawing for an ammeter (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Voltmeter):
                # Example drawing for a voltmeter (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Wattmeter):
                # Example drawing for a wattmeter (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Fuse):
                # Example drawing for a fuse (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, CircuitBreaker):
                # Example drawing for a circuit breaker (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Transformer):
                # Example drawing for a transformer (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)
                
            elif isinstance(component, Motor):
                # Example drawing for a motor (you can customize this)
                pygame.draw.line(self.screen, (0, 0, 0), component.start_point, component.end_point, 2)
                pygame.draw.circle(self.screen, (0, 0, 0), component.end_point, 5)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] - 5),
                                 (component.end_point[0] + 5, component.end_point[1] + 5), 2)
                pygame.draw.line(self.screen, (0, 0, 0), (component.end_point[0] - 5, component.end_point[1] + 5),
                                 (component.end_point[0] + 5, component.end_point[1] - 5), 2)


    def run(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        if self.components:
                            self.undone_components.append(self.components.pop())
                    elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        if self.undone_components:
                            self.components.append(self.undone_components.pop())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for component in self.components:
                        if isinstance(component, Conductor) and self.distance(mouse_pos, component.start_point) < 10:
                            self.start_pos = component.start_point
                            break
                        elif isinstance(component, Conductor) and self.distance(mouse_pos, component.end_point) < 10:
                            self.start_pos = component.end_point
                            break
                    else:
                        self.start_pos = mouse_pos
                    self.drawing = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    end_pos = mouse_pos
                    for component in self.components:
                        if isinstance(component, Conductor) and self.distance(mouse_pos, component.start_point) < 10:
                            end_pos = component.start_point
                            break
                        elif isinstance(component, Conductor) and self.distance(mouse_pos, component.end_point) < 10:
                            end_pos = component.end_point
                            break
                    if self.start_pos:
                        conductor = Conductor(self.component_id, self.start_pos, end_pos)
                        self.components.append(conductor)
                        self.component_id += 1
                        self.start_pos = None
                        self.drawing = False
                elif event.type == pygame.MOUSEMOTION:
                    self.draw_components()  # Draw all components
                    mouse_pos = pygame.mouse.get_pos()
                    for component in self.components:
                        if isinstance(component, Conductor):
                            if self.distance(mouse_pos, component.start_point) < 10:
                                pygame.draw.circle(self.screen, (255, 0, 0), component.start_point, 5)
                            if self.distance(mouse_pos, component.end_point) < 10:
                                pygame.draw.circle(self.screen, (255, 0, 0), component.end_point, 5)
                    if self.drawing:
                        end_pos = pygame.mouse.get_pos()
                        pygame.draw.line(self.screen, (0, 0, 0), self.start_pos, end_pos, 2)
                    pygame.display.flip()

            pygame.display.flip()

        pygame.quit()