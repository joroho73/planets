import matplotlib
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

# Create a dataset with planet data
data = {
    'Planet': ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune'],
    'Distance_from_Sun': [57.9, 108.2, 149.6, 227.9, 778.3, 1427, 2871, 4497.1],  # in million km
    'Diameter': [4879, 12104, 12756, 6792, 142984, 120536, 51118, 49528], # in km
    'xOffset': [5, 11, 30, 50, 200, 600, 400, 900], # x for point labels
    'yOffset': [27, 56, 55, 70, 550, 950, 1600, 2200] # y for point labels
        
}

# Convert the dataset into a DataFrame
df = pd.DataFrame(data)
df['Diameter_skewed'] = np.square(df['Diameter'])  # to make the size of points more visible
custom_params = {"axes.spines.right": False, "axes.spines.top": False,"axes.spines.left":False}

# Styles and themes
sns.set_theme(context='paper',
              font_scale = 0.8,
              style = 'darkgrid',
              rc={'text.color':'b',
                  'grid.color': 'b',
                  'lines.color': 'b',
                  'lines.markerfacecolor': 'b',
                  'patch.edgecolor': 'b',
                'patch.facecolor': 'b',
                'scatter.edgecolors': 'b',
                  }) #

sns.despine()


# Create a scatterplot
sns.scatterplot(data=df, x='Distance_from_Sun', 
                            y='Distance_from_Sun', 
                            hue='Planet', 
                            color='Planet',
                            size='Diameter_skewed', 
                            sizes=(100, 5000),
                            alpha=0.8)

# Annotate the points with planet names
for i in range(len(df)):
    plt.text(df.Distance_from_Sun[i] + df.xOffset[i], 
             df.Distance_from_Sun[i] - df.yOffset[i], 
             df.Planet[i] + ',\n' +
             'dist: ' + df.Distance_from_Sun[i].astype(str) + 'M km,\n' +
             'diam: ' + df.Diameter[i].astype(str) + ' km')

# Log axis
plt.xscale('log')
plt.yscale('log')

# hide legend and axis labels
plt.legend().remove()
plt.xlabel('')  
#plt.ylabel('')  
plt.xticks(ticks=[], labels=[])
#plt.yticks(ticks=[], labels=[])

# set axis limits
plt.xlim(40, 20000)
plt.ylim(40, 10000)
plt.tight_layout()

# Add title
plt.title('Planet Data: Distance from Sun vs Diameter (as size)')

# Show the plot
plt.savefig('scatterplot.png')
