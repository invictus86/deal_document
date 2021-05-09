import json
from cz_jiaoxie.dict_data_file import dict_data_all


def write_json_file(file_path, load_dict):
    """
    write json file from file path
    :param file_path:the path of file
    :param load_dict:dict data you want to write
    :return:
    """
    with open(file_path, "w") as dump_f:
        json.dump(load_dict, dump_f)


def read_json_file(file_path):
    """
    read json file from file path
    :param file_path:
    :return:
    """
    with open(file_path, 'r') as load_f:
        load_dict = json.load(load_f)
    return load_dict


# load_dict_0 = read_json_file("./jiaoxue.json")
# load_dict_1 = read_json_file("./jiaoxue1.json")
load_dict_800000 = read_json_file("./jiaoxue_800000.json")
load_dict_800001 = read_json_file("./jiaoxue_800001.json")
load_dict_800002 = read_json_file("./jiaoxue_800002.json")
load_dict_900000 = read_json_file("./jiaoxue_900000.json")
# load_dict_900001 = read_json_file("./jiaoxue_900001.json")
load_dict_1000000 = read_json_file("./jiaoxue_1000000.json")
load_dict_1000001 = read_json_file("./jiaoxue_1000001.json")
load_dict_1100000 = read_json_file("./jiaoxue_1100000.json")
load_dict_1200000 = read_json_file("./jiaoxue_1200000.json")
load_dict_1200001 = read_json_file("./jiaoxue_1200001.json")
load_dict_1300000 = read_json_file("./jiaoxue_1300000.json")
load_dict_1400000 = read_json_file("./jiaoxue_1400000.json")

all_data = load_dict_800000.get("down_list") + load_dict_800001.get("down_list") + load_dict_800002.get(
    "down_list") + load_dict_900000.get("down_list") + load_dict_1000000.get(
    "down_list") + load_dict_1000001.get("down_list") + load_dict_1100000.get("down_list") + load_dict_1200000.get(
    "down_list") + load_dict_1200001.get("down_list") + load_dict_1300000.get("down_list") + load_dict_1400000.get(
    "down_list")
print(len(all_data))

# list_new_data = []
# for data in all_data:
#     list_new_data.append(data[0])
# # print(all_data)
# print(len(list_new_data))
# new_list = list(set(list_new_data))
# print(len(new_list))


all_dict_data = {"down_list": all_data}
write_json_file("./jiaoxue_all_800000.json", all_dict_data)

# dict_data = read_json_file("./jiaoxue_all_800000.json")
# print(dict_data)
# print(len(dict_data.get("down_list")))
