import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("countries of the world.csv")
#pd.read_csv("countries of the world.csv").replace(to_replace=",",".")
def clean_1(data):
    if data != "" and isinstance(data,str):
        result = data.replace(",",".")
        return float(result)
    else:
        return data

df["Pop. Density (per sq. mi.)"]=df["Pop. Density (per sq. mi.)"].apply(clean_1)
df["Coastline (coast/area ratio)"]=df["Coastline (coast/area ratio)"].apply(clean_1)
df["Net migration"] = df["Net migration"].apply(clean_1)
df["Infant mortality (per 1000 births)"] = df["Infant mortality (per 1000 births)"].apply(clean_1)
df["Literacy (%)"] = df["Literacy (%)"].apply(clean_1)
df["Phones (per 1000)"] = df["Phones (per 1000)"].apply(clean_1)
df["Arable (%)"] = df["Arable (%)"].apply(clean_1)
df["Crops (%)"] = df["Crops (%)"].apply(clean_1)
df["Other (%)"] = df["Other (%)"].apply(clean_1)
df["Climate"] = df["Climate"].apply(clean_1)
df["Birthrate"] = df["Birthrate"].apply(clean_1)
df["Deathrate"] = df["Deathrate"].apply(clean_1)
df["Agriculture"] = df["Agriculture"].apply(clean_1)
df["Industry"] = df["Industry"].apply(clean_1)
df["Service"] = df["Service"].apply(clean_1)



df.info()

#df['GDP ($ per capita)'].value_counts().plot(kind = 'scatter', figsize = (8,5), grid = True)
df.plot(y = "Phones (per 1000)",
        x = 'Literacy (%)',
        kind='scatter')
plt.show()

df.to_csv("clean.csv",index=False)