#!/usr/bin/env python3
"""
Name:       Sara Nicholson
Date:       3 February 2022
Description: Classes Circle and Graduate Student 
"""
class Circle():
    """ class containing common mathematic methods for circles """
    def __init__(self, color, radius):
        self.color = color
        self.radius = radius

    def diameter(self):
        """ computes diameter of circle"""
        diameter = float(self.radius) * 2
        return diameter

    def circumfrence(self):
        """ calculates circumference of circle """
        circumference = 2 * 3.14 * self.radius
        return circumference

    def isRed(self):
        """ returns true if circle is red """
        if self.color.lower()  == "red":
                return True
        else:
            return False


class GraduateStudent():
    """ Grad Student Information """
    def __init__(self, first_name, last_name, year, major):
        self.first_name = first_name
        self.last_name = last_name
        self.year = year
        self.major = major

    def year_matriculated(self):
        """ returns year that student began studies """
        return 2021 - self.year


if __name__ == "__main__":
    """ Begin Utilization of Classes """
    circleA = Circle("Red", 5)
    circleB = Circle("blue", 2)
    print(circleA.isRed())
    print(circleB.isRed())
    print(circleA.circumfrence())
    
    Sara = GraduateStudent("sara", "nicholson", 3, "Bioinformatics")
    Dani = GraduateStudent("Dani", "Del Val", 1, "Marketing")
    print(Sara.year_matriculated())
    print(Dani.year_matriculated())
