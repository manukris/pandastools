import pandas as pd
import numpy as np

funding = pd.read_csv("startup_funding.csv")
print(funding.shape)

funding.Amount = funding.Amount.astype(int)

print(funding.dtypes)