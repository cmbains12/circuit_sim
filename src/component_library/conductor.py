## conductor.py

## Class definition for the Conductor class
# The Conductor class is a subclass of the Component class. It represents a conductor in an 
# electrical circuit. Conductors have negligible resistance, and are usually assumed to have a
# resistance of zero. They connect other components in the circuit, and allow current to flow
# between them. The Conductor class behaves similarly to a junction, but instead of connecting
# two or more components, it connects junctions (two and only two).  Because the resistance of
# is negligible and assumed to be zero, the voltage drop across a conductor is also zero.

# The Conductor class has the following attributes:
# - component_id: A unique identifier for the conductor (inherits from Component)
# - junctions: A list of connected junctions (at least 2) (inherits from Component)
# - current: The current through the conductor (direction notated by the sign in reference to the ID
#   values of the connected junctions) (zero by default) (inherits from Component)

# The attributes inherited from the Component class that are defined or not used:
# - voltage: The voltage across the conductor (zero by definition)
# - component_type: The type of the component (conductor by definition)
# - power: The power associated with the conductor (zero by definition)
# - resistance: The resistance of the conductor (zero by definition)


# The Conductor class has the following methods:
# - get_current(): Returns the current through the conductor (inherits from Component)
# - set_current(current): Sets the current through the conductor (inherits from Component)
# - get_id(): Returns the ID of the conductor (inherits from Component)
# - get_junctions(): Returns the list of connected junctions (inherits from Component)
# - add_junction(junction): Adds a junction to the list of connected junctions (inherits from Component)
# - remove_junction(junction): Removes a junction from the list of connected junctions (inherits from Component)
# - validate_conductor(): Validates the conductor and returns a list of validation errors
#   (called by the validate method of the Component class)


from component import Component

class Conductor(Component):
    def __init__(self, component_id, junctions):
        super().__init__(component_id, junctions, "conductor")


    def validate_conductor(self):
        errors = []
        if len(self.junctions) != 2:
            errors.append("Conductor {} does not have exactly 2 junctions".format(self.component_id))
        return errors
