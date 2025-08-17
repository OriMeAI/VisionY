"""
https://www.runninghub.cn/workflow/1944926505325744129

对图片进行简单的2倍放大

"""

def get_workflow_api(seed,image_prompt,base_image):
  return {    
          "extra_credits":0,
          "need_parse_url":False,
          "workflowId":"1944926505325744129",
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
                  "model_name": "4x_NMKD-Siax_200k.pth"
                },
                "class_type": "UpscaleModelLoader",
                "_meta": {
                  "title": "放大模型加载器"
                }
              },
              "3": {
                "inputs": {
                  "width": 1280,
                  "height": 1280,
                  "upscale_method": "nearest-exact",
                  "keep_proportion": "resize",
                  "pad_color": "0, 0, 0",
                  "crop_position": "center",
                  "divisible_by": 8,
                  "device": "cpu",
                  "image": [
                    "1",
                    0
                  ]
                },
                "class_type": "ImageResizeKJv2",
                "_meta": {
                  "title": "Resize Image v2"
                }
              },
              "4": {
                "inputs": {
                  "upscale_model": [
                    "2",
                    0
                  ],
                  "image": [
                    "3",
                    0
                  ]
                },
                "class_type": "ImageUpscaleWithModel",
                "_meta": {
                  "title": "图像通过模型放大"
                }
              },
              "5": {
                "inputs": {
                  "upscale_method": "lanczos",
                  "megapixels": 4.0,
                  "image": [
                    "4",
                    0
                  ]
                },
                "class_type": "ImageScaleToTotalPixels",
                "_meta": {
                  "title": "图像按像素缩放"
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
              "7": {
                "inputs": {
                  "unet_name": "flux1-dev-kontext_fp8_scaled.safetensors",
                  "weight_dtype": "fp8_e4m3fn"
                },
                "class_type": "UNETLoader",
                "_meta": {
                  "title": "UNET加载器"
                }
              },
              "8": {
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
              "9": {
                "inputs": {
                  "guidance": 4.5,
                  "conditioning": [
                    "8",
                    0
                  ]
                },
                "class_type": "FluxGuidance",
                "_meta": {
                  "title": "Flux引导"
                }
              },
              "10": {
                "inputs": {
                  "conditioning": [
                    "8",
                    0
                  ]
                },
                "class_type": "ConditioningZeroOut",
                "_meta": {
                  "title": "条件零化"
                }
              },
              "11": {
                "inputs": {
                  "seed": seed,
                  "steps": 6,
                  "cfg": 1,
                  "sampler_name": "euler",
                  "scheduler": "normal",
                  "denoise": 0.18,
                  "model": [
                    "7",
                    0
                  ],
                  "positive": [
                    "9",
                    0
                  ],
                  "negative": [
                    "10",
                    0
                  ],
                  "latent_image": [
                    "13",
                    0
                  ]
                },
                "class_type": "KSampler",
                "_meta": {
                  "title": "K采样器"
                }
              },
              "12": {
                "inputs": {
                  "vae_name": "ae.safetensors"
                },
                "class_type": "VAELoader",
                "_meta": {
                  "title": "VAE加载器"
                }
              },
              "13": {
                "inputs": {
                  "pixels": [
                    "16",
                    0
                  ],
                  "vae": [
                    "12",
                    0
                  ]
                },
                "class_type": "VAEEncode",
                "_meta": {
                  "title": "VAE编码"
                }
              },
              "14": {
                "inputs": {
                  "width_factor": 2,
                  "height_factor": 3,
                  "overlap_rate": 0.05,
                  "image": [
                    "5",
                    0
                  ]
                },
                "class_type": "TTP_Tile_image_size",
                "_meta": {
                  "title": "TTP_Tile_image_size"
                }
              },
              "15": {
                "inputs": {
                  "tile_width": [
                    "14",
                    0
                  ],
                  "tile_height": [
                    "14",
                    1
                  ],
                  "image": [
                    "5",
                    0
                  ]
                },
                "class_type": "TTP_Image_Tile_Batch",
                "_meta": {
                  "title": "TTP_Image_Tile_Batch"
                }
              },
              "16": {
                "inputs": {
                  "image": [
                    "15",
                    0
                  ]
                },
                "class_type": "ImpactImageBatchToImageList",
                "_meta": {
                  "title": "图像批次到图像列表"
                }
              },
              "17": {
                "inputs": {
                  "padding": 128,
                  "tiles": [
                    "19",
                    0
                  ],
                  "positions": [
                    "15",
                    1
                  ],
                  "original_size": [
                    "15",
                    2
                  ],
                  "grid_size": [
                    "15",
                    3
                  ]
                },
                "class_type": "TTP_Image_Assy",
                "_meta": {
                  "title": "TTP_Image_Assy"
                }
              },
              "18": {
                "inputs": {
                  "tile_size": 1024,
                  "overlap": 64,
                  "temporal_size": 64,
                  "temporal_overlap": 8,
                  "samples": [
                    "11",
                    0
                  ],
                  "vae": [
                    "12",
                    0
                  ]
                },
                "class_type": "VAEDecodeTiled",
                "_meta": {
                  "title": "VAE分块解码"
                }
              },
              "19": {
                "inputs": {
                  "images": [
                    "18",
                    0
                  ]
                },
                "class_type": "ImageListToImageBatch",
                "_meta": {
                  "title": "图像列表到图像批次"
                }
              },
              "20": {
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