# import_investigation.py
# By: Aidan
# Date: 16/6/2022

# import analyse_data

import analyse_data as ad   # assign alias to module 

# import numpy as np
# import pandas as pd

#(sum, average) = analyse_data.analyse_data([1,2,3,4])
(sum, average) = ad.analyse_data([1,2,3,4])

print (f"sum={sum} Average={average}")

# analyse_data.greet("Aidan")
ad.greet("Aidan")
print (ad.title)
print(ad.days)

from random import ra
