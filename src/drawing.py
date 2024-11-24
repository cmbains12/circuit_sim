# drawing.py
# This is the file that will contain the Screen class. This class
# will be responsible for creating the window and drawing the
# components of the electrical circuit. The Screen class will
# also be responsible for handling user input. The Screen class
# will be initialized with a width and height, and will respond
# to user clicks and key presses.

import pygame
import math


class Screen:
    # The Screen class will be responsible for creating the window
    def __init__(self, width, height):
        # Initialize pygame
        pygame.init()
        # Initialize the screen with the given width and height
        self.screen = pygame.display.set_mode((width, height))
        # Set the caption of the window to "Electrical Circuit Simulation Program"
        pygame.display.set_caption("Electrical Circuit Simulation Program")
        # Set the running attribute to True
        self.running = True
        self.start_pos = None
        self.drawing = False
        self.lines = []  # List to store all drawn lines
        self.undone_lines = []  # List to store undone lines

        self.screen.fill((255, 255, 255))  # Fill the screen with white

    def distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)
            
    # The run method will be responsible for handling user input
    def run(self):
        # While the running attribute is True
        while self.running:
            # For each event in the pygame event queue  
            for event in pygame.event.get():
                # If the event is a QUIT event
                if event.type == pygame.QUIT:
                    # Set the running attribute to False
                    self.running = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_z and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        if self.lines:
                            self.undone_lines.append(self.lines.pop())
                    elif event.key == pygame.K_y and pygame.key.get_mods() & pygame.KMOD_CTRL:
                        if self.undone_lines:
                            self.lines.append(self.undone_lines.pop())
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    # Check if the cursor is close to any line endpoints
                    for line in self.lines:
                        if self.distance(mouse_pos, line[0]) < 10:
                            self.start_pos = line[0]
                            break
                        elif self.distance(mouse_pos, line[1]) < 10:
                            self.start_pos = line[1]
                            break
                    else:
                        self.start_pos = mouse_pos
                    self.drawing = True
                elif event.type == pygame.MOUSEBUTTONUP:
                    mouse_pos = pygame.mouse.get_pos()
                    end_pos = mouse_pos
                    # Check if the cursor is close to any line endpoints
                    for line in self.lines:
                        if self.distance(mouse_pos, line[0]) < 10:
                            end_pos = line[0]
                            break
                        elif self.distance(mouse_pos, line[1]) < 10:
                            end_pos = line[1]
                            break
                    if self.start_pos:
                        self.lines.append((self.start_pos, end_pos))  # Store the line
                        self.start_pos = None
                        self.drawing = False
                        self.undone_lines.clear()  # Clear the undone lines stack
                elif event.type == pygame.MOUSEMOTION:
                    self.screen.fill((255, 255, 255))  # Clear the screen
                    mouse_pos = pygame.mouse.get_pos()
                    for line in self.lines:
                        pygame.draw.line(self.screen, (0, 0, 0), line[0], line[1], 2)
                        if self.distance(mouse_pos, line[0]) < 10:  # Check if the cursor is close to the start point
                            pygame.draw.circle(self.screen, (255, 0, 0), line[0], 5)  # Draw a small red circle
                        if self.distance(mouse_pos, line[1]) < 10:  # Check if the cursor is close to the end point
                            pygame.draw.circle(self.screen, (255, 0, 0), line[1], 5)  # Draw a small red circle
                    if self.drawing:
                        end_pos = pygame.mouse.get_pos()
                        pygame.draw.line(self.screen, (0, 0, 0), self.start_pos, end_pos, 2)
                    pygame.display.flip()

            pygame.display.flip()

        pygame.quit()