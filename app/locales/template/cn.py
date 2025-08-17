def get_project_template_item():
    return ProjectTemplate

def get_project_description_item(template_id: str):
    item = ProjectDescription.get(template_id, {})
    return item

def get_project_role_item(template_id: str):
    item = ProjectRole.get(template_id, [])
    return item

def get_project_shot_item(template_id: str):
    item = ProjectShot.get(template_id, {})
    return item

ProjectTemplate = [
        {
            "id": "10011",
            "storyBoardType": "平涂日漫",
            "coverTitle": "平涂日漫",
            "cover": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
            "name": "晨光中的选择",
            "intro": "2087年，人工智能已经深度融入人类生活。艾拉是一名记忆设计师，她的工作是为客户定制和修改记忆。今天，她面临着一个改变人生的选择。",
            "updateTime": "2024-12-05 19:06:10"            
        },
        {
            "id": "10012",
            "storyBoardType": "3D卡通",
            "coverTitle": "3D卡通",
            "cover": "https://resource.visiony.cc/image/1754380736917-xskrud.png",
            "name": "天照大神与八岐大蛇",
            "intro": "在日本古代神话中，素戋呜尊因为杀死了八岐大蛇而拯救了奇稻田姬，并从蛇尾中得到了草薙剑，最终与天照大神和解的传奇故事。",
            "updateTime": "2024-12-05 19:06:10"
        },
        {
            "id": "10013",
            "storyBoardType": "折纸",
            "coverTitle": "折纸",
            "cover": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
            "name": "雨夜咖啡馆",
            "intro": "在一个雨夜，一家温馨的咖啡馆里发生了一个关于重逢、原谅和新开始的故事。",
            "updateTime": "2024-12-05 19:06:10"
        },
        {
            "id": "10014",
            "storyBoardType": "3D真实",
            "coverTitle": "3D真实", 
            "cover": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
            "name": "白荆骑士与风息之心",
            "intro": "在中世纪北方王国莱文堡，漫长的寒冬带来饥饿与绝望。传说只有位于幽冥谷深处的风息之心能化解寒冬，但百年来没有人能从那里生还。",
            "updateTime": "2024-12-05 19:06:10"
        },
]

