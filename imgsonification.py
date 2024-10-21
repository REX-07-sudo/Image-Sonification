from matplotlib import pyplot as plt
import numpy as np
data = np.load('/Users/devanshnegi/Desktop/AIML/images.npy')
plt.imshow(data[234])
plt.axis('off')  
plt.show()