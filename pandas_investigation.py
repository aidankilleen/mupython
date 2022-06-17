import pandas as pd
import matplotlib.pyplot as plt;



data_frame = pd.DataFrame({'x_values':[1,2,3,4,5], 'y_values':[10,5,9,2,6]})
data_frame.plot(x='x_values', y='y_values')




