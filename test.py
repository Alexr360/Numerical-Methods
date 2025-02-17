import numpy as np

TC = np.array([23.5, 24.1, 22.8, 25.0, 23.9, 24.5, 22.7, 24.8, 23.6, 25.2])

def data_analysis_temperature_measurements(TC):
    mean = np.mean(TC)
    standard_deviation = np.std(TC)
    TF = (9/5) * TC + 32
    MaxF = TF.max()
    MinF = TF.min()
    MaxC = TC.max()
    MinC = TC.min()
    return: mean, standard_deviation, TF, MaxF, MinF, MaxC, MinC

mean, standard_deviation, TF, MaxF, MinF, MaxC, MinC = data_analysis_temperature_measurements(TC)