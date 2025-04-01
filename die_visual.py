from die import Die
import plotly.express as px

dice = Die()

results = []

for _ in range(1000):
    result = dice.roll()
    results.append(result)
    
    
frequencies = []
poss_results = range(1, dice.num_sides+1)
for value in poss_results:
    frequency = results.count(value)
    frequencies.append(frequency)
    

fig = px.bar(x=poss_results, y=frequencies)
fig.show()