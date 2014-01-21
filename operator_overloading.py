

class Point2D(object):

    def __init__(self, x=0.0, y=0.0):
        """
        Create a new Point2D object. Coordinates default to 0 if none 
        are given.
        """
        self.x = x
        self.y = y

    def __add__(self, other):
        """Add two Point2Ds together, and return a new Point2D."""
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Point2D(x_new, y_new)

    def __mul__(self, other):
        """
        Multiply self with other, returning the result in a new 
        Point2D.
        
        If other is a scalar, multiply other to both x and y, otherwise 
        corresponding coordinates are added.
        """

        if isinstance(other, int) or isinstance(other, float):
            return Point2D(self.x * other, self.y * other)
        else:
            return Point2D(self.x * other.x, self.y * other.y)

    def __eq__(self, other):
        """
        Test self and other for equality (self.x == other.x and 
        self.y == other.y)
        """
        if not isinstance(other, Point2D):
            return False
        else:
            return self.x == other.x and self.y == other.y

    def __repr__(self):
        return '<operator_overloading.Point2D at {0} with x={1} and y={2}>'.format(id(self), self.x, self.y)
