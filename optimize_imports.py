import datetime
import glob
import inspect
import os
import re
import shutil
import time
import urllib.request
import zipfile
from pathlib import Path

import numpy as np
import pandas as pd
import requests
import talib
import talib
from constants import download_dir, output_dir, root_dir, dtypes, BINANCE_DAILY_URL, BINANCE_MONTHLY_URL
from creating_arrays import CHART_TIME_ARRAY, MONTH_ARRAY, SYMBOL_ARRAY
from data_creation_utils import download_data, unzip_and_concatenate_csv, \
    calculate_wins_losses, calculate_indicator_values_old
from pandas.api.types import is_numeric_dtype
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
