from data_import import load_states, load_data
from helping_functions import get_state_id, id_to_state
import pandas as pd

#Load tsv file with polygon coordinates of US States
states = load_states('data\US States Polygons.tsv')

#Load the Data collected by Underwriter Sheila
data = load_data('data\Example Supplier List.xlsx')

#Prepare a dictionary with key:value as 'State Code': 'State Name'
code_to_state = id_to_state(states)

#Fill up 'States' column using Coordinates of sites
data['State'] = data['Coordinates'].apply(lambda x: code_to_state.get(get_state_id(x, states)))

#Find out State-wise accumulations using groupby
output = data.groupby('State')['Insured Limit ($ in thousands)'].sum()

output = output.add_suffix('').reset_index()

#Save the output to a csv file: 'State-level Accumulations.csv'
output.to_csv('State-level Accumulations.csv')