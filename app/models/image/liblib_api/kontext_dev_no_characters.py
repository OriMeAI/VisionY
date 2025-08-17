"""
https://www.liblib.art/apis/workflow?uuid=cdccb825553c4de486956975f47117b8&modelInfoPath=792c3b3fe8a3420e9c61169cda43ae86&from=personal_page

无角色，根据提示词生成场景图

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
        "workflowUuid": "cdccb825553c4de486956975f47117b8"
    }
}
    