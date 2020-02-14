import pandas as pd

def make_pd(lists, index, column_name):
    df = pd.DataFrame(data = lists, 
                      index = index, 
                      columns = [column_name])
    return df

df1 = make_pd([1,2,3], [1,2,3], 'hi')
df2 = make_pd([1,2,3], [4,5,6], 'hello')
print(df1)
print(df2)

result_df = df1.merge(
    df2, 
    how = 'outer', 
    left_index = True, 
    right_index = True
)
print(result_df)