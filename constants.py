import os

CHART_TIME_STRING = "12h, 15m, 1d, 1h, 1m, 1mo, 1w, 2h, 30m, 3d, 3m, 4h, 5m, 6h, 8h"
BINANCE_URL = "https://data.binance.vision/data/futures/um/monthly/klines/"
SYMBOL_STRING = "1000BTTCUSDT, 1000LUNCBUSD, 1000LUNCUSDT, 1000SHIBBUSD, 1000SHIBUSDT, 1000XECUSDT, 1INCHUSDT, AAVEUSDT," \
                "ADABUSD, ADAUSDT, AKROUSDT, ALGOUSDT, ALICEUSDT, ALPHAUSDT, AMBBUSD, ANCBUSD, ANCUSDT, ANKRUSDT, " \
                "ANTUSDT, APEBUSD, APEUSDT, API3USDT, APTBUSD, APTUSDT, ARPAUSDT, ARUSDT, ATAUSDT, ATOMUSDT, " \
                "AUCTIONBUSD, AUDIOUSDT, AVAXBUSD, AVAXUSDT, AXSUSDT, BAKEUSDT, BALUSDT, BANDUSDT, BATUSDT, BCHUSDT, " \
                "BELUSDT, BLUEBIRDUSDT, BLZUSDT, BNBBUSD, BNBUSDT, BNXUSDT, BTCBUSD, BTCBUSD_210129, BTCBUSD_210226, " \
                "BTCDOMUSDT, BTCSTUSDT, BTCUSDT, BTCUSDT_210326, BTCUSDT_210625, BTCUSDT_210924, BTCUSDT_211231, " \
                "BTCUSDT_220325, BTCUSDT_220624, BTCUSDT_220930, BTCUSDT_221230, BTCUSDT_230331, BTSUSDT, BTTUSDT, " \
                "BZRXUSDT, C98USDT, CELOUSDT, CELRUSDT, CHRUSDT, CHZUSDT, COMPUSDT, COTIUSDT, CRVUSDT, CTKUSDT, " \
                "CTSIUSDT, CVCUSDT, CVXBUSD, CVXUSDT, DARUSDT, DASHUSDT, DEFIUSDT, DENTUSDT, DGBUSDT, DODOBUSD, " \
                "DODOUSDT, DOGEBUSD, DOGEUSDT, DOTBUSD, DOTECOUSDT, DOTUSDT, DUSKUSDT, DYDXUSDT, EGLDUSDT, ENJUSDT, " \
                "ENSUSDT, EOSUSDT, ETCBUSD, ETCUSDT, ETHBUSD, ETHUSDT, ETHUSDT_210326, ETHUSDT_210625, " \
                "ETHUSDT_210924, ETHUSDT_211231, ETHUSDT_220325, ETHUSDT_220624, ETHUSDT_220930, ETHUSDT_221230, " \
                "ETHUSDT_230331, FILBUSD, FILUSDT, FLMUSDT, FLOWUSDT, FOOTBALLUSDT, FTMBUSD, FTMUSDT, FTTBUSD, " \
                "FTTUSDT, GALABUSD, GALAUSDT, GALBUSD, GALUSDT, GMTBUSD, GMTUSDT, GRTUSDT, GTCUSDT, HBARUSDT, " \
                "HNTUSDT, HOTUSDT, ICPBUSD, ICPUSDT, ICPUSDT_SETTLED, ICXUSDT, IMXUSDT, INJUSDT, IOSTUSDT, IOTAUSDT, " \
                "IOTXUSDT, JASMYUSDT, KAVAUSDT, KEEPUSDT, KLAYUSDT, KNCUSDT, KSMUSDT, LDOBUSD, LDOUSDT, LENDUSDT, " \
                "LEVERBUSD, LINAUSDT, LINKBUSD, LINKUSDT, LITUSDT, LPTUSDT, LRCUSDT, LTCBUSD, LTCUSDT, LUNA2BUSD, " \
                "LUNA2USDT, LUNABUSD, LUNAUSDT, MANAUSDT, MASKUSDT, MATICBUSD, MATICUSDT, MKRUSDT, MTLUSDT, NEARBUSD, " \
                "NEARUSDT, NEOUSDT, NKNUSDT, NUUSDT, OCEANUSDT, OGNUSDT, OMGUSDT, ONEUSDT, ONTUSDT, OPUSDT, " \
                "PEOPLEUSDT, PHBBUSD, QNTUSDT, QTUMUSDT, RAYUSDT, REEFUSDT, RENUSDT, RLCUSDT, ROSEUSDT, RSRUSDT, " \
                "RUNEUSDT, RVNUSDT, SANDBUSD, SANDUSDT, SCUSDT, SFPUSDT, SKLUSDT, SNXUSDT, SOLBUSD, SOLUSDT, " \
                "SPELLUSDT, SRMUSDT, STGUSDT, STMXUSDT, STORJUSDT, SUSHIUSDT, SXPUSDT, THETAUSDT, TLMBUSD, TLMUSDT, " \
                "TOMOUSDT, TRBUSDT, TRXBUSD, TRXUSDT, UNFIUSDT, UNIBUSD, UNIUSDT, VETUSDT, WAVESBUSD, WAVESUSDT, " \
                "WOOUSDT, XEMUSDT, XLMUSDT, XMRUSDT, XRPBUSD, XRPUSDT, XTZUSDT, YFIIUSDT, YFIUSDT, ZECUSDT, ZENUSDT, " \
                "ZILUSDT, ZRXUSDT "
