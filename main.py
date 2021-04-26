import pandas as pd

# DataFrame


x = pd.DataFrame({'Yes': [50, 21], 'No': [131, 2]}, index=['1', '2'])
# print(x)

y = pd.DataFrame({'Adam': ['Lubie pilke nozna', 'nie lubie golfa'],
                  'Kordian': ['Nie lubie pilki noznej', 'lubie jezidz konno '], },
                 index=['Opcja 1 ', 'Opcja 2 '])
# print(y)

# SERIES

k = pd.Series([1, 2, 3, 4, 5])
print(k)

pd.Series([30, 35, 40], index=['2015 Sales', '2016 Sales', '2017 Sales'], name='Product A')
