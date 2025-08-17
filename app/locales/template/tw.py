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
        "storyBoardType": "平塗日漫",
        "coverTitle": "平塗日漫",
        "cover": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
        "name": "晨光中的選擇",
        "intro": "2087年，人工智慧已經深度融入人類生活。艾拉是一名記憶設計師，她的工作是為客戶定製和修改記憶。今天，她面臨著一個改變人生的選擇。",
        "updateTime": "2024-12-05 19:06:10"
    },
    {
        "id": "10012",
        "storyBoardType": "3D卡通",
        "coverTitle": "3D卡通",
        "cover": "https://resource.visiony.cc/image/1754380736917-xskrud.png",
        "name": "天照大神與八岐大蛇",
        "intro": "在日本古代神話中，素戔嗚尊因為殺死了八岐大蛇而拯救了奇稻田姬，並從蛇尾中得到了草薙劍，最終與天照大神和解的傳奇故事。",
        "updateTime": "2024-12-05 19:06:10"
    },
    {
        "id": "10013",
        "storyBoardType": "摺紙",
        "coverTitle": "摺紙",
        "cover": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
        "name": "雨夜咖啡館",
        "intro": "在一個雨夜，一家溫馨的咖啡館裡發生了一個關於重逢、原諒和新開始的故事。",
        "updateTime": "2024-12-05 19:06:10"
    },
    {
        "id": "10014",
        "storyBoardType": "3D真實",
        "coverTitle": "3D真實",
        "cover": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
        "name": "白荊騎士與風息之心",
        "intro": "在中世紀北方王國萊文堡，漫長的寒冬帶來飢餓與絕望。傳說只有位於幽冥谷深處的風息之心能化解寒冬，但百年來沒有人能從那裡生還。",
        "updateTime": "2024-12-05 19:06:10"
    }
]

