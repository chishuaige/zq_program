import subprocess
import rapidocr_onnxruntime
import os


res_list = os.system('rapidocr_onnxruntime -img ' + 'test1.png')
print('====')  # 输出命令结果
print('res_list', res_list)