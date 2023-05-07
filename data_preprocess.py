import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

data = pd.read_csv(r"D:\Data_Science\datasets\Kaggle Competitions\competitive-data-science-predict-future-sales\sales_train.csv")

data = data[['date','item_cnt_day']]
data['date'] = pd.to_datetime(data['date'])
data = data.set_index('date')
print(data)

## showing the weekly sales
data_group = data.groupby(pd.Grouper(freq='W')).sum()
data_group = data_group.rename(columns={'item_cnt_day':'weekly_sales'})
data_group.plot()
plt.grid()
plt.show()

