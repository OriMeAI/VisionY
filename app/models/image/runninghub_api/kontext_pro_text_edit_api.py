"""
https://www.runninghub.cn/workflow/1944764695859351553

根据提示词对原图进行重绘，用的是flux kontext pro

"""

def get_workflow_api(seed,aspect_ratio,image_prompt,base_image):
  return {    
          "extra_credits":2, 
          "need_parse_url":True,
          "workflowId":"1944764695859351553",
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
                "text": image_prompt
              },
              "class_type": "CR Text",
              "_meta": {
                "title": "文本"
              }
            },
            "3": {
              "inputs": {
                "prompt": [
                  "2",
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
                  "1",
                  0
                ]
              },
              "class_type": "RH_ComfyFluxKontext",
              "_meta": {
                "title": "RH ComfyFlux Kontext"
              }
            },
            "5": {
              "inputs": {
                "text": [
                  "3",
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