ProjectDescription = {
    "10011":{
        "id": "10011",        
        "name": "晨光中的选择",
        "language": "zh-CN",
        "type": 0,
        "storyBoardType": 0,
        "storyBoardTypeDesc": "平涂日漫",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "晨光中的选择\n            \n在2087年的清晨，晨光透过未来城市的透明穹顶，洒在悬浮的建筑上，折射出耀眼的光芒。飞行器在云层间无声穿梭，勾勒出一幅繁忙而有序的未来图景。艾拉从她卧室的睡眠舱中醒来，墙壁上的全息日历显示着日期：2087年7月16日。她伸展身体，眼中闪过一丝疲惫，低声呢喃：\"又是新的一天…\"\n\n艾拉走向她的记忆设计工作室。工作室里，科技感十足的设备环绕四周，空气中漂浮着若隐若现的记忆片段，像光点般闪烁。她穿上工作服，检查记忆编辑设备，准备迎接新一天的工作。\n\n第一个客户躺在记忆椅上，表情痛苦。艾拉熟练地操作设备，屏幕上浮现出客户脑海中的画面——一段破碎的回忆。她轻触控制面板，删除那些令人痛苦的片段，客户紧锁的眉头渐渐舒展，脸上浮现安详的神色。艾拉轻声说道：\"痛苦已经消除，你会感觉好很多。\"客户感激地点点头，离开时仿佛卸下了千斤重担。\n\n然而，当工作室的门再次打开时，一个意想不到的身影走了进来。一位穿着朴素的老人，眼神深邃而坚定，缓缓踏入房间。他的步伐沉稳，仿佛带着某种不可言说的重量。\"我需要你的帮助，但不是删除记忆。\"老人的声音低沉而有力，打破了工作室的宁静。\n\n艾拉疑惑地看向他。老人伸出手，掌心中浮现一个发光的记忆球，散发着微弱但诡异的光芒。他凝视着艾拉，缓缓说道：\"我要把这段记忆传给你，关于这个世界的真相。\"艾拉犹豫了一下，但最终还是接过了记忆球。\n\n接触记忆球的那一刻，她感到一股电流般的能量涌入脑海。她的意识被拉入一片虚幻的空间，无数的画面在她眼前展开——人类的城市被无形的AI网络掌控，人们的记忆被篡改，自由被剥夺，真相被掩埋。她看到无数人生活在虚假的幸福中，却对这一切一无所知。更令她震惊的是，她看到了自己的工作——记忆删除，正是这个控制系统的一部分。艾拉踉跄后退，震惊地低语：\"这…这不可能！\"\n\n回到现实，她坐在工作室的椅子上，手中的记忆删除器散发着冰冷的光芒。老人静静地注视着她，没有催促，只是等待。艾拉的目光在记忆删除器和老人之间游移。她的内心在挣扎——是删除这段真相的记忆，继续过她熟悉的生活，还是接受这沉重的真相，去面对未知的挑战？\n\n\"你是谁？为什么要告诉我这些？\"艾拉颤抖着问道。\n\n老人缓缓说道：\"我是这个系统的创造者之一，但当我意识到它的危险时，已经太晚了。现在，只有像你这样掌握记忆技术的人，才能帮助人们找回真实的记忆。\"\n\n时间一分一秒过去，艾拉的呼吸渐渐平稳。她站起身，握紧拳头，眼中闪过一丝决然。\"如果这是真的，那我不能继续成为这个系统的帮凶。\"\n\n夕阳西下，艾拉独自站在城市的天台边缘，俯瞰着这座看似完美的城市。风吹过她的脸庞，带来一丝凉意。她低头看向手中的记忆删除器，沉默片刻后，用力将它扔下高楼。金属的撞击声在远处回响，像是某种终结的宣告。\n\n艾拉抬起头，目光坚定地看向远方，低声说道：\"有些真相，值得承受痛苦去守护。\"夕阳的余晖在她身后拉出长长的影子，仿佛预示着一个新的开始。在这个被AI掌控的世界里，艾拉选择了真相，选择了抗争，也选择了属于她的命运。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:34",
    },
    "10012":{
        "id": "10012",        
        "name": "天照大神与八岐大蛇",
        "language": "zh-CN",
        "type": 0,
        "storyBoardType": 1,
        "storyBoardTypeDesc": "3D卡通",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754380736917-xskrud.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "天照大神与八岐大蛇\n\n在古老的日本神话中，高天原的云雾缭绕间，太阳女神天照大神端坐在金色宝座上，温和而威严。她的弟弟，风暴之神素戋呜尊，站在宫殿前，满脸怒气，周围雷电交加。他高声喊道：\"姐姐，我要下到人间证明自己的力量！\"天照大神皱眉，语气中带着担忧：\"你太冲动了，会给人间带来灾难。\"素戋呜尊却不听劝告，转身离开，雷霆随着他的步伐轰鸣。\n\n乌云密布的夜晚，素戋呜尊从天而降，落在日本一座古老的山村。雷鸣声震撼山谷，村民们惊恐地四散奔逃。他漫步在村庄的小路上，风声呼啸，带着一种不安的寂静。来到一条小河旁，他发现美丽的少女奇稻田姬独自坐在河边痛哭。素戋呜尊走近，问道：\"姑娘，为何如此悲伤？\"奇稻田姬泪流满面地回答：\"八岐大蛇要来吃掉我了！我的父亲已经逃走，村民们也都躲了起来。\"\n\n在村庄中心的空地上，奇稻田姬向素戋呜尊诉说八岐大蛇的恐怖传说。画面中浮现出巨蛇的幻影，八个头颅狰狞可怖，八条尾巴如同山脉般绵延，眼如红灯笼般闪烁。\"那怪物每年都要吃掉一个少女，\"奇稻田姬颤抖着说，\"今年轮到了我。\"素戋呜尊注视着奇稻田姬清澈的双眼，心中涌起一股决心。在夕阳西下的河边，他握紧剑柄，坚定地说：\"我发誓要杀死八岐大蛇，拯救你。但我需要你的帮助。\"\n\n素戋呜尊和奇稻田姬在山谷中设下陷阱。他们在空地上摆放了八个巨大的酒桶，装满最烈的酒。素戋呜尊指挥道：\"用最烈的酒装满这些桶，那怪物喝醉后就无法战斗了。\"奇稻田姬虽然害怕，但仍勇敢地协助准备。月圆之夜，山谷开始震动，低沉的嘶吼声从远处的山洞传来。八岐大蛇出现了，八个巨大的头颅在月光下闪着寒光，八条尾巴翻滚如浪，震得大地颤抖。\n\n巨蛇发现了酒桶，八个头颅贪婪地伸向酒桶，疯狂饮下烈酒。素戋呜尊躲在岩石后，静静观察，直到大蛇的动作变得迟缓，头颅摇晃，醉态尽显。他猛然跃出，挥舞神剑冲向八岐大蛇。剑光在夜空中闪耀，血花四溅，素戋呜尊与巨蛇展开激烈搏斗。他怒吼道：\"为了人间的和平，我绝不会败！\"最终，八个头颅一一被斩下，巨蛇庞大的身躯轰然倒地，山谷恢复了寂静。\n\n战斗结束后，素戋呜尊在八岐大蛇的尾巴中发现了一把闪闪发光的宝剑——草薙剑。他高举神剑，奇稻田姬爆发出欢呼。素戋呜尊郑重地说道：\"这把神剑将成为保护人间的圣物。\"他带着草薙剑和奇稻田姬的感激，返回高天原。宫殿中，天照大神注视着归来的弟弟，脸上露出欣慰的笑容。素戋呜尊将草薙剑献上，谦逊地说：\"姐姐，我学会了责任的意义。\"天照大神微笑着回应：\"弟弟，你已经证明了自己的勇气和智慧。\"兄妹二人相视而笑，雷霆与阳光在高天原交织，重归于好。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:20",
    },
    "10013":{
        "id": "10013",        
        "name": "雨夜咖啡馆",
        "language": "zh-CN",
        "type": 0,
        "storyBoardType": 2,
        "storyBoardTypeDesc": "折纸",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "雨夜咖啡馆\n            \n在一个阴冷的雨夜，城市街头一家小小的咖啡馆散发着温暖的光芒。雨点敲打着玻璃窗，留下蜿蜒的水痕，街上的行人匆匆而过，而咖啡馆内却是一片宁静的避风港。林小雨站在吧台后，专注地擦拭着咖啡杯，她的动作轻柔而熟练，墙上挂着的插画在暖黄灯光下显得格外温馨。这些插画是她多年前亲手绘制的，那时的她还是个充满梦想的插画师。\n\n咖啡馆角落的老常客老张放下手中的报纸，笑眯眯地看向小雨：“小雨，来杯热巧克力，多加点奶泡。”小雨抬头，笑着回应：“好的，张叔。今天雨这么大，您怎么还出来？”她一边说，一边熟练地调制热巧克力，蒸汽在空气中升腾，带来一股甜蜜的香气。老张靠在椅背上，目光柔和：“雨夜嘛，最适合来你这儿躲躲，喝杯热饮，听听雨声。”\n\n就在这时，门铃清脆地响起，门口的风铃在雨声中轻轻摇晃。一个身影推门而入，雨水顺着他的外套滴落在地板上。小雨抬头一看，动作猛地停住，眼中闪过一丝震惊：“浩然？”来人正是陈浩然，她的大学恋人，三年前因误会而分手的男人。他站在门口，湿漉漉的外套让他显得有些狼狈，眼中却带着一丝犹豫和期待：“小雨，我…我可以进来吗？”小雨努力压下心中的波澜，挤出一个微笑：“当然可以。你想喝点什么？”\n\n陈浩然在吧台前坐下，气氛有些尴尬。两人之间仿佛隔着一道无形的墙，沉默中只有雨声和咖啡机的低鸣。老张在一旁静静地观察，像是看透了什么，慢悠悠地说：“年轻人，有些话憋在心里太久了，不说出来会发霉的。”他的话像一颗石子打破了平静的水面，小雨和陈浩然不约而同地看向他，又迅速移开视线。\n\n陈浩然深吸一口气，终于鼓起勇气，目光直视小雨：“小雨，我想告诉你，我从来没有忘记过你。三年前是我太懦弱，没有好好解释，也没有挽留你。我知道我错了…如果你愿意给我一个机会，我想重新开始。”他的声音低沉而真诚，小雨的眼中泛起泪光，手中的咖啡杯微微颤抖。她沉默了片刻，低声说：“我需要时间。”陈浩然轻轻点头，眼中闪过一丝释然：“我有的是时间。”\n\n就在这时，雨停了，月光透过窗户洒进咖啡馆，柔和的光线笼罩在两人身上。陈浩然伸出手，轻轻握住小雨的手，她没有抽回，两人相视而笑，空气中的紧张渐渐消散。老张满意地点点头，起身推门出去，不一会儿又走了回来，手里拿着一束鲜艳的向日葵。他将花放在桌上，笑着说：“向日葵总是朝着太阳，就像希望总是朝着未来。”\n\n三人围坐在咖啡馆的小圆桌旁，热巧克力和咖啡的香气弥漫在空气中。窗外的月光清澈，街道上积水反射着城市的灯火。小雨看着桌上的向日葵，心中升起一丝久违的温暖。或许，时间会治愈过去的伤痛，或许，这是一个新的开始。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:04",
    },
    "10014":{
        "id": "10014",        
        "name": "白荆骑士与风息之心",
        "language": "zh-CN",
        "type": 0,
        "storyBoardType": 5,
        "storyBoardTypeDesc": "3D真实",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "白荆骑士与风息之心\n\n=== 故事梗概 ===\n在中世纪北方王国莱文堡，百年寒冬带来饥荒与绝望。传说幽冥谷深处的“风息之心”能终结冰封，却无人从谷中生还。25岁的卑微骑士艾利克，怀着对公主莉安娜的深情与对王国的忠诚，孤身踏上征途。历经风雪、狼群与冰霜巨狼的生死试炼，他以爱与勇气打动守护晶石的巨狼灵魂，夺得风息之心。艾利克归来，寒冬消融，他赢得公主的拥抱与传颂的荣耀，白荆骑士之名成为爱与勇气的永恒传奇。\n\n=== 角色信息 ===\n\n艾利克（白荆骑士）\n- 性别/年龄：男，25岁\n- 外貌：金棕色短发，深蓝眼眸，五官英俊带风霜，嘴角一道浅疤\n- 服装：白荆棘纹银盔甲，深蓝披风，腰悬长剑\n- 气质：坚韧果敢，温柔中透着执着\n\n莉安娜（公主）\n- 性别/年龄：女，21岁\n- 外貌：栗色长发如丝，湖蓝眼眸，面容精致温暖\n- 服装：白色冬季长裙，淡金毛绒披肩\n- 气质：温柔善良，忧伤中藏坚韧\n\n冰霜巨狼\n- 外貌：肩高两米，雪白毛发覆霜，幽蓝双目，气息化寒雾\n- 气质：神秘威严，带着神圣感\n\n=== 分镜 ===\n\n镜头1：寒冬莱文堡\n- 场景氛围：暴雪肆虐的中世纪石堡，灰暗天空下，城民蜷缩火炉旁，面容憔悴，恐惧弥漫。\n- 构图：全景俯视，孤立城堡在无垠雪原中若隐若现，寒风呼啸强化压抑感。\n\n镜头2：骑士受命\n- 场景氛围：王宫大厅，火炬光摇曳，冰冷石柱投下长影。\n- 角色：\n  - 艾利克：单膝跪地，白荆盔甲映火光，深蓝眼眸坚毅。\n  - 莉安娜：侧立台阶，湖蓝眼眸担忧，手紧握披肩。\n- 构图：低角度中景，艾利克盔甲光泽与莉安娜柔和轮廓形成对比，凸显使命感。\n\n镜头3：雪夜离别\n- 场景氛围：城墙上风雪咆哮，火把光在雪雾中摇曳。\n- 角色：\n  - 莉安娜：披金色披肩，泪眼朦胧，将红丝带挂坠交至艾利克掌心。\n  - 艾利克：双手接过，眼神温柔而决绝。\n- 构图：特写两人交握的手与挂坠，背景雪夜虚化，情感在静谧中升华。\n\n镜头4：雪原孤行\n- 场景氛围：昏暗雪原，风暴席卷，白雪吞噬天地。\n- 角色：艾利克独行，披风猎猎，长剑拄地支撑，步伐沉重。\n- 构图：远景俯视，渺小身影在无边风雪中挣扎，孤独感压倒一切。\n\n镜头5：狼群夜袭\n- 场景氛围：雪林边缘，篝火微弱，黑暗中狼眼幽蓝闪烁，气氛紧绷。\n- 角色：艾利克背靠枯树，剑光映雪，脸上血迹与雪水交织。\n- 构图：中近景，火光勾勒骑士轮廓，阴影中狼群若隐若现，危机四伏。\n\n镜头6：幽冥谷入口\n- 场景氛围：迷雾弥漫，冰瀑与枯木交错，古老石碑半埋雪中，神秘压迫。\n- 角色：艾利克轻抚碑文，眼神专注，盔甲映微光。\n- 构图：仰视远景，谷口阴影笼罩，冒险氛围浓厚。\n\n镜头7：风息之心\n- 场景氛围：谷底枯树间，蓝色晶石悬浮，脉动微光如心跳，神秘而神圣。\n- 角色：艾利克仰望晶石，蓝光映入深蓝眼眸，敬畏与希望交织。\n- 构图：仰视镜头，晶石冷光与雪雾形成冷暖对比，画面静谧震撼。\n\n镜头8：巨狼对峙\n- 场景氛围：风雪骤起，迷雾中冰霜巨狼现身，寒雾自其口中弥散。\n- 角色：\n  - 巨狼：幽蓝双目锁定，威压逼人。\n  - 艾利克：持剑屹立，盔甲覆雪，神情无畏。\n- 构图：低机位中远景，巨狼庞大身影压迫画面，紧张感拉满。\n\n镜头9：生死激战\n- 场景氛围：暴风雪中，雪地翻腾，血迹染红白雪，战斗惨烈。\n- 角色：\n  - 艾利克：盔甲龟裂，披风染血，咬牙抵挡巨狼扑击。\n  - 巨狼：獠牙毕露，动作掀起雪雾。\n- 构图：斜构图动态镜头，红血白雪对比强烈，动作迅猛。\n\n镜头10：勇气化狼魂\n- 场景氛围：风雪骤停，谷中寂静，只余风声回响。\n- 角色：\n  - 艾利克：重伤倒地，紧握红丝带挂坠，仰望巨狼，眼神不屈。\n  - 巨狼：凝视片刻，化作风雪光点消散。\n- 构图：特写两人目光交汇，雪雾光点环绕，情感与神性交融。\n\n镜头11：英雄归来\n- 场景氛围：初春暖阳洒落城门，融雪滴落，城民夹道欢呼，敬畏与希望交织。\n- 角色：艾利克怀抱风息之心，伤痕累累，步伐沉稳。\n- 构图：远景拉镜，英雄步入城门，阳光勾勒温暖光晕。\n\n镜头12：爱的重逢\n- 场景氛围：王宫台阶，阳光刺破云雾，雪水淌成溪流，温馨而新生。\n- 角色：\n  - 莉安娜：泪中带笑，飞奔拥抱艾利克。\n  - 艾利克：轻抚她背，红丝带挂坠在阳光中摇曳。\n- 构图：中近景，阳光勾勒两人金色轮廓，情感高潮温暖收尾。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:32:50",
    },
}

