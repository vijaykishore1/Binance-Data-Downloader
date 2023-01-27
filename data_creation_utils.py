from creating_arrays import CHART_TIME_ARRAY, MONTH_ARRAY, SYMBOL_ARRAY
from constants import download_dir, output_dir, root_dir, dtypes, BINANCE_DAILY_URL, BINANCE_MONTHLY_URL
from pathlib import Path
import os
import re
import shutil
import talib
import datetime
import glob
import zipfile
import pandas as pd
from pandas.api.types import is_numeric_dtype
import inspect
import talib
import time
import numpy as np
import requests
import urllib.request


def download_data(master_dictionary, monthly_or_daily_1_2):
    if monthly_or_daily_1_2 in ["m", "M", "monthly", 1]:
        for symbol in master_dictionary["symbols"]:
            for chart_time in master_dictionary["chart_times"]:
                for month in master_dictionary["months"]:
                    # Construct the link
                    link = f"{BINANCE_MONTHLY_URL}{symbol}/{chart_time}/{symbol}-{chart_time}-{month}.zip"
                    # Create the file path
                    file_path = Path(download_dir) / f"{symbol}-{chart_time}-{month}.zip"
                    try:
                        # Download the file
                        urllib.request.urlretrieve(link, f"{symbol}-{chart_time}-{month}.zip")
                    #                 print(f'{file_path} downloaded successfully')
                    except:
                        print(f'{file_path} not found')
                        continue
        for symbol in master_dictionary["symbols"]:
            for chart_time in master_dictionary["chart_times"]:
                # Create the new folder path
                new_folder_path = Path(download_dir) / f"{symbol}-{chart_time}-monthly_data"
                new_folder_path.mkdir(parents=True, exist_ok=True)
                # match pattern of the file
                pattern = re.compile(f"^{symbol}-{chart_time}-\d{{4}}-\d{{2}}\.zip$")
                # list all files in the download directory
                files = os.listdir(root_dir)
                for file in files:
                    if pattern.match(file):
                        src = Path(root_dir) / file
                        dst = new_folder_path / file
                        src.rename(dst)
    if monthly_or_daily_1_2 in ["d", "D", "daily", 2]:
        for symbol in master_dictionary["symbols"]:
            for chart_time in master_dictionary["chart_times"]:
                for day in master_dictionary["days"]:
                    # Construct the link
                    link = f"{BINANCE_DAILY_URL}{symbol}/{chart_time}/{symbol}-{chart_time}-{day}.zip"
                    # Create the file path
                    file_path = Path(download_dir) / f"{symbol}-{chart_time}-{day}.zip"
                    try:
                        # Download the file
                        urllib.request.urlretrieve(link, f"{symbol}-{chart_time}-{day}.zip")
                        # print(f'{file_path} downloaded successfully')
                    except:
                        print(f'{file_path} not found')
                        continue
        for symbol in master_dictionary["symbols"]:
            for chart_time in master_dictionary["chart_times"]:
                # Create the new folder path
                new_folder_path = Path(download_dir) / f"{symbol}-{chart_time}-daily_data"
                new_folder_path.mkdir(parents=True, exist_ok=True)
                # match pattern of the file
                pattern = re.compile(f"^{symbol}-{chart_time}-\d{{4}}-\d{{2}}-\d{{2}}\.zip$")
                # list all files in the download directory
                files = os.listdir(root_dir)
                for file in files:
                    if pattern.match(file):
                        src = Path(root_dir) / file
                        dst = new_folder_path / file
                        if dst.exists():
                            dst.unlink()
                        src.rename(dst)
    return ("data downloaded")


