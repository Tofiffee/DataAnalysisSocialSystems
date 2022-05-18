import os

import pandas as pd
import scipy.stats as stats
import numpy as np

path = os.path.dirname(os.path.realpath(__file__))


together_two_36 = []


def claculationsTwo26(filename):
    together_two_26 = []
    socialTogether_two_26 = []

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '26Degree', filename), sep=';', encoding='utf-8')
    try:
        together_two_26.append(df['BeesTogether'].sum()*0.2)
    except KeyError:
        print(filename)

    socialContact = df['socialTogether'].tolist()
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
    socialTogether_two_26 = np.array(socialTogether_two_26)
    socialTogether_two_26 = socialTogether_two_26 * 0.2
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

    socialContact = df['socialTogether'].tolist()
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

    socialTogether_two_36 = np.array(socialTogether_two_36)
    socialTogether_two_36 = socialTogether_two_36 * 0.2
    return socialTogether_two_36


np_array_26 = np.array([])
np_array_36 = np.array([])


for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '26Degree')):
    array = claculationsTwo26(filename)
    np_array_26 = np.hstack((np_array_26,array))

for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree')):
    array = claculationsTwo36(filename)
    np_array_36 = np.hstack((np_array_36, array))

print(np_array_26)
print(np_array_36)        












# for filename in os.listdir(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree')):
#     df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree', filename), sep=';', encoding='utf-8')
#     try:
#         together_two_36.append(df['BeesTogether'].sum()*0.2)
#     except KeyError:
#         print(filename)

# print(together_two_26)
# print(together_two_36)

# print(stats.ks_2samp(together_two_26, together_two_36, alternative='greater', mode='exact'))
# print(stats.mannwhitneyu(together_two_26, together_two_36, alternative='less'))