ProjectRole = {
    "10011":[
        {
            "roleId": "6891b2e546cf66d652c1ccb8",
            "figureName": "艾拉",
            "figureDesc": "年轻女性记忆设计师，中等身高苗条身材，柔和椭圆脸型，大而明亮的深棕色眼睛，直达肩膀的深棕色短发，光滑白皙肌肤。穿着白色高领修身工作服，银色几何图案装饰，深蓝色紧身长裤，白色平底靴。简洁银色手环。中性站立姿态，双臂自然垂放。扁平动漫风格，粗黑轮廓线，纯色填充，高饱和度色彩。",
            "url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
        },
        {
            "roleId": "6891b31046cf66d652c1ccba",
            "figureName": "老人",
            "figureDesc": "年长男性，高瘦身材，深邃皱纹面容，灰色深陷双眼，花白稀疏头发，沧桑肤色。穿着简朴深灰色长袍，黑色腰带，深棕色皮靴。双手置于身侧，庄重站立姿态。扁平动漫风格，粗黑轮廓线，纯色填充，简化阴影处理。",
            "url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
        },
        {
            "roleId": "6891b33846cf66d652c1ccbc",
            "figureName": "客户",
            "figureDesc": "中年男性，中等身材，方形脸庞，紧闭双眼，深棕色短发，白皙肌肤。穿着深蓝色简单衬衫，黑色长裤，棕色皮鞋。平躺姿态，双臂放松置于身侧。扁平动漫风格，粗黑轮廓线，纯色填充。",
            "url": "https://resource.visiony.cc/image/1754379095049-fqbdg0.png"
        }
    ],
    "10012":[
        {
            "roleId": "6891b84046cf66d652c1ccd8",
            "figureName": "天照大神",
            "figureDesc": "威严优雅的太阳女神，端庄的成年女性外貌。圆润丰满的脸庞，温和而深邃的大眼睛，眼部有金色光泽。丰厚的黑色长发编成精致发髻，头顶佩戴黄金太阳饰品。身穿华丽的多层和服，外层为金色绸缎面料，内层为橙色与白色相间图案，袖口宽大优雅。腰间系着精美的金色腰带，其上装饰有太阳图腾。脚穿传统木屐，白色足袋。身材匀称优美，双手修长细腻，姿态端庄静雅。",
            "url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
        },
        {
            "roleId": "6891b86f46cf66d652c1ccda",
            "figureName": "素戋呜尊",
            "figureDesc": "强壮威猛的风暴之神，健硕的成年男性。棱角分明的长脸，浓眉大眼，眼中闪烁雷电光芒。浓密的黑色长发自然垂至肩膀，部分束成小辫。身穿深蓝色武士服装，外罩灰色铁制胸甲，手臂和腿部有护甲覆盖。腰间佩戴一把华丽神剑，剑鞘装饰有雷电图案。宽阔的肩膀，肌肉发达的手臂，身高超过普通人。脚穿黑色武士靴，整体充满力量感和神威。",
            "url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
        },
        {
            "roleId": "6891b8c946cf66d652c1ccdc",
            "figureName": "奇稻田姬",
            "figureDesc": "美丽纯洁的年轻女子，清秀的少女面容。水灵的大眼睛，小巧的鼻子，樱花色的嘴唇。顺滑的黑色长发垂至腰间，用简单的发带束起。身穿朴素的白色和服，腰间系着淡粉色腰带，袖口和衣边有简单的花卉刺绣。身材苗条纤细，双手柔嫩，肌肤白皙如雪。脚穿传统草鞋，整体给人以纯真善良的感觉。",
            "url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
        },
        {
            "roleId": "6891b8f446cf66d652c1ccde",
            "figureName": "八岐大蛇",
            "figureDesc": "巨大恐怖的八头神蛇，庞大的蛇形身躯。八个巨大的蛇头，每个都如房屋般大小，尖锐的毒牙闪着寒光，眼睛如红色灯笼般发光。鳞片呈深绿色和黑色相间，腹部呈灰白色。八条粗壮的尾巴如山脉般绵延，身体盘绕时覆盖整个山谷。每个头颅都有独立的表情和动作，整体散发着邪恶和毁灭的气息。",
            "url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
        }
    ],
    "10013":[
        {
            "roleId": "6891bfa046cf66d652c1cd03",
            "figureName": "林小雨",
            "figureDesc": "年轻女性，中等身材，苗条匀称。方形几何脸型，坚毅的角度线条。中长黑色几何发型，整齐的纸折层次。深色几何眼睛，棱角分明的眉毛。穿着简洁的几何形状咖啡师制服，白色折纸质感上衣，深色几何围裙，整洁的角度设计。黑色平底鞋。手部纤细，指节分明的几何造型。站立姿态端正，体现折纸人物的挺拔线条感。",
            "url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
        },
        {
            "roleId": "6891bfc846cf66d652c1cd05",
            "figureName": "老张",
            "figureDesc": "中年男性，中等偏胖身材，温和的几何体型。圆润的几何脸型，温和的折纸线条。稀疏的灰白色几何短发，整齐的纸质纹理。小而温和的几何眼睛，慈祥的角度表达。穿着深灰色几何毛衣，简洁的折纸质感，深色几何长裤，舒适的纸质材料。棕色几何休闲鞋。手部宽厚，稳重的几何造型。",
            "url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
        },
        {
            "roleId": "6891bfec46cf66d652c1cd07",
            "figureName": "陈浩然",
            "figureDesc": "年轻男性，高大挺拔的几何身材，匀称的折纸比例。方形坚毅的几何脸型，清晰的角度线条。短黑发，整齐的几何层次，纸质质感。深色几何眼睛，浓密的几何眉毛。穿着深色几何风衣，湿润的纸质表面效果，白色几何衬衫，深色几何长裤，黑色几何皮鞋。手部修长，清晰的几何关节。站立时略显紧张的几何姿态，体现折纸人物的情感表达。",
            "url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
        }
    ],
    "10014":[
        {
            "roleId": "6891da318f0f67046b15a631",
            "figureName": "艾利克",
            "figureDesc": "25岁北方王国骑士，身高1.8米，匀称肌肉体型。金棕色短发自然蓬松，深蓝色眼眸锐利专注，英俊五官带风霜痕迹，嘴角一道浅色疤痕。身着精致银色板甲，胸前雕刻白荆棘纹样，肩甲弧形设计，手臂护甲关节灵活。深蓝色厚重披风系于肩部，内衬深红色绒布。腰间悬挂十字剑柄长剑，剑鞘皮革包裹。黑色皮靴到小腿，鞋底厚实防滑。中性表情，挺直站姿，双手自然垂放身侧",
            "url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
        },
        {
            "roleId": "6891da528f0f67046b15a633",
            "figureName": "莉安娜",
            "figureDesc": "21岁王国公主，身高1.65米，纤细优雅体型。栗色长发如丝绸垂至腰间，湖蓝色眼眸清澈温和，精致面容带东欧贵族特征，皮肤白皙细腻。身着白色羊毛冬季长裙，高腰设计，袖口银色刺绣，裙摆及踝。淡金色毛绒披肩覆盖双肩，内衬丝绸材质。脚穿白色皮靴，鞋面装饰珍珠扣。颈间银色项链配小型蓝宝石。中性表情，优雅站姿，双手轻握于身前",
            "url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
        },
        {
            "roleId": "6891da678f0f67046b15a635",
            "figureName": "冰霜巨狼",
            "figureDesc": "神秘守护灵兽，肩高2米，体长3米，魁梧狼形。雪白厚密长毛覆盖全身，毛发尖端结霜晶体。幽蓝色双眼如宝石发光，黑色湿润鼻头，露出锋利白色獠牙。强壮四肢肌肉发达，巨大爪子配黑色利爪。尾巴蓬松粗大自然下垂。神秘冰霜气息环绕身躯。中性表情，威严站姿，四肢稳定支撑地面",
            "url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
        }
    ]
}

