"""
https://www.liblib.art/apis/workflow?uuid=88dfb71b23294cecaa1c05cc67eae164&modelInfoPath=32b0db0127974766934957286195b4c6&from=personal_page

基于角色生成场景图

"""

def get_workflow_api(seed,aspect_ratio,image_prompt):
    return {
    "templateUuid": "4df2efa0f18d46dc9758803e478eb51c",
    "generateParams": {
        "10": {
            "class_type": "FluxKontextProImageNode",
            "inputs": {
                "seed": seed,
                "guidance": 4.5,
                "prompt": image_prompt,
                "aspect_ratio": aspect_ratio
            }
        },
        "workflowUuid": "88dfb71b23294cecaa1c05cc67eae164"
    }
}
    
    