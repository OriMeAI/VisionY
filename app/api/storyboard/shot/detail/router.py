from fastapi import APIRouter
from fastapi.responses import JSONResponse

detail_router = APIRouter()

@detail_router.get('/detail')
async def operator():
    return JSONResponse(content={
        "code": 0,
        "data": [
            {
                "id": "1890191850984558593",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 2,
                "cellValue": "1",
                "cellValueType": "text",
                "storyBoardHeadName": "镜号"
            },
            {
                "id": "1890191850984558594",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 3,
                "cellValue": '{"image":"https://static.chuangyi-keji.com/generate_figure_images/c26472b272342af7/dfc26c3421a18902aa8eb5b8565f88bb.jpg?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,size_18,text_b25lc3RvcnkuYXJ0IEFJ55Sf5oiQ,color_FFFFFF,shadow_50,t_100,g_se,x_10,y_10","isHd": false}',
                "cellValueType": "image",
                "storyBoardHeadName": "画面"
            },
            {
                "id": "1890191850984558595",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 4,
                "cellValue": "",
                "cellValueType": "input",
                "storyBoardHeadName": "画面描述"
            },
            {
                "id": "1890191850984558596",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 5,
                "cellValue": "中景",
                "cellValueType": "select",
                "storyBoardHeadName": "景别"
            },
            {
                "id": "1890191850984558597",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 6,
                "cellValue": "1",
                "cellValueType": "input",
                "storyBoardHeadName": "时长"
            },
            {
                "id": "1890191850984558598",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 7,
                "cellValue": '[{"roleId":"1890191850774843394","figureName":"妮妮","mainFigureUrl":"https://static.chuangyi-keji.com/generate_figure_images/bb0d32a328ec7ba5a49994715ffd4fa7.jpg"}]',
                "cellValueType": "input",
                "storyBoardHeadName": "主要人物"
            },
            {
                "id": "1890191850984558599",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 9,
                "cellValue": "视平",
                "cellValueType": "select",
                "storyBoardHeadName": "机位角度"
            },
            {
                "id": "1890191850984558600",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 10,
                "cellValue": "旁白: 深夜里,妮妮拿着饭盒悄悄离开家门。",
                "cellValueType": "input",
                "storyBoardHeadName": "台词"
            },
            {
                "id": "1890191850984558601",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 13,
                "cellValue": "单人镜头",
                "cellValueType": "select",
                "storyBoardHeadName": "摄影机运动"
            },
            {
                "id": "1890191850984558602",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 158,
                "cellValue": '{"backgroundDetail":{"imgPrompts":"深夜的住宅门口","engPrompts":"(Medium shot),Clean Single,(()),,,The background is a residential doorway in the dead of night. The street is quiet and dimly lit by a streetlamp, casting long shadows and creating an atmosphere of secrecy and tranquility."}}',
                "cellValueType": "text",
                "storyBoardHeadName": "背景描述"
            },
            {
                "id": "1890191850984558603",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 159,
                "cellValue": '{"characterDetail":[{"imgPrompts":"拿着饭盒悄悄走路","engPrompts":"Walking stealthily, holding a meal box close to her chest, her expression is focused and cautious. She is positioned in the center of the frame, moving towards the doorway.","bboxCoords":[0.26953125,0.020833333333333332,0.697265625,1],"poseCoords":[],"name":"妮妮","roleId":"1890191850774843394","bboxModified":true}]}',
                "cellValueType": "text",
                "storyBoardHeadName": "角色描述"
            },
            {
                "id": "1890191850984558604",
                "storyboardId": "1890191850892283906",
                "storyBoardHeadId": 160,
                "cellValue": '{"otherDetail":[]}',
                "cellValueType": "text",
                "storyBoardHeadName": "其它描述"
            }
        ],
        "msg": ""
    })

