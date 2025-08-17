"""
https://www.runninghub.cn/workflow/1944752654247710721

根据原图和蒙版图进行局部重绘
"""

def get_workflow_api(seed,aspect_ratio,image_prompt,base_image,mask_image):
  return {    
          "extra_credits":2,
          "need_parse_url":True,
          "workflowId":"1944752654247710721",
          "workflow":{
            "1": {
              "inputs": {
                "image": base_image
              },
              "class_type": "LoadImage",
              "_meta": {
                "title": "加载图像"
              }
            },
            "2": {
              "inputs": {
                "image": mask_image
              },
              "class_type": "LoadImage",
              "_meta": {
                "title": "加载图像"
              }
            },
            "3": {
              "inputs": {
                "x": 0,
                "y": 0,
                "resize_source": True,
                "destination": [
                  "2",
                  0
                ],
                "source": [
                  "1",
                  0
                ],
                "mask": [
                  "2",
                  1
                ]
              },
              "class_type": "ImageCompositeMasked",
              "_meta": {
                "title": "图像遮罩复合"
              }
            },
            "4": {
              "inputs": {
                "prompt": [
                  "6",
                  0
                ],
                "model": "flux-kontext-pro",
                "apikey": "",
                "aspect_ratio": aspect_ratio,
                "num_of_images": 1,
                "seed": seed,
                "clear_image": True,
                "guidance_scale": 4.5,
                "api_provider": "bfl.ai",
                "output_format": "png",
                "prompt_upsampling": True,
                "safety_tolerance": 6,
                "only_output_image_urls": True,
                "input_image": [
                  "3",
                  0
                ]
              },
              "class_type": "RH_ComfyFluxKontext",
              "_meta": {
                "title": "RH ComfyFlux Kontext"
              }
            },
            "6": {
              "inputs": {
                "text": image_prompt
              },
              "class_type": "CR Text",
              "_meta": {
                "title": "文本"
              }
            },
            "9": {
              "inputs": {
                "text": [
                  "4",
                  1
                ],
                "output_file_path": "",
                "file_name": "",
                "file_extension": "txt",
                "overwrite": True
              },
              "class_type": "easy saveText",
              "_meta": {
                "title": "Save Text"
              }
            }
          }
  }




