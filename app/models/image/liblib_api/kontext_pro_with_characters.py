"""
https://www.liblib.art/apis/workflow?uuid=4e0afd73118b4b31b9fd46da368bf578&modelInfoPath=07a048fb817f4aeabd2c23e205a081e8&from=personal_page

基于角色生成场景图

"""

def get_workflow_api(seed,aspect_ratio,image_prompt,first_character,second_character,third_character):
    return {
    "templateUuid": "4df2efa0f18d46dc9758803e478eb51c",
    "generateParams": {
        "10": {
            "class_type": "FluxKontextProImageNode",
            "inputs": {
                "prompt": image_prompt,
                "guidance": 4.5,
                "seed": seed,
                "aspect_ratio": aspect_ratio
            }
        },
        "11": {
            "class_type": "LoadImage",
            "inputs": {
                "image": first_character
            }
        },
        "12": {
            "class_type": "LoadImage",
            "inputs": {
                "image": second_character
            }
        },
        "15": {
            "class_type": "LoadImage",
            "inputs": {
                "image": third_character
            }
        },
        "workflowUuid": "4e0afd73118b4b31b9fd46da368bf578"
    }
}
    
    