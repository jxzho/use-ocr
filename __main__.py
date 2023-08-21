import pprint

import json

from paddleocr import PaddleOCR

import list_images

pp = pprint.PrettyPrinter(indent=5, depth=8)

ocr = PaddleOCR()

for image_path in list_images.get():
    results = ocr.ocr(image_path, det=True, rec=True, cls=False)

    for line in results:
        # line is <List>
        mapLine = map(
          lambda item: item[0],
          list(map(lambda item: item[1], line))
        )
        str_results = list(mapLine)
        print(json.dumps(str_results, indent=4, check_circular=True, ensure_ascii=False))
        print(''.join(str_results))