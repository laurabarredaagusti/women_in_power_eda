import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.patches as mpatches
import numpy as np
from matplotlib.gridspec import GridSpec
import matplotlib as mpl


# Todos los archivos de la base de datos de Europe Force Work
# Incluye total, managers, professionals, technicians y support
europe_worker_force_total = pd.read_csv('total_european_work_force.csv')
europe_worker_force_total.drop('Unnamed: 0', inplace=True, axis=1)

europe_worker_force_managers = pd.read_csv('managers_european_work_force.csv')
europe_worker_force_managers.drop('Unnamed: 0', inplace=True, axis=1)

europe_worker_force_professionals = pd.read_csv('professionals_european_work_force.csv')
europe_worker_force_professionals.drop('Unnamed: 0', inplace=True, axis=1)

europe_worker_force_technicians = pd.read_csv('technicians_european_work_force.csv')
europe_worker_force_technicians.drop('Unnamed: 0', inplace=True, axis=1)

europe_worker_force_support = pd.read_csv('support_european_work_force.csv')
europe_worker_force_support.drop('Unnamed: 0', inplace=True, axis=1)

# Modificación de la tabla del total para incluir las variaciones por años del número de mujeres y hombres trabajando
distribution_men_women_total_work_force_europe = pd.DataFrame({
    'male' : [europe_worker_force_total.iloc[0]['2019_males'], europe_worker_force_total.iloc[0]['2020_males'], europe_worker_force_total.iloc[0]['2021_males'], europe_worker_force_total.iloc[0]['2022_males']],
    'female' : [europe_worker_force_total.iloc[0]['2019_females'], europe_worker_force_total.iloc[0]['2020_females'], europe_worker_force_total.iloc[0]['2021_females'], europe_worker_force_total.iloc[0]['2022_females']]
    },index = ['2019', '2020', '2021', '2022'])

# Mezcla de las tablas originales para mostrar todos los niveles juntos, de mujeres y hombres, del 2022
dictionary_worker_force_europe_2022 = {'managers' : [europe_worker_force_managers.iloc[0]['2022_females'], europe_worker_force_managers.iloc[0]['2022_males']],
                                        'professionals' : [europe_worker_force_professionals.iloc[0]['2022_females'], europe_worker_force_professionals.iloc[0]['2022_males']],
                                        'technicians' : [europe_worker_force_technicians.iloc[0]['2022_females'], europe_worker_force_technicians.iloc[0]['2022_males']],
                                        'support' : [europe_worker_force_support.iloc[0]['2022_females'], europe_worker_force_support.iloc[0]['2022_males']],
                                        'gender' : ['Female', 'Male']}

dataframe_worker_force_europe_2022 = pd.DataFrame.from_dict(dictionary_worker_force_europe_2022)

# Mezcla de las tablas originales para mostrar el dato de europa de todas las profesiones en todos los años
comparison_dictionary_años = {'años' : ['2019', '2019', '2020', '2020', '2021', '2021', '2022', '2022'],
                                    'numero_managers': [europe_worker_force_managers.iloc[0]['2022_females'], europe_worker_force_managers.iloc[0]['2022_males'], europe_worker_force_managers.iloc[0]['2021_females'], europe_worker_force_managers.iloc[0]['2021_males'], europe_worker_force_managers.iloc[0]['2020_females'], europe_worker_force_managers.iloc[0]['2020_males'], europe_worker_force_managers.iloc[0]['2019_females'], europe_worker_force_managers.iloc[0]['2019_males']],
                                    'numero_professionals' : [europe_worker_force_professionals.iloc[0]['2022_females'], europe_worker_force_professionals.iloc[0]['2022_males'], europe_worker_force_professionals.iloc[0]['2021_females'], europe_worker_force_professionals.iloc[0]['2021_males'], europe_worker_force_professionals.iloc[0]['2020_females'], europe_worker_force_professionals.iloc[0]['2020_males'], europe_worker_force_professionals.iloc[0]['2019_females'], europe_worker_force_professionals.iloc[0]['2019_males']],
                                    'numero_technicians' : [europe_worker_force_technicians.iloc[0]['2022_females'], europe_worker_force_technicians.iloc[0]['2022_males'], europe_worker_force_technicians.iloc[0]['2021_females'], europe_worker_force_technicians.iloc[0]['2021_males'], europe_worker_force_technicians.iloc[0]['2020_females'], europe_worker_force_technicians.iloc[0]['2020_males'], europe_worker_force_technicians.iloc[0]['2019_females'], europe_worker_force_technicians.iloc[0]['2019_males']],
                                    'numero_support' : [europe_worker_force_support.iloc[0]['2022_females'], europe_worker_force_support.iloc[0]['2022_males'], europe_worker_force_support.iloc[0]['2021_females'], europe_worker_force_support.iloc[0]['2021_males'], europe_worker_force_support.iloc[0]['2020_females'], europe_worker_force_support.iloc[0]['2020_males'], europe_worker_force_support.iloc[0]['2019_females'], europe_worker_force_support.iloc[0]['2019_males']],
                                    'gender' : ['F', 'M', 'F', 'M', 'F', 'M', 'F', 'M']}

comparison_dataframe_años = pd.DataFrame.from_dict(comparison_dictionary_años)

# Leemos el archivo de mujeres en boards en todo el mundo por países (porcentales)
boards_world_percentage = pd.read_csv('paises_seleccionados_board_world_percentage.csv')

# boards_world_percentage_max_min = pd.read_csv('women_board_percentage_max_min_world.csv')

# Leemos el archivo de mujeres en managers en todo el mundo por países (porcentales)
# managers_world_percentage_max_min = pd.read_csv('women_managers_worldwide.csv')