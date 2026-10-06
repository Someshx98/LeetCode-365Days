import pandas as pd

data = [[121, 'US', 'approved', 1000, '2018-12-18'], [122, 'US', 'declined', 2000, '2018-12-19'], [123, 'US', 'approved', 2000, '2019-01-01'], [124, 'DE', 'approved', 2000, '2019-01-07']]
income = pd.DataFrame(data, columns=['id', 'country', 'state', 'amount', 'trans_date']).astype({'id':'Int64', 'country':'object', 'state':'object', 'amount':'Int64', 'trans_date':'datetime64[ns]'})

print(income)

def monthly_transactions(transactions: pd.DataFrame) -> pd.DataFrame:
    transactions = transactions.copy()
    transactions["trans_date"] = pd.to_datetime(transactions["trans_date"])
    transactions["month"] = transactions["trans_date"].dt.strftime("%Y-%m")
    transactions["is_approved"] = transactions["state"] == "approved"
    transactions["approved_amount"] = transactions["amount"].where(transactions["is_approved"])

    result = transactions.groupby(["month", "country"], dropna=False).agg(
        trans_count=("id", "count"),
        approved_count=("is_approved", "sum"),
        trans_total_amount=("amount", "sum"),
        approved_total_amount=("approved_amount", "sum")
    ).reset_index()

    return result


print(monthly_transactions(income))