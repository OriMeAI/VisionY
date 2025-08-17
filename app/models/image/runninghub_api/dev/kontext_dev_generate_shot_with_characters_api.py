"""
https://www.runninghub.cn/workflow/1946142520205033473

依据角色的立绘图生成场景图的工作流

"""

def get_workflow_api(seed,width,height,image_prompt,first_character,second_character,third_character):
  return {   
          "extra_credits":0, 
          "need_parse_url":False,
          "workflowId":"1946142520205033473",
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
                "8": {
                  "inputs": {
                    "unet_name": "flux1-dev-kontext_fp8_scaled.safetensors",
                    "weight_dtype": "fp8_e4m3fn"
                  },
                  "class_type": "UNETLoader",
                  "_meta": {
                    "title": "UNET加载器"
                  }
                },
                "9": {
                  "inputs": {
                    "text": image_prompt,
                    "clip": [
                      "6",
                      0
                    ]
                  },
                  "class_type": "CLIPTextEncode",
                  "_meta": {
                    "title": "CLIP文本编码器"
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
                "11": {
                  "inputs": {
                    "pixels": [
                      "5",
                      0
                    ],
                    "vae": [
                      "10",
                      0
                    ]
                  },
                  "class_type": "VAEEncode",
                  "_meta": {
                    "title": "VAE编码"
                  }
                },
                "12": {
                  "inputs": {
                    "conditioning": [
                      "9",
                      0
                    ],
                    "latent": [
                      "11",
                      0
                    ]
                  },
                  "class_type": "ReferenceLatent",
                  "_meta": {
                    "title": "ReferenceLatent"
                  }
                },
                "13": {
                  "inputs": {
                    "conditioning": [
                      "9",
                      0
                    ]
                  },
                  "class_type": "ConditioningZeroOut",
                  "_meta": {
                    "title": "条件零化"
                  }
                },
                "14": {
                  "inputs": {
                    "guidance": 4.5,
                    "conditioning": [
                      "12",
                      0
                    ]
                  },
                  "class_type": "FluxGuidance",
                  "_meta": {
                    "title": "Flux引导"
                  }
                },
                "15": {
                  "inputs": {
                    "seed": seed,
                    "steps": 20,
                    "cfg": 1,
                    "sampler_name": "euler",
                    "scheduler": "simple",
                    "denoise": 1,
                    "model": [
                      "8",
                      0
                    ],
                    "positive": [
                      "14",
                      0
                    ],
                    "negative": [
                      "13",
                      0
                    ],
                    "latent_image": [
                      "16",
                      0
                    ]
                  },
                  "class_type": "KSampler",
                  "_meta": {
                    "title": "K采样器"
                  }
                },
                "16": {
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
                "17": {
                  "inputs": {
                    "samples": [
                      "15",
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
                "18": {
                  "inputs": {
                    "filename_prefix": "ComfyUI",
                    "save_image": True,
                    "include_workflow": False,
                    "images": [
                      "17",
                      0
                    ]
                  },
                  "class_type": "Save Image w/o Metadata",
                  "_meta": {
                    "title": "Save Image w/o Metadata"
                  }
                }
              }
  }



