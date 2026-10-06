from typing import Any
import pandas as pd

data = [[1, '2015-01-01', 10], [2, '2015-01-02', 25], [3, '2015-01-03', 20], [4, '2015-01-04', 30]]
weather = pd.DataFrame(data, columns=['id', 'recordDate', 'temperature']).astype(
    {'id': 'Int64', 'recordDate': 'datetime64[ns]', 'temperature': 'Int64'})


def rising_temperature(Weather: pd.DataFrame) -> pd.DataFrame:
    Weather["recordDate"] = pd.to_datetime(Weather["recordDate"])
    Weather = Weather.sort_values(by = "recordDate")

    next_day = (Weather["recordDate"] - Weather["recordDate"].shift(1)) == pd.Timedelta(days=1)

    is_warmer = Weather["temperature"] > Weather["temperature"].shift(1)

    result = Weather[next_day & is_warmer][["id"]]
    result.reset_index(drop=True, inplace=True)

    return result


print(rising_temperature(weather))
