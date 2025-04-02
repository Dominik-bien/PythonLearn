import plotly.express as px
from die import Die 

die = Die()

results = []
for roll_num in range(1000): 
    result = die.roll()
    results.append(result)

frequencies = []
poss_results = range(1, die.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


title = "Result dice roll D6 1000th "
labels = {'x': 'Result', 'y': 'Precence of frequency values'}
fig = px.line(x=poss_results, y=frequencies, title=title,  labels=labels)
fig.show()