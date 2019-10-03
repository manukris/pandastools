import pandas as pd
import numpy as np

missingValues = ['Undisclosed','N/A','undisclosed']
funding = pd.read_csv("startup_funding.csv",na_values=missingValues)
print(funding.shape)


for i in range(3009):
    amount = str(funding.Amount[i]).replace(",","")
    funding.Amount[i] = amount
# print(funding.Amount)
funding['Amount'] = pd.to_numeric(funding['Amount'],errors='coerce')
print(funding['Amount'].min())
