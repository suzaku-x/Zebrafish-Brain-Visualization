import csv
import matplotlib.pyplot as plt
import tifffile
import os
import numpy as np
import pandas as pd
plt.rcParams["figure.figsize"] = ((11, 8.5))

list_strike = [[52, 'Hunting initiation', 'nucleus isthmi'],
               [114, 'Strike', 'nucleus isthmi'],

               [85, 'Hunting initiation', 'dorsal thalamus proper'],
               [141, 'Strike', 'dorsal thalamus proper'],

               [50, 'Hunting initiation', 'dorsal telencephalon(pallium)'],
               [91, 'Strike', 'dorsal telencephalon(pallium)'],

               [41, 'Hunting initiation', 'cerebellum'],
               [75, 'Strike', 'cerebellum'],

               [114, 'Hunting initiation', 'pretectum'],
               [98, 'Strike', 'pretectum'],

               [83, 'Hunting initiation', 'superior medulla oblongata'],
               [174, 'Strike', 'superior medulla oblongata'],

               [52, 'Hunting initiation', 'periventricular layer'],
               [59, 'Strike', 'periventricular layer'],

               [22, 'Hunting initiation', 'lateral tegmentum'],
               [48, 'Strike', 'lateral tegmentum'],

               [24, 'Hunting initiation', 'tectal neuropil'],
               [27, 'Strike', 'tectal neuropil'],
               ]

# print(list_strike)

plt.rcParams["figure.figsize"] = ((14, 10))
# data = np.random.normal(size=(N,))
df = pd.DataFrame(list_strike, columns=['Rate', 'Type', 'Distance'])
# print(df)

import seaborn as sns

# Load some example data
# tips = sns.load_dataset("tips")
#

# print(tips)
# sns.set(font_scale=2)

hue_order = ['Hunting initiation', 'Strike']
# box_pairs=[
#     (("Stationary", "Hunting initiation"), ("Sweep+Stationary", "Hunting initiation")),
#     (("Stationary", "Hunting initiation"), ("Sweep+Flickering", "Hunting initiation")),
#     (("Stationary", "Strike"), ("Sweep+Stationary", "Strike")),
#     (("Stationary", "Strike"), ("Flickering", "Strike")),
#     (("Stationary", "Strike"), ("Sweep+Flickering", "Strike")),

#     ]

ax = sns.barplot(
    data=df,
    x="Distance",
    y="Rate",
    hue="Type",
    alpha=1,
    ci=85,
    palette=['#1f77b4', 'Magenta'],
    estimator=np.mean
)

# add_stat_annotation(ax, data=df, x="Distance", y="Rate",hue='Type', box_pairs=box_pairs,

#                            perform_stat_test=False,
#                         pvalues=[0.0094405200780494,0.005875685374135839,0.004618367743403307,
#                                  0.005579712641457377, 0.005331137357257343],

#                            text_format='star',

#                           loc='inside', verbose=2,
#                           line_offset=0.010, line_height=0.00, text_offset=-10,
#                         color='0.4', linewidth=1.5,
#                         fontsize=28)
ax.yaxis.grid(True)
# Get the legend from just the bar chart

handles, labels = ax.get_legend_handles_labels()

sns.stripplot(
    data=df,
    x="Distance",
    y="Rate",
    hue="Type",
    dodge=True,
    edgecolor="black",
    alpha=1,
    #     linewidth=.01,
    palette=['black', 'black'],
    size=0,
    ax=ax,
)

# Remove the old legend
ax.legend_.remove()
# Add just the bar chart legend back
ax.legend(
    handles,
    labels,
    loc=7,
    fontsize=29,
    bbox_to_anchor=(1.0, 0.90))

# ax.set_ylim(0, 125)
# ax.set_yticklabels([0, 20, 40, 60, 80, 100], fontsize=33)
ax.set_ylabel('# of neurons', fontsize=33)
plt.yticks(fontsize=33)
ax.set_xlabel('', fontsize=33)
# ax.set_xticklabels(rotation=45)
# ax.set_xlim(-0.5,3.20-0.5)
plt.xticks(fontsize=33, rotation=90)
plt.rcParams["font.family"] = "Arial"


plt.savefig('combine.png', bbox_inches='tight')
