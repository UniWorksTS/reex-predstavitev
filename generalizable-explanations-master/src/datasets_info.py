
import pandas as pd


df = pd.read_csv('../data/bbc/test.tsv', sep='\t')
print(df['label'].value_counts())
print(len(df['label']))

df = pd.read_csv('../data/authors/test.tsv', sep='\t')
print(df['label'].value_counts().sort_index())
print(len(df['label']))
print("mean")
print(df['text_a'].apply(len).mean())


df = pd.read_csv('../data/questions/dev.tsv', sep='\t')
print(df['label'].value_counts())
print(len(df['label']))