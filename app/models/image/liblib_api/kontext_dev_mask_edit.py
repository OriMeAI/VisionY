"""
https://www.liblib.art/apis/workflow?uuid=de7f5c1ebbca4c01bd51ee731af7372c&modelInfoPath=793ed6b2861848c0868b27ff75f80c9c&from=personal_page

基于蒙版修改图片内容

"""

def get_workflow_api(seed,image_prompt,base_image,mask_image):
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
                "image": base_image
            }
        },
        "18": {
            "class_type": "FluxGuidance",
            "inputs": {
                "guidance": 4.5
            }
        },
        "37": {
            "class_type": "LoadImage",
            "inputs": {
                "image": mask_image
            }
        },
        "workflowUuid": "de7f5c1ebbca4c01bd51ee731af7372c"
    }
}
    