import random

def rand_rotation(bool_list):
    # Determine the number of positions to rotate
    rotation = random.randint(0, 3)
    
    # Perform the rotation
    return bool_list[-rotation:] + bool_list[:-rotation]

def puzzle(bools):
    # your step 1 code
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    # your step 2 code
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)
    
    # your step 3 code
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    # your step 4 code
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    # your step 5 code
    if all(bools) or not any(bools): return "success"
    bools = rand_rotation(bools)

    # your step 6 code
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
