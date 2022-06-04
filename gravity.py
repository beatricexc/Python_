#! /usr/bin/env python
"""
This is free software: you can redistribute it and/or modify it under the terms
of the GNU General Public License as published by the Free Software Foundation,
either version 3 of the License, or (at your option) any later version. It is
distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY;
without even the implied warranty of MERCHANTABILITY or FITNESS FOR A
PARTICULAR PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with
the code.  If not, see <http://www.gnu.org/licenses/>.

File name: 	gravity.py
Created:	June 18th, 2020
Author:	Dr. Robert Lyon (lyonro@edgehill.ac.uk)

Contact: lyonro@edgehill.ac.uk
Web: www.edgehill.ac.uk/computerscience/people/academic-staff/robert-lyon/

"""


def compute_attraction(m1, m2, r):
    """
    Computes the force of gravitational attraction between two objects.

    :param m1: mass of the first object in kilograms.
    :param m2: mass of the second object in kilograms.
    :param r: distance between the objects in metres.

    :return: the attraction force between the objects in Newtons (float).
    """

    g = 6.6743 * pow(10, -11)  # Fixed gravitational constant

    return (g * m1 * m2) / (r * r)