ProjectDescription = {
    "10011":{
        "id": "10011",        
        "name": "晨光中的選擇",
        "language": "zh-TW",
        "type": 0,
        "storyBoardType": 0,
        "storyBoardTypeDesc": "平塗日漫",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "晨光中的選擇\n            \n在2087年的清晨，晨光透過未來城市的透明穹頂，灑在懸浮的建築上，折射出耀眼的光芒。飛行器在雲層間無聲穿梭，勾勒出一幅繁忙而有序的未來圖景。艾拉從她臥室的睡眠艙中醒來，牆壁上的全息日曆顯示著日期：2087年7月16日。她伸展身體，眼中閃過一絲疲憊，低聲呢喃：\"又是新的一天…\"\n\n艾拉走向她的記憶設計工作室。工作室裡，科技感十足的設備環繞四周，空氣中漂浮著若隱若現的記憶片段，像光點般閃爍。她穿上工作服，檢查記憶編輯設備，準備迎接新一天的工作。\n\n第一個客戶躺在記憶椅上，表情痛苦。艾拉熟練地操作設備，螢幕上浮現出客戶腦海中的畫面——一段破碎的回憶。她輕觸控制面板，刪除那些令人痛苦的片段，客戶緊鎖的眉頭漸漸舒展，臉上浮現安詳的神色。艾拉輕聲說道：\"痛苦已經消除，你會感覺好很多。\"客戶感激地點點頭，離開時彷彿卸下了千斤重擔。\n\n然而，當工作室的門再次打開時，一個意想不到的身影走了進來。一位穿著樸素的老人，眼神深邃而堅定，緩緩踏入房間。他的步伐沉穩，彷彿帶著某種不可言說的重量。\"我需要你的幫助，但不是刪除記憶。\"老人的聲音低沉而有力，打破了工作室的寧靜。\n\n艾拉疑惑地看向他。老人伸出手，掌心中浮現一個發光的記憶球，散發著微弱但詭異的光芒。他凝視著艾拉，緩緩說道：\"我要把這段記憶傳給你，關於這個世界的真相。\"艾拉猶豫了一下，但最終還是接過了記憶球。\n\n接觸記憶球的那一刻，她感到一股電流般的能量湧入腦海。她的意識被拉入一片虛幻的空間，無數的畫面在她眼前展開——人類的城市被無形的AI網路掌控，人們的記憶被篡改，自由被剝奪，真相被掩埋。她看到無數人生活在虛假的幸福中，卻對這一切一無所知。更令她震驚的是，她看到了自己的工作——記憶刪除，正是這個控制系統的一部分。艾拉踉蹌後退，震驚地低語：\"這…這不可能！\"\n\n回到現實，她坐在工作室的椅子上，手中的記憶刪除器散發著冰冷的光芒。老人靜靜地注視著她，沒有催促，只是等待。艾拉的目光在記憶刪除器和老人之間游移。她的內心在掙扎——是刪除這段真相的記憶，繼續過她熟悉的生活，還是接受這沉重的真相，去面對未知的挑戰？\n\n\"你是誰？為什麼要告訴我這些？\"艾拉顫抖著問道。\n\n老人緩緩說道：\"我是這個系統的創造者之一，但當我意識到它的危險時，已經太晚了。現在，只有像你這樣掌握記憶技術的人，才能幫助人們找回真實的記憶。\"\n\n時間一分一秒過去，艾拉的呼吸漸漸平穩。她站起身，握緊拳頭，眼中閃過一絲決然。\"如果這是真的，那我不能繼續成為這個系統的幫兇。\"\n\n夕陽西下，艾拉獨自站在城市的天台邊緣，俯瞰著這座看似完美的城市。風吹過她的臉龐，帶來一絲涼意。她低頭看向手中的記憶刪除器，沉默片刻後，用力將它扔下高樓。金屬的撞擊聲在遠處回響，像是某種終結的宣告。\n\n艾拉抬起頭，目光堅定地看向遠方，低聲說道：\"有些真相，值得承受痛苦去守護。\"夕陽的餘暉在她身後拉出長長的影子，彷彿預示著一個新的開始。在這個被AI掌控的世界裡，艾拉選擇了真相，選擇了抗爭，也選擇了屬於她的命運。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:34",
    },
    "10012":{
        "id": "10012",        
        "name": "天照大神與八岐大蛇",
        "language": "zh-TW",
        "type": 0,
        "storyBoardType": 1,
        "storyBoardTypeDesc": "3D卡通",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754380736917-xskrud.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "天照大神與八岐大蛇\n\n在古老的日本神話中，高天原的雲霧繚繞間，太陽女神天照大神端坐在金色寶座上，溫和而威嚴。她的弟弟，風暴之神素戔嗚尊，站在宮殿前，滿臉怒氣，周圍雷電交加。他高聲喊道：\"姐姐，我要下到人間證明自己的力量！\"天照大神皺眉，語氣中帶著擔憂：\"你太衝動了，會給人間帶來災難。\"素戔嗚尊卻不聽勸告，轉身離開，雷霆隨著他的步伐轟鳴。\n\n烏雲密佈的夜晚，素戔嗚尊從天而降，落在日本一座古老的山村。雷鳴聲震撼山谷，村民們驚恐地四散奔逃。他漫步在村莊的小路上，風聲呼嘯，帶著一種不安的寂靜。來到一條小河旁，他發現美麗的少女奇稻田姬獨自坐在河邊痛哭。素戔嗚尊走近，問道：\"姑娘，為何如此悲傷？\"奇稻田姬淚流滿面地回答：\"八岐大蛇要來吃掉我了！我的父親已經逃走，村民們也都躲了起來。\"\n\n在村莊中心的空地上，奇稻田姬向素戔嗚尊訴說八岐大蛇的恐怖傳說。畫面中浮現出巨蛇的幻影，八個頭顱猙獰可怖，八條尾巴如同山脈般綿延，眼如紅燈籠般閃爍。\"那怪物每年都要吃掉一個少女，\"奇稻田姬顫抖著說，\"今年輪到了我。\"素戔嗚尊注視著奇稻田姬清澈的雙眼，心中湧起一股決心。在夕陽西下的河邊，他握緊劍柄，堅定地說：\"我發誓要殺死八岐大蛇，拯救你。但我需要你的幫助。\"\n\n素戔嗚尊和奇稻田姬在山谷中設下陷阱。他們在空地上擺放了八個巨大的酒桶，裝滿最烈的酒。素戔嗚尊指揮道：\"用最烈的酒裝滿這些桶，那怪物喝醉後就無法戰鬥了。\"奇稻田姬雖然害怕，但仍勇敢地協助準備。月圓之夜，山谷開始震動，低沉的嘶吼聲從遠處的山洞傳來。八岐大蛇出現了，八個巨大的頭顱在月光下閃著寒光，八條尾巴翻滾如浪，震得大地顫抖。\n\n巨蛇發現了酒桶，八個頭顱貪婪地伸向酒桶，瘋狂飲下烈酒。素戔嗚尊躲在岩石後，靜靜觀察，直到大蛇的動作變得遲緩，頭顱搖晃，醉態盡顯。他猛然躍出，揮舞神劍衝向八岐大蛇。劍光在夜空中閃耀，血花四濺，素戔嗚尊與巨蛇展開激烈搏鬥。他怒吼道：\"為了人間的和平，我絕不會敗！\"最終，八個頭顱一一被斬下，巨蛇龐大的身軀轟然倒地，山谷恢復了寂靜。\n\n戰鬥結束後，素戔嗚尊在八岐大蛇的尾巴中發現了一把閃閃發光的寶劍——草薙劍。他高舉神劍，奇稻田姬爆發出歡呼。素戔嗚尊鄭重地說道：\"這把神劍將成為保護人間的聖物。\"他帶著草薙劍和奇稻田姬的感激，返回高天原。宮殿中，天照大神注視著歸來的弟弟，臉上露出欣慰的笑容。素戔嗚尊將草薙劍獻上，謙遜地說：\"姐姐，我學會了責任的意義。\"天照大神微笑著回應：\"弟弟，你已經證明了自己的勇氣和智慧。\"兄妹二人相視而笑，雷霆與陽光在高天原交織，重歸於好。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:20",
    },
    "10013":{
        "id": "10013",        
        "name": "雨夜咖啡館",
        "language": "zh-TW",
        "type": 0,
        "storyBoardType": 2,
        "storyBoardTypeDesc": "摺紙",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "雨夜咖啡館\n            \n在一個陰冷的雨夜，城市街頭一家小小的咖啡館散發著溫暖的光芒。雨點敲打著玻璃窗，留下蜿蜒的水痕，街上的行人匆匆而過，而咖啡館內卻是一片寧靜的避風港。林小雨站在吧台後，專注地擦拭著咖啡杯，她的動作輕柔而熟練，牆上掛著的插畫在暖黃燈光下顯得格外溫馨。這些插畫是她多年前親手繪製的，那時的她還是個充滿夢想的插畫師。\n\n咖啡館角落的老常客老張放下手中的報紙，笑瞇瞇地看向小雨：\"小雨，來杯熱巧克力，多加點奶泡。\"小雨抬頭，笑著回應：\"好的，張叔。今天雨這麼大，您怎麼還出來？\"她一邊說，一邊熟練地調製熱巧克力，蒸汽在空氣中升騰，帶來一股甜蜜的香氣。老張靠在椅背上，目光柔和：\"雨夜嘛，最適合來你這兒躲躲，喝杯熱飲，聽聽雨聲。\"\n\n就在這時，門鈴清脆地響起，門口的風鈴在雨聲中輕輕搖晃。一個身影推門而入，雨水順著他的外套滴落在地板上。小雨抬頭一看，動作猛地停住，眼中閃過一絲震驚：\"浩然？\"來人正是陳浩然，她的大學戀人，三年前因誤會而分手的男人。他站在門口，濕漉漉的外套讓他顯得有些狼狽，眼中卻帶著一絲猶豫和期待：\"小雨，我…我可以進來嗎？\"小雨努力壓下心中的波瀾，擠出一個微笑：\"當然可以。你想喝點什麼？\"\n\n陳浩然在吧台前坐下，氣氛有些尷尬。兩人之間彷彿隔著一道無形的牆，沉默中只有雨聲和咖啡機的低鳴。老張在一旁靜靜地觀察，像是看透了什麼，慢悠悠地說：\"年輕人，有些話憋在心裡太久了，不說出來會發霉的。\"他的話像一顆石子打破了平靜的水面，小雨和陳浩然不約而同地看向他，又迅速移開視線。\n\n陳浩然深吸一口氣，終於鼓起勇氣，目光直視小雨：\"小雨，我想告訴你，我從來沒有忘記過你。三年前是我太懦弱，沒有好好解釋，也沒有挽留你。我知道我錯了…如果你願意給我一個機會，我想重新開始。\"他的聲音低沉而真誠，小雨的眼中泛起淚光，手中的咖啡杯微微顫抖。她沉默了片刻，低聲說：\"我需要時間。\"陳浩然輕輕點頭，眼中閃過一絲釋然：\"我有的是時間。\"\n\n就在這時，雨停了，月光透過窗戶灑進咖啡館，柔和的光線籠罩在兩人身上。陳浩然伸出手，輕輕握住小雨的手，她沒有抽回，兩人相視而笑，空氣中的緊張漸漸消散。老張滿意地點點頭，起身推門出去，不一會兒又走了回來，手裡拿著一束鮮豔的向日葵。他將花放在桌上，笑著說：\"向日葵總是朝著太陽，就像希望總是朝著未來。\"\n\n三人圍坐在咖啡館的小圓桌旁，熱巧克力和咖啡的香氣瀰漫在空氣中。窗外的月光清澈，街道上積水反射著城市的燈火。小雨看著桌上的向日葵，心中升起一絲久違的溫暖。或許，時間會治癒過去的傷痛，或許，這是一個新的開始。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:04",
    },
    "10014":{
        "id": "10014",        
        "name": "白荊騎士與風息之心",
        "language": "zh-TW",
        "type": 0,
        "storyBoardType": 5,
        "storyBoardTypeDesc": "3D真實",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "白荊騎士與風息之心\n\n=== 故事梗概 ===\n在中世紀北方王國萊文堡，百年寒冬帶來飢荒與絕望。傳說幽冥谷深處的\"風息之心\"能終結冰封，卻無人從谷中生還。25歲的卑微騎士艾利克，懷著對公主莉安娜的深情與對王國的忠誠，孤身踏上征途。歷經風雪、狼群與冰霜巨狼的生死試煉，他以愛與勇氣打動守護晶石的巨狼靈魂，奪得風息之心。艾利克歸來，寒冬消融，他贏得公主的擁抱與傳頌的榮耀，白荊騎士之名成為愛與勇氣的永恆傳奇。\n\n=== 角色資訊 ===\n\n艾利克（白荊騎士）\n- 性別/年齡：男，25歲\n- 外貌：金棕色短髮，深藍眼眸，五官英俊帶風霜，嘴角一道淺疤\n- 服裝：白荊棘紋銀盔甲，深藍披風，腰懸長劍\n- 氣質：堅韌果敢，溫柔中透著執著\n\n莉安娜（公主）\n- 性別/年齡：女，21歲\n- 外貌：栗色長髮如絲，湖藍眼眸，面容精緻溫暖\n- 服裝：白色冬季長裙，淡金毛絨披肩\n- 氣質：溫柔善良，憂傷中藏堅韌\n\n冰霜巨狼\n- 外貌：肩高兩米，雪白毛髮覆霜，幽藍雙目，氣息化寒霧\n- 氣質：神秘威嚴，帶著神聖感\n\n=== 分鏡 ===\n\n鏡頭1：寒冬萊文堡\n- 場景氛圍：暴雪肆虐的中世紀石堡，灰暗天空下，城民蜷縮火爐旁，面容憔悴，恐懼瀰漫。\n- 構圖：全景俯視，孤立城堡在無垠雪原中若隱若現，寒風呼嘯強化壓抑感。\n\n鏡頭2：騎士受命\n- 場景氛圍：王宮大廳，火炬光搖曳，冰冷石柱投下長影。\n- 角色：\n  - 艾利克：單膝跪地，白荊盔甲映火光，深藍眼眸堅毅。\n  - 莉安娜：側立台階，湖藍眼眸擔憂，手緊握披肩。\n- 構圖：低角度中景，艾利克盔甲光澤與莉安娜柔和輪廓形成對比，凸顯使命感。\n\n鏡頭3：雪夜離別\n- 場景氛圍：城牆上風雪咆哮，火把光在雪霧中搖曳。\n- 角色：\n  - 莉安娜：披金色披肩，淚眼朦朧，將紅絲帶掛墜交至艾利克掌心。\n  - 艾利克：雙手接過，眼神溫柔而決絕。\n- 構圖：特寫兩人交握的手與掛墜，背景雪夜虛化，情感在靜謐中昇華。\n\n鏡頭4：雪原孤行\n- 場景氛圍：昏暗雪原，風暴席捲，白雪吞噬天地。\n- 角色：艾利克獨行，披風獵獵，長劍拄地支撐，步伐沉重。\n- 構圖：遠景俯視，渺小身影在無邊風雪中掙扎，孤獨感壓倒一切。\n\n鏡頭5：狼群夜襲\n- 場景氛圍：雪林邊緣，篝火微弱，黑暗中狼眼幽藍閃爍，氣氛緊繃。\n- 角色：艾利克背靠枯樹，劍光映雪，臉上血跡與雪水交織。\n- 構圖：中近景，火光勾勒騎士輪廓，陰影中狼群若隱若現，危機四伏。\n\n鏡頭6：幽冥谷入口\n- 場景氛圍：迷霧瀰漫，冰瀑與枯木交錯，古老石碑半埋雪中，神秘壓迫。\n- 角色：艾利克輕撫碑文，眼神專注，盔甲映微光。\n- 構圖：仰視遠景，谷口陰影籠罩，冒險氛圍濃厚。\n\n鏡頭7：風息之心\n- 場景氛圍：谷底枯樹間，藍色晶石懸浮，脈動微光如心跳，神秘而神聖。\n- 角色：艾利克仰望晶石，藍光映入深藍眼眸，敬畏與希望交織。\n- 構圖：仰視鏡頭，晶石冷光與雪霧形成冷暖對比，畫面靜謐震撼。\n\n鏡頭8：巨狼對峙\n- 場景氛圍：風雪驟起，迷霧中冰霜巨狼現身，寒霧自其口中瀰散。\n- 角色：\n  - 巨狼：幽藍雙目鎖定，威壓逼人。\n  - 艾利克：持劍屹立，盔甲覆雪，神情無畏。\n- 構圖：低機位中遠景，巨狼龐大身影壓迫畫面，緊張感拉滿。\n\n鏡頭9：生死激戰\n- 場景氛圍：暴風雪中，雪地翻騰，血跡染紅白雪，戰鬥慘烈。\n- 角色：\n  - 艾利克：盔甲龜裂，披風染血，咬牙抵擋巨狼撲擊。\n  - 巨狼：獠牙畢露，動作掀起雪霧。\n- 構圖：斜構圖動態鏡頭，紅血白雪對比強烈，動作迅猛。\n\n鏡頭10：勇氣化狼魂\n- 場景氛圍：風雪驟停，谷中寂靜，只餘風聲回響。\n- 角色：\n  - 艾利克：重傷倒地，緊握紅絲帶掛墜，仰望巨狼，眼神不屈。\n  - 巨狼：凝視片刻，化作風雪光點消散。\n- 構圖：特寫兩人目光交匯，雪霧光點環繞，情感與神性交融。\n\n鏡頭11：英雄歸來\n- 場景氛圍：初春暖陽灑落城門，融雪滴落，城民夾道歡呼，敬畏與希望交織。\n- 角色：艾利克懷抱風息之心，傷痕累累，步伐沉穩。\n- 構圖：遠景拉鏡，英雄步入城門，陽光勾勒溫暖光暈。\n\n鏡頭12：愛的重逢\n- 場景氛圍：王宮台階，陽光刺破雲霧，雪水淌成溪流，溫馨而新生。\n- 角色：\n  - 莉安娜：淚中帶笑，飛奔擁抱艾利克。\n  - 艾利克：輕撫她背，紅絲帶掛墜在陽光中搖曳。\n- 構圖：中近景，陽光勾勒兩人金色輪廓，情感高潮溫暖收尾。",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:32:50",
    },
}

