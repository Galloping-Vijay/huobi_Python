from huobi.connection import RestApiSyncClient
from huobi.constant import *
from huobi.model.trade import *
from huobi.utils import *


class GetOrderByIdService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        order_id = self.params["order_id"]
        def get_channel():
            path = "/v1/order/orders/{}"
            return path.format(order_id)

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, Order, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, get_channel(), self.params, parse)






