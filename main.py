import numpy as np
from scipy.interpolate import interp1d
import matplotlib.pyplot as plt

x = np.linspace(1, 30, 15)
y = np.sin(x)

f1 = interp1d(x, y, kind = 'linear')
f2 = interp1d(x, y, kind = 'quadratic')
f3 = interp1d(x, y, kind = 'nearest')

x_new = np.linspace(1, 30, 200)
y_new = np.sin(x_new)

fig, axs = plt.subplots(figsize = (18, 7), nrows = 1, ncols = 1)

axs.plot(x_new, y_new)
axs.plot(x_new, f1(x_new), '-')
axs.plot(x_new, f2(x_new), '--')
axs.plot(x_new, f3(x_new), '*')
axs.plot(x, y, 'o', markersize = 8, color = 'black')


axs.legend(['Исходная функция', 'Линейная', 'Квадратичная', 'Ближайший сосед', 'Узлы интерполяции'],
            loc = 3)
axs.set_title(r"Интерполирование функции $\sin{(x)}$ на интервале $(1, 30)$", fontsize = 20)
plt.show()
