"""
https://www.liblib.art/apis/workflow?uuid=378e75caeaf94370acb77d6fbf4940c0&modelInfoPath=7ab024d8ad78432b953c4cddd8b37f35&from=personal_page

生成角色图片

"""
import logging

style_Lora_List = {
  "Flat Japanese Anime Style":{
    "lora_name":"aa62500d35bf49148c4d0fe99ed1d0e3",
    "trigger_word":"Anime-style"
  },
  "Origami Style":{
    "lora_name":"ce7107e7163e4bb9b9b2d828ef056d28",
    "trigger_word":"paper style"
  },
  "3D Cartoon Style":{
    "lora_name":"b676ff5e50354fb7bf8964a513f9441b",
    "trigger_word":"3D Cartoon style"
  },
  "JoJo Style":{
    "lora_name":"b676ff5e50354fb7bf8964a513f9441b",
    "trigger_word":"JOJO stylized comic book-style"
  },
  "Ukiyo-e Style":{
    "lora_name":"8813d20d04394669974ccc4d7f7b0b8a",
    "trigger_word":"Ukiyo-e style"
  },
  "3D Realistic Style":{
    "lora_name":"8de072c35f984ce595949df93512cb28",
    "trigger_word":"3D Realistic style"
  },
  "Colored Crayon Style":{
    "lora_name":"19fd345ffbe948ad9e0d6d6d23d120d9",
    "trigger_word":"kdacbty style"
  },
  "Studio Ghibli Style":{
    "lora_name":"aa88cca502d8401ea64119dca696e0e0",
    "trigger_word":"Studio Ghibli style"
  },
  "Pencil Sketch Style":{
    "lora_name":"7a9d0549dfd144c281ea928366cc18bd",
    "trigger_word":"Pencil Sketch style"
  },
}


def get_workflow_api(seed,image_style,width,height,image_prompt):
    
    lora_info = style_Lora_List.get(image_style,"")
    
    if not lora_info:
        logging.info(f"Can not find lora_name for style_name:{image_style}")

        lora_name = "aa62500d35bf49148c4d0fe99ed1d0e3",
        trigger_word = "Anime-style"
    else:
        lora_name = lora_info["lora_name"]
        trigger_word = lora_info["trigger_word"]
        
    image_prompt = f"{trigger_word}. {image_prompt}"
    
    return {
    "templateUuid": "4df2efa0f18d46dc9758803e478eb51c",
    "generateParams": {
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "seed": seed
            }
        },
        "5": {
            "class_type": "EmptyLatentImage",
            "inputs": {
                "width": width,
                "height": height
            }
        },
        "6": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": image_prompt
            }
        },
        "11": {
            "class_type": "FluxGuidance",
            "inputs": {
                "guidance": 4.5
            }
        },
        "19": {
            "class_type": "LoraLoaderModelOnly",
            "inputs": {
                "lora_name": lora_name
            }
        },
        "workflowUuid": "378e75caeaf94370acb77d6fbf4940c0"
    }
}
    
    