#%%
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a dataset with planet data
data = {
    'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'Distance_from_Sun': [57.9, 108.2, 149.6, 227.9, 778.3, 1427, 2871, 4497.1],  # in million km
    'Diameter': [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528]  # in km
}

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)

# Create a scatterplotsu
scatter_plot = sns.scatterplot(data=df, x='Distance_from_Sun', y='Diameter', hue='Planet', s=100)

# Add titles and labels
plt.title('Planet Data: Distance from Sun vs Diameter')
plt.xlabel('Distance from Sun (million km)')
plt.ylabel('Diameter (km)')

# Show the plot
plt.show()