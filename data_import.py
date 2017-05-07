import pandas as pd

def load_states(filename):
    """
    Load US States' Polygon Coordinates data and add a column 'Polygon Coordinates' with Polygon coordinates in
    appropriate format
    
    Input: filename, type: string
    
    Output: US States' Polygon Coordinates data, type: Pandas Dataframe
    """
    f = open(filename, 'r')
    S = list(f)
    columns =  S[0].strip('\n').split('\t')
    us_states_dict = dict()
    i = 0
    for line in S[1:]:
        us_states_dict[i] = {key: value for (key, value) in zip(columns, line.strip('\n').split('\t'))}
        i += 1
    f.close()

    df = pd.DataFrame.from_dict(us_states_dict, orient='index')

    t = df['GEOMETRY'].apply(lambda x: x.split(' (')[1].strip(')(').split(','))
    df['Polygon Coordinates'] = t.apply(lambda y: map(lambda x: (float(x.strip(' ').split(' ')[0]), float(x.strip(' ').split(' ')[1])), y))
    return df

def load_data(filename):
    """
    Load Accumulation data and add a column 'Coordinates' with site coordinates in appropriate format
    
    Input: filename, type: string
    
    Output: Accumulation data, type: Pandas Dataframe
    """
    df = pd.read_excel(filename, sheetname= 'supplier list')
    df['Coordinates'] = map(lambda x,y: (x, y), df['Longitude'], df['Latitude'])
    return df