"""
https://www.runninghub.cn/workflow/1944590849630195714

纯粹靠风格化文字描述来生成风格化图片，用于角色生成。最后生成的是 576*1024大小的角色图片。
这样就不用在生成场景图的时间，单独拼装角色图片了。
extra_credits 是额外费用，不在计费中返回

"""

def get_workflow_api(seed,image_prompt,width,height):
  return {    
          "extra_credits":0,
          "need_parse_url":False,
          "workflowId":"1944590849630195714",
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
                "unet_name": "flux1-dev-kontext_fp8_scaled.safetensors",
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
                  "2",
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
                  "18",
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
            "18": {
              "inputs": {
                "invert_mask": False,
                "top": [
                  "17",
                  0
                ],
                "bottom": 0,
                "left": 0,
                "right": 0,
                "image": [
                  "12",
                  0
                ],
                "color": [
                  "20",
                  0
                ]
              },
              "class_type": "LayerUtility: ExtendCanvas",
              "_meta": {
                "title": "扩展画布"
              }
            },
            "20": {
              "inputs": {
                "hex": "#FFFFFF"
              },
              "class_type": "Color (hexadecimal)",
              "_meta": {
                "title": "Color (hexadecimal)"
              }
            }
          }
  }


