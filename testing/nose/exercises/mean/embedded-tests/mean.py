def mean(numlist):
    try:
        total = sum(numlist)
        length = len(numlist)
    except TypeError:
        raise TypeError("The number list was not a list of numbers.")
    except:
        print "There was a problem evaluating the number list."
    return total/length


def test_mean():
    assert mean([0, 0, 0, 0]) == 0
    assert mean([0, 200]) == 100
    assert mean([0, -200]) == -100
    assert mean([0]) == 0


def test_floating_mean():
    assert mean([1, 2]) == 1.5
