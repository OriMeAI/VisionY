"""
https://www.liblib.art/apis/workflow?uuid=6d1e6c57f6ee4ca790e4d9e2e1654441&modelInfoPath=90951d88e81043ec8f68ceb967d28f12&from=personal_page

简单的图像放大

"""

def get_workflow_api(seed,image_prompt,image_url):
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
        "10": {
            "class_type": "LoadImage",
            "inputs": {
                "image": image_url
            }
        },
        "18": {
            "class_type": "FluxGuidance",
            "inputs": {
                "guidance": 4.5
            }
        },
        "workflowUuid": "6d1e6c57f6ee4ca790e4d9e2e1654441"
    }
}
    