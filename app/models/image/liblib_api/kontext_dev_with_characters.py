"""
https://www.liblib.art/apis/workflow?uuid=e15ea957f0064263937a3647b8fb82fe&modelInfoPath=7fb8d28083534ac78e34d994c1788503&from=personal_page

基于角色生成场景图

"""

def get_workflow_api(seed,width,height,image_prompt,first_character,second_character,third_character):
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
        "10": {
            "class_type": "LoadImage",
            "inputs": {
                "image": first_character
            }
        },
        "11": {
            "class_type": "LoadImage",
            "inputs": {
                "image": second_character
            }
        },
        "12": {
            "class_type": "LoadImage",
            "inputs": {
                "image": third_character
            }
        },
        "21": {
            "class_type": "FluxGuidance",
            "inputs": {
                "guidance": 4.5
            }
        },
        "workflowUuid": "e15ea957f0064263937a3647b8fb82fe"
    }
}
    
    