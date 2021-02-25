from huobi.client.generic import GenericClient
from huobi.utils import *

generic_client = GenericClient()
list_obj = generic_client.get_exchange_symbols()
print(list_obj)