def unzip_and_concatenate_csv(master_dictionary, monthly_or_daily_1_2):
    if monthly_or_daily_1_2 in ["m", "M", "monthly", 1]:
        for symbol in master_dictionary["symbols"]:
            for chart_time in master_dictionary["chart_times"]:
                # Set up an empty list for the data frames
                df_list = []

                # Compile the regular expression pattern
                pattern = re.compile(f"^{symbol}-{chart_time}-\d{{4}}-\d{{2}}\.zip$")

                # Create the new folder path for ZIP files
                new_zip_folder_path = os.path.join(download_dir,
                                                   f"{symbol}-{chart_time}-monthly_data")

                # Create the new folder path for CSV files
                new_csv_folder_path = os.path.join(output_dir,
                                                   f"{symbol}-{chart_time}-monthly_data")

                # Iterate over the files in the new zip folder
                for file in os.listdir(new_zip_folder_path):
                    # Check if the file matches the pattern
                    if pattern.match(file):
                        # Construct the file path
                        file_path = os.path.join(new_zip_folder_path, file)

                        # Extract the ZIP file
                        with zipfile.ZipFile(file_path, "r") as zip_ref:
                            zip_ref.extractall(new_csv_folder_path)

                        # Construct the CSV file path
                        csv_file_path = os.path.join(
                            new_csv_folder_path,
                            f"{symbol}-{chart_time}{file[-12:-4]}.csv")

                        # Read the CSV file into a data frame, ignoring the headers
                        df = pd.read_csv(csv_file_path, header=None)

                        # Remove the first row (which contains the header)
                        df = df.iloc[1:]

                        # Add it to the list
                        df_list.append(df)

                # Concatenate the data frames in the list
                df_final = pd.concat(df_list, ignore_index=True)

                # Read the headers from the first CSV file
                headers = pd.read_csv(csv_file_path, nrows=1).columns

                # Set the headers as the column names of the final dataframe
                df_final.columns = headers

                # Convert 'open_time' and 'close_time' columns to datetime
                df_final['open_time'] = pd.to_datetime(
                    df_final['open_time'],
                    unit='ms').dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata')
                df_final['close_time'] = pd.to_datetime(
                    df_final['close_time'],
                    unit='ms').dt.tz_localize('UTC').dt.tz_convert('Asia/Kolkata')

                # Delete the 'ignore' column
                df_final = df_final.drop(['ignore'], axis=1)

                # Add a new column called 'entry' that will take previous close
                df_final['entry'] = df_final['close'].shift(1)
                # Set the file name
                file_name = f"{symbol}-{chart_time}.csv"

                # Construct the file path
                file_path = os.path.join(new_csv_folder_path, file_name)

                # Write the data frame to the Excel file
                df_final.to_csv(file_path, index=False)
    if monthly_or_daily_1_2 in ["d", "D", "daily", 2]:
        for symbol in master_dictionary["symbols"]:
            for chart_time in master_dictionary["chart_times"]:
                # Set up an empty list for the data frames
                df_list = []

                # Compile the regular expression pattern for daily zip files
                pattern = re.compile(f"^{symbol}-{chart_time}-\d{{4}}-\d{{2}}-\d{{2}}\.zip$")

                # Create the new folder path for daily ZIP files
                new_daily_zip_folder_path = os.path.join(download_dir, f"{symbol}-{chart_time}-daily_data")

                if not os.path.exists(new_daily_zip_folder_path):
                    os.mkdir(new_daily_zip_folder_path)

                # Create the new folder path for daily CSV files
                new_daily_csv_folder_path = os.path.join(output_dir, f"{symbol}-{chart_time}-daily_data")

                if not os.path.exists(new_daily_csv_folder_path):
                    os.mkdir(new_daily_csv_folder_path)

                # Iterate over the files in the new daily zip folder
                for file in os.listdir(new_daily_zip_folder_path):
                    # Check if the file matches the pattern
                    if pattern.match(file):
                        # Construct the file path
                        file_path = os.path.join(new_daily_zip_folder_path, file)

                        # Extract the ZIP file
                        with zipfile.ZipFile(file_path, "r") as zip_ref:

                            # Construct the CSV file path
                            csv_file_path = os.path.join(new_daily_csv_folder_path,
                                                         f"{symbol}-{chart_time}-{file.split('-')[-3]}-{file.split('-')[-2]}-{file.split('-')[-1][:-4]}.csv")

                            # Check if the extracted csv already exists, and if so, delete it
                            if os.path.exists(csv_file_path):
                                os.remove(csv_file_path)

                            zip_ref.extractall(new_daily_csv_folder_path)

                        # Read the CSV file into a data frame, ignoring the headers
                        df = pd.read_csv(csv_file_path, header=None)

                        # Remove the first row (which contains the header)
                        df = df.iloc[1:]

                        # Add it to the list
                        df_list.append(df)

                # Concatenate the data frames in the list
                df_final = pd.concat(df_list, ignore_index=True)

                # Read the headers from the first CSV file
                headers = pd.read_csv(csv_file_path, nrows=1).columns

                # Set the headers as the column names of the final dataframe
                df_final.columns = headers

                # Convert 'open_time' and 'close_time' columns to datetime
                df_final['open_time'] = pd.to_datetime(df_final['open_time'], unit='ms').dt.tz_localize(
                    'UTC').dt.tz_convert('Asia/Kolkata')
                df_final['close_time'] = pd.to_datetime(df_final['close_time'], unit='ms').dt.tz_localize(
                    'UTC').dt.tz_convert('Asia/Kolkata')

                # Delete the 'ignore' column
                df_final = df_final.drop(['ignore'], axis=1)

                # Add a new column called 'entry' that will take previous close
                df_final['entry'] = df_final['close'].shift(1)

                # Set the file name
                file_name = f"{symbol}-{chart_time}.csv"

                # Construct the file path
                file_path = os.path.join(new_daily_csv_folder_path, file_name)

                # Check if the file already exists and remove it
                if os.path.exists(file_path):
                    os.remove(file_path)

                # Write the data frame to the Excel file
                df_final.to_csv(file_path, index=False)
    return ("csvs have been concatenated")


