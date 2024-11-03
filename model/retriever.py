import requests
import pandas as pd

BASE_URL = "https://fapi.binance.com"
FAPI_URL = "fapi/v1/klines"
REALTIME_DATA_COLUMNS = [
    "Kline open time",
    "Open price",
    "High price",
    "Low price",
    "Close price",
    "Volume",
    "Kline Close time",
    "Quote asset volume",
    "Number of trades",
    "Taker buy base asset volume",
    "Taker buy quote asset volume",
    "unused",
]


def get_real_time_data(symbol: str, interval: str):
    endpoint_url = f"{BASE_URL}/{FAPI_URL}?SYMBOL={symbol}&INTERVAL={interval}"
    resp = requests.get(endpoint_url)
    if resp.status_code != 200:
        raise ConnectionError(f"Unable to retrieve data from endpoint: {endpoint_url}")

    return resp.json()


def convert_real_time_data_to_df(data: list):
    return pd.DataFrame(data, columns=REALTIME_DATA_COLUMNS)


if __name__ == "__main__":
    data = get_real_time_data(symbol="BTCUSDT", interval="1m")
    df = convert_real_time_data_to_df(data=data)
    print(df)
