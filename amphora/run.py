import pandas as pd
import numpy as np
from datetime import datetime, timedelta

from pandemic.simulation import simulate
from pandemic.conventions import VULNERABLE, INFECTED, SYMPTOMATIC, POSITIVE, RECOVERED, DECEASED
from pandemic.example_parameters import TOY_TOWN

# VULNERABLE, INFECTED, SYMPTOMATIC, POSITIVE, RECOVERED, DECEASED

t0 = datetime.utcnow()

column_names = {
    't': 't',
    'day': 'day',
    'day_fraction': 'day_fraction',
    VULNERABLE: 'vulnerable',
    INFECTED: 'infected',
    SYMPTOMATIC: 'symptomatic',
    POSITIVE: 'positive',
    RECOVERED: 'recovered',
    DECEASED: 'deceased',
}

data = {
    't': [],
    'day': [],
    'day_fraction': [],
    VULNERABLE: [],
    INFECTED: [],
    SYMPTOMATIC: [],
    POSITIVE: [],
    RECOVERED: [],
    DECEASED: [],
}

def data_append(row: dict, key: str):
    if key in row:
        data[key].append(row[key])
    else:
        data[key].append(0)


# callback(day=day, day_fraction=day_fraction , home=home, work=work, positions=positions, status=status, params=params, step_no=step_no, plot_hourly=plot_hourly, plt=plt)
def c(day, day_fraction , home, work, positions, status, params, step_no, plot_hourly, plt ):

    unique, counts = np.unique(status, return_counts=True)
    d = dict(zip(unique, counts))
    # append things
    data['day'].append(day)
    data['day_fraction'].append(day_fraction)
    data['t'].append(t0 + timedelta(days=day, minutes=day_fraction * 3600))
    data_append(d, VULNERABLE)
    data_append(d, INFECTED)
    data_append(d, SYMPTOMATIC)
    data_append(d, POSITIVE)
    data_append(d, RECOVERED)
    data_append(d, DECEASED)

print("Starting Simulation...")
simulate(TOY_TOWN, callback=c)

df = pd.DataFrame(data)

df = df.rename(columns=column_names)

print(df.head())

print("Finished.")