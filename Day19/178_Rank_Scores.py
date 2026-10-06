import pandas as pd

data = [[1, 3.5], [2, 3.65], [3, 4.0], [4, 3.85], [5, 4.0], [6, 3.65]]
mark = pd.DataFrame(data, columns=['id', 'score']).astype({'id':'Int64', 'score':'Float64'})
print(mark)

def order_scores(scores: pd.DataFrame) -> pd.DataFrame:
    scores = scores.sort_values(by=['score'], ascending=False).reset_index(drop=True)
    scores['rank'] = scores['score'].rank(method='dense', ascending=False).astype(int)

    return scores[['score', 'rank']]

print(order_scores(mark))