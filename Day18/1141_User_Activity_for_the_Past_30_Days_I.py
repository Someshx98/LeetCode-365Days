import pandas as pd

data = [[1, 1, '2019-07-20', 'open_session'], [1, 1, '2019-07-20', 'scroll_down'], [1, 1, '2019-07-20', 'end_session'], [2, 4, '2019-07-20', 'open_session'], [2, 4, '2019-07-21', 'send_message'], [2, 4, '2019-07-21', 'end_session'], [3, 2, '2019-07-21', 'open_session'], [3, 2, '2019-07-21', 'send_message'], [3, 2, '2019-07-21', 'end_session'], [4, 3, '2019-06-25', 'open_session'], [4, 3, '2019-06-25', 'end_session']]
work = pd.DataFrame(data, columns=['user_id', 'session_id', 'activity_date', 'activity_type']).astype({'user_id':'Int64', 'session_id':'Int64', 'activity_date':'datetime64[ns]', 'activity_type':'object'})

print(work)

import pandas as pd

def user_activity(activity: pd.DataFrame) -> pd.DataFrame:
    activity = activity.copy()
    activity["activity_date"] = pd.to_datetime(activity["activity_date"])

    end_date = pd.to_datetime("2019-07-27")
    start_date = end_date - pd.Timedelta(days=29)

    mask = activity["activity_date"].between(start_date, end_date)
    filtered = activity.loc[mask]

    result = (
        filtered.groupby("activity_date")["user_id"]
        .nunique()
        .reset_index()
        .rename(columns={"activity_date": "day", "user_id": "active_users"})
    )
    return result


print(user_activity(work))