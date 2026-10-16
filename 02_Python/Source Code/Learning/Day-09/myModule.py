def normalise(data):
    """Normalise a list of numbers to 0-1 range"""
    mn, mx = min(data), max(data)
    return [(x - mn) / (mx - mn) for x in data]

def get_grade(marks):
    """Return grade letter for a marks value"""
    for t, g in [(90,"A+"),(80,"A"),(70,"B"),(60,"C"),(50,"D")]:
        if marks >= t:
            return g
    return "F"

PI = 3.14159

def class_stats(marks):
    if marks >= 50:
        return f"{marks} --> Pass"
    else:
        return f"{marks} --> Fail"