# // export async function GET(request: Request) {
# //   return Response.json({
# //     code: 0,
# //     data: [
# //       {
# //         id: "1890191850984558593",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 2,
# //         cellValue: "1",
# //         cellValueType: "text",
# //         storyBoardHeadName: "镜号",
# //       },
# //       {
# //         id: "1890191850984558594",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 3,
# //         cellValue:
# //                 '{"image":"https://static.chuangyi-keji.com/generate_figure_images/c26472b272342af7/dfc26c3421a18902aa8eb5b8565f88bb.jpg?x-oss-process=image/watermark,type_d3F5LXplbmhlaQ,size_18,text_b25lc3RvcnkuYXJ0IEFJ55Sf5oiQ,color_FFFFFF,shadow_50,t_100,g_se,x_10,y_10","isHd": false}',
# //         cellValueType: "image",
# //         storyBoardHeadName: "画面",
# //       },
# //       {
# //         id: "1890191850984558595",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 4,
# //         cellValue: "",
# //         cellValueType: "input",
# //         storyBoardHeadName: "画面描述",
# //       },
# //       {
# //         id: "1890191850984558596",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 5,
# //         cellValue: "中景",
# //         cellValueType: "select",
# //         storyBoardHeadName: "景别",
# //       },
# //       {
# //         id: "1890191850984558597",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 6,
# //         cellValue: "1",
# //         cellValueType: "input",
# //         storyBoardHeadName: "时长",
# //       },
# //       {
# //         id: "1890191850984558598",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 7,
# //         cellValue:
# //           '[{"roleId":"1890191850774843394","figureName":"妮妮","mainFigureUrl":"https://static.chuangyi-keji.com/generate_figure_images/bb0d32a328ec7ba5a49994715ffd4fa7.jpg"}]',
# //         cellValueType: "input",
# //         storyBoardHeadName: "主要人物",
# //       },
# //       {
# //         id: "1890191850984558599",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 9,
# //         cellValue: "视平",
# //         cellValueType: "select",
# //         storyBoardHeadName: "摄像机角度",
# //       },
# //       {
# //         id: "1890191850984558600",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 10,
# //         cellValue: "旁白: 深夜里,妮妮拿着饭盒悄悄离开家门。",
# //         cellValueType: "input",
# //         storyBoardHeadName: "台词",
# //       },
# //       {
# //         id: "1890191850984558601",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 13,
# //         cellValue: "单人镜头",
# //         cellValueType: "select",
# //         storyBoardHeadName: "镜头类型",
# //       },
# //       {
# //         id: "1890191850984558602",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 158,
# //         cellValue:
# //           '{"backgroundDetail":{"imgPrompts":"深夜的住宅门口","engPrompts":"(Medium shot),Clean Single,(()),,,The background is a residential doorway in the dead of night. The street is quiet and dimly lit by a streetlamp, casting long shadows and creating an atmosphere of secrecy and tranquility."}}',
# //         cellValueType: "text",
# //         storyBoardHeadName: "背景描述",
# //       },
# //       {
# //         id: "1890191850984558603",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 159,
# //         cellValue:
# //           '{"characterDetail":[{"imgPrompts":"拿着饭盒悄悄走路","engPrompts":"Walking stealthily, holding a meal box close to her chest, her expression is focused and cautious. She is positioned in the center of the frame, moving towards the doorway.","bboxCoords":[0.26953125,0.020833333333333332,0.697265625,1],"poseCoords":[],"name":"妮妮","roleId":"1890191850774843394","bboxModified":true}]}',
# //         cellValueType: "text",
# //         storyBoardHeadName: "角色描述",
# //       },
# //       {
# //         id: "1890191850984558604",
# //         storyboardId: "1890191850892283906",
# //         storyBoardHeadId: 160,
# //         cellValue: '{"otherDetail":[]}',
# //         cellValueType: "text",
# //         storyBoardHeadName: "其它描述",
# //       },
# //     ],
# //     msg: "",
# //   });
# // }
