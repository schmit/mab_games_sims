import pickle
import time

def dump(obj, fname):
    """
    Saves simulation outcome to pickle file
    """
    fpath = "simulations/{}.pickle".format(fname)
    with open(fpath, "wb") as f:
        pickle.dump(obj, f)

    # print("Dumped to {}".format(fpath))

def loads(fname):
    """
    Loads simulation from pickle file
    """
    fpath = "simulations/{}.pickle".format(fname)
    with open(fpath, "rb") as f:
        obj = pickle.load(f)
    # print("Loaded from {}".format(fpath))

    return obj


def lifespan_to_beta(lifespan):
    """ convert average lifespan to beta"""
    return 1 - 1/lifespan

def progress(itr, total, t_start):
    """ print progress """
    runtime = time.time() - t_start
    p_done = (itr+1) / total

    eta = (1-p_done)/p_done * runtime
    print("\t {:5.1f}% \t {:5.2f}s \t {:5.2f}s".format(100*p_done, runtime, eta))
