# world.execute(me).py
Python implementation of [Mili - world.execute(me)](https://www.youtube.com/watch?v=ESx_hy1n7HA)

```python
"""
This program implements an application that
creates an empty simulated world with no meaning or purpose.

@author nyanye
"""

from objects import *

# Switch on the power line
# Remember to put on
# PROTECTION
def main():
    # Lay down your pieces
    # And let's begin
    # OBJECT CREATION
    me = Lovable("Me", 0, True, -1, False)
    you = Lovable("You", 0, True, -1, False)

    # Set up our new world
    world = World()
    world.add_thing(me)
    world.add_thing(you)

    # And let's begin the
    # SIMULATION
    world.start_simulation()

    # If I'm a set of points
    if isinstance(me, PointSet):
        # Then I will give you my
        # DIMENSION
        you.add_attribute(me.get_dimensions().to_attribute())

    # If I'm a circle
    if isinstance(me, Circle):
        # Then I will give you my
        # CIRCUMFERENCE
        you.add_attribute(me.get_circumference().to_attribute())

    # If I'm a sine wave
    if isinstance(me, SineWave):
        # Then you can sit on all my
        # TANGENTS
        you.add_action("sit", me.get_tangent(you.get_x_position()))

    # If I approach infinity
    if isinstance(me, Sequence):
        # Then you can be my
        # LIMITATIONS
        me.set_limit(you.to_limit())

    # Switch my current
    # To AC to DC
    me.toggle_current()

    # And then blind my vision
    me.can_see = False
    # So dizzy, so dizzy
    me.add_feeling("dizzy")

    # Oh, we can travel
    world.time_travel_for_two("AD", 617, me, you)
    # From A.D to B.C
    world.time_travel_for_two("BC", 3691, me, you)

    # And we can unite
    # So deeply, so deeply
    world.unite(me, you)



    # If I can
    # If I can, give you all
    # THE SIMULATIONS
    if (me.get_simulations_available()) >= (
        you.get_num_simulations_needed()):
        # Then I can
        # Then I can, be your only
        # SATISFACTION
        you.set_satisfaction(me.to_satisfaction())

    # If I can make you happy
    if (you.get_feeling_index("happy") != -1):
        # Then I'll run the
        # EXECUTION
        me.request_execution(me)

    # Though we are trapped
    # In this strange, strange
    # SIMULATION
    world.lock_thing(me)
    world.lock_thing(you)

    # If I'm an eggplant
    if isinstance(me, Eggplant):
        # Then I will give you my
        # NUTRIENTS
        you.add_attribute(me.get_dimensions().to_attribute())

    # If I'm a tomato
    if isinstance(me, Tomato):
        # Then I'll give you
        # ANTIOXIDANTS
        you.add_attribute(me.get_circumference().to_attribute())

    # If I'm a tabby cat
    if isinstance(me, TabbyCat):
        # Then I will purr for your
        # ENJOYMENT
        you.add_action("sit", me.get_tangent(you.get_x_position()))

    # If I'm the only god
    if world.get_god().equals(me):
        # Then your the proof of my
        # EXISTENCE
        me.set_proof(you.to_proof())



    # Switch my gender
    # To F to M
    me.toggle_gender()
    # And then do whatever
    # From AM to PM
    world.procreate(me, you)
    # I will switch my role
    # To S to M
    me.toggle_role_bdsm()
    # So we can enter
    # The trance, the trance
    world.make_high(me)
    world.make_high(you)



    # If I can
    # If I can, feel your
    # VIBRATIONS
    if me.get_sense_index("vibration"):
        # Then I can
        # Then I can, finally be
        # COMPLETION
        me.add_feeling("complete")
    # Though you have left
    world.unlock(you)
    world.remove_thing(you)
    # You have left
    me.look_for(you, world)
    # You have left
    me.look_for(you, world)
    # You have left
    me.look_for(you, world)
    # You have left
    me.look_for(you, world)
    # You have left me in
    me.look_for(you, world)
    # ISOLATION

    # If I can
    # If I can, erase all the pointless
    # FRAGMENTS
    if me.get_memory().is_erasable():
        # Then maybe
        # Then maybe, you won't leave me so
        # DISHEARTENED
        me.remove_feeling("disheartened")

    # Challenging your god
    try:
        me.set_opinion(me.get_opinion_index("you are here"), False)
    # You have made some
    except IllegalArgumentException:
        # ILLEGAL ARGUMENTS
        world.announce("God is always true.")

    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EXECUTION
    world.run_execution()
    # EIN
    world.announce("1", "de") # ein; German
    # DOS
    world.announce("2", "es") # dos; Español
    # TROIS
    world.announce("3", "fr") # trois; French
    # NE
    world.announce("4", "kr") # 넷; Korean
    # FEM
    world.announce("5", "se") # fem; Swedish
    # LIU
    world.announce("6", "cn") # 六; Chinese
    # EXECUTION
    world.run_execution()



    # If I can
    # If I can, give you all the
    # EXECUTION
    if world.is_executable_by(me):
        # Then I can
        # Then I can, be your only
        # EXECUTION
        you.set_execution(me.to_execution())

    # If I can, have you back
    if (world.get_thing_index(you) != -1):
        # Then I will run the
        # EXECUTION
        world.run_execution()
    
    # Though we are trapped
    # We are trapped ah
    me.escape(world)

    # I've studied
    # I've studied how to properly
    # LO-O-OVE
    me.learn_topic("love")
    # Question me
    # Question me I can answer all
    # LO-O-OVE
    me.take_exam_topic("love")
    # I know the algebraic expression of
    # LO-O-OVE
    me.get_algebraic_expression("love")
    # Though you are free
    # I am trapped, trapped in
    # LO-O-OVE
    try:
        me.escape("love")
    except Trapped:
        # EXECUTION
        world.execute(me)
    

if __name__ == '__main__':
    main()
    sing()
```