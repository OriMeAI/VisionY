"""
获取场景图片的尺寸

符合标准尺寸的比率关系
    # def get_aspect_ratio(self,size):
    #     #解析 aspect_ratio
    #     if size == "1024x1024":
    #         aspect_ratio = "1:1"
    #     elif size == "1344x768":
    #         aspect_ratio = "16:9"
    #     elif size == "1152x896":
    #         aspect_ratio = "4:3"
    #     elif size == "1216x832":
    #         aspect_ratio = "3:2"
    #     elif size == "832x1216":
    #         aspect_ratio = "2:3"
    #     elif size == "896x1152":
    #         aspect_ratio = "3:4"
    #     elif size == "768x1344":
    #         aspect_ratio = "9:16"
    #     else:
    #         aspect_ratio = "9:16"
    #     return aspect_ratio


"""

IMAGE_SIZE_LIST = [
    {
      "id": 1,
      "label": "1:1",
      "value": "1:1",
      "className": "w-6 h-6",
      "tip": "1024x1024",
      "imgWidth": 1024,
      "imgHeight": 1024,
    },
    {
      "id": 2,
      "label": "16:9",
      "value": "16:9",
      "className": "w-6 h-3.5",
      "tip": "1344x768",
      "imgWidth": 1344,
      "imgHeight": 768,
    },
    {
      "id": 3,
      "label": "4:3",
      "value": "4:3",
      "className": "w-6 h-[18px]",
      "tip": "1152x896",
      "imgWidth": 1152,
      "imgHeight": 896,
    },
    {
      "id": 4,
      "label": "3:2",
      "value": "3:2",
      "className": "w-6 h-4",
      "tip": "1216x832",
      "imgWidth": 1216,
      "imgHeight": 832,
    },
    {
      "id": 5,
      "label": "2:3",
      "value": "2:3",
      "className": "w-4 h-6",       
      "tip": "832x1216",
      "imgWidth": 832,
      "imgHeight": 1216,
    },
    {
      "id": 6,
      "label": "3:4",
      "value": "3:4",
      "className": "w-[18px] h-6",
      "tip": "896x1152",
      "imgWidth": 896,
      "imgHeight": 1152,
    },
    {
      "id": 7,
      "label": "9:16",
      "value": "9:16",
      "className": "w-3.5 h-6",
      "tip": "768x1344",
      "imgWidth": 768,
      "imgHeight": 1344,
    },
]

def get_project_image_size_list():
    """
    获取尺寸列表
    :return:
    """
    return IMAGE_SIZE_LIST