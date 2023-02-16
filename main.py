import logging
from connectors.binance_futures import BinanceFuturesClient
from connectors.bitmex import BitmexClient
from interface.root_component import Root
from fastapi import FastAPI

app = FastAPI()

logger = logging.getLogger()
logger.setLevel(logging.INFO)

stream_handler = logging.StreamHandler()
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO)

file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG)

logger.addHandler(stream_handler)
logger.addHandler(file_handler)

@app.get("/")
async def root():
    return {"message": "Hello World"}

if __name__ == '__main__':
    binance = BinanceFuturesClient("b060e27bd61e4942d4990fba88802cc4c4e803d2f23af9f10addef377411beb5", "0a1cfe7bffd303a2828b8a655f029a9526a0ed8f25c323db8e0302c3584ea805", True)
    bitmex = BitmexClient("hYTGJ0OaFURGv1GTt3amaYGC", "YhHsRt609CAZaQ-kQsA3x0EIloGC_AVoSfDvZTmiVIof75xk", True)

    root = Root(binance, bitmex)
    root.mainloop()