ProjectRole = {
    "10011":[
        {
            "roleId": "6891b2e546cf66d652c1ccb8",
            "figureName": "艾拉",
            "figureDesc": "年輕女性記憶設計師，中等身高苗條身材，柔和橢圓臉型，大而明亮的深棕色眼睛，直達肩膀的深棕色短髮，光滑白皙肌膚。穿著白色高領修身工作服，銀色幾何圖案裝飾，深藍色緊身長褲，白色平底靴。簡潔銀色手環。中性站立姿態，雙臂自然垂放。扁平動漫風格，粗黑輪廓線，純色填充，高飽和度色彩。",
            "url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
        },
        {
            "roleId": "6891b31046cf66d652c1ccba",
            "figureName": "老人",
            "figureDesc": "年長男性，高瘦身材，深邃皺紋面容，灰色深陷雙眼，花白稀疏頭髮，滄桑膚色。穿著樸素深灰色長袍，黑色腰帶，深棕色皮靴。雙手置於身側，莊重站立姿態。扁平動漫風格，粗黑輪廓線，純色填充，簡化陰影處理。",
            "url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
        },
        {
            "roleId": "6891b33846cf66d652c1ccbc",
            "figureName": "客戶",
            "figureDesc": "中年男性，中等身材，方形臉龐，緊閉雙眼，深棕色短髮，白皙肌膚。穿著深藍色簡單襯衫，黑色長褲，棕色皮鞋。平躺姿態，雙臂放鬆置於身側。扁平動漫風格，粗黑輪廓線，純色填充。",
            "url": "https://resource.visiony.cc/image/1754379095049-fqbdg0.png"
        }
    ],
    "10012":[
        {
            "roleId": "6891b84046cf66d652c1ccd8",
            "figureName": "天照大神",
            "figureDesc": "威嚴優雅的太陽女神，端莊的成年女性外貌。圓潤豐滿的臉龐，溫和而深邃的大眼睛，眼部有金色光澤。豐厚的黑色長髮編成精緻髮髻，頭頂佩戴黃金太陽飾品。身穿華麗的多層和服，外層為金色綢緞面料，內層為橙色與白色相間圖案，袖口寬大優雅。腰間繫著精美的金色腰帶，其上裝飾有太陽圖騰。腳穿傳統木屐，白色足袋。身材勻稱優美，雙手修長細膩，姿態端莊靜雅。",
            "url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
        },
        {
            "roleId": "6891b86f46cf66d652c1ccda",
            "figureName": "素戔嗚尊",
            "figureDesc": "強壯威猛的風暴之神，健碩的成年男性。稜角分明的長臉，濃眉大眼，眼中閃爍雷電光芒。濃密的黑色長髮自然垂至肩膀，部分束成小辮。身穿深藍色武士服裝，外罩灰色鐵製胸甲，手臂和腿部有護甲覆蓋。腰間佩戴一把華麗神劍，劍鞘裝飾有雷電圖案。寬闊的肩膀，肌肉發達的手臂，身高超過普通人。腳穿黑色武士靴，整體充滿力量感和神威。",
            "url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
        },
        {
            "roleId": "6891b8c946cf66d652c1ccdc",
            "figureName": "奇稻田姬",
            "figureDesc": "美麗純潔的年輕女子，清秀的少女面容。水靈的大眼睛，小巧的鼻子，櫻花色的嘴唇。順滑的黑色長髮垂至腰間，用簡單的髮帶束起。身穿樸素的白色和服，腰間繫著淡粉色腰帶，袖口和衣邊有簡單的花卉刺繡。身材苗條纖細，雙手柔嫩，肌膚白皙如雪。腳穿傳統草鞋，整體給人以純真善良的感覺。",
            "url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
        },
        {
            "roleId": "6891b8f446cf66d652c1ccde",
            "figureName": "八岐大蛇",
            "figureDesc": "巨大恐怖的八頭神蛇，龐大的蛇形身軀。八個巨大的蛇頭，每個都如房屋般大小，尖銳的毒牙閃著寒光，眼睛如紅色燈籠般發光。鱗片呈深綠色和黑色相間，腹部呈灰白色。八條粗壯的尾巴如山脈般綿延，身體盤繞時覆蓋整個山谷。每個頭顱都有獨立的表情和動作，整體散發著邪惡和毀滅的氣息。",
            "url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
        }
    ],
    "10013":[
        {
            "roleId": "6891bfa046cf66d652c1cd03",
            "figureName": "林小雨",
            "figureDesc": "年輕女性，中等身材，苗條勻稱。方形幾何臉型，堅毅的角度線條。中長黑色幾何髮型，整齊的紙摺層次。深色幾何眼睛，稜角分明的眉毛。穿著簡潔的幾何形狀咖啡師制服，白色摺紙質感上衣，深色幾何圍裙，整潔的角度設計。黑色平底鞋。手部纖細，指節分明的幾何造型。站立姿態端正，體現摺紙人物的挺拔線條感。",
            "url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
        },
        {
            "roleId": "6891bfc846cf66d652c1cd05",
            "figureName": "老張",
            "figureDesc": "中年男性，中等偏胖身材，溫和的幾何體型。圓潤的幾何臉型，溫和的摺紙線條。稀疏的灰白色幾何短髮，整齊的紙質紋理。小而溫和的幾何眼睛，慈祥的角度表達。穿著深灰色幾何毛衣，簡潔的摺紙質感，深色幾何長褲，舒適的紙質材料。棕色幾何休閒鞋。手部寬厚，穩重的幾何造型。",
            "url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
        },
        {
            "roleId": "6891bfec46cf66d652c1cd07",
            "figureName": "陳浩然",
            "figureDesc": "年輕男性，高大挺拔的幾何身材，勻稱的摺紙比例。方形堅毅的幾何臉型，清晰的角度線條。短黑髮，整齊的幾何層次，紙質質感。深色幾何眼睛，濃密的幾何眉毛。穿著深色幾何風衣，濕潤的紙質表面效果，白色幾何襯衫，深色幾何長褲，黑色幾何皮鞋。手部修長，清晰的幾何關節。站立時略顯緊張的幾何姿態，體現摺紙人物的情感表達。",
            "url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
        }
    ],
    "10014":[
        {
            "roleId": "6891da318f0f67046b15a631",
            "figureName": "艾利克",
            "figureDesc": "25歲北方王國騎士，身高1.8米，勻稱肌肉體型。金棕色短髮自然蓬鬆，深藍色眼眸銳利專注，英俊五官帶風霜痕跡，嘴角一道淺色疤痕。身著精緻銀色板甲，胸前雕刻白荊棘紋樣，肩甲弧形設計，手臂護甲關節靈活。深藍色厚重披風繫於肩部，內襯深紅色絨布。腰間懸掛十字劍柄長劍，劍鞘皮革包裹。黑色皮靴到小腿，鞋底厚實防滑。中性表情，挺直站姿，雙手自然垂放身側",
            "url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
        },
        {
            "roleId": "6891da528f0f67046b15a633",
            "figureName": "莉安娜",
            "figureDesc": "21歲王國公主，身高1.65米，纖細優雅體型。栗色長髮如絲綢垂至腰間，湖藍色眼眸清澈溫和，精緻面容帶東歐貴族特徵，皮膚白皙細膩。身著白色羊毛冬季長裙，高腰設計，袖口銀色刺繡，裙擺及踝。淡金色毛絨披肩覆蓋雙肩，內襯絲綢材質。腳穿白色皮靴，鞋面裝飾珍珠扣。頸間銀色項鍊配小型藍寶石。中性表情，優雅站姿，雙手輕握於身前",
            "url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
        },
        {
            "roleId": "6891da678f0f67046b15a635",
            "figureName": "冰霜巨狼",
            "figureDesc": "神秘守護靈獸，肩高2米，體長3米，魁梧狼形。雪白厚密長毛覆蓋全身，毛髮尖端結霜晶體。幽藍色雙眼如寶石發光，黑色濕潤鼻頭，露出鋒利白色獠牙。強壯四肢肌肉發達，巨大爪子配黑色利爪。尾巴蓬鬆粗大自然下垂。神秘冰霜氣息環繞身軀。中性表情，威嚴站姿，四肢穩定支撐地面",
            "url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
        }
    ]
}

