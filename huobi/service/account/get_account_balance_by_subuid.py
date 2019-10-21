from huobi.connection import RestApiSyncClient
from huobi.constant.system import HttpMethod
from huobi.model.account import *
from huobi.utils import *



class GetAccountBalanceBySubUidService:

    def __init__(self, params):
        self.params = params

    def request(self, **kwargs):
        sub_uid = self.params["sub_uid"]

        def get_channel():
            path = "/v1/account/accounts/{}"
            return path.format(sub_uid)

        def parse(dict_data):
            data_list = dict_data.get("data", [])
            return default_parse_list_dict(data_list, Balance, [])

        return RestApiSyncClient(**kwargs).request_process(HttpMethod.GET_SIGN, get_channel(), self.params, parse)