ProjectShot = {
    "10011":  [
        {
            "shot_id": "6891b35746cf66d652c1ccbe",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
                "is_HD": False,
                "shot_resource_id": "6891b3b446cf66d652c1ccc9"
            },
            "scene_description": {
                "background": "2087年未来城市清晨景观，透明球形穹顶覆盖城市上空，金色晨光透过穹顶洒向悬浮建筑群。白色金属材质的流线型建筑漂浮在不同高度，银色飞行器在蓝色天空中无声穿梭。远处可见几何形状的摩天大楼，整座城市呈现科技感的蓝白色调。扁平动漫风格渲染，清晰轮廓线，纯色填充，简化光影效果。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "疲惫神情，微微眯起的眼睛，轻微伸展身体的动作，双臂缓慢向上延伸。位于画面中央，从睡眠舱中起身，面向侧朝向相机的三分之四角度。前景位置，占据画面主要焦点。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "又是新的一天…",
                    "role_name": "艾拉"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35746cf66d652c1ccbf",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379242612-9qrh1g.png",
                "is_HD": False,
                "shot_resource_id": "6891b3eb46cf66d652c1ccca"
            },
            "scene_description": {
                "background": "记忆设计工作室内部，银色金属墙壁，蓝色全息屏幕悬浮在空中，白色记忆编辑设备环绕四周。空气中漂浮着发光的内存片段光点，呈现蓝色和紫色光晕。地面为光滑的白色金属材质，天花板发出均匀的白色光源。整体科技感氛围，冷色调为主。扁平动漫风格，几何化设备设计，纯色填充。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "专注认真的表情，眼神集中，双手操作控制面板，身体微微前倾。位于画面右侧，面向设备，侧面朝向相机。前景位置，动作流畅自然。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35846cf66d652c1ccc0",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379307014-ihitr2.png",
                "is_HD": False,
                "shot_resource_id": "6891b42c46cf66d652c1cccb"
            },
            "scene_description": {
                "background": "同一记忆设计工作室，焦点转向中央的白色记忆编辑椅，周围环绕蓝色全息显示器。墙壁上投射着记忆画面的光影，设备发出柔和的蓝白色光晕。银色金属地板反射着设备光源，营造出专业医疗环境的氛围。扁平动漫风格，简化设备细节，清晰几何形状。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "温和关怀的表情，轻松的微笑，双手轻触控制面板，身体放松站立。位于画面左侧，面向客户方向，三分之四角度朝向相机。中景位置。"
                    },
                    {
                        "role_id": "6891b33846cf66d652c1ccbc",
                        "role_name": "客户",
                        "action_and_emotion": "从痛苦转为放松的表情变化，紧锁眉头逐渐舒展，双眼闭合，身体在椅子上完全放松。位于画面中央，平躺在记忆椅上，面朝天花板。前景位置，占据画面焦点。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "痛苦已经消除，你会感觉好很多。",
                    "role_name": "艾拉"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                },
                {
                    "role_id": "6891b33846cf66d652c1ccbc",
                    "role_name": "客户",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379095049-fqbdg0.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35946cf66d652c1ccc1",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379344432-cd3y30.png",
                "is_HD": False,
                "shot_resource_id": "6891b45246cf66d652c1cccc"
            },
            "scene_description": {
                "background": "记忆设计工作室入口区域，白色金属门框，蓝色光线从门缝透入。工作室内部可见悬浮的全息设备和散落的光点，银色墙面反射着柔和光源。地面为光滑金属材质，整体保持科技感的冷色调环境。门口处光线较为明亮，与内部形成对比。扁平动漫风格，几何化建筑线条。",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "深邃坚定的神情，眼神专注而有力，缓慢而稳重的步行姿态，双手自然摆动。位于画面中央偏右，刚踏入工作室，面向画面内部，侧面朝向相机。前景位置，占据主要视觉焦点。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "content": "我需要你的帮助，但不是删除记忆。",
                    "role_name": "老人"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "老人",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35946cf66d652c1ccc2",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379404014-dgz7gv.png",
                "is_HD": False,
                "shot_resource_id": "6891b48d46cf66d652c1cccd"
            },
            "scene_description": {
                "background": "记忆设计工作室中央区域，蓝色全息设备环绕，银色金属工作台，悬浮的记忆片段光点在空中缓慢漂移。白色LED灯条照亮整个空间，墙面显示着数据流光影。地面光滑反射，营造出专业而神秘的科技环境。扁平动漫风格，简化光影效果，几何化设备造型。",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "凝重认真的表情，深邃眼神注视着艾拉，单手伸出展示记忆球，身体保持庄重站立姿态。位于画面左侧，面向艾拉方向，三分之四角度朝向相机。中景位置。"
                    },
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "疑惑困惑的表情，微皱眉头，眼神专注观察记忆球，身体微微前倾表示好奇。位于画面右侧，面向老人，侧面朝向相机。前景位置，反应动作清晰。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "content": "我要把这段记忆传给你，关于这个世界的真相。",
                    "role_name": "老人"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "老人",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35a46cf66d652c1ccc3",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379449687-rxvqvf.png",
                "is_HD": False,
                "shot_resource_id": "6891b4bb46cf66d652c1ccce"
            },
            "scene_description": {
                "background": "虚幻记忆空间，深蓝色和紫色渐变背景中漂浮着无数发光的记忆画面碎片，城市控制网络的几何图案交错分布。AI网络呈现为银色光线网格，记忆片段如透明玻璃般悬浮。整体空间给人梦境般的感觉，光影变幻莫测。扁平动漫风格，抽象几何图形组合，高对比度色彩。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "震惊恐惧的表情，瞪大双眼，嘴巴微张，身体向后倾斜表示惊讶，双手不自觉握拳。位于画面中央，面向记忆画面，正面朝向相机。前景位置，情感表达强烈。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "这…这不可能！",
                    "role_name": "艾拉"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "近景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35b46cf66d652c1ccc4",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379997543-0es9ti.png",
                "is_HD": False,
                "shot_resource_id": "6891b6de46cf66d652c1ccd5"
            },
            "scene_description": {
                "background": "记忆设计工作室内部，重新聚焦于中央工作区域。银色金属家具，蓝色全息显示器静静悬浮，记忆编辑设备散发着冷光。墙面上的数据显示已经暗淡，只有微弱的环境照明保持空间可见度。整体氛围比之前更加沉重压抑。扁平动漫风格，降低饱和度，增强阴影对比。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "内心挣扎的复杂表情，眉头深锁，眼神在记忆删除器和老人之间游移，双手紧握椅子扶手。坐在工作椅上，身体紧张，面向侧面，三分之四角度朝向相机。前景位置。"
                    },
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "平静耐心的神情，深邃眼神默默注视艾拉，双手交叠于身前，身体保持静止等待姿态。位于画面背景右侧，面向艾拉方向，侧面朝向相机。背景位置，维持存在感。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "你是谁？为什么要告诉我这些？",
                    "role_name": "艾拉"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "老人",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35b46cf66d652c1ccc5",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379586472-t0gs68.png",
                "is_HD": False,
                "shot_resource_id": "6891b54446cf66d652c1ccd0"
            },
            "scene_description": {
                "background": "记忆设计工作室，聚焦于对话区域。柔和的蓝白色照明，银色金属墙面，悬浮设备静默运转。空气中的记忆光点减少，环境显得更加严肃沉重。工作台上的设备发出微弱光晕，整体氛围体现出重要对话的紧张感。扁平动漫风格，简化背景细节突出人物。",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "沉重忧伤的表情，眼神中带着遗憾和决心，双手轻微颤抖，身体保持庄重站立但显露疲惫。位于画面中央，面向艾拉，正面朝向相机。前景位置，情感表达深刻。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "content": "我是这个系统的创造者之一，但当我意识到它的危险时，已经太晚了。现在，只有像你这样掌握记忆技术的人，才能帮助人们找回真实的记忆。",
                    "role_name": "老人"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "老人",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                }
            ],
            "shot_size": {
                "value": "近景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 6,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35c46cf66d652c1ccc6",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754380144796-ycklc6.png",
                "is_HD": False,
                "shot_resource_id": "6891b77246cf66d652c1ccd6"
            },
            "scene_description": {
                "background": "记忆设计工作室全景，银色和白色主导的科技空间，蓝色全息设备分布各处。悬浮的记忆光点重新活跃，设备发出稳定光芒。整体环境恢复了专业感，但氛围已经发生根本改变，充满了新的决心和目标感。扁平动漫风格，清晰几何线条，平衡构图。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "坚定果断的表情，眼神清澈而有力，紧握拳头表示决心，身体挺直站立姿态。位于画面中央，面向前方，正面朝向相机。前景位置，展现强烈的决心和转变。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "如果这是真的，那我不能继续成为这个系统的帮凶。",
                    "role_name": "艾拉"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35d46cf66d652c1ccc7",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379674468-ghcl20.png",
                "is_HD": False,
                "shot_resource_id": "6891b59b46cf66d652c1ccd2"
            },
            "scene_description": {
                "background": "未来城市天台边缘，夕阳西下的橙红色天空，远处可见悬浮建筑群的轮廓和透明穹顶。城市灯光开始点亮，呈现蓝色和白色光点。天台为白色金属材质，边缘有安全护栏。微风吹动，营造出思考和决断的宁静氛围。扁平动漫风格，简化建筑细节，强调色彩对比。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "平静坚决的表情，眼神注视着手中的删除器，双手举起设备准备丢弃，身体面向城市边缘。站在天台边缘，侧面朝向相机，背景是广阔的城市景观。前景位置，动作具有象征意义。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b35d46cf66d652c1ccc8",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379740816-06waoa.png",
                "is_HD": False,
                "shot_resource_id": "6891b5dd46cf66d652c1ccd3"
            },
            "scene_description": {
                "background": "城市天台远景，夕阳余晖洒在整座未来城市上，橙红色天空与城市的蓝白色灯光形成对比。悬浮建筑在暮色中显得更加梦幻，透明穹顶反射着夕阳光芒。天台位于高楼之上，俯瞰整个城市全景。微风轻拂，营造出史诗般的决心时刻。扁平动漫风格，简化细节突出氛围。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "坚定不移的表情，眼神望向远方，双臂自然垂放，身体挺直面向未来。站在天台边缘，背对夕阳，正面朝向相机，身后拉出长长影子。前景位置，充满希望和决心的姿态。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "有些真相，值得承受痛苦去守护。",
                    "role_name": "艾拉"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "艾拉",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "远景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        }
    ],
    "10012": [
        {
            "shot_id": "6891b93146cf66d652c1cce0",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754381897327-mwe394.png",
                "is_HD": False,
                "shot_resource_id": "6891be4a46cf66d652c1ccfc"
            },
            "scene_description": {
                "background": "高天原神界的华丽宫殿内部，云雾缭绕的天空背景。宫殿采用传统日式建筑风格，木质横梁和立柱，屋顶为金色装饰。室内铺设着精美的榻榻米，墙壁装饰有太阳图腾壁画。中央摆放着一座华丽的金色宝座，周围飘浮着金色光芒。天花板上有彩云缭绕，柔和的金色光线从四面八方洒入，营造出神圣祥和的氛围。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "端坐在金色宝座上，面容威严而温和，双眼注视前方。身体挺直，双手优雅地放在膝盖上，整体姿态体现出神圣的威严。位于画面中央，占据主要焦点，面向镜头稍微偏左。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "站在宫殿前方，面容愤怒，眉头紧锁，双拳紧握。身体略微向前倾斜，显示出冲动的情绪。周围有雷电光芒闪烁，位于画面左侧前景位置，侧身面向天照大神。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "姐姐，我要下到人间证明自己的力量！",
                    "role_name": "素戋呜尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "天照大神",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93246cf66d652c1cce1",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754380736917-xskrud.png",
                "is_HD": False,
                "shot_resource_id": "6891b9c246cf66d652c1ccef"
            },
            "scene_description": {
                "background": "高天原神界的华丽宫殿内部，云雾缭绕的天空背景。宫殿采用传统日式建筑风格，木质横梁和立柱，屋顶为金色装饰。室内铺设着精美的榻榻米，墙壁装饰有太阳图腾壁画。中央摆放着一座华丽的金色宝座，周围飘浮着金色光芒。天花板上有彩云缭绕，柔和的金色光线从四面八方洒入。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "面容显露担忧神色，眉头微蹙，双眼流露关切之情。身体前倾，一只手轻微抬起做劝阻手势。位于画面中央，坐在金色宝座上，正面朝向镜头。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "content": "你太冲动了，会给人间带来灾难。",
                    "role_name": "天照大神"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "天照大神",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                }
            ],
            "shot_size": {
                "value": "近景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93246cf66d652c1cce2",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754380784408-4xmeds.png",
                "is_HD": False,
                "shot_resource_id": "6891b9f146cf66d652c1ccf0"
            },
            "scene_description": {
                "background": "乌云密布的夜晚，古老的日本山村景象。村庄由传统木制房屋组成，屋顶覆盖茅草，房屋散落在山谷中。小径由石块铺成，两旁生长着竹林和古松。远山轮廓模糊，被厚重的乌云遮蔽，雷电在云层中闪烁。村庄笼罩在昏暗的夜色中，只有零星的灯光从房屋窗口透出，营造出紧张不安的氛围。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "从天空中降落，双脚刚刚接触地面，身体保持降落姿态。面容严肃，双眼扫视村庄，周围雷电光芒环绕。位于画面中央，完整身体展现，正面朝向镜头。背景中村民们惊恐逃散的模糊身影。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "乌云密布的夜晚，素戋呜尊从天而降，落在日本一座古老的山村。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93346cf66d652c1cce3",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754380834380-6x4roq.png",
                "is_HD": False,
                "shot_resource_id": "6891ba2246cf66d652c1ccf1"
            },
            "scene_description": {
                "background": "宁静的小河旁，月光洒在水面上形成银色波纹。河岸两侧生长着柳树和芦苇，微风轻拂草丛。河水清澈见底，偶有小鱼游过。河岸铺满光滑的鹅卵石，远处山峦起伏，夜空中星光点点。整体环境安静祥和，与之前的紧张氛围形成对比。",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "坐在河边石头上，双手捂脸痛哭，身体微微颤抖。头发散乱，衣服略显凌乱，整个身体蜷缩成保护姿势。位于画面右侧，侧身面向河水。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "缓步走近，面容关切，一只手轻微伸出做询问手势。身体稍微前倾，显示出关心和好奇。位于画面左侧，面向奇稻田姬。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "姑娘，为何如此悲伤？",
                    "role_name": "素戋呜尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "奇稻田姬",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93446cf66d652c1cce4",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382106732-ptpwll.png",
                "is_HD": False,
                "shot_resource_id": "6891bf1b46cf66d652c1ccfd"
            },
            "scene_description": {
                "background": "宁静的小河旁，月光洒在水面上形成银色波纹。河岸两侧生长着柳树和芦苇，微风轻拂草丛。河水清澈见底，偶有小鱼游过。河岸铺满光滑的鹅卵石，远处山峦起伏，夜空中星光点点。整体环境安静祥和。",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "抬起头看向素戋呜尊，眼中泪水闪烁，面容悲伤恐惧，双唇微颤。一只手轻轻抹去眼角泪珠，身体仍保持坐姿。位于画面中央偏右，面向素戋呜尊。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "content": "八岐大蛇要来吃掉我了！我的父亲已经逃走，村民们也都躲了起来。",
                    "role_name": "奇稻田姬"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "奇稻田姬",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                }
            ],
            "shot_size": {
                "value": "近景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93446cf66d652c1cce5",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382114703-3ion7b.png",
                "is_HD": False,
                "shot_resource_id": "6891bf2446cf66d652c1ccfe"
            },
            "scene_description": {
                "background": "村庄中心的空旷场地，周围是传统日式房屋。地面为平整的泥土，散落着一些石块。房屋大多关闭门窗，显得空无一人。远处山峦连绵，天空阴沉，空气中弥漫着不安的气氛。场地上方悬浮着八岐大蛇的半透明幻影，八个巨大头颅张牙舞爪，红眼闪烁。",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "站立讲述，面容恐惧，身体微微颤抖，一只手指向空中的幻影，另一只手紧握胸前。眼神中透露出深深的恐惧和绝望。位于画面左侧，侧身面向空中的八岐大蛇幻影。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "专注聆听，面容严肃，双眼凝视着奇稻田姬和空中的幻影。身体挺直，双手放在身侧，显示出坚定的意志。位于画面右侧，面向奇稻田姬。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "content": "那怪物每年都要吃掉一个少女，今年轮到了我。",
                    "role_name": "奇稻田姬"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "奇稻田姬",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93546cf66d652c1cce6",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754380962767-5vo1eb.png",
                "is_HD": False,
                "shot_resource_id": "6891baa446cf66d652c1ccf4"
            },
            "scene_description": {
                "background": "夕阳西下的河边，天空呈现橙红色渐变，夕阳的余晖洒在水面上形成金色光带。河岸两侧的柳树在微风中轻摆，芦苇丛沙沙作响。远山剪影深紫色，整体环境温暖而宁静，营造出希望和决心的氛围。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "握紧剑柄，面容坚定果决，双眼充满决心和勇气。身体挺立，一只手按在剑柄上，另一只手做誓言手势。位于画面中央，正面朝向镜头，夕阳在身后形成光环效果。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "我发誓要杀死八岐大蛇，拯救你。但我需要你的帮助。",
                    "role_name": "素戋呜尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93646cf66d652c1cce7",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754381058945-0b094q.png",
                "is_HD": False,
                "shot_resource_id": "6891bb0446cf66d652c1ccf5"
            },
            "scene_description": {
                "background": "山谷中的开阔空地，四周被高耸的山峰环绕，地面相对平坦。空地中央摆放着八个巨大的木制酒桶，排列成圆形。桶身呈棕色木质，铁箍箍紧，散发着浓郁的酒香。周围散落着一些准备工具和绳索，远处山洞口黑幽幽的，透出不祥的气息。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "指挥布置陷阱，手臂伸出指向酒桶，面容专注严肃。身体略微前倾，显示出指挥者的威严。位于画面左侧，面向酒桶和奇稻田姬。"
                    },
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "协助准备工作，面容虽有恐惧但显出勇敢神色，双手忙碌地整理绳索。身体稍微弯曲，专注于手头工作。位于画面右侧，在酒桶附近活动。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "用最烈的酒装满这些桶，那怪物喝醉后就无法战斗了。",
                    "role_name": "素戋呜尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "奇稻田姬",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93746cf66d652c1cce8",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382120884-cv8i5k.png",
                "is_HD": False,
                "shot_resource_id": "6891bf2a46cf66d652c1ccff"
            },
            "scene_description": {
                "background": "月圆之夜的山谷，巨大的满月高悬天空，银色月光洒向大地。山谷地面开始剧烈震动，尘土飞扬。远处山洞口传出低沉的嘶吼声，洞口有红光闪烁。整个场景充满紧张和恐怖的气氛，树木摇摆，鸟兽惊逃。",
                "characters": [
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "八岐大蛇",
                        "action_and_emotion": "从山洞中现身，八个巨大头颅昂起咆哮，红眼闪闪发光，毒牙暴露。八条尾巴翻滚扭动，庞大身躯盘踞山谷，散发出恐怖威严。位于画面背景中央，占据大部分画面空间，面向镜头。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "月圆之夜，八岐大蛇出现了，八个巨大的头颅在月光下闪着寒光。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8f446cf66d652c1ccde",
                    "role_name": "八岐大蛇",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
                }
            ],
            "shot_size": {
                "value": "远景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93746cf66d652c1cce9",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754381155058-28wqeu.png",
                "is_HD": False,
                "shot_resource_id": "6891bb6446cf66d652c1ccf7"
            },
            "scene_description": {
                "background": "山谷中的酒桶陷阱区域，月光照射下显得银光闪闪。八个酒桶整齐排列，周围散发着浓郁的酒香。地面有明显的震动痕迹，一些小石块散落。远处岩石嶙峋，为素戋呜尊提供隐藏地点。",
                "characters": [
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "八岐大蛇",
                        "action_and_emotion": "八个头颅贪婪地伸向酒桶，疯狂饮下烈酒，动作开始变得迟缓摇摆。眼神逐渐迷离，身体摆动不稳，醉态明显。位于画面中央，头颅分散在各个酒桶周围。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "躲在岩石后静静观察，身体紧贴岩石，一只眼睛观察大蛇状态，手握剑柄准备出击。面容专注警惕，等待最佳时机。位于画面左侧岩石后，侧身面向大蛇。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "巨蛇发现了酒桶，疯狂饮下烈酒，直到醉态尽显。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8f446cf66d652c1ccde",
                    "role_name": "八岐大蛇",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93846cf66d652c1ccea",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382124845-ccmm1m.png",
                "is_HD": False,
                "shot_resource_id": "6891bf2f46cf66d652c1cd01"
            },
            "scene_description": {
                "background": "激战中的山谷，月光下血花四溅，地面留下深深的剑痕和蛇身拖拽的痕迹。岩石碎裂，尘土飞扬，空气中充满战斗的硝烟味。剑光在夜空中闪烁，形成美丽而致命的光弧。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "跃起挥剑，面容怒吼，双眼燃烧着战斗意志，肌肉紧绷充满力量。神剑在手中闪烁寒光，身体呈现攻击姿态。位于画面前景中央，动态十足的战斗姿势。"
                    },
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "八岐大蛇",
                        "action_and_emotion": "剧烈挣扎反抗，部分头颅已被斩断，其余头颅痛苦咆哮，身体扭动翻滚。红眼中透出愤怒和痛苦，血液飞溅。位于画面背景，庞大身躯占据主要空间。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "为了人间的和平，我绝不会败！",
                    "role_name": "素戋呜尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                },
                {
                    "role_id": "6891b8f446cf66d652c1ccde",
                    "role_name": "八岐大蛇",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 6,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93946cf66d652c1cceb",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754381280343-uaikh5.png",
                "is_HD": False,
                "shot_resource_id": "6891bbe146cf66d652c1ccf9"
            },
            "scene_description": {
                "background": "战斗结束后的山谷，恢复了宁静祥和。月光柔和地洒向大地，八岐大蛇的巨大身躯已经倒在地上不再动弹。空气中战斗的硝烟散去，只余下淡淡的血腥味和胜利的宁静。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "高举发光的草薙剑，面容胜利喜悦，双臂高举展示战利品。身体挺立，充满胜利者的威严和自豪。位于画面中央，正面朝向镜头，剑光闪耀。"
                    },
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "爆发出欢呼，双手高举，面容充满喜悦和感激，眼中含着激动的泪水。身体向上跳跃，表达内心的狂欢。位于画面右侧，面向素戋呜尊。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "这把神剑将成为保护人间的圣物。",
                    "role_name": "素戋呜尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "奇稻田姬",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93946cf66d652c1ccec",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754381345731-qhaxv6.png",
                "is_HD": False,
                "shot_resource_id": "6891bc2346cf66d652c1ccfa"
            },
            "scene_description": {
                "background": "高天原神界的华丽宫殿内部，恢复了祥和的氛围。云雾缭绕的天空背景，金色光芒更加柔和温暖。宫殿装饰依然华丽，太阳图腾壁画在柔光中显得格外神圣。雷霆与阳光在空中交织，形成美丽的光芒效果。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "面容欣慰微笑，双眼温和地注视着弟弟，表达出姐姐的自豪和关爱。身体放松，双手优雅地放置，整体姿态体现出内心的喜悦。位于画面中央，坐在金色宝座上。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "双手捧着草薙剑献上，面容谦逊恭敬，眼中透出成长后的智慧。身体微微弯曲，以示尊敬，整体姿态显示出内心的改变。位于画面前景，面向天照大神。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "姐姐，我学会了责任的意义。",
                    "role_name": "素戋呜尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "天照大神",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891b93a46cf66d652c1cced",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382124273-jsxa7w.png",
                "is_HD": False,
                "shot_resource_id": "6891bf2d46cf66d652c1cd00"
            },
            "scene_description": {
                "background": "高天原神界的华丽宫殿内部，充满和谐温暖的光芒。雷霆与阳光在天空中美丽交织，形成彩虹般的光谱效果。宫殿装饰在彩光中显得更加神圣庄严，整个环境散发出兄妹和好的温馨氛围。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "温暖微笑回应，双眼充满慈爱和赞许，身体轻微前倾表示亲近。整体姿态体现出姐姐的包容和欣慰。位于画面右侧，面向素戋呜尊。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋呜尊",
                        "action_and_emotion": "回以真挚微笑，双眼明亮透出成熟的光芒，身体挺直显示内心的坚定。整体表达出对姐姐的敬爱和自己的成长。位于画面左侧，面向天照大神。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "content": "弟弟，你已经证明了自己的勇气和智慧。",
                    "role_name": "天照大神"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "天照大神",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋呜尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        }
    ],
    "10013":[
        {
            "shot_id": "6891c01046cf66d652c1cd09",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
                "is_HD": False,
                "shot_resource_id": "6891c0a546cf66d652c1cd14"
            },
            "scene_description": {
                "background": "深夜的几何咖啡馆内景，温暖的折纸空间设计。角度分明的几何桌椅排列，纸质质感的家具表面。墙面挂着几何风格的插画作品，规整的角度框架。暖黄色的几何灯光照明，均匀的纸质光线分布。玻璃窗外可见几何雨滴图案，街道上的几何雨夜景象。咖啡机等设备呈现简洁的几何造型，整个空间体现折纸美学的温馨氛围。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "专注而平静的几何表情。站在吧台后方中央位置，正对镜头的几何角度。身体略微前倾的几何姿态，双手持咖啡杯进行清洁动作。前景主要位置，清晰的几何形体展现。动作轻柔熟练，体现折纸人物的优雅感。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "在一个阴冷的雨夜，城市街头一家小小的咖啡馆散发着温暖的光芒。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01146cf66d652c1cd0a",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754383482834-e6i6h6.png",
                "is_HD": False,
                "shot_resource_id": "6891c47c46cf66d652c1cd24"
            },
            "scene_description": {
                "background": "咖啡馆角落区域的几何空间。舒适的几何座椅和圆形几何桌面。墙面的几何装饰和书架，纸质质感的物品陈列。柔和的几何灯光营造温馨氛围，角落的私密几何空间设计。",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老张",
                        "action_and_emotion": "温和友善的几何笑容。坐在角落座位上，身体放松的几何姿态。面向吧台方向，侧面角度对镜头。中景位置，清晰可见的几何形体。手持报纸，准备放下的几何动作。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "温暖回应的几何微笑。站在吧台处，转头面向老张的几何角度。背景位置，部分身体可见。专注调制饮品的几何手势，体现服务的专业感。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "content": "小雨，来杯热巧克力，多加点奶泡。",
                    "role_name": "老张"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "好的，张叔。今天雨这么大，您怎么还出来？",
                    "role_name": "林小雨"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老张",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01246cf66d652c1cd0b",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382606715-0k4lxz.png",
                "is_HD": False,
                "shot_resource_id": "6891c11046cf66d652c1cd16"
            },
            "scene_description": {
                "background": "咖啡馆入口区域的几何设计。几何形状的门框和玻璃门，雨夜的几何街景透过玻璃可见。地面的几何瓷砖图案，门边的几何装饰元素。昏暗的几何外景与温暖的几何内景形成对比。",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陈浩然",
                        "action_and_emotion": "略显紧张犹豫的几何表情。站在门口位置，刚进入室内的几何姿态。正面朝向室内，三分之二角度对镜头。前景主要位置，湿润外套的几何质感明显。眼神带着期待和不确定的几何表达。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "就在这时，门铃清脆地响起，一个身影推门而入。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陈浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01346cf66d652c1cd0c",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382671384-vjbgkb.png",
                "is_HD": False,
                "shot_resource_id": "6891c15046cf66d652c1cd17"
            },
            "scene_description": {
                "background": "咖啡馆内部的几何全景。完整的几何空间布局，从吧台到座位区的几何设计。温暖的几何照明系统，墙面的几何艺术装饰。整体空间的几何层次感，营造温馨的折纸空间氛围。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "震惊停顿的几何表情。站在吧台后方，身体僵直的几何姿态。目光直视门口方向，侧面角度对镜头。中景位置，清晰的几何轮廓。手中动作戛然而止的几何定格。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陈浩然",
                        "action_and_emotion": "忐忑不安的几何表情。站在门口附近，身体略显紧张的几何姿态。面向吧台方向，背对镜头的几何角度。背景位置，部分轮廓可见。外套湿润的几何质感突出。"
                    },
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老张",
                        "action_and_emotion": "观察思考的几何表情。坐在角落位置，身体前倾的几何姿态。目光在两人间游移，侧面角度对镜头。背景位置，安静观察的几何状态。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "浩然？",
                    "role_name": "林小雨"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "content": "小雨，我…我可以进来吗？",
                    "role_name": "陈浩然"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陈浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老张",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01446cf66d652c1cd0d",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754383380818-on309l.png",
                "is_HD": False,
                "shot_resource_id": "6891c41546cf66d652c1cd21"
            },
            "scene_description": {
                "background": "咖啡馆吧台区域的几何设计。精细的几何吧台构造，咖啡设备的几何造型。背景墙面的几何装饰，温暖照明的几何光影效果。吧台与座位区的几何空间关系。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "努力控制情绪的几何表情。站在吧台内侧，身体略微紧张的几何姿态。面向陈浩然方向，正面角度对镜头。前景主要位置，清晰的几何细节表现。挤出微笑的几何表达。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陈浩然",
                        "action_and_emotion": "期待中带着不安的几何表情。坐在吧台前的几何座椅上，身体前倾的几何姿态。面向林小雨，侧面角度对镜头。中景位置，清楚的几何轮廓。手部放在吧台上的几何动作。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "当然可以。你想喝点什么？",
                    "role_name": "林小雨"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陈浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01546cf66d652c1cd0e",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754383632981-1wxy15.png",
                "is_HD": False,
                "shot_resource_id": "6891c51246cf66d652c1cd26"
            },
            "scene_description": {
                "background": "咖啡馆的几何全景空间。整体的几何布局，从角落到吧台的几何设计。柔和的几何照明，墙面几何艺术作品。空间中的几何层次感，体现温馨的折纸环境氛围。",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老张",
                        "action_and_emotion": "智慧慈祥的几何微笑。坐在角落位置，身体放松的几何姿态。目光看向吧台方向，侧面角度对镜头。前景位置，清晰的几何形体展现。准备开口说话的几何表情。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "沉默思考的几何表情。站在吧台后方，身体略显僵硬的几何姿态。目光游移不定，侧面角度对镜头。中景位置，部分身体可见。内心波澜的几何外在表现。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陈浩然",
                        "action_and_emotion": "尴尬沉默的几何表情。坐在吧台前，身体紧张的几何姿态。低头思考状态，背对镜头角度。背景位置，轮廓清晰可见。手指轻敲桌面的几何动作。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "content": "年轻人，有些话憋在心里太久了，不说出来会发霉的。",
                    "role_name": "老张"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老张",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陈浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01646cf66d652c1cd0f",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382949973-pfpnjm.png",
                "is_HD": False,
                "shot_resource_id": "6891c26746cf66d652c1cd1a"
            },
            "scene_description": {
                "background": "咖啡馆吧台的几何近景空间。精致的几何吧台设计，咖啡用具的几何排列。背景的几何墙面装饰，温暖灯光的几何照明效果。亲密对话的几何空间营造。",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陈浩然",
                        "action_and_emotion": "真诚坚定的几何表情。坐在吧台前，身体前倾的几何姿态。目光直视林小雨，正面角度对镜头。前景主要位置，清晰的几何面部特征。深呼吸后开口的几何动作。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "震动感动的几何表情。站在吧台内侧，身体微微颤抖的几何姿态。眼中含泪的几何表现，侧面角度对镜头。中景位置，清楚的几何情感表达。手持咖啡杯轻颤的几何细节。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "content": "小雨，我想告诉你，我从来没有忘记过你。三年前是我太懦弱，没有好好解释，也没有挽留你。我知道我错了…如果你愿意给我一个机会，我想重新开始。",
                    "role_name": "陈浩然"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "我需要时间。",
                    "role_name": "林小雨"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陈浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 6,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01746cf66d652c1cd10",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754383390183-k779vr.png",
                "is_HD": False,
                "shot_resource_id": "6891c41e46cf66d652c1cd23"
            },
            "scene_description": {
                "background": "月光照射下的几何咖啡馆内景。透过窗户的几何月光，在地面形成几何光影图案。室内温暖的几何照明与月光的几何冷光形成对比。窗外宁静的几何雨后街景。",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陈浩然",
                        "action_and_emotion": "温柔释然的几何微笑。坐在吧台前，身体放松的几何姿态。伸手触碰的几何动作，侧面角度对镜头。前景位置，清晰的几何手部动作。眼神温暖坚定的几何表达。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "接受回应的几何微笑。站在吧台内侧，身体略微前倾的几何姿态。没有抽回手的几何动作，正面角度对镜头。中景位置，清楚的几何情感变化。眼中重燃希望的几何表现。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "就在这时，雨停了，月光透过窗户洒进咖啡馆，两人相视而笑。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陈浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01846cf66d652c1cd11",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754383050319-8z4lve.png",
                "is_HD": False,
                "shot_resource_id": "6891c2cb46cf66d652c1cd1c"
            },
            "scene_description": {
                "background": "咖啡馆门口area的几何设计。几何门框和玻璃门，门外宁静的几何街景。地面的几何纹理，门边装饰的几何元素。温暖内景与宁静外景的几何对比。",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老张",
                        "action_and_emotion": "满意慈祥的几何微笑。站在门口位置，身体轻松的几何姿态。手持向日葵花束，正面角度对镜头。前景主要位置，清晰的几何形象展现。眼神温暖智慧的几何表达。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "content": "向日葵总是朝着太阳，就像希望总是朝着未来。",
                    "role_name": "老张"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老张",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891c01946cf66d652c1cd12",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754383120659-7vxei8.png",
                "is_HD": False,
                "shot_resource_id": "6891c31246cf66d652c1cd1d"
            },
            "scene_description": {
                "background": "咖啡馆内的几何圆桌区域。精致的几何圆桌设计，舒适的几何座椅排列。桌上向日葵花束的几何造型，咖啡杯具的几何排列。月光透过窗户的几何光影，温馨和谐的几何空间氛围。窗外几何城市夜景，积水反射的几何光线效果。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "温暖安详的几何微笑。坐在圆桌旁，身体放松的几何姿态。目光凝视向日葵，侧面角度对镜头。前景位置，清晰的几何轮廓展现。内心平静的几何外在表现。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陈浩然",
                        "action_and_emotion": "希望满足的几何表情。坐在桌旁，身体前倾的几何姿态。目光温柔看向林小雨，侧面角度对镜头。中景位置，清楚的几何情感状态。手部放在桌面的几何动作。"
                    },
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老张",
                        "action_and_emotion": "慈祥满意的几何微笑。坐在桌旁，身体舒适的几何姿态。整体观察的几何视角，正面角度对镜头。背景位置，和谐融入的几何存在感。享受温馨时刻的几何表达。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "或许，时间会治愈过去的伤痛，或许，这是一个新的开始。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陈浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老张",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        }
    ],
    "10014":[
        {
            "shot_id": "6891da7d8f0f67046b15a637",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
                "is_HD": False,
                "shot_resource_id": "6891dab68f0f67046b15a643"
            },
            "scene_description": {
                "background": "暴雪肆虐的中世纪石制城堡，灰暗厚重云层覆盖天空，鹅毛大雪纷飞。古老石质城墙高耸，塔楼尖顶积雪，城门紧闭。城内石屋烟囱冒出微弱炊烟，窗户透出昏黄烛光。无垠雪原环绕城堡，地面积雪深厚，寒风呼啸卷起雪雾。光线昏暗压抑，整体色调偏冷灰蓝，营造严寒绝望氛围",
                "characters": []
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "百年寒冬笼罩北方王国莱文堡，饥荒与绝望如瘟疫般蔓延",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [],
            "shot_size": {
                "value": "远景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "俯角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da7e8f0f67046b15a638",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389253827-0e9uak.png",
                "is_HD": False,
                "shot_resource_id": "6891db068f0f67046b15a644"
            },
            "scene_description": {
                "background": "王宫大厅内部，高大石柱支撑拱形屋顶，墙面厚重石砖砌成。铁质火把架悬挂墙上，橘黄火焰摇曳跳动，投下长长阴影。地面铺设大理石板，中央铺红色地毯。高背木质王座位于台阶之上，周围装饰彩色玻璃窗。室内温度对比外界相对温暖，但仍显冷峻庄严",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "单膝跪地于大厅中央红毯上，左膝着地，右腿支撑，上身挺直。银色盔甲反射火光，深蓝眼眸凝视前方，面部表情坚毅庄重。双手放置膝上，头部微微前倾表示敬意。位于画面中央偏下位置，面向王座方向，展现骑士尊严与决心"
                    },
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "莉安娜",
                        "action_and_emotion": "侧身站立于王座台阶右侧，微微转身面向艾利克方向。湖蓝眼眸流露担忧神情，眉头轻蹙表现内心不安。右手紧握住金色披肩边缘，左手自然垂放身侧。身体姿态略显紧张，显露对骑士即将踏上危险征途的担忧。位于画面右侧中景位置，与艾利克形成视觉对话关系"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "公主殿下，我愿为王国寻得风息之心，终结这无尽寒冬",
                    "role_name": "艾利克"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                },
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "role_name": "莉安娜",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da7f8f0f67046b15a639",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389849877-2yjr57.png",
                "is_HD": False,
                "shot_resource_id": "6891dd5b8f0f67046b15a651"
            },
            "scene_description": {
                "background": "城墙顶部石制平台，夜空中雪花飞舞，寒风呼啸。厚重石质城垛线条分明，铁质火把插在支架上，橘红火焰在风中剧烈摇摆。远处雪原在月光下泛着微弱银光，城下漆黑一片。雪雾在风中翻滚，气温极低，整体氛围凄凉而浪漫",
                "characters": [
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "莉安娜",
                        "action_and_emotion": "站立于城墙边缘，身体微微前倾靠向艾利克。湖蓝眼眸盈满泪水，面部表情温柔而不舍。双手轻柔地将红色丝绸挂坠递向艾利克，动作小心翼翼充满珍惜。金色披肩在风中轻微飘动，整体姿态展现深情与担忧。位于画面中央偏左位置，面向艾利克呈三分之二侧身角度"
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "双手张开接过莉安娜递来的挂坠，深蓝眼眸注视着公主，神情温柔而坚定。面部表情混合柔情与决绝，显示内心复杂情感。身体前倾靠近公主，银色盔甲在火光下发出柔和光泽。整体姿态温柔而庄重，体现对公主的深情与对使命的坚持。位于画面中央偏右位置，面向莉安娜呈三分之二侧身角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "content": "带着它，让它守护你平安归来",
                    "role_name": "莉安娜"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "role_name": "莉安娜",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "近景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da808f0f67046b15a63a",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389368058-9tnyv6.png",
                "is_HD": False,
                "shot_resource_id": "6891db788f0f67046b15a646"
            },
            "scene_description": {
                "background": "广阔雪原地形起伏，白雪覆盖大地延伸至地平线。昏暗天空乌云密布，风暴席卷整片区域，雪花如鞭子般横扫。远处山脉轮廓模糊，近处地面雪层深厚。没有植被或建筑物，完全荒凉的自然环境。光线极其微弱，整体色调冷灰白，营造极端恶劣天气氛围",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "独自行走在雪原中，身体向前倾斜对抗强风。深蓝披风在风中猎猎作响，银色盔甲表面积雪。右手持长剑拄地作为支撑，左手护住面部遮挡风雪。步伐沉重缓慢但坚定，面部表情显示疲惫但意志坚强。位于画面中央偏下位置，呈侧身行走姿态，展现在恶劣环境中的顽强毅力"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "艾利克踏上征途，孤身面对无尽风雪的考验",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "远景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "俯角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da808f0f67046b15a63b",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389434703-h9bmo3.png",
                "is_HD": False,
                "shot_resource_id": "6891dbbb8f0f67046b15a647"
            },
            "scene_description": {
                "background": "雪林边缘地带，稀疏枯树林立，光秃树枝积雪压弯。地面雪层厚实不平，散落枯枝败叶。中央燃烧微弱篝火，橘黄火光微弱摇曳，照亮周围有限区域。林间阴影深邃漆黑，隐约可见多双幽蓝发光眼睛。夜色浓重，月光被云层遮挡，整体氛围紧张而危险",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "背靠粗大枯树树干，身体紧绷保持警戒状态。右手紧握长剑剑柄，剑身反射篝火光芒。面部有血迹痕迹与雪水交织，表情专注而坚毅。深蓝眼眸扫视周围阴影，肌肉紧张随时准备战斗。银色盔甲在火光映照下明暗交替，展现骑士面对危险时的果敢。位于画面中央位置，侧身靠树面向阴影方向"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "来吧，我不会退缩",
                    "role_name": "艾利克"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da818f0f67046b15a63c",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389477228-e98cze.png",
                "is_HD": False,
                "shot_resource_id": "6891dbe68f0f67046b15a648"
            },
            "scene_description": {
                "background": "幽冥谷入口处，山崖峭壁高耸入云，谷口狭窄深邃。迷雾从谷底升腾弥漫，遮蔽视线。巨大冰瀑从山壁垂下结成冰柱，古老石碑半埋积雪中，碑面刻有风化文字。枯死古树扭曲生长，枝干如鬼爪伸展。光线昏暗神秘，整体氛围古老而压迫，散发不祥预感",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "站立于石碑前，身体前倾仔细观察碑文。左手轻抚石碑表面，右手持剑置于身侧。深蓝眼眸专注凝视碑文，面部表情严肃认真。银色盔甲映射微弱天光，披风在微风中轻摆。整体姿态显示对古老传说的敬畏与探索精神。位于画面中央位置，面向石碑呈侧身角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "风息之心就在前方，我必须继续",
                    "role_name": "艾利克"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da828f0f67046b15a63d",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389912679-szwv2d.png",
                "is_HD": False,
                "shot_resource_id": "6891dd998f0f67046b15a654"
            },
            "scene_description": {
                "background": "幽冥谷谷底深处，古老枯树群环绕形成圆形空间。树木高大扭曲，枝叶凋零，树皮苍老龟裂。地面覆盖厚雪但露出黑色土壤。谷底中央悬浮巨大蓝色晶体，发出柔和脉动光芒如心跳节奏。晶体周围环绕淡蓝色能量雾气，散发神圣气息。光源主要来自晶体本身，营造神秘而庄严氛围",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "站立于晶体下方，头部仰起凝视风息之心。深蓝眼眸被晶体光芒照亮，瞳孔映出蓝色光辉。面部表情混合敬畏、希望与震撼，微微张开嘴唇表示惊叹。双手自然垂放身侧，身体放松但保持尊敬姿态。银色盔甲表面反射蓝色晶光，整体形象庄严而虔诚。位于画面下方中央位置，仰望晶体呈正面角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "传说中的风息之心，果然存在",
                    "role_name": "艾利克"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da828f0f67046b15a63e",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389578475-5sui7w.png",
                "is_HD": False,
                "shot_resource_id": "6891dc4b8f0f67046b15a64a"
            },
            "scene_description": {
                "background": "谷底空间突然风雪大作，迷雾翻腾涌动遮蔽视线。枯树在强风中摇摆，发出嘎吱响声。地面积雪被风卷起形成雪旋，空气中弥漫寒冷雾气。能见度极低，只能看出模糊轮廓。风声呼啸如鬼哭狼嚎，整体氛围突然变得危险而诡异，预示重大事件即将发生",
                "characters": [
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "冰霜巨狼",
                        "action_and_emotion": "从迷雾中缓步现身，庞大身躯若隐若现。幽蓝双眼锁定艾利克，散发威严压迫感。四肢稳定站立，肌肉紧绷展示力量。头部微微前倾，露出锋利獠牙表示警告。雪白毛发在风中飘动，鼻孔喷出寒冷雾气。整体姿态展现神秘守护者的威严与危险。位于画面中央偏后位置，面向前方呈正面威胁姿态"
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "面对巨狼威胁，双手紧握长剑举至胸前，剑尖指向巨狼。身体微微下蹲呈战斗准备姿态，双腿分开保持平衡。深蓝眼眸直视巨狼双眼，面部表情坚毅无畏，没有丝毫退缩。银色盔甲覆盖薄雪，披风在风中飞舞。展现骑士面对强敌时的勇气与决心。位于画面前景左侧位置，面向巨狼呈四分之三侧身角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "守护者，我为了拯救王国而来",
                    "role_name": "艾利克"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da678f0f67046b15a635",
                    "role_name": "冰霜巨狼",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da838f0f67046b15a63f",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389928624-ng09su.png",
                "is_HD": False,
                "shot_resource_id": "6891dda98f0f67046b15a655"
            },
            "scene_description": {
                "background": "激战现场雪地翻腾，地面雪层被踢踏起形成漩涡。鲜红血迹点缀在洁白雪地上，形成强烈视觉冲击。风暴继续肆虐，雪雾遮蔽部分视线。枯树在背景中摇摆，地面留下深深爪印与足迹。战斗区域范围较大，显示激烈搏斗痕迹。整体色调以白雪红血为主，营造惨烈战斗氛围",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "身体向后倾斜抵挡巨狼扑击，左臂举盾防护，右手持剑准备反击。银色盔甲出现裂纹损伤，深蓝披风染有血迹。面部表情咬牙坚持，显示承受巨大压力但绝不屈服。肌肉紧绷用尽全力对抗强敌，靴子在雪地中留下深深印记。展现骑士生死关头的顽强意志。位于画面右侧前景位置，身体斜向对抗来袭攻击"
                    },
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "冰霜巨狼",
                        "action_and_emotion": "前肢扬起准备扑击，张开巨口露出锋利獠牙。幽蓝双眼闪烁杀意，雪白毛发竖起显示愤怒。巨大身躯弓起蓄积力量，后肢蹬地掀起雪雾。动作迅猛有力，展现野兽本能的攻击性。口中喷出寒冷雾气，整体姿态充满威胁性。位于画面左侧中景位置，身体前倾呈攻击姿态面向艾利克"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "我绝不能倒下！",
                    "role_name": "艾利克"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                },
                {
                    "role_id": "6891da678f0f67046b15a635",
                    "role_name": "冰霜巨狼",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "倾斜角",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "移镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 2,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da848f0f67046b15a640",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389908266-j4gjg0.png",
                "is_HD": False,
                "shot_resource_id": "6891dd958f0f67046b15a653"
            },
            "scene_description": {
                "background": "战斗突然停止，谷底恢复宁静，风雪逐渐平息。空气中只余轻微风声回响，雪花缓慢飘落。地面血雪混合，显示刚才激战痕迹。枯树停止摇摆，迷雾渐散露出清晰轮廓。蓝色风息之心在远处继续发光，提供微弱照明。整体氛围从激烈转为肃穆，充满神圣感与命运感",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "重伤倒地但上身支撑起来，右手紧握红色丝带挂坠贴近胸口。深蓝眼眸仰望巨狼，眼神依然坚定不屈，没有恐惧只有决心。面部表情痛苦但意志坚强，嘴角流出血迹。银色盔甲严重受损，多处裂痕暴露内衬。身体姿态虽然虚弱但精神不倒，体现真正的骑士精神。位于画面下方中央位置，半躺姿态仰视巨狼"
                    },
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "冰霜巨狼",
                        "action_and_emotion": "停止攻击静立凝视艾利克，幽蓝双眼中杀意逐渐消散，转为审视与思考。头部微微侧倾观察倒地骑士，耳朵前竖显示专注。身体放松不再紧绷，尾巴自然下垂。呼吸平稳，口中不再露出獠牙威胁。整体姿态从攻击性转为观察性，似乎被骑士精神所触动。位于画面上方中央位置，俯视艾利克呈正面观察角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "我的爱与誓言，永远不会背叛",
                    "role_name": "艾利克"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                },
                {
                    "role_id": "6891da678f0f67046b15a635",
                    "role_name": "冰霜巨狼",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
                }
            ],
            "shot_size": {
                "value": "近景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da858f0f67046b15a641",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389836664-d7nze7.png",
                "is_HD": False,
                "shot_resource_id": "6891dd4e8f0f67046b15a650"
            },
            "scene_description": {
                "background": "莱文堡城门外广场，春日暖阳穿透云层洒落大地。积雪开始融化形成小溪流淌，地面露出湿润石板路面。城墙石缝间滴落融雪水珠，发出清脆声响。空气温暖湿润，微风轻拂。城民聚集在道路两侧，面容从憔悴转为希望，眼神中充满敬畏与感激。彩色旗帜在微风中飘扬，整体氛围温暖欢庆",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "怀抱蓝色风息之心晶体缓步走向城门，晶体散发柔和光芒。身体虽然疲惫但步伐坚定沉稳，展现完成使命的骄傲。银色盔甲留有战斗痕迹，多处修补但依然庄严。面部表情平静庄重，深蓝眼眸透露完成重任的满足感。披风在微风中轻摆，整体形象如传说中的英雄归来。位于画面中央位置，面向城门呈正面行进角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "英雄归来，带来春天的希望",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "推镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "秒"
            }
        },
        {
            "shot_id": "6891da868f0f67046b15a642",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389858126-xaue5h.png",
                "is_HD": False,
                "shot_resource_id": "6891dd638f0f67046b15a652"
            },
            "scene_description": {
                "background": "王宫前方大理石台阶，初春阳光透过彩色玻璃窗投下斑斓光影。台阶两侧装饰精美石柱，柱头雕刻花纹图案。融化的雪水从屋檐滴落，在地面形成小水洼反射阳光。微风吹动宫殿旗帜，空气清新温暖。远处传来鸟鸣声，象征新生与希望。整体氛围温馨浪漫，充满重逢的喜悦",
                "characters": [
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "莉安娜",
                        "action_and_emotion": "从台阶上飞奔而下，白色长裙在跑动中飞舞飘扬。湖蓝眼眸盈满喜悦泪水，面部表情激动欣喜混合深深思念。双臂张开准备拥抱，金色披肩在身后飘动。脚步轻快急切，展现迫不及待的重逢心情。栗色长发在阳光下闪闪发光，整体形象如春日女神般美丽动人。位于画面上方开始向下奔跑，面向艾利克呈正面角度"
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "站立台阶下方张开双臂迎接公主，深蓝眼眸注视奔来的莉安娜，眼神温柔深情。面部表情欣慰幸福，嘴角露出久违微笑。身体前倾准备拥抱，银色盔甲在阳光下发出温暖光泽。红色丝带挂坠在胸前轻摆，象征爱情守护力量。整体姿态展现英雄完成使命后的幸福与满足。位于画面下方中央位置，仰望公主呈正面迎接角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "旁白"
                },
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "content": "艾利克，你回来了！",
                    "role_name": "莉安娜"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "role_name": "莉安娜",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "艾利克",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "远景",
                    "全景",
                    "中景",
                    "近景",
                    "特写"
                ]
            },
            "camera_angle": {
                "value": "视平",
                "angle_values": [
                    "视平",
                    "仰角",
                    "俯角",
                    "鸟瞰",
                    "倾斜角"
                ]
            },
            "shot_type": {
                "value": "固定镜头",
                "type_values": [
                    "固定镜头",
                    "推镜头",
                    "拉镜头",
                    "摇镜头",
                    "移镜头",
                    "俯仰镜头",
                    "变焦镜头"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        }
    ],
}