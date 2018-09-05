import pandas as pd
train_df = pd.read_csv('Titanic/train.csv')
test_df = pd.read_csv('Titanic/test.csv')
combine = [train_df, test_df]
combine_df = pd.concat(combine, sort=False)
print('Features:', ', '.join(combine_df.columns))
print(combine_df.head())
combine_df.info()