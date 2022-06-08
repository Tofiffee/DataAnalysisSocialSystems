import os

import pandas as pd
import numpy as np


def speedOne26(filename):

    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'OneBee', '26Degree', filename), sep=';', encoding='utf-8')

    speedValues = df['distancePerSec'].to_numpy()
    speedValues = np.setdiff1d(speedValues, np.array([0]))

    return speedValues

def speedOne36(filename):

    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'OneBee', '36Degree', filename), sep=';', encoding='utf-8')

    speedValues = df['distancePerSec'].to_numpy()
    speedValues = np.setdiff1d(speedValues, np.array([0]))

    return speedValues

def speedTwo26(filename):

    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '26Degree', filename), sep=';', encoding='utf-8')

    speedValues1 = df['distancePerSec1'].to_numpy()
    speedValues2 = df['distancePerSec2'].to_numpy()
    speedValues = np.hstack((speedValues1, speedValues2))
    speedValues = np.setdiff1d(speedValues, np.array([0]))

    return speedValues


def speedTwo36(filename):
    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'TwoBees', '36Degree', filename), sep=';', encoding='utf-8')

    speedValues1 = df['distancePerSec1'].to_numpy()
    speedValues2 = df['distancePerSec2'].to_numpy()
    speedValues = np.hstack((speedValues1, speedValues2))
    speedValues = np.setdiff1d(speedValues, np.array([0]))

    return speedValues


def speedThree26(filename):

    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '26Degree', filename), sep=';', encoding='utf-8')

    speedValues1 = df['distancePerSec1'].to_numpy()
    speedValues2 = df['distancePerSec2'].to_numpy()
    speedValues3 = df['distancePerSec3'].to_numpy()
    speedValues = np.hstack((speedValues1, speedValues2))
    speedValues = np.hstack((speedValues, speedValues3))
    speedValues = np.setdiff1d(speedValues, np.array([0]))

    return speedValues

def speedThree36(filename):

    path = os.path.dirname(os.path.realpath(__file__))

    df = pd.read_csv(os.path.join(os.path.dirname(path), 'data', 'processedData', 'ThreeBees', '36Degree', filename), sep=';', encoding='utf-8')

    speedValues1 = df['distancePerSec1'].to_numpy()
    speedValues2 = df['distancePerSec2'].to_numpy()
    speedValues3 = df['distancePerSec3'].to_numpy()
    speedValues = np.hstack((speedValues1, speedValues2))
    speedValues = np.hstack((speedValues, speedValues3))
    speedValues = np.setdiff1d(speedValues, np.array([0]))

    return speedValues
