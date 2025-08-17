"""
https://www.runninghub.cn/workflow/1950413130867326977

依据角色的立绘图生成场景图的工作流

"""
def get_workflow_api(seed,aspect_ratio,image_prompt):
  return {   
          "extra_credits":2, 
          "need_parse_url":True,
          "workflowId":"1950413130867326977",
          "workflow":{
            "6": {
              "inputs": {
                "prompt": [
                  "7",
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
                "only_output_image_urls": True
              },
              "class_type": "RH_ComfyFluxKontext",
              "_meta": {
                "title": "RH ComfyFlux Kontext"
              }
            },
            "7": {
              "inputs": {
                "text": image_prompt
                },
              "class_type": "CR Text",
              "_meta": {
                "title": "文本"
              }
            },
            "12": {
              "inputs": {
                "text": [
                  "6",
                  1
                ],
                "output_file_path": "",
                "file_name": "",
                "file_extension": "txt",
                "overwrite": False
              },
              "class_type": "easy saveText",
              "_meta": {
                "title": "Save Text"
              }
            }
          }
  }



