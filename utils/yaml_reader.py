# -*- coding: utf-8 -*-
# @__author__:choppa
# @DATA 2021/8/19
import yaml

from utils import dir_path


def read_yaml_data(yaml_dir):
    with open(yaml_dir, encoding='utf8') as fo:
        data = yaml.safe_load(fo.read())
        return data


if __name__ == '__main__':
    print(read_yaml_data(dir_path.yaml_dir)['LoginPage'])