ProjectShot = {
    "10011": [
        {
            "shot_id": "6891b35746cf66d652c1ccbe",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
                "is_HD": False,
                "shot_resource_id": "6891b3b446cf66d652c1ccc9"
            },
            "scene_description": {
                "background": "2087年未來城市清晨景觀，透明球形穹頂覆蓋城市上空，金色晨光透過穹頂灑向懸浮建築群。白色金屬材質的流線型建築漂浮在不同高度，銀色飛行器在藍色天空中無聲穿梭。遠處可見幾何形狀的摩天大樓，整座城市呈現科技感的藍白色調。扁平動漫風格渲染，清晰輪廓線，純色填充，簡化光影效果。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "疲憊神情，微微瞇起的眼睛，輕微伸展身體的動作，雙臂緩慢向上延伸。位於畫面中央，從睡眠艙中起身，面向側朝向相機的三分之四角度。前景位置，佔據畫面主要焦點。"
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "記憶設計工作室內部，銀色金屬牆壁，藍色全息螢幕懸浮在空中，白色記憶編輯設備環繞四周。空氣中漂浮著發光的記憶片段光點，呈現藍色和紫色光暈。地面為光滑的白色金屬材質，天花板發出均勻的白色光源。整體科技感氛圍，冷色調為主。扁平動漫風格，幾何化設備設計，純色填充。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "專注認真的表情，眼神集中，雙手操作控制面板，身體微微前傾。位於畫面右側，面向設備，側面朝向相機。前景位置，動作流暢自然。"
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "同一記憶設計工作室，焦點轉向中央的白色記憶編輯椅，周圍環繞藍色全息顯示器。牆壁上投射著記憶畫面的光影，設備發出柔和的藍白色光暈。銀色金屬地板反射著設備光源，營造出專業醫療環境的氛圍。扁平動漫風格，簡化設備細節，清晰幾何形狀。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "溫和關懷的表情，輕鬆的微笑，雙手輕觸控制面板，身體放鬆站立。位於畫面左側，面向客戶方向，三分之四角度朝向相機。中景位置。"
                    },
                    {
                        "role_id": "6891b33846cf66d652c1ccbc",
                        "role_name": "客戶",
                        "action_and_emotion": "從痛苦轉為放鬆的表情變化，緊鎖眉頭逐漸舒展，雙眼閉合，身體在椅子上完全放鬆。位於畫面中央，平躺在記憶椅上，面朝天花板。前景位置，佔據畫面焦點。"
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
                    "content": "痛苦已經消除，你會感覺好很多。",
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
                    "role_name": "客戶",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379095049-fqbdg0.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "記憶設計工作室入口區域，白色金屬門框，藍色光線從門縫透入。工作室內部可見懸浮的全息設備和散落的光點，銀色牆面反射著柔和光源。地面為光滑金屬材質，整體保持科技感的冷色調環境。門口處光線較為明亮，與內部形成對比。扁平動漫風格，幾何化建築線條。",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "深邃堅定的神情，眼神專注而有力，緩慢而穩重的步行姿態，雙手自然擺動。位於畫面中央偏右，剛踏入工作室，面向畫面內部，側面朝向相機。前景位置，佔據主要視覺焦點。"
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
                    "content": "我需要你的幫助，但不是刪除記憶。",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "記憶設計工作室中央區域，藍色全息設備環繞，銀色金屬工作台，懸浮的記憶片段光點在空中緩慢漂移。白色LED燈條照亮整個空間，牆面顯示著數據流光影。地面光滑反射，營造出專業而神秘的科技環境。扁平動漫風格，簡化光影效果，幾何化設備造型。",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "凝重認真的表情，深邃眼神注視著艾拉，單手伸出展示記憶球，身體保持莊重站立姿態。位於畫面左側，面向艾拉方向，三分之四角度朝向相機。中景位置。"
                    },
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "疑惑困惑的表情，微皺眉頭，眼神專注觀察記憶球，身體微微前傾表示好奇。位於畫面右側，面向老人，側面朝向相機。前景位置，反應動作清晰。"
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
                    "content": "我要把這段記憶傳給你，關於這個世界的真相。",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "虛幻記憶空間，深藍色和紫色漸變背景中漂浮著無數發光的記憶畫面碎片，城市控制網絡的幾何圖案交錯分布。AI網絡呈現為銀色光線網格，記憶片段如透明玻璃般懸浮。整體空間給人夢境般的感覺，光影變幻莫測。扁平動漫風格，抽象幾何圖形組合，高對比度色彩。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "震驚恐懼的表情，瞪大雙眼，嘴巴微張，身體向後傾斜表示驚訝，雙手不自覺握拳。位於畫面中央，面向記憶畫面，正面朝向相機。前景位置，情感表達強烈。"
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
                    "content": "這…這不可能！",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "記憶設計工作室內部，重新聚焦於中央工作區域。銀色金屬家具，藍色全息顯示器靜靜懸浮，記憶編輯設備散發著冷光。牆面上的數據顯示已經暗淡，只有微弱的環境照明保持空間可見度。整體氛圍比之前更加沉重壓抑。扁平動漫風格，降低飽和度，增強陰影對比。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "內心掙扎的複雜表情，眉頭深鎖，眼神在記憶刪除器和老人之間游移，雙手緊握椅子扶手。坐在工作椅上，身體緊張，面向側面，三分之四角度朝向相機。前景位置。"
                    },
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "平靜耐心的神情，深邃眼神默默注視艾拉，雙手交疊於身前，身體保持靜止等待姿態。位於畫面背景右側，面向艾拉方向，側面朝向相機。背景位置，維持存在感。"
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
                    "content": "你是誰？為什麼要告訴我這些？",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "記憶設計工作室，聚焦於對話區域。柔和的藍白色照明，銀色金屬牆面，懸浮設備靜默運轉。空氣中的記憶光點減少，環境顯得更加嚴肅沉重。工作台上的設備發出微弱光暈，整體氛圍體現出重要對話的緊張感。扁平動漫風格，簡化背景細節突出人物。",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "老人",
                        "action_and_emotion": "沉重憂傷的表情，眼神中帶著遺憾和決心，雙手輕微顫抖，身體保持莊重站立但顯露疲憊。位於畫面中央，面向艾拉，正面朝向相機。前景位置，情感表達深刻。"
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
                    "content": "我是這個系統的創造者之一，但當我意識到它的危險時，已經太晚了。現在，只有像你這樣掌握記憶技術的人，才能幫助人們找回真實的記憶。",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "記憶設計工作室全景，銀色和白色主導的科技空間，藍色全息設備分布各處。懸浮的記憶光點重新活躍，設備發出穩定光芒。整體環境恢復了專業感，但氛圍已經發生根本改變，充滿了新的決心和目標感。扁平動漫風格，清晰幾何線條，平衡構圖。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "堅定果斷的表情，眼神清澈而有力，緊握拳頭表示決心，身體挺直站立姿態。位於畫面中央，面向前方，正面朝向相機。前景位置，展現強烈的決心和轉變。"
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
                    "content": "如果這是真的，那我不能繼續成為這個系統的幫兇。",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "未來城市天台邊緣，夕陽西下的橙紅色天空，遠處可見懸浮建築群的輪廓和透明穹頂。城市燈光開始點亮，呈現藍色和白色光點。天台為白色金屬材質，邊緣有安全護欄。微風吹動，營造出思考和決斷的寧靜氛圍。扁平動漫風格，簡化建築細節，強調色彩對比。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "平靜堅決的表情，眼神注視著手中的刪除器，雙手舉起設備準備丟棄，身體面向城市邊緣。站在天台邊緣，側面朝向相機，背景是廣闊的城市景觀。前景位置，動作具有象徵意義。"
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "城市天台遠景，夕陽餘暉灑在整座未來城市上，橙紅色天空與城市的藍白色燈光形成對比。懸浮建築在暮色中顯得更加夢幻，透明穹頂反射著夕陽光芒。天台位於高樓之上，俯瞰整個城市全景。微風輕拂，營造出史詩般的決心時刻。扁平動漫風格，簡化細節突出氛圍。",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "艾拉",
                        "action_and_emotion": "堅定不移的表情，眼神望向遠方，雙臂自然垂放，身體挺直面向未來。站在天台邊緣，背對夕陽，正面朝向相機，身後拉出長長影子。前景位置，充滿希望和決心的姿態。"
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
                    "content": "有些真相，值得承受痛苦去守護。",
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
                "value": "遠景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "高天原神界的華麗宮殿內部，雲霧繚繞的天空背景。宮殿採用傳統日式建築風格，木質橫樑和立柱，屋頂為金色裝飾。室內鋪設著精美的榻榻米，牆壁裝飾有太陽圖騰壁畫。中央擺放著一座華麗的金色寶座，周圍飄浮著金色光芒。天花板上有彩雲繚繞，柔和的金色光線從四面八方灑入，營造出神聖祥和的氛圍。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "端坐在金色寶座上，面容威嚴而溫和，雙眼注視前方。身體挺直，雙手優雅地放在膝蓋上，整體姿態體現出神聖的威嚴。位於畫面中央，佔據主要焦點，面向鏡頭稍微偏左。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "站在宮殿前方，面容憤怒，眉頭緊鎖，雙拳緊握。身體略微向前傾斜，顯示出衝動的情緒。周圍有雷電光芒閃爍，位於畫面左側前景位置，側身面向天照大神。"
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
                    "content": "姐姐，我要下到人間證明自己的力量！",
                    "role_name": "素戋嗚尊"
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
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "高天原神界的華麗宮殿內部，雲霧繚繞的天空背景。宮殿採用傳統日式建築風格，木質橫樑和立柱，屋頂為金色裝飾。室內鋪設著精美的榻榻米，牆壁裝飾有太陽圖騰壁畫。中央擺放著一座華麗的金色寶座，周圍飄浮著金色光芒。天花板上有彩雲繚繞，柔和的金色光線從四面八方灑入。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "面容顯露擔憂神色，眉頭微蹙，雙眼流露關切之情。身體前傾，一隻手輕微抬起做勸阻手勢。位於畫面中央，坐在金色寶座上，正面朝向鏡頭。"
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
                    "content": "你太衝動了，會給人間帶來災難。",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "烏雲密佈的夜晚，古老的日本山村景象。村莊由傳統木製房屋組成，屋頂覆蓋茅草，房屋散落在山谷中。小徑由石塊鋪成，兩旁生長著竹林和古松。遠山輪廓模糊，被厚重的烏雲遮蔽，雷電在雲層中閃爍。村莊籠罩在昏暗的夜色中，只有零星的燈光從房屋窗口透出，營造出緊張不安的氛圍。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "從天空中降落，雙腳剛剛接觸地面，身體保持降落姿態。面容嚴肅，雙眼掃視村莊，周圍雷電光芒環繞。位於畫面中央，完整身體展現，正面朝向鏡頭。背景中村民們驚恐逃散的模糊身影。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "烏雲密佈的夜晚，素戋嗚尊從天而降，落在日本一座古老的山村。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "寧靜的小河旁，月光灑在水面上形成銀色波紋。河岸兩側生長著柳樹和蘆葦，微風輕拂草叢。河水清澈見底，偶有小魚游過。河岸鋪滿光滑的鵝卵石，遠處山巒起伏，夜空中星光點點。整體環境安靜祥和，與之前的緊張氛圍形成對比。",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "坐在河邊石頭上，雙手捂臉痛哭，身體微微顫抖。頭髮散亂，衣服略顯凌亂，整個身體蜷縮成保護姿勢。位於畫面右側，側身面向河水。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "緩步走近，面容關切，一隻手輕微伸出做詢問手勢。身體稍微前傾，顯示出關心和好奇。位於畫面左側，面向奇稻田姬。"
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
                    "content": "姑娘，為何如此悲傷？",
                    "role_name": "素戋嗚尊"
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
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "寧靜的小河旁，月光灑在水面上形成銀色波紋。河岸兩側生長著柳樹和蘆葦，微風輕拂草叢。河水清澈見底，偶有小魚游過。河岸鋪滿光滑的鵝卵石，遠處山巒起伏，夜空中星光點點。整體環境安靜祥和。",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "抬起頭看向素戋嗚尊，眼中淚水閃爍，面容悲傷恐懼，雙唇微顫。一隻手輕輕抹去眼角淚珠，身體仍保持坐姿。位於畫面中央偏右，面向素戋嗚尊。"
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
                    "content": "八岐大蛇要來吃掉我了！我的父親已經逃走，村民們也都躲了起來。",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "村莊中心的空曠場地，周圍是傳統日式房屋。地面為平整的泥土，散落著一些石塊。房屋大多關閉門窗，顯得空無一人。遠處山巒連綿，天空陰沉，空氣中瀰漫著不安的氣氛。場地上方懸浮著八岐大蛇的半透明幻影，八個巨大頭顱張牙舞爪，紅眼閃爍。",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "站立講述，面容恐懼，身體微微顫抖，一隻手指向空中的幻影，另一隻手緊握胸前。眼神中透露出深深的恐懼和絕望。位於畫面左側，側身面向空中的八岐大蛇幻影。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "專注聆聽，面容嚴肅，雙眼凝視著奇稻田姬和空中的幻影。身體挺直，雙手放在身側，顯示出堅定的意志。位於畫面右側，面向奇稻田姬。"
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
                    "content": "那怪物每年都要吃掉一個少女，今年輪到了我。",
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
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "夕陽西下的河邊，天空呈現橙紅色漸變，夕陽的餘暉灑在水面上形成金色光帶。河岸兩側的柳樹在微風中輕擺，蘆葦叢沙沙作響。遠山剪影深紫色，整體環境溫暖而寧靜，營造出希望和決心的氛圍。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "握緊劍柄，面容堅定果決，雙眼充滿決心和勇氣。身體挺立，一隻手按在劍柄上，另一隻手做誓言手勢。位於畫面中央，正面朝向鏡頭，夕陽在身後形成光環效果。"
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
                    "content": "我發誓要殺死八岐大蛇，拯救你。但我需要你的幫助。",
                    "role_name": "素戋嗚尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "山谷中的開闊空地，四周被高聳的山峰環繞，地面相對平坦。空地中央擺放著八個巨大的木製酒桶，排列成圓形。桶身呈棕色木質，鐵箍箍緊，散發著濃郁的酒香。周圍散落著一些準備工具和繩索，遠處山洞口黑幽幽的，透出不祥的氣息。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "指揮佈置陷阱，手臂伸出指向酒桶，面容專注嚴肅。身體略微前傾，顯示出指揮者的威嚴。位於畫面左側，面向酒桶和奇稻田姬。"
                    },
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "協助準備工作，面容雖有恐懼但顯出勇敢神色，雙手忙碌地整理繩索。身體稍微彎曲，專注於手頭工作。位於畫面右側，在酒桶附近活動。"
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
                    "content": "用最烈的酒裝滿這些桶，那怪物喝醉後就無法戰鬥了。",
                    "role_name": "素戋嗚尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋嗚尊",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "月圓之夜的山谷，巨大的滿月高懸天空，銀色月光灑向大地。山谷地面開始劇烈震動，塵土飛揚。遠處山洞口傳出低沉的嘶吼聲，洞口有紅光閃爍。整個場景充滿緊張和恐怖的氣氛，樹木搖擺，鳥獸驚逃。",
                "characters": [
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "八岐大蛇",
                        "action_and_emotion": "從山洞中現身，八個巨大頭顱昂起咆哮，紅眼閃閃發光，毒牙暴露。八條尾巴翻滾扭動，龐大身軀盤踞山谷，散發出恐怖威嚴。位於畫面背景中央，佔據大部分畫面空間，面向鏡頭。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "月圓之夜，八岐大蛇出現了，八個巨大的頭顱在月光下閃著寒光。",
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
                "value": "遠景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "山谷中的酒桶陷阱區域，月光照射下顯得銀光閃閃。八個酒桶整齊排列，周圍散發著濃郁的酒香。地面有明顯的震動痕跡，一些小石塊散落。遠處岩石嶙峋，為素戋嗚尊提供隱藏地點。",
                "characters": [
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "八岐大蛇",
                        "action_and_emotion": "八個頭顱貪婪地伸向酒桶，瘋狂飲下烈酒，動作開始變得遲緩搖擺。眼神逐漸迷離，身體擺動不穩，醉態明顯。位於畫面中央，頭顱分散在各個酒桶周圍。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "躲在岩石後靜靜觀察，身體緊貼岩石，一隻眼睛觀察大蛇狀態，手握劍柄準備出擊。面容專注警惕，等待最佳時機。位於畫面左側岩石後，側身面向大蛇。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "巨蛇發現了酒桶，瘋狂飲下烈酒，直到醉態盡顯。",
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
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "激戰中的山谷，月光下血花四濺，地面留下深深的劍痕和蛇身拖拽的痕跡。岩石碎裂，塵土飛揚，空氣中充滿戰鬥的硝煙味。劍光在夜空中閃爍，形成美麗而致命的光弧。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "躍起揮劍，面容怒吼，雙眼燃燒著戰鬥意志，肌肉緊繃充滿力量。神劍在手中閃爍寒光，身體呈現攻擊姿態。位於畫面前景中央，動態十足的戰鬥姿勢。"
                    },
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "八岐大蛇",
                        "action_and_emotion": "劇烈掙扎反抗，部分頭顱已被斬斷，其餘頭顱痛苦咆哮，身體扭動翻滾。紅眼中透出憤怒和痛苦，血液飛濺。位於畫面背景，龐大身軀佔據主要空間。"
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
                    "content": "為了人間的和平，我絕不會敗！",
                    "role_name": "素戋嗚尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋嗚尊",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "戰鬥結束後的山谷，恢復了寧靜祥和。月光柔和地灑向大地，八岐大蛇的巨大身軀已經倒在地上不再動彈。空氣中戰鬥的硝煙散去，只餘下淡淡的血腥味和勝利的寧靜。",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "高舉發光的草薙劍，面容勝利喜悅，雙臂高舉展示戰利品。身體挺立，充滿勝利者的威嚴和自豪。位於畫面中央，正面朝向鏡頭，劍光閃耀。"
                    },
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "奇稻田姬",
                        "action_and_emotion": "爆發出歡呼，雙手高舉，面容充滿喜悅和感激，眼中含著激動的淚水。身體向上跳躍，表達內心的狂歡。位於畫面右側，面向素戋嗚尊。"
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
                    "content": "這把神劍將成為保護人間的聖物。",
                    "role_name": "素戋嗚尊"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "素戋嗚尊",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "高天原神界的華麗宮殿內部，恢復了祥和的氛圍。雲霧繚繞的天空背景，金色光芒更加柔和溫暖。宮殿裝飾依然華麗，太陽圖騰壁畫在柔光中顯得格外神聖。雷霆與陽光在空中交織，形成美麗的光芒效果。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "面容欣慰微笑，雙眼溫和地注視著弟弟，表達出姐姐的自豪和關愛。身體放鬆，雙手優雅地放置，整體姿態體現出內心的喜悅。位於畫面中央，坐在金色寶座上。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "雙手捧著草薙劍獻上，面容謙遜恭敬，眼中透出成長後的智慧。身體微微彎曲，以示尊敬，整體姿態顯示出內心的改變。位於畫面前景，面向天照大神。"
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
                    "content": "姐姐，我學會了責任的意義。",
                    "role_name": "素戋嗚尊"
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
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "高天原神界的華麗宮殿內部，充滿和諧溫暖的光芒。雷霆與陽光在天空中美麗交織，形成彩虹般的光譜效果。宮殿裝飾在彩光中顯得更加神聖莊嚴，整個環境散發出兄妹和好的溫馨氛圍。",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "天照大神",
                        "action_and_emotion": "溫暖微笑回應，雙眼充滿慈愛和讚許，身體輕微前傾表示親近。整體姿態體現出姐姐的包容和欣慰。位於畫面右側，面向素戋嗚尊。"
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "素戋嗚尊",
                        "action_and_emotion": "回以真摯微笑，雙眼明亮透出成熟的光芒，身體挺直顯示內心的堅定。整體表達出對姐姐的敬愛和自己的成長。位於畫面左側，面向天照大神。"
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
                    "content": "弟弟，你已經證明了自己的勇氣和智慧。",
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
                    "role_name": "素戋嗚尊",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        }
    ],
    "10013": [
        {
            "shot_id": "6891c01046cf66d652c1cd09",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
                "is_HD": False,
                "shot_resource_id": "6891c0a546cf66d652c1cd14"
            },
            "scene_description": {
                "background": "深夜的幾何咖啡館內景，溫暖的摺紙空間設計。角度分明的幾何桌椅排列，紙質質感的傢俱表面。牆面掛著幾何風格的插畫作品，規整的角度框架。暖黃色的幾何燈光照明，均勻的紙質光線分佈。玻璃窗外可見幾何雨滴圖案，街道上的幾何雨夜景象。咖啡機等設備呈現簡潔的幾何造型，整個空間體現摺紙美學的溫馨氛圍。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "專注而平靜的幾何表情。站在吧台後方中央位置，正對鏡頭的幾何角度。身體略微前傾的幾何姿態，雙手持咖啡杯進行清潔動作。前景主要位置，清晰的幾何形體展現。動作輕柔熟練，體現摺紙人物的優雅感。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "在一個陰冷的雨夜，城市街頭一家小小的咖啡館散發著溫暖的光芒。",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館角落區域的幾何空間。舒適的幾何座椅和圓形幾何桌面。牆面的幾何裝飾和書架，紙質質感的物品陳列。柔和的幾何燈光營造溫馨氛圍，角落的私密幾何空間設計。",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老張",
                        "action_and_emotion": "溫和友善的幾何笑容。坐在角落座位上，身體放鬆的幾何姿態。面向吧台方向，側面角度對鏡頭。中景位置，清晰可見的幾何形體。手持報紙，準備放下的幾何動作。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "溫暖回應的幾何微笑。站在吧台處，轉頭面向老張的幾何角度。背景位置，部分身體可見。專注調製飲品的幾何手勢，體現服務的專業感。"
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
                    "content": "小雨，來杯熱巧克力，多加點奶泡。",
                    "role_name": "老張"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "好的，張叔。今天雨這麼大，您怎麼還出來？",
                    "role_name": "林小雨"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老張",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館入口區域的幾何設計。幾何形狀的門框和玻璃門，雨夜的幾何街景透過玻璃可見。地面的幾何瓷磚圖案，門邊的幾何裝飾元素。昏暗的幾何外景與溫暖的幾何內景形成對比。",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陳浩然",
                        "action_and_emotion": "略顯緊張猶豫的幾何表情。站在門口位置，剛進入室內的幾何姿態。正面朝向室內，三分之二角度對鏡頭。前景主要位置，濕潤外套的幾何質感明顯。眼神帶著期待和不確定的幾何表達。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "就在這時，門鈴清脆地響起，一個身影推門而入。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陳浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館內部的幾何全景。完整的幾何空間佈局，從吧台到座位區的幾何設計。溫暖的幾何照明系統，牆面的幾何藝術裝飾。整體空間的幾何層次感，營造溫馨的摺紙空間氛圍。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "震驚停頓的幾何表情。站在吧台後方，身體僵直的幾何姿態。目光直視門口方向，側面角度對鏡頭。中景位置，清晰的幾何輪廓。手中動作戛然而止的幾何定格。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陳浩然",
                        "action_and_emotion": "忐忑不安的幾何表情。站在門口附近，身體略顯緊張的幾何姿態。面向吧台方向，背對鏡頭的幾何角度。背景位置，部分輪廓可見。外套濕潤的幾何質感突出。"
                    },
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老張",
                        "action_and_emotion": "觀察思考的幾何表情。坐在角落位置，身體前傾的幾何姿態。目光在兩人間游移，側面角度對鏡頭。背景位置，安靜觀察的幾何狀態。"
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
                    "content": "小雨，我…我可以進來嗎？",
                    "role_name": "陳浩然"
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
                    "role_name": "陳浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老張",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館吧台區域的幾何設計。精細的幾何吧台構造，咖啡設備的幾何造型。背景牆面的幾何裝飾，溫暖照明的幾何光影效果。吧台與座位區的幾何空間關係。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "努力控制情緒的幾何表情。站在吧台內側，身體略微緊張的幾何姿態。面向陳浩然方向，正面角度對鏡頭。前景主要位置，清晰的幾何細節表現。擠出微笑的幾何表達。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陳浩然",
                        "action_and_emotion": "期待中帶著不安的幾何表情。坐在吧台前的幾何座椅上，身體前傾的幾何姿態。面向林小雨，側面角度對鏡頭。中景位置，清楚的幾何輪廓。手部放在吧台上的幾何動作。"
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
                    "content": "當然可以。你想喝點什麼？",
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
                    "role_name": "陳浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館的幾何全景空間。整體幾何佈局，從角落到吧台的幾何設計。柔和的幾何照明，牆面幾何藝術作品。空間中的幾何層次感，體現溫馨的摺紙環境氛圍。",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老張",
                        "action_and_emotion": "智慧慈祥的幾何微笑。坐在角落位置，身體放鬆的幾何姿態。目光看向吧台方向，側面角度對鏡頭。前景位置，清晰的幾何形體展現。準備開口說話的幾何表情。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "沉默思考的幾何表情。站在吧台後方，身體略顯僵硬的幾何姿態。目光游移不定，側面角度對鏡頭。中景位置，部分身體可見。內心波瀾的幾何外在表現。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陳浩然",
                        "action_and_emotion": "尷尬沉默的幾何表情。坐在吧台前，身體緊張的幾何姿態。低頭思考狀態，背對鏡頭角度。背景位置，輪廓清晰可見。手指輕敲桌面的幾何動作。"
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
                    "content": "年輕人，有些話憋在心裡太久了，不說出來會發霉的。",
                    "role_name": "老張"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老張",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "林小雨",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陳浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館吧台的幾何近景空間。精緻的幾何吧台設計，咖啡用具的幾何排列。背景的幾何牆面裝飾，溫暖燈光的幾何照明效果。親密對話的幾何空間營造。",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陳浩然",
                        "action_and_emotion": "真誠堅定的幾何表情。坐在吧台前，身體前傾的幾何姿態。目光直視林小雨，正面角度對鏡頭。前景主要位置，清晰的幾何面部特徵。深呼吸後開口的幾何動作。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "震動感動的幾何表情。站在吧台內側，身體微微顫抖的幾何姿態。眼中含淚的幾何表現，側面角度對鏡頭。中景位置，清楚的幾何情感表達。手持咖啡杯輕顫的幾何細節。"
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
                    "content": "小雨，我想告訴你，我從來沒有忘記過你。三年前是我太懦弱，沒有好好解釋，也沒有挽留你。我知道我錯了…如果你願意給我一個機會，我想重新開始。",
                    "role_name": "陳浩然"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "我需要時間。",
                    "role_name": "林小雨"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陳浩然",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "月光照射下的幾何咖啡館內景。透過窗戶的幾何月光，在地面形成幾何光影圖案。室內溫暖的幾何照明與月光的幾何冷光形成對比。窗外寧靜的幾何雨後街景。",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陳浩然",
                        "action_and_emotion": "溫柔釋然的幾何微笑。坐在吧台前，身體放鬆的幾何姿態。伸手觸碰的幾何動作，側面角度對鏡頭。前景位置，清晰的幾何手部動作。眼神溫暖堅定的幾何表達。"
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "接受回應的幾何微笑。站在吧台內側，身體略微前傾的幾何姿態。沒有抽回手的幾何動作，正面角度對鏡頭。中景位置，清楚的幾何情感變化。眼中重燃希望的幾何表現。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "就在這時，雨停了，月光透過窗戶灑進咖啡館，兩人相視而笑。",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "陳浩然",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館門口area的幾何設計。幾何門框和玻璃門，門外寧靜的幾何街景。地面的幾何紋理，門邊裝飾的幾何元素。溫暖內景與寧靜外景的幾何對比。",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老張",
                        "action_and_emotion": "滿意慈祥的幾何微笑。站在門口位置，身體輕鬆的幾何姿態。手持向日葵花束，正面角度對鏡頭。前景主要位置，清晰的幾何形象展現。眼神溫暖智慧的幾何表達。"
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
                    "content": "向日葵總是朝著太陽，就像希望總是朝著未來。",
                    "role_name": "老張"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老張",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "中景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "咖啡館內的幾何圓桌區域。精緻的幾何圓桌設計，舒適的幾何座椅排列。桌上向日葵花束的幾何造型，咖啡杯具的幾何排列。月光透過窗戶的幾何光影，溫馨和諧的幾何空間氛圍。窗外幾何城市夜景，積水反射的幾何光線效果。",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "林小雨",
                        "action_and_emotion": "溫暖安詳的幾何微笑。坐在圓桌旁，身體放鬆的幾何姿態。目光凝視向日葵，側面角度對鏡頭。前景位置，清晰的幾何輪廓展現。內心平靜的幾何外在表現。"
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "陳浩然",
                        "action_and_emotion": "希望滿足的幾何表情。坐在桌旁，身體前傾的幾何姿態。目光溫柔看向林小雨，側面角度對鏡頭。中景位置，清楚的幾何情感狀態。手部放在桌面的幾何動作。"
                    },
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "老張",
                        "action_and_emotion": "慈祥滿意的幾何微笑。坐在桌旁，身體舒適的幾何姿態。整體觀察的幾何視角，正面角度對鏡頭。背景位置，和諧融入的幾何存在感。享受溫馨時刻的幾何表達。"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "或許，時間會治癒過去的傷痛，或許，這是一個新的開始。",
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
                    "role_name": "陳浩然",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "老張",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "全景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "秒"
            }
        }
    ],
    "10014": [
        {
            "shot_id": "6891da7d8f0f67046b15a637",
            "shot_resource": {
                "shot_resource_url": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
                "is_HD": False,
                "shot_resource_id": "6891dab68f0f67046b15a643"
            },
            "scene_description": {
                "background": "暴雪肆虐的中世紀石製城堡，灰暗厚重雲層覆蓋天空，鵝毛大雪紛飛。古老石質城牆高聳，塔樓尖頂積雪，城門緊閉。城內石屋煙囪冒出微弱炊煙，窗戶透出昏黃燭光。無垠雪原環繞城堡，地面積雪深厚，寒風呼嘯捲起雪霧。光線昏暗壓抑，整體色調偏冷灰藍，營造嚴寒絕望氛圍",
                "characters": []
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "百年寒冬籠罩北方王國萊文堡，饑荒與絕望如瘟疫般蔓延",
                    "role_name": "旁白"
                }
            ],
            "main_characters": [],
            "shot_size": {
                "value": "遠景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "俯角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "王宮大廳內部，高大石柱支撐拱形屋頂，牆面厚重石磚砌成。鐵質火把架懸掛牆上，橘黃火焰搖曳跳動，投下長長陰影。地面鋪設大理石板，中央鋪紅色地毯。高背木質王座位於台階之上，周圍裝飾彩色玻璃窗。室內溫度對比外界相對溫暖，但仍顯冷峻莊嚴",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "單膝跪地於大廳中央紅毯上，左膝著地，右腿支撐，上身挺直。銀色盔甲反射火光，深藍眼眸凝視前方，面部表情堅毅莊重。雙手放置膝上，頭部微微前傾表示敬意。位於畫面中央偏下位置，面向王座方向，展現騎士尊嚴與決心"
                    },
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "莉安娜",
                        "action_and_emotion": "側身站立於王座台階右側，微微轉身面向艾利克方向。湖藍眼眸流露擔憂神情，眉頭輕蹙表現內心不安。右手緊握住金色披肩邊緣，左手自然垂放身側。身體姿態略顯緊張，顯露對騎士即將踏上危險征途的擔憂。位於畫面右側中景位置，與艾利克形成視覺對話關係"
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
                    "content": "公主殿下，我願為王國尋得風息之心，終結這無盡寒冬",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "城牆頂部石製平台，夜空中雪花飛舞，寒風呼嘯。厚重石質城垛線條分明，鐵質火把插在支架上，橘紅火焰在風中劇烈搖擺。遠處雪原在月光下泛著微弱銀光，城下漆黑一片。雪霧在風中翻滾，氣溫極低，整體氛圍淒涼而浪漫",
                "characters": [
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "莉安娜",
                        "action_and_emotion": "站立於城牆邊緣，身體微微前傾靠向艾利克。湖藍眼眸盈滿淚水，面部表情溫柔而不捨。雙手輕柔地將紅色絲綢掛墜遞向艾利克，動作小心翼翼充滿珍惜。金色披肩在風中輕微飄動，整體姿態展現深情與擔憂。位於畫面中央偏左位置，面向艾利克呈三分之二側身角度"
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "雙手張開接過莉安娜遞來的掛墜，深藍眼眸注視著公主，神情溫柔而堅定。面部表情混合柔情與決絕，顯示內心複雜情感。身體前傾靠近公主，銀色盔甲在火光下發出柔和光澤。整體姿態溫柔而莊重，體現對公主的深情與對使命的堅持。位於畫面中央偏右位置，面向莉安娜呈三分之二側身角度"
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
                    "content": "帶著它，讓它守護你平安歸來",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "廣闊雪原地形起伏，白雪覆蓋大地延伸至地平線。昏暗天空烏雲密佈，風暴席捲整片區域，雪花如鞭子般橫掃。遠處山脈輪廓模糊，近處地面雪層深厚。沒有植被或建築物，完全荒涼的自然環境。光線極其微弱，整體色調冷灰白，營造極端惡劣天氣氛圍",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "獨自行走在雪原中，身體向前傾斜對抗強風。深藍披風在風中獵獵作響，銀色盔甲表面積雪。右手持長劍拄地作為支撐，左手護住面部遮擋風雪。步伐沉重緩慢但堅定，面部表情顯示疲憊但意志堅強。位於畫面中央偏下位置，呈側身行走姿態，展現在惡劣環境中的頑強毅力"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "艾利克踏上征途，孤身面對無盡風雪的考驗",
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
                "value": "遠景",
                "size_values": [
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "俯角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "雪林邊緣地帶，稀疏枯樹林立，光禿樹枝積雪壓彎。地面雪層厚實不平，散落枯枝敗葉。中央燃燒微弱篝火，橘黃火光微弱搖曳，照亮周圍有限區域。林間陰影深邃漆黑，隱約可見多雙幽藍發光眼睛。夜色濃重，月光被雲層遮擋，整體氛圍緊張而危險",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "背靠粗大枯樹樹幹，身體緊繃保持警戒狀態。右手緊握長劍劍柄，劍身反射篝火光芒。面部有血跡痕跡與雪水交織，表情專注而堅毅。深藍眼眸掃視周圍陰影，肌肉緊張隨時準備戰鬥。銀色盔甲在火光映照下明暗交替，展現騎士面對危險時的果敢。位於畫面中央位置，側身靠樹面向陰影方向"
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
                    "content": "來吧，我不會退縮",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "幽冥谷入口處，山崖峭壁高聳入雲，谷口狹窄深邃。迷霧從谷底升騰瀰漫，遮蔽視線。巨大冰瀑從山壁垂下結成冰柱，古老石碑半埋積雪中，碑面刻有風化文字。枯死古樹扭曲生長，枝幹如鬼爪伸展。光線昏暗神秘，整體氛圍古老而壓迫，散發不祥預感",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "站立於石碑前，身體前傾仔細觀察碑文。左手輕撫石碑表面，右手持劍置於身側。深藍眼眸專注凝視碑文，面部表情嚴肅認真。銀色盔甲映射微弱天光，披風在微風中輕擺。整體姿態顯示對古老傳說的敬畏與探索精神。位於畫面中央位置，面向石碑呈側身角度"
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
                    "content": "風息之心就在前方，我必須繼續",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "幽冥谷谷底深處，古老枯樹群環繞形成圓形空間。樹木高大扭曲，枝葉凋零，樹皮蒼老龜裂。地面覆蓋厚雪但露出黑色土壤。谷底中央懸浮巨大藍色晶體，發出柔和脈動光芒如心跳節奏。晶體周圍環繞淡藍色能量霧氣，散發神聖氣息。光源主要來自晶體本身，營造神秘而莊嚴氛圍",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "站立於晶體下方，頭部仰起凝視風息之心。深藍眼眸被晶體光芒照亮，瞳孔映出藍色光輝。面部表情混合敬畏、希望與震撼，微微張開嘴唇表示驚嘆。雙手自然垂放身側，身體放鬆但保持尊敬姿態。銀色盔甲表面反射藍色晶光，整體形象莊嚴而虔誠。位於畫面下方中央位置，仰望晶體呈正面角度"
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
                    "content": "傳說中的風息之心，果然存在",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "谷底空間突然風雪大作，迷霧翻騰湧動遮蔽視線。枯樹在強風中搖擺，發出嘎吱響聲。地面積雪被風捲起形成雪旋，空氣中瀰漫寒冷霧氣。能見度極低，只能看出模糊輪廓。風聲呼嘯如鬼哭狼嚎，整體氛圍突然變得危險而詭異，預示重大事件即將發生",
                "characters": [
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "冰霜巨狼",
                        "action_and_emotion": "從迷霧中緩步現身，龐大身軀若隱若現。幽藍雙眼鎖定艾利克，散發威嚴壓迫感。四肢穩定站立，肌肉緊繃展示力量。頭部微微前傾，露出鋒利獠牙表示警告。雪白毛髮在風中飄動，鼻孔噴出寒冷霧氣。整體姿態展現神秘守護者的威嚴與危險。位於畫面中央偏後位置，面向前方呈正面威脅姿態"
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "面對巨狼威脅，雙手緊握長劍舉至胸前，劍尖指向巨狼。身體微微下蹲呈戰鬥準備姿態，雙腿分開保持平衡。深藍眼眸直視巨狼雙眼，面部表情堅毅無畏，沒有絲毫退縮。銀色盔甲覆蓋薄雪，披風在風中飛舞。展現騎士面對強敵時的果敢。位於畫面前景左側位置，面向巨狼呈四分之三側身角度"
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
                    "content": "守護者，我為了拯救王國而來",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "仰角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "激戰現場雪地翻騰，地面積雪被踢踏起形成漩渦。鮮紅血跡點綴在潔白雪地上，形成強烈視覺衝擊。風暴繼續肆虐，雪霧遮蔽部分視線。枯樹在背景中搖擺，地面留下深深爪印與足跡。戰鬥區域範圍較大，顯示激烈搏鬥痕跡。整體色調以白雪紅血為主，營造慘烈戰鬥氛圍",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "身體向後傾斜抵擋巨狼撲擊，左臂舉盾防護，右手持劍準備反擊。銀色盔甲出現裂紋損傷，深藍披風染有血跡。面部表情咬牙堅持，顯示承受巨大壓力但絕不屈服。肌肉緊繃用盡全力對抗強敵，靴子在雪地中留下深深印記。展現騎士生死關頭的頑強意志。位於畫面右側前景位置，身體斜向對抗來襲攻擊"
                    },
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "冰霜巨狼",
                        "action_and_emotion": "前肢揚起準備撲擊，張開巨口露出鋒利獠牙。幽藍雙眼閃爍殺意，雪白毛髮豎起顯示憤怒。巨大身軀弓起蓄積力量，後肢蹬地掀起雪霧。動作迅猛有力，展現野獸本能的攻擊性。口中噴出寒冷霧氣，整體姿態充滿威脅性。位於畫面左側中景位置，身體前傾呈攻擊姿態面向艾利克"
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
                    "content": "我絕不能倒下！",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "傾斜角",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "移鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "戰鬥突然停止，谷底恢復寧靜，風雪逐漸平息。空氣中只餘輕微風聲迴響，雪花緩慢飄落。地面血雪混合，顯示剛才激戰痕跡。枯樹停止搖擺，迷霧漸散露出清晰輪廓。藍色風息之心在遠處繼續發光，提供微弱照明。整體氛圍從激烈轉為肅穆，充滿神聖感與命運感",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "重傷倒地但上身支撐起來，右手緊握紅色絲帶掛墜貼近胸口。深藍眼眸仰望巨狼，眼神依然堅定不屈，沒有恐懼只有決心。面部表情痛苦但意志堅強，嘴角流出血跡。銀色盔甲嚴重受損，多處裂痕暴露內襯。身體姿態雖然虛弱但精神不倒，體現真正的騎士精神。位於畫面下方中央位置，半躺姿態仰視巨狼"
                    },
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "冰霜巨狼",
                        "action_and_emotion": "停止攻擊靜立凝視艾利克，幽藍雙眼中殺意逐漸消散，轉為審視與思考。頭部微微側傾觀察倒地騎士，耳朵前豎顯示專注。身體放鬆不再緊繃，尾巴自然下垂。呼吸平穩，口中不再露出獠牙威脅。整體姿態從攻擊性轉為觀察性，似乎被騎士精神所觸動。位於畫面上方中央位置，俯視艾利克呈正面觀察角度"
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
                    "content": "我的愛與誓言，永遠不會背叛",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "萊文堡城門外廣場，春日暖陽穿透雲層洒落大地。積雪開始融化形成小溪流淌，地面露出濕潤石板路面。城牆石縫間滴落融雪水珠，發出清脆聲響。空氣溫暖濕潤，微風輕拂。城民聚集在道路兩側，面容從憔悴轉為希望，眼神中充滿敬畏與感激。彩色旗幟在微風中飄揚，整體氛圍溫暖歡慶",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "懷抱藍色風息之心晶體緩步走向城門，晶體散發柔和光芒。身體雖然疲憊但步伐堅定沉穩，展現完成使命的驕傲。銀色盔甲留有戰鬥痕跡，多處修補但依然莊嚴。面部表情平靜莊重，深藍眼眸透露完成重任的滿足感。披風在微風中輕擺，整體形象如傳說中的英雄歸來。位於畫面中央位置，面向城門呈正面行進角度"
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "英雄歸來，帶來春天的希望",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "推鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
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
                "background": "王宮前方大理石台階，初春陽光透過彩色玻璃窗投下斑斕光影。台階兩側裝飾精美石柱，柱頭雕刻花紋圖案。融化的雪水從屋簷滴落，在地面形成小水窪反射陽光。微風吹動宮殿旗幟，空氣清新溫暖。遠處傳來鳥鳴聲，象徵新生與希望。整體氛圍溫馨浪漫，充滿重逢的喜悅",
                "characters": [
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "莉安娜",
                        "action_and_emotion": "從台階上飛奔而下，白色長裙在跑動中飛舞飄揚。湖藍眼眸盈滿喜悅淚水，面部表情激動欣喜混合深深思念。雙臂張開準備擁抱，金色披肩在身後飄動。腳步輕快急切，展現迫不及待的重逢心情。栗色長髮在陽光下閃閃發光，整體形象如春日女神般美麗動人。位於畫面上方開始向下奔跑，面向艾利克呈正面角度"
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "艾利克",
                        "action_and_emotion": "站立台階下方張開雙臂迎接公主，深藍眼眸注視奔來的莉安娜，眼神溫柔深情。面部表情欣慰幸福，嘴角露出久違微笑。身體前傾準備擁抱，銀色盔甲在陽光下發出溫暖光澤。紅色絲帶掛墜在胸前輕擺，象徵愛情守護力量。整體姿態展現英雄完成使命後的幸福與滿足。位於畫面下方中央位置，仰望公主呈正面迎接角度"
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
                    "content": "艾利克，你回來了！",
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
                    "遠景",
                    "全景",
                    "中景",
                    "近景",
                    "特寫"
                ]
            },
            "camera_angle": {
                "value": "平視",
                "angle_values": [
                    "平視",
                    "仰角",
                    "俯角",
                    "鳥瞰",
                    "傾斜角"
                ]
            },
            "shot_type": {
                "value": "固定鏡頭",
                "type_values": [
                    "固定鏡頭",
                    "推鏡頭",
                    "拉鏡頭",
                    "搖鏡頭",
                    "移鏡頭",
                    "俯仰鏡頭",
                    "變焦鏡頭"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "秒"
            }
        }
    ]
}