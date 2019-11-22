import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt 
import seaborn as sns
import json
sns.set_style('darkgrid')

# Use this in notebook to show plots
%matplotlib inline

def idToName(ID, dic):
    champ = dic['name'][ID]
    return champ

def getTag(name, data):
    tags = data['tags'][name][0]
    return tags

def numToColor(data):
    if data == 0:
        color = 'blue'
    else:
        color = 'red'
    return color
