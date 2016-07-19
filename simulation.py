import collections
import random

import mcsim


def fractions(xs):
    s = sum(xs)
    return [x / s for x in xs]

def new_thetas(types):
    """
    Return new thetas
    """
    return [random.betavariate(a, b) for a, b in types]

def generate_agent(config):
    """
    Generate a new agent

    Args:
        - k: number of arms
    """
    # Agent is defined as tuple (history, thetas)
    # where history = [(wins, total_pulls) for arm in arms]
    # and thetas is [theta for arm in arms]
    k = config["k"]
    return ([(0, 0) for _ in range(k)], new_thetas(config["types"]))

def initial_state_from_config(config):
    """
    Create initial state with empty histories based on config
    """
    k = config["k"]
    nagents = config["nagents"]
    initial_state = {"agents": [generate_agent(config) for _ in range(nagents)]}
    return initial_state

def regenerate(state, config, log):
    """
    Regenerate each agent with probability config["beta"]
    """
    def regeneration(agent, beta, k):
        """
        Regenerate an agent with probability 1-beta
        """
        # regeneration occurs
        if random.random() < 1-beta:
            return generate_agent(config)
        # otherwise, just return agent
        return agent

    newagents = [regeneration(agent, config["beta"], config["k"]) for agent in state["agents"]]
    state["agents"] = newagents
    return state

def select_arms(state, config, log):
    """
    Each agent selects an arm based on the MAB strategy.
    """
    actions = [config["strategy"](agent[0]) for agent in state["agents"]]
    log["actions"] = actions
    state["actions"] = actions
    return state

def generate_payoffs(state, config, log):
    """
    Generate pay-off for each agent based on their theta and the population profile
    """
    # compute fraction each arm is pulled
    counter_actions = collections.Counter(state["actions"])
    pop_profile = fractions([counter_actions[i] for i in range(config["k"])])

    # generate payoffs based on agent types and population profile
    payoffs = [int(random.random() < config["payoff"](agent[1][action], pop_profile[action]))
               for agent, action in zip(state["agents"], state["actions"])]

    log["pop_profile"] = pop_profile
    log["payoffs"] = payoffs

    state["payoffs"] = payoffs
    return state

def update_histories(state, config, log):
    """
    Updates histories of agents based on their actions and payoffs
    """
    newagents = []
    for agent, action, payoff in zip(state["agents"], state["actions"], state["payoffs"]):
        wins, total = agent[0][action]
        agent[0][action] = (wins + payoff, total + 1)
    return state

def simulate(config, steps):
    """
    Run simuation for <steps> rounds

    Args:
        - config: configuration dictionary
        - steps: number of time steps

    Returns:
        Dictionary with logs
    """
    # define simulation chain
    chain = [regenerate, select_arms, generate_payoffs, update_histories]
    # run simulation
    outcomes = mcsim.simulate(chain, steps, initial_state=initial_state_from_config(config), config=config)
    return mcsim.unzip_dict(outcomes)