# BINANCE_URL = BINANCE_URL.replace("?prefix=", "")
download_dir = os.path.join(os.getcwd(), "downloaded_data")
output_dir = os.path.join(os.getcwd(), "extracted_data")
dtypes = {
    'open': 'float',
    'high': 'float',
    'low': 'float',
    'close': 'float',
    'volume': 'float',
    'quote_volume': 'float',
    'count': 'int',
    'taker_buy_volume': 'float',
    'taker_buy_quote_volume': 'float',
    'ignore': 'int'
}
HTML_TEXT = """<html class=" jrviugss idc0_345"><head>
  <title>Binance Data Collection</title>
  <link href="bootstrap.min.css" rel="stylesheet">
<style>undefined</style><base href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/"><link rel="preconnect" href="https://fonts.googleapis.com" crossorigin="true"><link rel="preconnect" href="https://fonts.gstatic.com"><link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Mulish:wght@200;300;400;500;600;700;800;900&amp;display=swa"></head>
<body>
  <nav class="navbar navbar-dark bg-dark">
    <div class="container-md">
      <div class="row justify-content-between" style="width: 100%">
        <div class="col-sm">
          <a href="/"><img src="logo.png" height="30" class="d-inline-block align-top" alt=""></a>
          <span class="navbar-brand" style="padding-left: 10px;">Market Data</span>
        </div>
        <div class="col-sm" style="text-align: right">
          <a href="https://github.com/binance/binance-public-data/" data-toggle="tooltip" title="" data-original-title="Public data document">
            <svg class="octicon octicon-mark-github v-align-middle" height="25" viewBox="0 0 16 16" version="1.1" width="25" aria-hidden="true" style="fill: rgb(255, 255, 255); --darkreader-inline-fill:#e8e6e3;" data-darkreader-inline-fill="">
              <path fill-rule="evenodd" d="M8 0C3.58 0 0 3.58 0 8c0 3.54 2.29 6.53 5.47 7.59.4.07.55-.17.55-.38 0-.19-.01-.82-.01-1.49-2.01.37-2.53-.49-2.69-.94-.09-.23-.48-.94-.82-1.13-.28-.15-.68-.52-.01-.53.63-.01 1.08.58 1.23.82.72 1.21 1.87.87 2.33.66.07-.52.28-.87.51-1.07-1.78-.2-3.64-.89-3.64-3.95 0-.87.31-1.59.82-2.15-.08-.2-.36-1.02.08-2.12 0 0 .67-.21 2.2.82.64-.18 1.32-.27 2-.27.68 0 1.36.09 2 .27 1.53-1.04 2.2-.82 2.2-.82.44 1.1.16 1.92.08 2.12.51.56.82 1.27.82 2.15 0 3.07-1.87 3.75-3.65 3.95.29.25.54.73.54 1.48 0 1.07-.01 1.93-.01 2.2 0 .21.15.46.55.38A8.013 8.013 0 0016 8c0-4.42-3.58-8-8-8z"></path>
            </svg>
          </a>
        </div>
      </div>
    </div>
  </nav>
  <div class="container-md">
    <div id="navigation" class="h6" style="margin-top: .8rem"><a href="?prefix=">Home</a> / <a href="?prefix=data/">data</a> / <a href="?prefix=data/futures/">futures</a> / <a href="?prefix=data/futures/um/">um</a> / <a href="?prefix=data/futures/um/monthly/">monthly</a> / <a href="?prefix=data/futures/um/monthly/klines/">klines</a> / <a href="?prefix=data/futures/um/monthly/klines//"></a></div>

    <table class="table table-hover">
      <thead>
        <tr>
          <th scope="col">Item</th>
          <th scope="col">Size</th>
          <th scope="col">Last Modified</th>
        </tr>
      </thead>
      <tbody id="listing"><tr><td><a href="?prefix=data/futures/um/monthly/">../</a></td><td></td><td></td></tr><tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/1000BTTCUSDT/">1000BTTCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/1000LUNCBUSD/">1000LUNCBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/1000LUNCUSDT/">1000LUNCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/1000SHIBBUSD/">1000SHIBBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/1000SHIBUSDT/">1000SHIBUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/1000XECUSDT/">1000XECUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/1INCHUSDT/">1INCHUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AAVEUSDT/">AAVEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ADABUSD/">ADABUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ADAUSDT/">ADAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AKROUSDT/">AKROUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ALGOUSDT/">ALGOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ALICEUSDT/">ALICEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ALPHAUSDT/">ALPHAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AMBBUSD/">AMBBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ANCBUSD/">ANCBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ANCUSDT/">ANCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ANKRUSDT/">ANKRUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ANTUSDT/">ANTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/APEBUSD/">APEBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/APEUSDT/">APEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/API3USDT/">API3USDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/APTBUSD/">APTBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/APTUSDT/">APTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ARPAUSDT/">ARPAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ARUSDT/">ARUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ATAUSDT/">ATAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ATOMUSDT/">ATOMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AUCTIONBUSD/">AUCTIONBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AUDIOUSDT/">AUDIOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AVAXBUSD/">AVAXBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AVAXUSDT/">AVAXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/AXSUSDT/">AXSUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BAKEUSDT/">BAKEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BALUSDT/">BALUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BANDUSDT/">BANDUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BATUSDT/">BATUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BCHUSDT/">BCHUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BELUSDT/">BELUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BLUEBIRDUSDT/">BLUEBIRDUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BLZUSDT/">BLZUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BNBBUSD/">BNBBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BNBUSDT/">BNBUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BNXUSDT/">BNXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCBUSD/">BTCBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCBUSD_210129/">BTCBUSD_210129/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCBUSD_210226/">BTCBUSD_210226/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCDOMUSDT/">BTCDOMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCSTUSDT/">BTCSTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT/">BTCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_210326/">BTCUSDT_210326/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_210625/">BTCUSDT_210625/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_210924/">BTCUSDT_210924/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_211231/">BTCUSDT_211231/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_220325/">BTCUSDT_220325/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_220624/">BTCUSDT_220624/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_220930/">BTCUSDT_220930/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_221230/">BTCUSDT_221230/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTCUSDT_230331/">BTCUSDT_230331/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTSUSDT/">BTSUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BTTUSDT/">BTTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/BZRXUSDT/">BZRXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/C98USDT/">C98USDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CELOUSDT/">CELOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CELRUSDT/">CELRUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CHRUSDT/">CHRUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CHZUSDT/">CHZUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/COMPUSDT/">COMPUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/COTIUSDT/">COTIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CRVUSDT/">CRVUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CTKUSDT/">CTKUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CTSIUSDT/">CTSIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CVCUSDT/">CVCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CVXBUSD/">CVXBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/CVXUSDT/">CVXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DARUSDT/">DARUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DASHUSDT/">DASHUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DEFIUSDT/">DEFIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DENTUSDT/">DENTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DGBUSDT/">DGBUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DODOBUSD/">DODOBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DODOUSDT/">DODOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DOGEBUSD/">DOGEBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DOGEUSDT/">DOGEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DOTBUSD/">DOTBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DOTECOUSDT/">DOTECOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DOTUSDT/">DOTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DUSKUSDT/">DUSKUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/DYDXUSDT/">DYDXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/EGLDUSDT/">EGLDUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ENJUSDT/">ENJUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ENSUSDT/">ENSUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/EOSUSDT/">EOSUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETCBUSD/">ETCBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETCUSDT/">ETCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHBUSD/">ETHBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT/">ETHUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_210326/">ETHUSDT_210326/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_210625/">ETHUSDT_210625/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_210924/">ETHUSDT_210924/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_211231/">ETHUSDT_211231/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_220325/">ETHUSDT_220325/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_220624/">ETHUSDT_220624/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_220930/">ETHUSDT_220930/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_221230/">ETHUSDT_221230/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ETHUSDT_230331/">ETHUSDT_230331/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FILBUSD/">FILBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FILUSDT/">FILUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FLMUSDT/">FLMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FLOWUSDT/">FLOWUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FOOTBALLUSDT/">FOOTBALLUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FTMBUSD/">FTMBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FTMUSDT/">FTMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FTTBUSD/">FTTBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/FTTUSDT/">FTTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GALABUSD/">GALABUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GALAUSDT/">GALAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GALBUSD/">GALBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GALUSDT/">GALUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GMTBUSD/">GMTBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GMTUSDT/">GMTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GRTUSDT/">GRTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/GTCUSDT/">GTCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/HBARUSDT/">HBARUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/HNTUSDT/">HNTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/HOTUSDT/">HOTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ICPBUSD/">ICPBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ICPUSDT/">ICPUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ICPUSDT_SETTLED/">ICPUSDT_SETTLED/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ICXUSDT/">ICXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/IMXUSDT/">IMXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/INJUSDT/">INJUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/IOSTUSDT/">IOSTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/IOTAUSDT/">IOTAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/IOTXUSDT/">IOTXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/JASMYUSDT/">JASMYUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/KAVAUSDT/">KAVAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/KEEPUSDT/">KEEPUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/KLAYUSDT/">KLAYUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/KNCUSDT/">KNCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/KSMUSDT/">KSMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LDOBUSD/">LDOBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LDOUSDT/">LDOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LENDUSDT/">LENDUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LEVERBUSD/">LEVERBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LINAUSDT/">LINAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LINKBUSD/">LINKBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LINKUSDT/">LINKUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LITUSDT/">LITUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LPTUSDT/">LPTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LRCUSDT/">LRCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LTCBUSD/">LTCBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LTCUSDT/">LTCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LUNA2BUSD/">LUNA2BUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LUNA2USDT/">LUNA2USDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LUNABUSD/">LUNABUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/LUNAUSDT/">LUNAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/MANAUSDT/">MANAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/MASKUSDT/">MASKUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/MATICBUSD/">MATICBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/MATICUSDT/">MATICUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/MKRUSDT/">MKRUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/MTLUSDT/">MTLUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/NEARBUSD/">NEARBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/NEARUSDT/">NEARUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/NEOUSDT/">NEOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/NKNUSDT/">NKNUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/NUUSDT/">NUUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/OCEANUSDT/">OCEANUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/OGNUSDT/">OGNUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/OMGUSDT/">OMGUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ONEUSDT/">ONEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ONTUSDT/">ONTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/OPUSDT/">OPUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/PEOPLEUSDT/">PEOPLEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/PHBBUSD/">PHBBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/QNTUSDT/">QNTUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/QTUMUSDT/">QTUMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/RAYUSDT/">RAYUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/REEFUSDT/">REEFUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/RENUSDT/">RENUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/RLCUSDT/">RLCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ROSEUSDT/">ROSEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/RSRUSDT/">RSRUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/RUNEUSDT/">RUNEUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/RVNUSDT/">RVNUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SANDBUSD/">SANDBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SANDUSDT/">SANDUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SCUSDT/">SCUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SFPUSDT/">SFPUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SKLUSDT/">SKLUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SNXUSDT/">SNXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SOLBUSD/">SOLBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SOLUSDT/">SOLUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SPELLUSDT/">SPELLUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SRMUSDT/">SRMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/STGUSDT/">STGUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/STMXUSDT/">STMXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/STORJUSDT/">STORJUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SUSHIUSDT/">SUSHIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/SXPUSDT/">SXPUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/THETAUSDT/">THETAUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/TLMBUSD/">TLMBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/TLMUSDT/">TLMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/TOMOUSDT/">TOMOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/TRBUSDT/">TRBUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/TRXBUSD/">TRXBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/TRXUSDT/">TRXUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/UNFIUSDT/">UNFIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/UNIBUSD/">UNIBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/UNIUSDT/">UNIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/VETUSDT/">VETUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/WAVESBUSD/">WAVESBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/WAVESUSDT/">WAVESUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/WOOUSDT/">WOOUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/XEMUSDT/">XEMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/XLMUSDT/">XLMUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/XMRUSDT/">XMRUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/XRPBUSD/">XRPBUSD/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/XRPUSDT/">XRPUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/XTZUSDT/">XTZUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/YFIIUSDT/">YFIIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/YFIUSDT/">YFIUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ZECUSDT/">ZECUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ZENUSDT/">ZENUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ZILUSDT/">ZILUSDT/</a></td><td></td><td></td></tr>
<tr><td><a href="https://data.binance.vision/?prefix=data/futures/um/monthly/klines/ZRXUSDT/">ZRXUSDT/</a></td><td></td><td></td></tr>
</tbody>
    </table>
  </div>
  <script type="text/javascript" src="jquery.min.js"></script>
  <script type="text/javascript" src="bootstrap.bundle.min.js"></script>
  <script type="text/javascript">
    var S3BL_IGNORE_PATH = true;
    var BUCKET_URL = 'https://s3-ap-northeast-1.amazonaws.com/data.binance.vision';
    var BUCKET_WEBSITE_URL = 'https://data.binance.vision'
    var S3B_SORT = 'A2Z';
    var EXCLUDE_FILE = 'index.html'; 
    var S3B_ROOT_DIR = 'data/';
    $(function () {
      $('[data-toggle="tooltip"]').tooltip()
    })
  </script>
  <script type="text/javascript" src="list.js"></script>


</body></html>"""