def calculate_wins_losses(master_dictionary, monthly_or_daily_1_2, win_perc=0.5, loss_perc=0.4):
    for symbol in master_dictionary["symbols"]:
        for chart_time in master_dictionary["chart_times"]:
            # Construct the file name
            file_name = f"{symbol}-{chart_time}.csv"
            if monthly_or_daily_1_2 in ["m", "M", "monthly", 1]:
                # Construct the file path
                file_path = Path(output_dir) / f"{symbol}-{chart_time}-monthly_data/{file_name}"
            if monthly_or_daily_1_2 in ["d", "D", "daily", 2]:
                file_path = Path(output_dir) / f"{symbol}-{chart_time}-daily_data/{file_name}"
            # Read the CSV file into a dataframe
            df = pd.read_csv(file_path)
            df["if_short"] = 0
            df["if_long"] = 0
            df["long_target"] = np.nan
            df["short_target"] = np.nan
            df["long_stop_loss"] = np.nan
            df["short_stop_loss"] = np.nan
            df["shorts_win_after"] = np.nan
            df["longs_win_after"] = np.nan
            df["dual_loss"] = 0
            df["entered_before"] = np.nan

            for i in range(len(df)):
                if df["entry"][i]:
                    long_target = df["entry"][i] * (1 + win_perc / 100)
                    short_target = df["entry"][i] * (1 - win_perc / 100)
                    long_stop_loss = df["entry"][i] * (1 - loss_perc / 100)
                    short_stop_loss = df["entry"][i] * (1 + loss_perc / 100)
                    df.loc[i, 'long_target'] = long_target
                    df.loc[i, 'long_stop_loss'] = long_stop_loss
                    for j in range(i, len(df)):
                        if df["high"][j] >= long_target:
                            if df["low"][j] <= long_stop_loss:
                                df.loc[i, 'if_long'] = -1
                                df.loc[i, 'dual_loss'] = 1
                                df.loc[i, 'entered_before'] = j - i
                            else:
                                df.loc[i, 'if_long'] = 1
                                df.loc[i, 'longs_win_after'] = j - i
                            break
                        elif df["low"][j] <= long_stop_loss:
                            df.loc[i, 'if_long'] = -1
                            break
                    df.loc[i, 'short_target'] = short_target
                    df.loc[i, 'short_stop_loss'] = short_stop_loss
                    for j in range(i, len(df)):
                        if df["low"][j] <= short_target:
                            if df["high"][j] >= short_stop_loss:
                                df.loc[i, 'if_short'] = -1
                                df.loc[i, 'dual_loss'] = 1
                                df.loc[i, 'entered_before'] = j - i
                            else:
                                df.loc[i, 'if_short'] = 1
                                df.loc[i, 'shorts_win_after'] = j - i
                            break
                        elif df["high"][j] >= short_stop_loss:
                            df.loc[i, 'if_short'] = -1
                            break
            # Save the updated dataframe to the CSV file
            df.to_csv(file_path, index=False)
    return ("calculated wins and losses ")


