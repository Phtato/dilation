# 加载图像
from PIL import Image
import numpy as np
import os
import log

def dilation( Mask, image_names, block_range, outputPath):
    #mask_np = np.array(Mask)
    #mask = mask_np > 0
    if not os.path.exists(outputPath):
        os.makedirs(outputPath)
    for image_name in image_names:
        image = Image.open(image_name).convert("RGB")
        log.log("打开文件 " + image_name + " 应该是成了")
        im = np.array(image)

        half_block_length = 3
        block_length = half_block_length * 2

        output = np.zeros_like(im)
        for x in range(1, im.shape[0] - 1):
            for y in range(1, im.shape[1] - 1):
                # 如果当前像素不为 (0, 0, 0)
                if np.all(im[x, y] == 0):
                    # 提取 3x3 邻域窗口
                    neighborhood = im[x - block_range:x + block_range, y - block_range:y + block_range]
                    # 筛选非 (0, 0, 0) 的像素
                    non_zero_pixels = neighborhood[np.any(neighborhood != [0, 0, 0], axis=-1)]
                    # 如果有非零像素，计算均值
                    if non_zero_pixels.size > 0:
                        output[x, y] = np.mean(non_zero_pixels, axis=0)
                else:
                    output[x, y] = im[x, y]
        im = Image.fromarray(output)
        log.log("导出文件 " + image_name + " 中")
        im.save(outputPath + image_name)