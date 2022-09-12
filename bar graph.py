import numpy as np
import matplotlib.pyplot as plt

# here i am giving similar name as like my thesis paper. STPMSVM and angle STPMSVM

dataset = ['Sonar', 'Haberman', 'Liver Disorder', 'House Votes', 'CMC']
STPMSVM = [78.3333, 74.5161, 65.2101, 94.2706, 67.3543]
Angel_STPMSVM = [78.8095, 75.1505, 65.5294, 94.5032, 67.4223]

# height = 0.25
# width = 0.25

X_axis = np.arange(len(dataset))

plt.bar(X_axis - 0.1, STPMSVM, 0.2, label='STPMSVM')
plt.bar(X_axis + 0.1, Angel_STPMSVM, 0.2, label='Angle STPMSVM')

plt.xticks(X_axis, dataset)
plt.xlabel("Datasets")
plt.ylabel("Test Accuracy")
plt.title("comparison of ......")
plt.legend()
plt.show()