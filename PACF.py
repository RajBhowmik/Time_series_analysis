from statsmodels.graphics.tsaplots import plot_pacf
import matplotlib.pyplot as plt

from data_preprocess import data_group

pacf_plot = plot_pacf(data_group['weekly_sales'].values, lags=70)

plt.xlabel('lag')
plt.ylabel('pacf_coeff')
plt.show()
