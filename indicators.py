import numpy as np


def calc_rsi(df, length=8):
    # Calculate the difference between the current close price and the previous close price
    diff = df['Close'].diff()

    # Create a new dataframe to store the positive and negative differences
    df_diff = pd.DataFrame(index=df.index)
    df_diff['pos'] = np.where(diff > 0, diff, 0)
    df_diff['neg'] = np.where(diff < 0, abs(diff), 0)

    # Calculate the exponential moving average of the positive and negative differences
    df_diff['pos_ema'] = df_diff['pos'].ewm(com=length - 1, min_periods=length).mean()
    df_diff['neg_ema'] = df_diff['neg'].ewm(com=length - 1, min_periods=length).mean()

    # Calculate the relative strength index
    df_diff['rsi'] = 100 - (100 / (1 + df_diff['pos_ema'] / df_diff['neg_ema']))

    # Return the relative strength index
    return df_diff['rsi']

# # Add the relative strength index as a new column to the dataframe
# df['RSI'] = calc_rsi(df)
