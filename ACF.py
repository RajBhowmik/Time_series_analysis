from data_preprocess import data_group
from statsmodels.graphics.tsaplots import plot_acf
import matplotlib.pyplot as plt
plt.rcParams["figure.figsize"] = (20,7)

acf_plot = plot_acf(data_group['weekly_sales'].values, lags =70)
plt.xlabel('lag')
plt.ylabel('correlation')
plt.show()

