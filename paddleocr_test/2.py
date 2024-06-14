from paddleocr import PaddleOCR, draw_ocr
import time
start_t = time.time()
# Paddleocr目前支持的多语言语种可以通过修改lang参数进行切换
# 例如`ch`, `en`, `fr`, `german`, `korean`, `japan`
ocr = PaddleOCR(use_angle_cls=True, lang="ch")  # need to run only once to download and load model into memory
img_path = './imgs/test1.png'
result = ocr.ocr(img_path, cls=True)
for idx in range(len(result)):
    res = result[idx]
    # for line in res:
    #     print(line)
# txts = [line[1][0] for line in result]
# print('txts', txts)


# 显示结果
from PIL import Image
result = result[0]
image = Image.open(img_path).convert('RGB')
boxes = [line[0] for line in result]
res_list = [line[1][0] for line in result]
print('res_list', res_list)
end_t = time.time()
print(end_t-start_t)
# 8*4车型    对应f1轴和f2轴 有两个前束




# 6*4车型    对应f1轴  有一个前束



