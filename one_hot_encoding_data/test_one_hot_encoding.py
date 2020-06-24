import pandas as pd
from one_hot_encoding_data.one_hot_encoding import clean_data

values = ["banana", "orage", "banana", "apple", "pears", "pears"]
column_name = "test_values"

df = pd.DataFrame(values, columns=[column_name])

one_hot = clean_data(df)
one_hot.one_hot_encoding_column(column_name, True)

print(one_hot.data)
print("Qtd columns = qtd values: " + str(len(one_hot.data.columns) == len(set(values))))

for i in range(len(values)):
    value = values[i]
    print("Set correct value: " + str(one_hot.data.at[i, value] == 1))
