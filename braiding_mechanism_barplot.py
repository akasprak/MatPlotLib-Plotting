import numpy as np
import matplotlib.pyplot as plt


# Number of mechanisms and their volumetric contributions
N = 10
field_dep = (1826, 28, 14050, 911, 9142, 8557, 117, 14379, 1076, 163)
field_erode = (-11319, -306, -409, -2171, -311, -380, -2272, -1127, -1010, -2)

model_dep = (25, 32, 34, 20, 25, 30, 42, 15, 18, 27)
model_erode = (0, -10, 0, -5, 0, 0, 0, -20, 0, 0)

ind = np.arange(N)  # the x locations for the groups
width = 0.45       # the width of the bars

# plot the field and then the model values 
fig, ax = plt.subplots()
rects1 = ax.barh(ind, field_dep, width, color='b', label = 'Field-Surveyed', hatch = "//")
rects2 = ax.barh(ind, field_erode, width, color='r', label = 'Field-Surveyed', hatch = "//")

rects3 = ax.barh(ind+width, model_dep, width, color='b', label = 'Modeled')
rects4 = ax.barh(ind+width, model_erode, width, color='r', label = 'Modeled')

# add some text for labels, title and axes ticks
ax.set_yticks(ind + width)
ax.set_yticklabels( ('Lobe Dissection', 'Confluence\n Pool Scour', 'Bank Erosion', 'Chute Cutoff', 'Channel Incision', 'Central Bar\n Development', 'Bar Edge\n Trimming', 'Transverse Bar\n Conversion', 'Lateral Bar\n Development', 'Overbank Sheets', 'Questionable or\n Unresolved') )

#set up the axis labels
ax.set_ylabel('Braiding Mechanism')
ax.set_xlabel('Volumetric Change ($m^3$)')
ax.set_title('Rees Braiding Mechanisms, E01 - E02')

#plot a line at zero
plt.axvline(color='black')

#insert the legend
leg = plt.legend([rects1, rects3],["Field", "Model"], loc = "best")



plt.show()
