#from codecs import make_identity_dict

from PIL import Image
import numpy as np
from scipy.ndimage import gaussian_filter
import matplotlib.pyplot as plt
import os

import time
from scipy.sparse import block_array
import traceback
import dilation
import log
import tkinter as tk


def get_mask_and_related_files_dict(directory):
    result = {}  # 存储结果字典

    # 遍历目录，找到所有包含"Mask"的文件
    for root, _, files in os.walk(directory):
        for file in files:
            if "Mask" in file:  # 检查文件名是否包含"Mask"
                full_mask_path = os.path.join(root, file)
                prefix = file.split("Mask")[0]  # 提取前缀

                # 初始化字典，键为Mask文件，值为一个列表
                result[full_mask_path] = []

                # 查找所有以该前缀开头的文件
                for related_file in files:
                    if related_file.startswith(prefix) and related_file != file:
                        result[full_mask_path].append(os.path.join(root, related_file))

    return result

if __name__ == '__main__':
    # 示例用法
    path = "./"
    outputPath = './output/'
    file_mapping = get_mask_and_related_files_dict(path)

    # 打印结果
    for mask_file, related_files in file_mapping.items():
        # with open('log.txt', 'w') as f:
            log.log(f"Mask file: {mask_file}\n")
            log.log(f"related image: {related_files}\n")
            log.log("\n")

    blockRange = 10

    for mask_file, related_files in file_mapping.items():
        dilation.dilation(mask_file, related_files, blockRange, outputPath)

    # plt.imshow(output)
    # plt.axis('off')
    # plt.show()
