import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA

df = pd.read_excel(r"D:\HSLU_Projects\course_setting\Data\bereinigte_DATEN_ano.xls")

df.head(10)
df_2 = df._get_numeric_data()
print(df_2.columns)
y = df.loc[:,['athlete']].values
x = df_2.drop(['athlete', 'gender', 'Unnamed: 0', 'run'], axis = 1)
features = x.columns
x = x.values
x = StandardScaler().fit_transform(x)
pca = PCA(n_components= len(features))
principlecomponents = pca.fit_transform(x)

principalDF = pd.DataFrame(data = principlecomponents, columns= features)

final_df = pd.concat([df[['athlete']], principalDF], axis = 1)




