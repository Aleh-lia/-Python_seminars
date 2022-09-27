from user_interface import choice
from main import data_processor
from data_provider import *


data = 'processing_model.csv'
user_list = data_processor(read_file(data), choice())
print(user_list)


write_file(user_list, mod='a')