def calculate_indicator_values_new(master_dictionary, monthly_or_daily_1_2):
    # Iterate over the symbols and chart times
    for symbol in master_dictionary["symbols"]:
        for chart_time in master_dictionary["chart_times"]:
            # Construct the file name
            file_name = f"{symbol}-{chart_time}.csv"

            if monthly_or_daily_1_2 in ["m", "M", "monthly", 1]:
                # Construct the file path
                file_path = Path(output_dir) / f"{symbol}-{chart_time}-monthly_data/{file_name}"
            elif monthly_or_daily_1_2 in ["d", "D", "daily", 2]:
                # Construct the file path
                file_path = Path(output_dir) / f"{symbol}-{chart_time}-daily_data/{file_name}"

            # Read the CSV file into a dataframe
            df = pd.read_csv(file_path)
            print(df.dtypes)
            #########Overlap Studies
            df['HT_TRENDLINE'] = talib.HT_TRENDLINE(df['close'])
            #         df['MAMA'], df['FAMA'] = talib.MAMA(df['close'], fastlimit=0, slowlimit=0)
            #         df['MAVP'] = talib.MAVP(df['close'], periods=None, minperiod=2, maxperiod=30, matype=0)
            df['SAR'] = talib.SAR(df['high'], df['low'], acceleration=0, maximum=0)
            df['SAREXT'] = talib.SAREXT(df['high'], df['low'])
            df['T3'] = talib.T3(df['close'], timeperiod=5, vfactor=0)
            #########Momentum Indicators
            df['APO'] = talib.APO(df['close'], fastperiod=12, slowperiod=26)
            df['BOP'] = talib.BOP(df['open'], df['high'], df['low'], df['close'])
            df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['close'], fastperiod=12, slowperiod=26,
                                                                        signalperiod=9)
            df['PPO'] = talib.PPO(df['close'], fastperiod=12, slowperiod=26, matype=0)
            df['TRIX'] = talib.TRIX(df['close'])
            df['ULTOSC'] = talib.ULTOSC(df['high'], df['low'], df['close'])
            df['WILLR'] = talib.WILLR(df['high'], df['low'], df['close'])

            # Not Working ATM
            #         df['STOCH'] = talib.STOCH(df['high'], df['low'], df['close'])
            #         df['STOCHF'] = talib.STOCHF(df['high'], df['low'], df['close'])
            #         df['STOCHRSI'] = talib.STOCHRSI(df['close'])
            #         df['MACDEXT'] = talib.MACDEXT(df['close'], fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
            #         df['MACDFIX'] = talib.MACDFIX(df['close'], signalperiod=9)
            #########Volume Indicators
            df['AD'] = talib.AD(df['high'], df['low'], df['close'], df['volume'])
            df['ADOSC'] = talib.ADOSC(df['high'], df['low'], df['close'], df['volume'], fastperiod=3, slowperiod=10)
            df['OBV'] = talib.OBV(df['close'], df['volume'])
            #########Cycle Indicators
            df['HT_DCPERIOD'] = talib.HT_DCPERIOD(df['close'])
            df['HT_DCPHASE'] = talib.HT_DCPHASE(df['close'])
            df['HT_PHASOR_inphase'], df['HT_PHASOR_quadrature'] = talib.HT_PHASOR(df['close'])
            #         df['HT_SINE'] = talib.HT_SINE(df['close'])
            df['HT_TRENDMODE'] = talib.HT_TRENDMODE(df['close'])
            #########Price Transform
            df['AVGPRICE'] = talib.AVGPRICE(df['open'], df['high'], df['low'], df['close'])
            df['MEDPRICE'] = talib.MEDPRICE(df['high'], df['low'])
            df['TYPPRICE'] = talib.TYPPRICE(df['high'], df['low'], df['close'])
            df['WCLPRICE'] = talib.WCLPRICE(df['high'], df['low'], df['close'])
            #########Volatility Indicators
            df['TRANGE'] = talib.TRANGE(df['high'], df['low'], df['close'])
            #########Pattern Recognition
            df['CDL2CROWS'] = talib.CDL2CROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDL3BLACKCROWS'] = talib.CDL3BLACKCROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDL3INSIDE'] = talib.CDL3INSIDE(df['open'], df['high'], df['low'], df['close'])
            df['CDL3LINESTRIKE'] = talib.CDL3LINESTRIKE(df['open'], df['high'], df['low'], df['close'])
            df['CDL3OUTSIDE'] = talib.CDL3OUTSIDE(df['open'], df['high'], df['low'], df['close'])
            df['CDL3STARSINSOUTH'] = talib.CDL3STARSINSOUTH(df['open'], df['high'], df['low'], df['close'])
            df['CDL3WHITESOLDIERS'] = talib.CDL3WHITESOLDIERS(df['open'], df['high'], df['low'], df['close'])
            df['CDLABANDONEDBABY'] = talib.CDLABANDONEDBABY(df['open'], df['high'], df['low'], df['close'],
                                                            penetration=0)
            df['CDLADVANCEBLOCK'] = talib.CDLADVANCEBLOCK(df['open'], df['high'], df['low'], df['close'])
            df['CDLBELTHOLD'] = talib.CDLBELTHOLD(df['open'], df['high'], df['low'], df['close'])
            df['CDLBREAKAWAY'] = talib.CDLBREAKAWAY(df['open'], df['high'], df['low'], df['close'])
            df['CDLCLOSINGMARUBOZU'] = talib.CDLCLOSINGMARUBOZU(df['open'], df['high'], df['low'], df['close'])
            df['CDLCONCEALBABYSWALL'] = talib.CDLCONCEALBABYSWALL(df['open'], df['high'], df['low'], df['close'])
            df['CDLCOUNTERATTACK'] = talib.CDLCOUNTERATTACK(df['open'], df['high'], df['low'], df['close'])
            df['CDLDARKCLOUDCOVER'] = talib.CDLDARKCLOUDCOVER(df['open'], df['high'], df['low'], df['close'],
                                                              penetration=0)
            df['CDLDOJI'] = talib.CDLDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLDOJISTAR'] = talib.CDLDOJISTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLDRAGONFLYDOJI'] = talib.CDLDRAGONFLYDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLENGULFING'] = talib.CDLENGULFING(df['open'], df['high'], df['low'], df['close'])
            df['CDLEVENINGDOJISTAR'] = talib.CDLEVENINGDOJISTAR(df['open'], df['high'], df['low'], df['close'],
                                                                penetration=0)
            df['CDLEVENINGSTAR'] = talib.CDLEVENINGSTAR(df['open'], df['high'], df['low'], df['close'], penetration=0)
            df['CDLGAPSIDESIDEWHITE'] = talib.CDLGAPSIDESIDEWHITE(df['open'], df['high'], df['low'], df['close'])
            df['CDLGRAVESTONEDOJI'] = talib.CDLGRAVESTONEDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLHAMMER'] = talib.CDLHAMMER(df['open'], df['high'], df['low'], df['close'])
            df['CDLHANGINGMAN'] = talib.CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close'])
            df['CDLHARAMI'] = talib.CDLHARAMI(df['open'], df['high'], df['low'], df['close'])
            df['CDLHARAMICROSS'] = talib.CDLHARAMICROSS(df['open'], df['high'], df['low'], df['close'])
            df['CDLHIGHWAVE'] = talib.CDLHIGHWAVE(df['open'], df['high'], df['low'], df['close'])
            df['CDLHIKKAKE'] = talib.CDLHIKKAKE(df['open'], df['high'], df['low'], df['close'])
            df['CDLHIKKAKEMOD'] = talib.CDLHIKKAKEMOD(df['open'], df['high'], df['low'], df['close'])
            df['CDLHOMINGPIGEON'] = talib.CDLHOMINGPIGEON(df['open'], df['high'], df['low'], df['close'])
            df['CDLIDENTICAL3CROWS'] = talib.CDLIDENTICAL3CROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDLINNECK'] = talib.CDLINNECK(df['open'], df['high'], df['low'], df['close'])
            df['CDLINVERTEDHAMMER'] = talib.CDLINVERTEDHAMMER(df['open'], df['high'], df['low'], df['close'])
            df['CDLKICKING'] = talib.CDLKICKING(df['open'], df['high'], df['low'], df['close'])
            df['CDLKICKINGBYLENGTH'] = talib.CDLKICKINGBYLENGTH(df['open'], df['high'], df['low'], df['close'])
            df['CDLLADDERBOTTOM'] = talib.CDLLADDERBOTTOM(df['open'], df['high'], df['low'], df['close'])
            df['CDLLONGLEGGEDDOJI'] = talib.CDLLONGLEGGEDDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLLONGLINE'] = talib.CDLLONGLINE(df['open'], df['high'], df['low'], df['close'])
            df['CDLMARUBOZU'] = talib.CDLMARUBOZU(df['open'], df['high'], df['low'], df['close'])
            df['CDLMATCHINGLOW'] = talib.CDLMATCHINGLOW(df['open'], df['high'], df['low'], df['close'])
            df['CDLMATHOLD'] = talib.CDLMATHOLD(df['open'], df['high'], df['low'], df['close'], penetration=0)
            df['CDLMORNINGDOJISTAR'] = talib.CDLMORNINGDOJISTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLMORNINGSTAR'] = talib.CDLMORNINGSTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLONNECK'] = talib.CDLONNECK(df['open'], df['high'], df['low'], df['close'])
            df['CDLPIERCING'] = talib.CDLPIERCING(df['open'], df['high'], df['low'], df['close'])
            df['CDLRICKSHAWMAN'] = talib.CDLRICKSHAWMAN(df['open'], df['high'], df['low'], df['close'])
            df['CDLRISEFALL3METHODS'] = talib.CDLRISEFALL3METHODS(df['open'], df['high'], df['low'], df['close'])
            df['CDLSEPARATINGLINES'] = talib.CDLSEPARATINGLINES(df['open'], df['high'], df['low'], df['close'])
            df['CDLSHOOTINGSTAR'] = talib.CDLSHOOTINGSTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLSHORTLINE'] = talib.CDLSHORTLINE(df['open'], df['high'], df['low'], df['close'])
            df['CDLSPINNINGTOP'] = talib.CDLSPINNINGTOP(df['open'], df['high'], df['low'], df['close'])
            df['CDLSTALLEDPATTERN'] = talib.CDLSTALLEDPATTERN(df['open'], df['high'], df['low'], df['close'])
            df['CDLSTICKSANDWICH'] = talib.CDLSTICKSANDWICH(df['open'], df['high'], df['low'], df['close'])
            df['CDLTAKURI'] = talib.CDLTAKURI(df['open'], df['high'], df['low'], df['close'])
            df['CDLTASUKIGAP'] = talib.CDLTASUKIGAP(df['open'], df['high'], df['low'], df['close'])
            df['CDLTHRUSTING'] = talib.CDLTHRUSTING(df['open'], df['high'], df['low'], df['close'])
            df['CDLTRISTAR'] = talib.CDLTRISTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLUNIQUE3RIVER'] = talib.CDLUNIQUE3RIVER(df['open'], df['high'], df['low'], df['close'])
            df['CDLUPSIDEGAP2CROWS'] = talib.CDLUPSIDEGAP2CROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDLXSIDEGAP3METHODS'] = talib.CDLXSIDEGAP3METHODS(df['open'], df['high'], df['low'], df['close'])
            #########Statistic Functions
            df['LINEARREG'] = talib.LINEARREG(df['close'])
            df['LINEARREG_ANGLE'] = talib.LINEARREG_ANGLE(df['close'])
            df['LINEARREG_INTERCEPT'] = talib.LINEARREG_INTERCEPT(df['close'])
            df['LINEARREG_SLOPE'] = talib.LINEARREG_SLOPE(df['close'])
            #         df['STDDEV'] = df['close'].rolling(timeperiod).std()
            df['TSF'] = talib.TSF(df['close'])
            df['VAR'] = talib.VAR(df['close'])
            # Iterate over the time periods
            for timeperiod in master_dictionary["timeperiods"]:
                #########Overlap Studies
                df[f'BB_upper_{timeperiod}'], df[f'BB_middle_{timeperiod}'], df[
                    f'BB_lower_{timeperiod}'] = talib.BBANDS(df['close'], timeperiod=timeperiod)
                df[f'DEMA_{timeperiod}'] = talib.DEMA(df['close'], timeperiod=timeperiod)
                df[f'EMA_{timeperiod}'] = talib.EMA(df['close'], timeperiod=timeperiod)
                df[f'KAMA_{timeperiod}'] = talib.KAMA(df['close'], timeperiod=timeperiod)
                df[f'MA_{timeperiod}'] = talib.MA(df['close'], timeperiod=timeperiod)
                #         df['MAMA'], df['FAMA'] = talib.MAMA(df['close'], fastlimit=0, slowlimit=0)
                #         df['MAVP'] = talib.MAVP(df['close'], periods=None, minperiod=2, maxperiod=30, matype=0)
                df[f'MIDPOINT_{timeperiod}'] = talib.MIDPOINT(df['close'], timeperiod=timeperiod)
                df[f'MIDPRICE_{timeperiod}'] = talib.MIDPRICE(df['high'], df['low'], timeperiod=timeperiod)
                df[f'SMA_{timeperiod}'] = talib.SMA(df['close'], timeperiod=timeperiod)
                df[f'TEMA_{timeperiod}'] = talib.TEMA(df['close'], timeperiod=timeperiod)
                df[f'TRIMA_{timeperiod}'] = talib.TRIMA(df['close'], timeperiod=timeperiod)
                df[f'WMA_{timeperiod}'] = talib.WMA(df['close'], timeperiod=timeperiod)
                df[f'ADX_{timeperiod}'] = talib.ADX(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                df[f'ADXR_{timeperiod}'] = talib.ADXR(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                df[f'AROON_up_{timeperiod}'], df[f'AROON_down_{timeperiod}'] = talib.AROON(df['high'], df['low'],
                                                                                           timeperiod=timeperiod)
                df[f'AROONOSC_{timeperiod}'] = talib.AROONOSC(df['high'], df['low'], timeperiod=timeperiod)
                df[f'CCI_{timeperiod}'] = talib.CCI(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                df[f'CMO_{timeperiod}'] = talib.CMO(df['close'], timeperiod=timeperiod)
                df[f'DX_{timeperiod}'] = talib.DX(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                df[f'MFI_{timeperiod}'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'],
                                                    timeperiod=timeperiod)
                df[f'MINUS_DI_{timeperiod}'] = talib.MINUS_DI(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                df[f'MINUS_DM_{timeperiod}'] = talib.MINUS_DM(df['high'], df['low'], timeperiod=timeperiod)
                df[f'MOM_{timeperiod}'] = talib.MOM(df['close'], timeperiod=timeperiod)
                df[f'PLUS_DI_{timeperiod}'] = talib.PLUS_DI(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                df[f'PLUS_DM_{timeperiod}'] = talib.PLUS_DM(df['high'], df['low'], timeperiod=timeperiod)
                df[f'ROC_{timeperiod}'] = talib.ROC(df['close'], timeperiod=timeperiod)
                df[f'ROCP_{timeperiod}'] = talib.ROCP(df['close'], timeperiod=timeperiod)
                df[f'ROCR_{timeperiod}'] = talib.ROCR(df['close'], timeperiod=timeperiod)
                df[f'ROCR100_{timeperiod}'] = talib.ROCR100(df['close'], timeperiod=timeperiod)
                df[f'RSI_{timeperiod}'] = talib.RSI(df['close'], timeperiod=timeperiod)

                df[f'ATR_{timeperiod}'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                df[f'NATR_{timeperiod}'] = talib.NATR(df['high'], df['low'], df['close'], timeperiod=timeperiod)
                #########Statistic Functions
                df[f'BETA_{timeperiod}'] = talib.BETA(df['high'], df['low'], timeperiod=timeperiod)
                df[f'CORREL_{timeperiod}'] = talib.CORREL(df['high'], df['low'], timeperiod=timeperiod)
            # Save the updated dataframe to the CSV file
            df.to_csv(file_path, index=False)
    return ("indicators are added to the csv")


def calculate_indicator_values_old(master_dictionary, monthly_or_daily_1_2):
    # Iterate over the symbols and chart times
    for symbol in master_dictionary["symbols"]:
        for chart_time in master_dictionary["chart_times"]:
            # Construct the file name
            file_name = f"{symbol}-{chart_time}.csv"
            if monthly_or_daily_1_2 in ["m", "M", "monthly", 1]:
                # Construct the file path
                file_path = Path(output_dir) / f"{symbol}-{chart_time}-monthly_data/{file_name}"
            elif monthly_or_daily_1_2 in ["d", "D", "daily", 2]:
                # Construct the file path
                file_path = Path(output_dir) / f"{symbol}-{chart_time}-daily_data/{file_name}"
            # Read the CSV file into a dataframe
            df = pd.read_csv(file_path)
            print(df.dtypes)
            #########Overlap Studies
            df['BB_upper'], df['BB_middle'], df['BB_lower'] = talib.BBANDS(df['close'], timeperiod=5)
            df['DEMA'] = talib.DEMA(df['close'], timeperiod=30)
            df['EMA-50'] = talib.EMA(df['close'], timeperiod=50)
            df['EMA-200'] = talib.EMA(df['close'], timeperiod=200)
            df['HT_TRENDLINE'] = talib.HT_TRENDLINE(df['close'])
            df['KAMA'] = talib.KAMA(df['close'], timeperiod=30)
            df['MA'] = talib.MA(df['close'], timeperiod=14)
            #         df['MAMA'], df['FAMA'] = talib.MAMA(df['close'], fastlimit=0, slowlimit=0)
            #         df['MAVP'] = talib.MAVP(df['close'], periods=None, minperiod=2, maxperiod=30, matype=0)
            df['MIDPOINT'] = talib.MIDPOINT(df['close'], timeperiod=14)
            df['MIDPRICE'] = talib.MIDPRICE(df['high'], df['low'], timeperiod=14)
            df['SAR'] = talib.SAR(df['high'], df['low'], acceleration=0, maximum=0)
            df['SAREXT'] = talib.SAREXT(df['high'], df['low'])
            df['SMA'] = talib.SMA(df['close'], timeperiod=14)
            df['T3'] = talib.T3(df['close'], timeperiod=5, vfactor=0)
            df['TEMA'] = talib.TEMA(df['close'])
            df['TRIMA'] = talib.TRIMA(df['close'])
            df['WMA'] = talib.WMA(df['close'])
            #########Momentum Indicators
            df['ADX'] = talib.ADX(df['high'], df['low'], df['close'], timeperiod=14)
            df['ADXR'] = talib.ADXR(df['high'], df['low'], df['close'], timeperiod=14)
            df['APO'] = talib.APO(df['close'], fastperiod=12, slowperiod=26)
            df['AROON_up'], df['AROON_down'] = talib.AROON(df['high'], df['low'], timeperiod=14)
            df['AROONOSC'] = talib.AROONOSC(df['high'], df['low'], timeperiod=14)
            df['BOP'] = talib.BOP(df['open'], df['high'], df['low'], df['close'])
            df['CCI'] = talib.CCI(df['high'], df['low'], df['close'], timeperiod=14)
            df['CMO'] = talib.CMO(df['close'], timeperiod=14)
            df['DX'] = talib.DX(df['high'], df['low'], df['close'], timeperiod=14)
            df['MACD'], df['MACD_signal'], df['MACD_hist'] = talib.MACD(df['close'], fastperiod=12, slowperiod=26,
                                                                        signalperiod=9)
            df['MFI'] = talib.MFI(df['high'], df['low'], df['close'], df['volume'], timeperiod=14)
            df['MINUS_DI'] = talib.MINUS_DI(df['high'], df['low'], df['close'], timeperiod=14)
            df['MINUS_DM'] = talib.MINUS_DM(df['high'], df['low'], timeperiod=14)
            df['MOM'] = talib.MOM(df['close'], timeperiod=14)
            df['PLUS_DI'] = talib.PLUS_DI(df['high'], df['low'], df['close'], timeperiod=14)
            df['PLUS_DM'] = talib.PLUS_DM(df['high'], df['low'], timeperiod=14)
            df['PPO'] = talib.PPO(df['close'], fastperiod=12, slowperiod=26, matype=0)
            df['ROC'] = talib.ROC(df['close'], timeperiod=14)
            df['ROCP'] = talib.ROCP(df['close'], timeperiod=14)
            df['ROCR'] = talib.ROCR(df['close'], timeperiod=14)
            df['ROCR100'] = talib.ROCR100(df['close'], timeperiod=14)
            df['RSI'] = talib.RSI(df['close'], timeperiod=8)
            df['TRIX'] = talib.TRIX(df['close'])
            df['ULTOSC'] = talib.ULTOSC(df['high'], df['low'], df['close'])
            df['WILLR'] = talib.WILLR(df['high'], df['low'], df['close'])

            # Not Working ATM
            #         df['STOCH'] = talib.STOCH(df['high'], df['low'], df['close'])
            #         df['STOCHF'] = talib.STOCHF(df['high'], df['low'], df['close'])
            #         df['STOCHRSI'] = talib.STOCHRSI(df['close'])
            #         df['MACDEXT'] = talib.MACDEXT(df['close'], fastperiod=12, fastmatype=0, slowperiod=26, slowmatype=0, signalperiod=9, signalmatype=0)
            #         df['MACDFIX'] = talib.MACDFIX(df['close'], signalperiod=9)
            #########Volume Indicators
            df['AD'] = talib.AD(df['high'], df['low'], df['close'], df['volume'])
            df['ADOSC'] = talib.ADOSC(df['high'], df['low'], df['close'], df['volume'], fastperiod=3, slowperiod=10)
            df['OBV'] = talib.OBV(df['close'], df['volume'])
            #########Cycle Indicators
            df['HT_DCPERIOD'] = talib.HT_DCPERIOD(df['close'])
            df['HT_DCPHASE'] = talib.HT_DCPHASE(df['close'])
            df['HT_PHASOR_inphase'], df['HT_PHASOR_quadrature'] = talib.HT_PHASOR(df['close'])
            #         df['HT_SINE'] = talib.HT_SINE(df['close'])
            df['HT_TRENDMODE'] = talib.HT_TRENDMODE(df['close'])
            #########Price Transform
            df['AVGPRICE'] = talib.AVGPRICE(df['open'], df['high'], df['low'], df['close'])
            df['MEDPRICE'] = talib.MEDPRICE(df['high'], df['low'])
            df['TYPPRICE'] = talib.TYPPRICE(df['high'], df['low'], df['close'])
            df['WCLPRICE'] = talib.WCLPRICE(df['high'], df['low'], df['close'])
            #########Volatility Indicators
            df['ATR'] = talib.ATR(df['high'], df['low'], df['close'], timeperiod=14)
            df['NATR'] = talib.NATR(df['high'], df['low'], df['close'], timeperiod=14)
            df['TRANGE'] = talib.TRANGE(df['high'], df['low'], df['close'])
            #########Pattern Recognition
            df['CDL2CROWS'] = talib.CDL2CROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDL3BLACKCROWS'] = talib.CDL3BLACKCROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDL3INSIDE'] = talib.CDL3INSIDE(df['open'], df['high'], df['low'], df['close'])
            df['CDL3LINESTRIKE'] = talib.CDL3LINESTRIKE(df['open'], df['high'], df['low'], df['close'])
            df['CDL3OUTSIDE'] = talib.CDL3OUTSIDE(df['open'], df['high'], df['low'], df['close'])
            df['CDL3STARSINSOUTH'] = talib.CDL3STARSINSOUTH(df['open'], df['high'], df['low'], df['close'])
            df['CDL3WHITESOLDIERS'] = talib.CDL3WHITESOLDIERS(df['open'], df['high'], df['low'], df['close'])
            df['CDLABANDONEDBABY'] = talib.CDLABANDONEDBABY(df['open'], df['high'], df['low'], df['close'],
                                                            penetration=0)
            df['CDLADVANCEBLOCK'] = talib.CDLADVANCEBLOCK(df['open'], df['high'], df['low'], df['close'])
            df['CDLBELTHOLD'] = talib.CDLBELTHOLD(df['open'], df['high'], df['low'], df['close'])
            df['CDLBREAKAWAY'] = talib.CDLBREAKAWAY(df['open'], df['high'], df['low'], df['close'])
            df['CDLCLOSINGMARUBOZU'] = talib.CDLCLOSINGMARUBOZU(df['open'], df['high'], df['low'], df['close'])
            df['CDLCONCEALBABYSWALL'] = talib.CDLCONCEALBABYSWALL(df['open'], df['high'], df['low'], df['close'])
            df['CDLCOUNTERATTACK'] = talib.CDLCOUNTERATTACK(df['open'], df['high'], df['low'], df['close'])
            df['CDLDARKCLOUDCOVER'] = talib.CDLDARKCLOUDCOVER(df['open'], df['high'], df['low'], df['close'],
                                                              penetration=0)
            df['CDLDOJI'] = talib.CDLDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLDOJISTAR'] = talib.CDLDOJISTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLDRAGONFLYDOJI'] = talib.CDLDRAGONFLYDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLENGULFING'] = talib.CDLENGULFING(df['open'], df['high'], df['low'], df['close'])
            df['CDLEVENINGDOJISTAR'] = talib.CDLEVENINGDOJISTAR(df['open'], df['high'], df['low'], df['close'],
                                                                penetration=0)
            df['CDLEVENINGSTAR'] = talib.CDLEVENINGSTAR(df['open'], df['high'], df['low'], df['close'], penetration=0)
            df['CDLGAPSIDESIDEWHITE'] = talib.CDLGAPSIDESIDEWHITE(df['open'], df['high'], df['low'], df['close'])
            df['CDLGRAVESTONEDOJI'] = talib.CDLGRAVESTONEDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLHAMMER'] = talib.CDLHAMMER(df['open'], df['high'], df['low'], df['close'])
            df['CDLHANGINGMAN'] = talib.CDLHANGINGMAN(df['open'], df['high'], df['low'], df['close'])
            df['CDLHARAMI'] = talib.CDLHARAMI(df['open'], df['high'], df['low'], df['close'])
            df['CDLHARAMICROSS'] = talib.CDLHARAMICROSS(df['open'], df['high'], df['low'], df['close'])
            df['CDLHIGHWAVE'] = talib.CDLHIGHWAVE(df['open'], df['high'], df['low'], df['close'])
            df['CDLHIKKAKE'] = talib.CDLHIKKAKE(df['open'], df['high'], df['low'], df['close'])
            df['CDLHIKKAKEMOD'] = talib.CDLHIKKAKEMOD(df['open'], df['high'], df['low'], df['close'])
            df['CDLHOMINGPIGEON'] = talib.CDLHOMINGPIGEON(df['open'], df['high'], df['low'], df['close'])
            df['CDLIDENTICAL3CROWS'] = talib.CDLIDENTICAL3CROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDLINNECK'] = talib.CDLINNECK(df['open'], df['high'], df['low'], df['close'])
            df['CDLINVERTEDHAMMER'] = talib.CDLINVERTEDHAMMER(df['open'], df['high'], df['low'], df['close'])
            df['CDLKICKING'] = talib.CDLKICKING(df['open'], df['high'], df['low'], df['close'])
            df['CDLKICKINGBYLENGTH'] = talib.CDLKICKINGBYLENGTH(df['open'], df['high'], df['low'], df['close'])
            df['CDLLADDERBOTTOM'] = talib.CDLLADDERBOTTOM(df['open'], df['high'], df['low'], df['close'])
            df['CDLLONGLEGGEDDOJI'] = talib.CDLLONGLEGGEDDOJI(df['open'], df['high'], df['low'], df['close'])
            df['CDLLONGLINE'] = talib.CDLLONGLINE(df['open'], df['high'], df['low'], df['close'])
            df['CDLMARUBOZU'] = talib.CDLMARUBOZU(df['open'], df['high'], df['low'], df['close'])
            df['CDLMATCHINGLOW'] = talib.CDLMATCHINGLOW(df['open'], df['high'], df['low'], df['close'])
            df['CDLMATHOLD'] = talib.CDLMATHOLD(df['open'], df['high'], df['low'], df['close'], penetration=0)
            df['CDLMORNINGDOJISTAR'] = talib.CDLMORNINGDOJISTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLMORNINGSTAR'] = talib.CDLMORNINGSTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLONNECK'] = talib.CDLONNECK(df['open'], df['high'], df['low'], df['close'])
            df['CDLPIERCING'] = talib.CDLPIERCING(df['open'], df['high'], df['low'], df['close'])
            df['CDLRICKSHAWMAN'] = talib.CDLRICKSHAWMAN(df['open'], df['high'], df['low'], df['close'])
            df['CDLRISEFALL3METHODS'] = talib.CDLRISEFALL3METHODS(df['open'], df['high'], df['low'], df['close'])
            df['CDLSEPARATINGLINES'] = talib.CDLSEPARATINGLINES(df['open'], df['high'], df['low'], df['close'])
            df['CDLSHOOTINGSTAR'] = talib.CDLSHOOTINGSTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLSHORTLINE'] = talib.CDLSHORTLINE(df['open'], df['high'], df['low'], df['close'])
            df['CDLSPINNINGTOP'] = talib.CDLSPINNINGTOP(df['open'], df['high'], df['low'], df['close'])
            df['CDLSTALLEDPATTERN'] = talib.CDLSTALLEDPATTERN(df['open'], df['high'], df['low'], df['close'])
            df['CDLSTICKSANDWICH'] = talib.CDLSTICKSANDWICH(df['open'], df['high'], df['low'], df['close'])
            df['CDLTAKURI'] = talib.CDLTAKURI(df['open'], df['high'], df['low'], df['close'])
            df['CDLTASUKIGAP'] = talib.CDLTASUKIGAP(df['open'], df['high'], df['low'], df['close'])
            df['CDLTHRUSTING'] = talib.CDLTHRUSTING(df['open'], df['high'], df['low'], df['close'])
            df['CDLTRISTAR'] = talib.CDLTRISTAR(df['open'], df['high'], df['low'], df['close'])
            df['CDLUNIQUE3RIVER'] = talib.CDLUNIQUE3RIVER(df['open'], df['high'], df['low'], df['close'])
            df['CDLUPSIDEGAP2CROWS'] = talib.CDLUPSIDEGAP2CROWS(df['open'], df['high'], df['low'], df['close'])
            df['CDLXSIDEGAP3METHODS'] = talib.CDLXSIDEGAP3METHODS(df['open'], df['high'], df['low'], df['close'])
            #########Statistic Functions
            df['BETA'] = talib.BETA(df['high'], df['low'], timeperiod=5)
            df['CORREL'] = talib.CORREL(df['high'], df['low'], timeperiod=30)
            df['LINEARREG'] = talib.LINEARREG(df['close'])
            df['LINEARREG_ANGLE'] = talib.LINEARREG_ANGLE(df['close'])
            df['LINEARREG_INTERCEPT'] = talib.LINEARREG_INTERCEPT(df['close'])
            df['LINEARREG_SLOPE'] = talib.LINEARREG_SLOPE(df['close'])
            #         df['STDDEV'] = df['close'].rolling(timeperiod).std()
            df['TSF'] = talib.TSF(df['close'])
            df['VAR'] = talib.VAR(df['close'])

            # Save the updated dataframe to the CSV file
            df.to_csv(file_path, index=False)
    return ("indicators are added to the csv")
