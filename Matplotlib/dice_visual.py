import plotly.express as px
from die import Die 

die1 = Die(6)
die2 = Die(6)


results = []
for roll_num in range(1000): 
    result = die1.roll() * die2.roll()
    results.append(result)

frequencies = []
max_result = die1.num_sides + die2.num_sides
poss_results = range(2, max_result+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)


title = "Result dice roll D6 1000th "
labels = {'x': 'Result', 'y': 'Precence of frequency values'}
fig = px.bar(x=poss_results, y=frequencies, title=title,  labels=labels)

fig.update_layout(xaxis_dtick=1)
fig.write_html('dice_visual_d6d10.html')
fig.show()