
import matplotlib.pyplot as plt
import numpy as np


np.random.seed(565)

idk = 100
idk0 = np.random.rand(idk)
idk1 = np.random.rand(idk)

color0 = '#ff00ea'

color = np.random.rand(idk)
area = (30 * np.random.rand(idk))**2
plt.scatter(idk0, idk1, s= area, c= color, alpha= 0.5, label= 'Random Polka-Dot')
plt.show()

np.random.seed(567)

idk = 200
idk0 = np.random.rand(idk)
idk1 = np.random.rand(idk)

color0 = '#ff00ea'

color = np.random.rand(idk)
area = (30 * np.random.rand(idk))**2
plt.scatter(idk0, idk1, s= area, c= color, alpha= 0.5)
plt.show()

np.random.seed(565)

idk = 100
idk0 = np.random.rand(idk)
idk1 = np.random.rand(idk)

color1 = '#00ff8c'

color = np.random.rand(idk)
area = (30 * np.random.rand(idk))**2
plt.scatter(idk0, idk1, s= area, c= color1, alpha= 0.5, label= 'Turquoise Polka-Dot')
plt.legend(loc= 'best')
plt.show()

np.random.seed(567)

idk = 200
idk0 = np.random.rand(idk)
idk1 = np.random.rand(idk)

color0 = '#ff00ea'

color = np.random.rand(idk)
area = (30 * np.random.rand(idk))**2
plt.scatter(idk0, idk1, s= area, c= color0, alpha= 0.5)
plt.show()

np.random.seed(567)

idk = 200
idk0 = np.random.rand(idk)
idk1 = np.random.rand(idk)

color0 = '#ff00ea'

color = np.random.rand(idk)
area = (30 * np.random.rand(idk))**2
plt.scatter(idk0, idk1, s= area, c= 'darkorchid', alpha= 0.5)
plt.show()

np.random.seed(567)

idk = 200
idk0 = np.random.rand(idk)
idk1 = np.random.rand(idk)

color0 = '#ff00ea'

color = np.random.rand(idk)
area = (30 * np.random.rand(idk))**2
plt.scatter(idk0, idk1, s= area, c= 'deeppink', alpha= 0.5)
plt.show()

np.random.seed(567)

idk = 200
idk0 = np.random.rand(idk)
idk1 = np.random.rand(idk)

color0 = '#ff00ea'

color = np.random.rand(idk)
area = (30 * np.random.rand(idk))**2
plt.scatter(idk0, idk1, s= area, c= 'color0', alpha= 0.5)
plt.show()
