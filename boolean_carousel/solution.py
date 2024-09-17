import random

def rand_rotation(bool_list):
    # Determine the number of positions to rotate
    rotation = random.randint(0, 3)
    
    # Perform the rotation
    return bool_list[-rotation:] + bool_list[:-rotation]

def puzzle(bools):
    # step 1 code
    bools[0], bools[2] = True, True
    """ current state of our knowledge
        note: the orientation  of  the
        circle  is arbitrary. We don't 
        know the rotation.
    
               True 
            
           ?         ?
                
               True 
    """
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)


    # Step 2 code
    bools[0], bools[1] = True, True
    """current state of our knowledge

                True
            
          True          ? 

                True
    """
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    """Since we didn't return success, we have:

                True
            
          True        False

                True

        Again, the order is arbitrary, we still
        don't know **where** stuff is, it could
        be:
        [True True True False] or
        [True True False True] or
        [True False True True] or
        [False True True True]
    """
    
    # step 3 code
    if    bools[0] == False: bools[0] = True # and we're done
    elif  bools[1] == False: bools[1] = True # and we're done
    else: bools[0]  = False

    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    """ So we're still here, which means we must
        have hit the case above where both elems
        were True, and we set the  first  one to 
        False. So what doese that mean? Well, we
        basically have two cases:
        Case 1:
        ======


                True

          False       False

                True

        Case 2:
        ======
                True
        
        True           False
        
                False

        Again, these are the only two cases not
        counting rotation.

        This understandably doesn't feel like
        progress, but it is in fact  easy  to
        figure out which case we are in,  our
        next step.
    """


    # step 4 code
    our_case = 2  
    if (bools[0] == bools[2]):
        our_case = 1
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    """Now, if we're in case 2 we transform it 
       to case 1 to set up our final step."""
    # step 5 code
    if our_case == 2:
        if  bools[0] == bools[1]:
            bools[0] =  not bools[0]
            bools[1] =  not bools[1] # and we're done
        else:
            bools[0], bools[1] = bools[1], bools[0]
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)


    """ 
    State of knowledge
                True
            
          False       False

                True
    """

    # step 6 code
    bools[0] = not bools[0]
    bools[2] = not bools[2]
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    return "failure"

def generate_random_bools():
    return [random.choice([True, False]) for _ in range(4)]

def run_puzzle_tests(num_tests=1000):
    for i in range(num_tests):
        bool_list = generate_random_bools()
        if puzzle(bool_list) == "failure":
            return "failure"
    return "success"

if __name__ == "__main__":
    print(run_puzzle_tests())
