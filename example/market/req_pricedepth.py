
from huobi.client import MarketClient
from huobi.constant import DepthStep, HUOBI_WEBSOCKET_URI_VN


def callback(price_depth_req: 'PriceDepthReq'):
    price_depth_req.print_object()


def error(e: 'HuobiApiException'):
    print(e.error_code + e.error_message)


sub_client = MarketClient(url=HUOBI_WEBSOCKET_URI_VN, auto_close=True)
sub_client.req_pricedepth("btcusdt", DepthStep.STEP0, callback, error)
