#!/usr/bin/python

"""
Python Core object Types
"""

import math

def numbers_and_strings():
    """
    This is to review numbers and strings and basic operations.
    """
    # Assign a string "EE551" to a variable x
    x = "EE551";
    print('x = ',x);
    
    # Assign a string "Stevens" to a variable y
    y = "Stevens";
    print('y = ', y);
    
    # Repeat variable y 5 times
    z = y * 5;
    print('z = ', z);
    
    # What is the length of z?    
    length = len(z);
    print('length of z is ', length);
    
    # Concatenate variable y with string " is good"    
    m = y + ' is good';
    print('m = ',m);
    
    # Replace "good" with "awesome" in variable m and assign it to a new variable n   
    n = m.replace('good', 'awesome');
    print('n = ',n);
    print('-----------------------------------------------------');
    return x, y, z, length, m, n;

def lists():
    """
    This is to review basic operations with lists.
    """
    n = "Stevens is awesome";

    # Split variable n on a delimiter space into a list of substrings
    p = n.split(' ');
    print('p = ',p);
    
    # Get all the items past the first of the third substring
    r = p[2][1:];
    print('r = ',r);
    
    # Create a 3 x 3 matrix as nested list such that
    #   first row is [1, 4, 5]
    #   second row is [6, 10, 11]
    #   third row is [12, 17, 38]
    A = [[1, 4, 5], [6, 10, 11], [12, 17, 38]];
    print('matrix A is ',A);
    
    # Collect the items in the last column of matrix A using list comprehension
    c = [];
    for row in A:
        c.append(row[2]);
    print('c = ',c);
    # Collect only the even items of the diagonal of matrix A using list comprehension
    d = [];
    for each in A[0][0], A[0][2], A[1][1], A[2][0], A[2][2]:
        if (each % 2 == 0):
            d.append(each);
    print('d = ',d);
    # We can convert a single character to its underlying integer code (e.g., its ASCII byte value)
    # by passing it to the built-in ord function. Generate a list of these integers to represent
    # each character of the string "Stevens" using list comprehension.
    o = [ord(each) for each in 'Stevens'];
    print('o = ',o);
    print('-----------------------------------------------------');
    return p, r, c, d, o


def dictionaries():
    """
    This is to review basic operations with dictionaries.
    """
    # Create a dictionary that maps:
    #   fruit => "apple"
    #   quantity => 4
    #   color => "green"
    f = {'fruit' : 'apple', 'quantity' : 4, 'color' : 'green'};
    print('f = ',f);
    
    # Get the item in dictionary f that the key "fruit" maps to
    a = f['fruit'];
    print('a = ',a);
    
    # Increase the quantity of f by 1
    # IMPLEMENT IT HERE
    f['quantity'] = f['quantity'] + 1;
    print('The quantity of f increased by 1 is ',f['quantity']);
    
    # Create a nested dictionary where:
    #   name => {first_name => "Grace", last_name => "Hopper"} (a dictionary)
    #   jobs => ["scientist", "engineer"] (a list)
    #   age => 85
    amzing_grace = {'name' : {'first_name' : 'Grace', 'last_name' : 'Hopper'}, 'jobs' : ['scientist', 'engineer'], 'age' : 85};
    print('amzing_grace = ', dict);
    # Add "programmer" to the list of jobs Grace has
    # IMPLEMENT IT HERE
    amazing_grace['jobs'].append('programmer');
    # Get the third job Grace has that you recently added
    p = amazing_grace['jobs'][2];
    print['The third job Grace has is ', p];
    # Use the sort() function to get sorted keys of amazing_grace in alphabetically ascending order
    
    return a, f, p, k

numbers_and_strings()
lists()
dictionaries()
