def valid_triangle(sides):
    return (
        all(side > 0 for side in sides)
        and sides[0] + sides[1] >= sides[2]
        and sides[0] + sides[2] >= sides[1]
        and sides[1] + sides[2] >= sides[0]
    )

def equilateral(sides):
    if any(side == 0 for side in sides):
        return False
    if sides[0] == sides[1] == sides[2]:
        return True
    return False


def isosceles(sides):
    return (
        valid_triangle(sides)
        and (
            sides[0] == sides[1]
            or sides[0] == sides[2]
            or sides[1] == sides[2]
        )
    )

def scalene(sides):
  return (
        valid_triangle(sides)and
        sides[0] != sides[1] and
        sides[0] != sides[2] and
        sides[1] != sides[2]    
    )
