import os
import re
from creating_arrays import CHART_TIME_ARRAY, MONTH_ARRAY, SYMBOL_ARRAY
from constants import BINANCE_URL

BINANCE_URL = BINANCE_URL.replace("?prefix=", "")
# Set up the download directory
download_dir = os.path.join(os.getcwd(), "downloaded_data")

# Iterate over the symbols and chart times
for symbol in symbols:
    for chart_time in chart_times:
        # Compile the regular expression pattern
        pattern = re.compile(f"^{symbol}-{chart_time}-\d{{4}}-\d{{2}}\.zip$")

        # Iterate over the files in the download directory
        for file in os.listdir(download_dir):
            # Check if the file matches the pattern
            if pattern.match(file):
                # Construct the destination directory path
                dest_subdir = os.path.join(download_dir, f"{symbol}_{chart_time}")

                # Check if the destination subdirectory exists
                if not os.path.exists(dest_subdir):
                    # Create the destination subdirectory
                    os.makedirs(dest_subdir)

                # Move the file to the destination subdirectory
                os.replace(os.path.join(download_dir, file), os.path.join(dest_subdir, file))
