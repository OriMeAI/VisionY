"""
https://www.liblib.art/apis/workflow?uuid=cb8a3a3b96f94227a2db3f10abf9dddb&modelInfoPath=f2045f7fc7da4b6cb8ac8f7e6cc38e26&from=personal_page

基于文字修改图片内容

"""

def get_workflow_api(seed,image_prompt,base_image):
    return {
    "templateUuid": "4df2efa0f18d46dc9758803e478eb51c",
    "generateParams": {
        "3": {
            "class_type": "KSampler",
            "inputs": {
                "seed": seed
            }
        },
        "6": {
            "class_type": "CLIPTextEncode",
            "inputs": {
                "text": image_prompt
            }
        },
        "12": {
            "class_type": "LoadImage",
            "inputs": {
                "image": base_image
            }
        },
        "17": {
            "class_type": "FluxGuidance",
            "inputs": {
                "guidance": 4.5
            }
        },
        "workflowUuid": "cb8a3a3b96f94227a2db3f10abf9dddb"
    }
}
    