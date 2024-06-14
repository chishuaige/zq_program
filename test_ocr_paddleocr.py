from paddleocr import PaddleOCR, draw_ocr
import time

start_t = time.time()
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch", use_gpu=True)  # need to run only once to download and load model into memory
print(time.time() - start_t)
img_path = './imgs/test1.png'
result = ocr.ocr(img_path, cls=True)
# 显示结果
from PIL import Image

result = result[0]
# image = Image.open(img_path).convert('RGB')
# boxes = [line[0] for line in result]
res_list = [line[1][0] for line in result]
print('res_list', res_list)
end_t = time.time()
print(end_t - start_t)


# 8*4车型
# 6*4车型

# =======================================莱芜工厂 start=======================================================
def get_double_axle_param_laiwu(res_list):
    # 车辆识别号
    vin = res_list[res_list.index('Vin') + 1]
    # 类型
    vtype = res_list[res_list.index('类型：') + 1]
    # 车桥偏移
    S = res_list[res_list.index('方向盘水平仪') + 1]
    # 一桥前束和
    T1 = res_list[res_list.index('前束和') + 1]
    # 二桥前束和
    first_position = res_list.index('前束和')
    second_position = res_list.index('前束和', first_position + 1)
    T2 = res_list[second_position + 1]
    # 一桥平行度
    P13 = res_list[res_list.index('平行度') + 1]
    # 相对一桥平行度
    first_position = res_list.index('平行度')
    second_position = res_list.index('平行度', first_position + 1)
    P12 = res_list[second_position + 1]
    axle_param = {'axle_type': '双桥', 'vin': vin, 'vtype': vtype, 'S': S, 'T1': T1, 'T2': T2, 'P13': P13, 'P12': P12}
    return axle_param


def get_single_axle_param_laiwu(res_list):
    # 车辆识别号
    vin = res_list[res_list.index('Vin') + 1]
    # 类型
    vtype = res_list[res_list.index('类型：') + 1]
    # 车桥偏移
    S = res_list[res_list.index('方向盘水平仪') + 1]
    # 一桥前束和
    T1 = res_list[res_list.index('前束和') + 1]
    # 一桥平行度
    P13 = res_list[res_list.index('行驶角') + 1]
    axle_param = {'axle_type': '单桥', 'vin': vin, 'vtype': vtype, 'S': S, 'T1': T1, 'P13': P13}
    return axle_param


def get_result_laiwu(res_list):
    # 双桥
    if 'F1,F2轴' in res_list:
        axle_param = get_double_axle_param_laiwu(res_list)
    # 单桥
    else:
        axle_param = get_single_axle_param_laiwu(res_list)
    print(axle_param)
    return axle_param


# =======================================莱芜工厂 end=======================================================
get_result_laiwu(res_list)
# {'axle_type': '单桥', 'vin': 'RA153557', 'vtype': '4x2', 'S': '0.7', 'T1': '-0.74', 'P13': '5.75'}
# {'axle_type': '双桥', 'vin': 'RA152497', 'vtype': '6x2(2)', 'S': '-0.6', 'T1': '3.12', 'T2': '1.98', 'P13': '-6.21', 'P12': '19.50'}
