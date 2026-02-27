import pandas as pd

#1
def dic_a_series(diccionario):
    serie = pd.Series(list(diccionario.values()), index = list(diccionario.keys()))
    min, max, mean, std = serie.min(), serie.max(), serie.mean(), serie.std()
    serie_calc = pd.Series([min, max, mean, std], index = ["Min", "Max", "Mean", "Std"])
    return serie_calc

dic_notas_alumnos = {"Alumno 1": 5, "Alumno 2": 4.3,
                     "Alumno 3" : 4.4, "Alumno 5": 2}

output = dic_a_series(dic_notas_alumnos)
print(output)

#2
dataFrame = pd.read_csv("pacientes_VitalDB (1).csv")
dataFrame = dataFrame.rename(columns={'weight': 'height', 'height': 'weight'})
print(dataFrame.iloc[[0, -1]])
print(dataFrame.describe())


dataFrame["BMI"] = dataFrame["weight"] / (dataFrame["height"]/100)**2
print(dataFrame["BMI"])