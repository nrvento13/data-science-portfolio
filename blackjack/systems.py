def hi_lo(rank):
    counts = {
        '2': 1,
        '3': 1,
        '4': 1,
        '5': 1,
        '6': 1,
        '7': 0, 
        '8': 0,
        '9': 0,
        '10': -1,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1
    }
    return counts[rank]

def hi_opt_i(rank):
    counts = {
        2: 0,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 0, 
        8: 0,
        9: 0,
        10: -1,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': 0
    }
    return counts[rank]

def hi_opt_ii(rank):
    counts = {
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 1,
        7: 1, 
        8: 0,
        9: 0,
        10: -2,
        'J': -2,
        'Q': -2,
        'K': -2,
        'A': 0
    }
    return counts[rank]

def ko(rank):
    counts = {
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1, 
        8: 0,
        9: 0,
        10: -1,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1
    }
    return counts[rank]

def omega_ii(rank):
    counts = {
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 1, 
        8: 0,
        9: -1,
        10: -2,
        'J': -2,
        'Q': -2,
        'K': -2,
        'A': 0
    }
    return counts[rank]

def red_7(rank):
    counts = {
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1, 
        8: 0,
        9: 0,
        10: -1,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1
    }
    return counts[rank]

def halves(rank):
    counts = {
        2: 0.5,
        3: 1,
        4: 1,
        5: 1.5,
        6: 1,
        7: 0.5, 
        8: 0,
        9: -0.5,
        10: -1,
        'J': -1,
        'Q': -1,
        'K': -1,
        'A': -1
    }
    return counts[rank]

def zen_count(rank):
    counts = {
        2: 1,
        3: 1,
        4: 2,
        5: 2,
        6: 2,
        7: 1, 
        8: 0,
        9: 0,
        10: -2,
        'J': -2,
        'Q': -2,
        'K': -2,
        'A': -1
    }
    return counts[rank]

def ten_count(rank):
    counts = {
        2: 1,
        3: 1,
        4: 1,
        5: 1,
        6: 1,
        7: 1, 
        8: 1,
        9: 1,
        10: -2,
        'J': -2,
        'Q': -2,
        'K': -2,
        'A': 1
    }
    return counts[rank]