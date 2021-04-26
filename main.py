import pandas as pd

# DataFrame


pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}, index=['1', '2'])
# print(x)

pd.DataFrame({'Adam': ['Lubie pilke nozna', 'nie lubie golfa'],
                  'Kordian': ['Nie lubie pilki noznej', 'lubie jezidz konno '], },
                 index=['Opcja 1 ', 'Opcja 2 '])
# print(y)

# SERIES

pd.Series([1, 2, 3, 4, 5])

#print(k)

x = pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
#print(x)

wine_reviews = pd.read_csv("housing.csv")

print(wine_reviews.head())

print(wine_reviews.shape)

