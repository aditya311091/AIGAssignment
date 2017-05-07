import pandas as pd

def isleft(p0, p1, p2):
    """
    Tests if a point is Left|On|Right of an infinite line
    
    Input: 3 points p0, p1 and p2 such that p0 and p1 make a line with respect to which direction of p2 is determined
    
    Output: >0 for P2 left of the line through P0 and P1
            =0 for P2  on the line
            <0 for P2  right of the line
    """
    return ((p1[0] - p0[0]) * (p2[1] - p0[1]) - (p2[0] -  p0[0]) * (p1[1] - p0[1]))

    
def wn_PnPoly(Point, Polygon):
    """
    Winding number test for determining if a given point lies in a given polygon
    
    Input:
    1. Point: Coordinates of the Given Point, type = tuple in the format (Longitude, Latitude)
    2. Polygon: List of Coordinates of the Given Polygon, type = list of tuples in same format as Point
        with same first and last tuples(Closed Polygon)
    
    Output: wn, Winding Number, type = float with value = 0 only when Point is outside the Polygon
    """
    wn = 0
    n = len(Polygon) - 1
    for i in range(n):
        if Polygon[i][1] <= Point[1]:
            if (Polygon[i+1][1] > Point[1]) and (isleft(Polygon[i], Polygon[i+1], Point) > 0):
                wn += 1
        else:
            if (Polygon[i+1][1] <= Point[1]) and (isleft(Polygon[i], Polygon[i+1], Point) < 0):
                wn -= 1
    return wn

def get_state_id(Coordinates, states):
    """
    Find out the State whose polygon coordinates enclose a given set of Coordinates
    
    Input:
    1. Coordinates, type = tuple in the format (Longitude, Latitude)
    2. States, type = Pandas Dataframe consisting of tsv file of US States coordinates
    
    Output: State Code of the enclosing State, type = str
    """
    
    for (i,polygon) in enumerate(states['Polygon Coordinates']):
        if (wn_PnPoly(Coordinates, polygon) != 0):
            return list(states['STATE_CODE'])[i]
        
def id_to_state(states):
    """
    Store unique State names and codes in a dictionary
    
    Input: states, type = Pandas Dataframe consisting of tsv file of US States coordinates
    
    Output: id_to_state, type = dictionary with keys as State Codes and values as State Names
    """
    
    state_id = states[['STATE_CODE','STATE_NAME']].drop_duplicates()

    id_to_state = {k.strip(' '):v.strip(' ') for (k, v) in zip(state_id['STATE_CODE'], state_id['STATE_NAME'])}
    
    return id_to_state