import os

import pandas as pd
import numpy as np

path = os.path.dirname(os.path.realpath(__file__))

def claculationsTwo26(filename: str) -> np.ndarray:
    """This function calculates the time the bees spent together as well as the social time the bees spend together

    Args:
        filename (str): the file that should be processed from the given folder

    Returns:
        np.ndarray: array of the durations of social contacts in one experimental run
    """
    together_two_26 = []
    socialTogether_two_26 = []

    # reads in the data from the processed data dir
    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '26Degree', filename), sep=';', encoding='utf-8')

    # cycle trough social contact to look how long the social contact is
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

    # transformes timespeps of social contact to seconds
    socialTogether_two_26 = np.array(socialTogether_two_26) * 0.2
    # removes all social contacts with duration less then 1 second
    socialTogether_two_26 = np.setdiff1d(socialTogether_two_26, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_two_26

def claculationsTwo36(filename: str) -> np.ndarray:
    """This function calculates the time the bees spent together as well as the social time the bees spend together

    Args:
        filename (str): the file that should be processed from the given folder

    Returns:
        np.ndarray: array of the durations of social contacts in one experimental run
    """
    together_two_36 = []
    socialTogether_two_36 = []

    # reads in the data from the processed data dir
    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )

    # cycle trough social contact to look how long the social contact is
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
    
    # transformes timespeps of social contact to seconds
    socialTogether_two_36 = np.array(socialTogether_two_36) * 0.2
    # removes all social contacts with duration less then 1 second
    socialTogether_two_36 = np.setdiff1d(socialTogether_two_36, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_two_36

def claculationsThree26(filename: str) -> np.ndarray:
    """This function calculates the time the bees spent together as well as the social time the bees spend together

    Args:
        filename (str): the file that should be processed from the given folder

    Returns:
        np.ndarray: array of the durations of social contacts in one experimental run
    """
    together_three_26 = []
    socialTogether_three_26 = []

    # reads in the data from the processed data dir
    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '26Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )

    # cycle trough social contact to look how long the social contact is
    socialContact = df['socialTogether'].to_numpy()
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
    
    # transformes timespeps of social contact to seconds
    socialTogether_three_26 = np.array(socialTogether_three_26) * 0.2
    # removes all social contacts with duration less then 1 second
    socialTogether_three_26 = np.setdiff1d(socialTogether_three_26, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_three_26

def claculationsThree36(filename: str) -> np.ndarray:
    """This function calculates the time the bees spent together as well as the social time the bees spend together

    Args:
        filename (str): the file that should be processed from the given folder

    Returns:
        np.ndarray: array of the durations of social contacts in one experimental run
    """
    together_three_36 = []
    socialTogether_three_36 = []

    # reads in the data from the processed data dir
    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '36Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )

    # cycle trough social contact to look how long the social contact is
    socialContact = df['socialTogether'].to_numpy()
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
    
    # transformes timespeps of social contact to seconds
    socialTogether_three_36 = np.array(socialTogether_three_36) * 0.2
    # removes all social contacts with duration less then 1 second
    socialTogether_three_36 = np.setdiff1d(socialTogether_three_36, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_three_36

def claculationsThree26Two(filename: str) -> np.ndarray:
    """This function calculates the time the bees spent together as well as the social time the bees spend together

    Args:
        filename (str): the file that should be processed from the given folder

    Returns:
        np.ndarray: array of the durations of social contacts in one experimental run
    """
    socialTogether_three_26_Two = []

    # reads in the data from the processed data dir
    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '26Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )

    # cycle trough social contact to look how long the social contact is
    socialContact = df['socialTogetherTwo'].to_numpy()
    counter = 0

    for i in socialContact:
        if i == 1:
            counter += 1
        elif i == 0:
            if counter != 0:
                socialTogether_three_26_Two.append(counter)
                counter = 0
            elif counter == 0:
                pass
    
    # transformes timespeps of social contact to seconds
    socialTogether_three_26_Two = np.array(socialTogether_three_26_Two) * 0.2
    # removes all social contacts with duration less then 1 second
    socialTogether_three_26_Two = np.setdiff1d(socialTogether_three_26_Two, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_three_26_Two

def claculationsThree36Two(filename: str) -> np.ndarray:
    """This function calculates the time the bees spent together as well as the social time the bees spend together

    Args:
        filename (str): the file that should be processed from the given folder

    Returns:
        np.ndarray: array of the durations of social contacts in one experimental run
    """
    socialTogether_three_36_Two = []

    # reads in the data from the processed data dir
    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '36Degree', filename), 
    sep=';', 
    encoding='utf-8'
    )

    # cycle trough social contact to look how long the social contact is
    socialContact = df['socialTogetherTwo'].to_numpy()
    counter = 0
    
    for i in socialContact:
        if i == 1:
            counter += 1
        elif i == 0:
            if counter != 0:
                socialTogether_three_36_Two.append(counter)
                counter = 0
            elif counter == 0:
                pass
    
    # transformes timespeps of social contact to seconds
    socialTogether_three_36_Two = np.array(socialTogether_three_36_Two) * 0.2
    # removes all social contacts with duration less then 1 second
    socialTogether_three_36_Two = np.setdiff1d(socialTogether_three_36_Two, np.array([0.2, 0.4, 0.6, 0.8]))

    return socialTogether_three_36_Two