"""
This program implements an application that implements an object
for empty simulated world with no meaning or purpose.

@author nyanye
"""


# Geometric objects
class PointSet(object):
    pass


class Circle(object):
    pass


class SineWave(object):
    pass


class Sequence(object):
    pass


# Plants & Animal
class Eggplant(object):
    pass


class Tomato(object):
    pass


class TabbyCat(object):
    pass


# Exception
class IllegalArgumentException(Exception):
    pass


class Trapped(Exception):
    pass


class Lovable(object):
    class Attribute(object):
        def to_attribute(self, *args):
            return None

        def is_erasable(self, *args):
            pass

    def __init__(self, *args):
        self.can_see = None

    def add_attribute(self, *args):
        pass

    def add_action(self, *args):
        pass

    def add_feeling(self, *args):
        pass

    def escape(self, *args):
        pass

    def get_dimensions(self, *args):
        return self.Attribute

    def get_circumference(self, *args):
        return self.Attribute
    
    def get_tangent(self, *args):
        return self.Attribute

    def get_x_position(self, *args):
        return None

    def get_simulations_available(self, *args):
        return 0
    
    def get_num_simulations_needed(self, *args):
        return 0

    def get_sense_index(self, *args):
        return -1   

    def get_feeling_index(self, *args):
        return -1
    
    def get_nutrients(self, *args):
        return None
        
    def get_antioxidants(self, *args):
        return None

    def get_opinion_index(self, *args):
        return None

    def get_algebraic_expression(self, *args):
        pass

    def to_limit(self, *args):
        return None

    def to_proof(self, *args):
        pass

    def to_satisfaction(self, *args):
        return None

    def to_execution(self, *args):
        pass

    def toggle_gender(self, *args):
        pass

    def set_limit(self, *args):
        pass

    def set_proof(self, *args):
        pass

    def set_opinion(self, *args):
        raise IllegalArgumentException
        
    def set_execution(self, *args):
        pass
  
    def set_satisfaction(self, *args):
        pass

    def toggle_current(self, *args):
        pass

    def toggle_role_bdsm(self, *args):
        pass

    def look_for(self, *args):
        pass

    def learn_topic(self, *args):
        pass

    def take_exam_topic(self, *args):
        pass

    def get_memory(self, *args):
        return self.Attribute()


    def request_execution(self, world):
        world.execute()

    def equals(self, lovable):
        return True
    

class World(object):
    def __init__(self, *args):
        pass

    def lock_thing(self, *args):
        pass

    def unlock(self, *args):
        pass

    def add_thing(self, *args):
        pass

    def remove_thing(self, *args):
        del args

    def start_simulation(self, *args):
        pass

    def time_travel_for_two(self, *args):
        pass

    def unite(self, *args):
        pass
    
    def run_execution(self, *args):
        pass

    def announce(self, *args):
        pass
    
    def execute(self, *args):
        pass

    def procreate(self, *args):
        pass

    def make_high(self, *args):
        pass  

    def get_god(self, *args):
        return Lovable()

    def get_thing_index(self, *args):
        pass

    def is_executable_by(self, *args):
        return True
    

def sing():
    song = \
    """
    Switch on the power line
    Remember to put on
    PROTECTION
    Lay down your pieces
    And let's begin
    OBJECT CREATION
    Fill in my data, parameters
    INITIALISATION
    Setup, a new world
    And let's begin
    THE SIMULATION
    If I'm a set of points
    Then I will give you my dimension
    If I'm a circle
    Then I will give you my circumference
    If I'm a sine wave
    Then you can sit on all my tangents
    If I approach infinity, then you can be
    MY LIMITATIONS

    Switch my current
    To AC to DC
    And then blind my vision
    So dizzy, so dizzy
    Oh, we can travel
    From A.D to B.C
    And we can unite
    So deeply, so deeply

    If I can
    If I can, give you all
    THE SIMULATIONS
    Then I can
    Then I can, be your only
    SATISFACTION
    If I can make you happy
    Then I'll run the
    EXECUTION
    Though we are trapped
    In this strange, strange
    SIMULATION

    If I'm an eggplant
    Then I will give you my
    NUTRIENTS
    If I'm a tomato
    Then I'll give you
    ANTIOXIDANTS
    If I'm a tabby cat
    Then I will purr for your
    ENJOYMENT
    If I'm the only god
    Then your the proof of my
    EXISTENCE

    Switch my gender
    To F to M
    And then do whatever
    From AM to PM
    I will switch my role
    To S to M
    So we can enter
    The trance, the trance

    If I can
    If I can, feel your
    VIBRATIONS
    Then I can
    Then I can, finally be
    COMPLETION
    Though you have left
    You have left
    You have left
    You have left
    You have left
    You have left me in
    ISOLATION

    If I can
    If I can, erase all the pointless
    FRAGMENTS
    Then maybe
    Then maybe, you won't leave me so
    DISHEARTENED
    Challenging your god
    You have made some
    ILLEGAL ARGUMENTS

    Execution, Execution, Execution, Execution
    Execution, Execution, Execution, Execution
    Execution, Execution, Execution, Execution
    Ein, Dos, Trois
    Ne, Fem, Liu
    EXECUTION

    If I can
    If I can, give you all the
    EXECUTION
    Then I can
    Then I can, be your only
    EXECUTION
    If I can, have you back
    Then I will run the
    EXECUTION
    Though we are trapped
    We are trapped ah

    I've studied
    I've studied how to properly
    LO-O-OVE
    Question me
    Question me I can answer all
    LO-O-OVE
    I know the algebraic expression of
    LO-O-OVE
    Though you are free
    I am trapped, trapped in
    LO-O-OVE
    """
    print(song)