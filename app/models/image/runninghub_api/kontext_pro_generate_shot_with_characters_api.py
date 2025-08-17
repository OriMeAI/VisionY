"""
https://www.runninghub.cn/workflow/1950547977658093570

依据角色的立绘图生成场景图的工作流

"""
def get_workflow_api(seed,aspect_ratio,image_prompt,first_character,second_character,third_character):
  return {   
          "extra_credits":2, 
          "need_parse_url":True,
          "workflowId":"1950547977658093570",
          "workflow":{
            "1": {
              "inputs": {
                "image": first_character
              },
              "class_type": "LoadImage",
              "_meta": {
                "title": "加载图像"
              }
            },
            "2": {
              "inputs": {
                "image": second_character
              },
              "class_type": "LoadImage",
              "_meta": {
                "title": "加载图像"
              }
            },
            "3": {
              "inputs": {
                "image": third_character
              },
              "class_type": "LoadImage",
              "_meta": {
                "title": "加载图像"
              }
            },
            "4": {
              "inputs": {
                "direction": "right",
                "match_image_size": False,
                "image1": [
                  "1",
                  0
                ],
                "image2": [
                  "2",
                  0
                ]
              },
              "class_type": "easy imageConcat",
              "_meta": {
                "title": "图像联结"
              }
            },
            "5": {
              "inputs": {
                "direction": "right",
                "match_image_size": False,
                "image1": [
                  "4",
                  0
                ],
                "image2": [
                  "3",
                  0
                ]
              },
              "class_type": "easy imageConcat",
              "_meta": {
                "title": "图像联结"
              }
            },
            "6": {
              "inputs": {
                "prompt":image_prompt,
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
                  "5",
                  0
                ]
              },
              "class_type": "RH_ComfyFluxKontext",
              "_meta": {
                "title": "RH ComfyFlux Kontext"
              }
            },
            "8": {
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



