"""
This file implements pay-off functions Q(theta, fraction)
"""

def linear_none_payoff(theta, pop):
    return theta

def linear_linear_neg(theta, pop):
    return 0.5 + 0.5*(theta-pop)

def linear_linear_pos(theta, pop):
    return 0.5*(theta+pop)

def none_linear_pos(theta, pop):
    return pop

def none_linear_neg(theta, pop):
    return 1-pop

def create_pop_only(gamma):
    def pop_only(theta, pop):
        return gamma * pop

    return pop_only

def create_neg_externatilities(L):
    """
    Create Q with payoff decreasing with population profile for arm

    As L increases, the population profile gets more important
    """
    def neg_externalities(theta, pop):
        return theta / (1 + L * pop)

    return neg_externalities

def pos_externalities(theta, pop):
    """
    As rewards go up, so does the benefit from population profile
    """
    return theta * pop

def create_coord_game(gamma):
    """
    Create a coordination game where the pay-off is
    Q = gamma * theta + (1-gamma) * pop

    As gamma decreases, the population profile gets more important.
    """
    def coord_game(theta, pop):
        return gamma * theta + (1-gamma) * pop

    return coord_game


