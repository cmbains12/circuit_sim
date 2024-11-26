# resistor.py

## Class definition for the Resistor class
# The Resistor class is a subclass of the Component class. It represents a resistor in an electrical
# circuit. Resistors have a resistance value associated with them, which determines the amount of
# opposition they provide to the flow of current. The voltage drop across a resistor is proportional
# to the current flowing through it and its resistance value. A Resistor can connect to two junctions.
# A Resistor is a load and consumes power. The power consumed by a resistor is given by the formula:
# power = current^2 * resistance (P = I^2 * R), known as Joule's Law. The power consumed by a resistor
# is always positive, indicating that energy is leaving the circuit through the resistor 
# (known as passive sign convention).

# The Resistor class has the following attributes:
# - component_id: A unique identifier for the resistor (provided to the constructor)
# - junctions: A list of connected junctions (exactly 2) (provided to the constructor)
# - voltage: The voltage across the resistor (calculated elsewhere in the program)
# - current: The current through the resistor (calculated elsewhere in the program)
# - resistance: The resistance value of the resistor (provided to the constructor)
# - power: The power consumed by the resistor (calculated elsewhere in the program)

# The attributes inherited from the Component class that are defined or not used:
# - component_type: The type of the component (resistor by definition)

# The Resistor class has the following methods:
# - get_current(): Returns the current through the resistor (inherits from Component)
# - set_current(current): Sets the current through the resistor (inherits from Component)
# - get_id(): Returns the ID of the resistor (inherits from Component)
# - get_junctions(): Returns the list of connected junctions (inherits from Component)
# - add_junction(junction): Adds a junction to the list of connected junctions (inherits from Component)
# - remove_junction(junction): Removes a junction from the list of connected junctions (inherits from Component)
# - validate_conductor(): Validates the resistor and returns a list of validation errors
#   (called by the validate method of the Component class)

from component import Component

class Resistor(Component):
    def __init__(self, component_id, junctions, resistance):
        super().__init__(component_id, junctions, "resistor")
        self.resistance = resistance

    def validate_resistor(self):
        errors = []
        if len(self.junctions) != 2:
            errors.append("Resistor {} does not have exactly 2 junctions".format(self.component_id))
        if self.resistance <= 0:
            errors.append("Resistor {} has non-positive resistance".format(self.component_id))
        if self.power < 0:
            errors.append("Resistor {} has negative power, which indicates power generation".format(self.component_id))
        return errors

