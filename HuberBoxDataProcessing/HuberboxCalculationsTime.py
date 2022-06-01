import os

import pandas as pd
import numpy as np

path = os.path.dirname(os.path.realpath(__file__))

def claculationsTwo26(filename):
    together_two_26 = []
    socialTogether_two_26 = []

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '26Degree', filename), sep=';', encoding='utf-8')
    try:
        together_two_26.append(df['BeesTogether'].sum()*0.2)
    except KeyError:
        print(filename)

    socialContact = df['socialTogether'].to_numpy()
    counter = 0
    for i in socialContact:
        if i == 1:
            counter += 1
        elif i == 0:
            if counter != 0:
                socialTogether_two_26.append(counter)
                counter = 0
            elif counter == 0:
                pass

    socialTogether_two_26 = np.array(socialTogether_two_26) * 0.2
    socialTogether_two_26 = np.setdiff1d(socialTogether_two_26, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_two_26

def claculationsTwo36(filename):
    together_two_36 = []
    socialTogether_two_36 = []

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )
    
    try:
        together_two_36.append(df['BeesTogether'].sum()*0.2)
    except KeyError:
        print(filename)

    socialContact = df['socialTogether'].to_numpy()
    counter = 0
    for i in socialContact:
        if i == 1:
            counter += 1
        elif i == 0:
            if counter != 0:
                socialTogether_two_36.append(counter)
                counter = 0
            elif counter == 0:
                pass

    socialTogether_two_36 = np.array(socialTogether_two_36) * 0.2
    socialTogether_two_36 = np.setdiff1d(socialTogether_two_36, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_two_36

def claculationsThree26(filename):
    together_three_26 = []
    socialTogether_three_26 = []

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '26Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )
    
    try:
        together_three_26.append(df['BeesClose1_2_3'].sum()*0.2)
    except KeyError:
        print(filename)

    try:
        socialContact = df['socialTogether'].to_numpy()
    except KeyError:
        print(filename)
    counter = 0
    
    for i in socialContact:
        if i == 1:
            counter += 1
        elif i == 0:
            if counter != 0:
                socialTogether_three_26.append(counter)
                counter = 0
            elif counter == 0:
                pass

    socialTogether_three_26 = np.array(socialTogether_three_26) * 0.2
    socialTogether_three_26 = np.setdiff1d(socialTogether_three_26, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_three_26

def claculationsThree36(filename):
    together_three_36 = []
    socialTogether_three_36 = []

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '36Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )
    
    try:
        together_three_36.append(df['BeesClose1_2_3'].sum()*0.2)
    except KeyError:
        print(filename)

    try:
        socialContact = df['socialTogether'].to_numpy()
    except KeyError:
        print(filename)
    
    counter = 0
    
    for i in socialContact:
        if i == 1:
            counter += 1
        elif i == 0:
            if counter != 0:
                socialTogether_three_36.append(counter)
                counter = 0
            elif counter == 0:
                pass

    socialTogether_three_36 = np.array(socialTogether_three_36) * 0.2
    socialTogether_three_36 = np.setdiff1d(socialTogether_three_36, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_three_36