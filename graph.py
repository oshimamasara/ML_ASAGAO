from matplotlib import pyplot as plt
from matplotlib import style
import numpy as np

style.use('ggplot')

x,y = np.loadtxt('data.csv', unpack= True, delimiter=',')

plt.plot(x, y, 'go')

plt.title('How long Growth( ASAGAO ) ?')
plt.ylabel('Length (cm)')
plt.xlabel('Passed Days')

plt.show()