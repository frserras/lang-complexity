from math import trunc
import pandas as pd
d90_file = './results/complexity_utf-16_1010_10_10_bibles_90_lcm.csv'
dall_file = './results/complexity_utf-16_2020_10_10_bibles_lcm.csv'

df90 = pd.read_csv(d90_file, index_col=False)
df90 = df90[df90.language != 'NAMBIKUÁRA'] # We removed Nambikuára because it has tone annotation
df90.loc[df90.metric == 'del-chars', 'value'] = - df90.loc[df90.metric == 'del-chars', 'value']
df90 = df90[df90.metric != 'do-nothing']
df90 = df90[df90.algorithm != 'none']

dfall = pd.read_csv(dall_file, index_col=False)
dfall = dfall[dfall.language != 'NAMBIKUÁRA'] # We removed Nambikuára because it has tone annotation
dfall.loc[dfall.metric == 'del-chars', 'value'] = - dfall.loc[dfall.metric == 'del-chars', 'value']
dfall = dfall[dfall.metric != 'do-nothing']
dfall = dfall[dfall.algorithm != 'none']

family = pd.read_csv('./dataset/family.csv', index_col=None)

dfall = dfall.drop(columns=['language']).merge(family.drop(columns=['countries', 'branch']), on='wals', how='inner').rename(columns={ 'wals' : 'code'})
df90 = df90.drop(columns=['language']).merge(family.drop(columns=['countries', 'branch']), on='wals', how='inner').rename(columns={ 'wals' : 'code'})

# print(df90.columns)
# import sys
# sys.exit(1)

metric_rename = {'del-chars'  : r'$\mu_{\times}^{\mathbb{M}}(\mathscr{T})$',
                 'del-verses' : r'$\mu_{\times}^{\mathbb{P}}(\mathscr{T})$',
                 'del-words'  : r'$\mu_{\times}^{\mathbb{S}}(\mathscr{T})$',
                 'rep-words'  : r'$\mu_{\circ}^{\mathbb{M}}(\mathscr{T})$',
                 'do-nothing' : 'size'
                }

dfall = dfall.replace(metric_rename)
df90 = df90.replace(metric_rename)



rall = dfall.groupby(by=['family', 'code', 'metric', 'algorithm']).agg({'value' : ['mean', 'var']})
r90 = df90.groupby(by=['language', 'code', 'metric', 'algorithm']).agg({'value' : ['mean', 'var']})


#round = {'mean' : 3, 'var' : 7}
decimals = int(1e8)
rall.map(lambda x: trunc(x * decimals)/decimals).to_csv('./results/dall.csv')
r90.map(lambda x: trunc(x * decimals)/decimals).to_csv('./results/d90.csv')
#rall.round(round).to_csv('./results/dall.csv')
#r90.round(round).to_csv('./results/d90.csv')