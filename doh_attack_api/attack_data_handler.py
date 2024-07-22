import pandas as pd
# from doh_attack.serializer import *


def handler():
    datasets = pd.read_csv('../doh_attack/attack_data.csv')
    for index, row in datasets.iterrows():
        print(f"Index: {index}")
        print(f"Row data: {row}")
        print()  # 打印空行分隔每一行的输出


if __name__ == '__main__':
    handler()
