import pandas as pd

data = [[1, '2017-01-01', 10], [2, '2017-01-02', 109], [3, '2017-01-03', 150], [4, '2017-01-04', 99], [5, '2017-01-05', 145], [6, '2017-01-06', 1455], [7, '2017-01-07', 199], [8, '2017-01-09', 188]]
hall = pd.DataFrame(data, columns=['id', 'visit_date', 'people']).astype({'id':'Int64', 'visit_date':'datetime64[ns]', 'people':'Int64'})

def human_traffic(stadium: pd.DataFrame) -> pd.DataFrame:
    stadium["visit_date"] = pd.to_datetime(stadium["visit_date"])
    stadium.sort_values(by="id", inplace=True)

    result = stadium[stadium["people"] >= 100].copy()


    result["rank"] = result["id"].rank(method="dense")
    result["diff"] = result["id"] - result["rank"]

    result = result[result.groupby("diff")["id"].transform("count") >= 3]

    return result[["id", "visit_date", "people"]].sort_values("visit_date")


print(human_traffic(hall))