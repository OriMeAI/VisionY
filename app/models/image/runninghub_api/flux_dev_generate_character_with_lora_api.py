"""
https://www.runninghub.cn/workflow/1947949940761866241

用于角色生成。最后生成的是 576*1024大小的角色图片。
这样就不用在生成场景图的时间，单独拼装角色图片了。
extra_credits 是额外费用，不在计费中返回

如果能找到lora_name，就用flux1.dev,如果找不到就用 flux kontext dev

"""
import logging

style_Lora_List = {
  "Flat Japanese Anime Style":{
    "lora_name":"AnimePainting l 二次元-F.1_v1.0.safetensors",
    "trigger_word":"Anime-style"
  },
  "Origami Style":{
    "lora_name":"立体折纸艺术_立体折纸艺术_1.safetensors",
    "trigger_word":"paper style"
  },
  "3D Cartoon Style":{
    "lora_name":"皮克斯动画_Pixar_3D卡通动漫_v1.0.safetensors",
    "trigger_word":"Pixar 3D Cartoon"
  },
  "JoJo Style":{
    "lora_name":"JOJOFantasia l JOJO风格-FLUX_动漫风格_v1.0.safetensors",
    "trigger_word":"JOJO stylized comic book-style"
  },
  "Ukiyo-e Style":{
    "lora_name":"可爱复古浮世绘风格_v1.0.safetensors",
    "trigger_word":"Ukiyo-e style"
  },
  "3D Realistic Style":{
    "lora_name":"F.1多场景风格3D写实小说推文，多风格场景和画风_F.1通用多风格v1.0.safetensors",
    "trigger_word":"3D Realistic style"
  },
  "Colored Crayon Style":{
    "lora_name":"Colored_pen_doodle.safetensors",
    "trigger_word":"kdacbty style"
  },
  "Studio Ghibli Style":{
    "lora_name":"Flux宫崎骏吉卜力动漫美学风格_V1.0.safetensors",
    "trigger_word":"Studio Ghibli style"
  },
  "Pencil Sketch Style":{
    "lora_name":"pencilSketch_FLUX.safetensors",
    "trigger_word":"Pencil Sketch style"
  },
}

def get_workflow_api(seed,image_style, image_prompt,width,height):
  
  lora_info = style_Lora_List.get(image_style,"")
  
  if not lora_info:
    logging.info(f"Can not find lora_name for style_name:{image_style}")

    lora_name = "3D卡通人物_职场人物_v1.0.safetensors",
    trigger_word = "3D Cartoon style"
  else:
    lora_name = lora_info["lora_name"]
    trigger_word = lora_info["trigger_word"]
    
  image_prompt = f"{trigger_word}, {image_prompt}"
  return {    
          "extra_credits":0,
          "need_parse_url":False,
          "workflowId":"1947949940761866241",
          "workflow": {
            "1": {
              "inputs": {
                "clip_name1": "clip_l.safetensors",
                "clip_name2": "t5xxl_fp8_e4m3fn.safetensors",
                "type": "flux",
                "device": "default"
              },
              "class_type": "DualCLIPLoader",
              "_meta": {
                "title": "双CLIP加载器"
              }
            },
            "2": {
              "inputs": {
                "unet_name": "flux1-dev-fp8.safetensors",
                "weight_dtype": "fp8_e4m3fn"
              },
              "class_type": "UNETLoader",
              "_meta": {
                "title": "UNET加载器"
              }
            },
            "3": {
              "inputs": {
                "text": image_prompt,
                "clip": [
                  "1",
                  0
                ]
              },
              "class_type": "CLIPTextEncode",
              "_meta": {
                "title": "CLIP文本编码器"
              }
            },
            "4": {
              "inputs": {
                "guidance": 4.5,
                "conditioning": [
                  "3",
                  0
                ]
              },
              "class_type": "FluxGuidance",
              "_meta": {
                "title": "Flux引导"
              }
            },
            "5": {
              "inputs": {
                "conditioning": [
                  "3",
                  0
                ]
              },
              "class_type": "ConditioningZeroOut",
              "_meta": {
                "title": "条件零化"
              }
            },
            "6": {
              "inputs": {
                "seed": seed,
                "steps": 20,
                "cfg": 1,
                "sampler_name": "euler",
                "scheduler": "simple",
                "denoise": 1,
                "model": [
                  "24",
                  0
                ],
                "positive": [
                  "4",
                  0
                ],
                "negative": [
                  "5",
                  0
                ],
                "latent_image": [
                  "9",
                  0
                ]
              },
              "class_type": "KSampler",
              "_meta": {
                "title": "K采样器"
              }
            },
            "9": {
              "inputs": {
                "width": width,
                "height": height,
                "batch_size": 1
              },
              "class_type": "EmptyLatentImage",
              "_meta": {
                "title": "空Latent"
              }
            },
            "10": {
              "inputs": {
                "vae_name": "ae.safetensors"
              },
              "class_type": "VAELoader",
              "_meta": {
                "title": "VAE加载器"
              }
            },
            "12": {
              "inputs": {
                "samples": [
                  "6",
                  0
                ],
                "vae": [
                  "10",
                  0
                ]
              },
              "class_type": "VAEDecode",
              "_meta": {
                "title": "VAE解码"
              }
            },
            "15": {
              "inputs": {
                "filename_prefix": "Flux",
                "save_image": True,
                "include_workflow": False,
                "images": [
                  "25",
                  0
                ]
              },
              "class_type": "Save Image w/o Metadata",
              "_meta": {
                "title": "Save Image w/o Metadata"
              }
            },
            "16": {
              "inputs": {
                "image": [
                  "12",
                  0
                ]
              },
              "class_type": "GetImageSize",
              "_meta": {
                "title": "获取图像尺寸"
              }
            },
            "17": {
              "inputs": {
                "expression": "1024-a",
                "a": [
                  "16",
                  1
                ]
              },
              "class_type": "MathExpression|pysssss",
              "_meta": {
                "title": "数学表达式"
              }
            },
            "24": {
              "inputs": {
                "lora_name": lora_name,
                "strength_model": 1,
                "model": [
                  "2",
                  0
                ]
              },
              "class_type": "LoraLoaderModelOnly",
              "_meta": {
                "title": "LoRA加载器(仅模型)"
              }
            },
            "25": {
              "inputs": {
                "invert_mask": False,
                "top": [
                  "17",
                  0
                ],
                "bottom": 0,
                "left": 0,
                "right": 0,
                "color": "#ffffff",
                "image": [
                  "12",
                  0
                ]
              },
              "class_type": "LayerUtility: ExtendCanvas",
              "_meta": {
                "title": "扩展画布"
              }
            }
          }
  }


