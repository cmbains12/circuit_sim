## junction.py

## Junction class definition
# The Junction class works in conjunction with the Component classes to model
# the complete electrical circuit network. Junctions are the connection points
# between components in the circuit. They have a voltage value associated with
# them and a list of connected components. The voltage value is calculated based
# on the connected components and their properties. The voltage value is
# calculated elsewhere in the program and set using the set_voltage method.

# Junctions have the following attributes:
# - junction_id: A unique identifier for the junction
# - voltage: The voltage value at the junction
# - components: A list of connected components IDs
# - currents: A list of currents through the connected components with the convention that current 
#   leaving the junction is positive and current entering the junction is negative. The sum of 
#   currents at a junction should be zero in a valid circuit.
# - current: The total current at the junction, used for validation (should be zero in a valid circuit)

# Junctions have the following methods:
# - get_voltage(): Returns the voltage at the junction
# - set_voltage(voltage): Sets the voltage at the junction
# - get_id(): Returns the ID of the junction
# - get_components(): Returns the list of connected components
# - add_component(component): Adds a component to the list of connected components
# - remove_component(component): Removes a component from the list of connected components

## FIRST PRINCIPLES
# Kirchhoff's Current Law: The sum of currents entering a junction is equal to the sum of currents 
# leaving the junction. This law is based on the principle of conservation of charge. It is used to
# calculate the current at a junction based on the currents through the connected components.

class Junction:
    def __init__(self, junction_id, components):
        self.junction_id = junction_id
        self.voltage = 0
        self.current = 0
        self.components = components

    def get_voltage(self):
        return self.voltage

    def set_voltage(self, voltage):
        self.voltage = voltage

    def get_id(self):
        return self.junction_id

    def get_components(self):
        return self.components

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)
