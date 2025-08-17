"""
https://www.liblib.art/apis/workflow?uuid=c1bc72b8ab0f4dd09f49eb2048a561ca&modelInfoPath=18118369cd224e62b5612db0a37f55fd&from=personal_page

生成角色图片

"""

def get_workflow_api(seed,width,height,image_prompt):
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
        "workflowUuid": "c1bc72b8ab0f4dd09f49eb2048a561ca"
    }
}
    
    