import pandas as pd

if __name__ =='__main__':
    sentence = "Hello welcometo Cathay 60th year anniversary"
    new_sentence = sentence.replace(" ","").upper()
    sorted_sentence = "".join(sorted(new_sentence))
    print(pd.Series(list(sorted_sentence)).value_counts().sort_index())