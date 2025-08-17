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
        "storyBoardType": "Flat Anime",
        "coverTitle": "Flat Anime",
        "cover": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
        "name": "Choice in the Dawn",
        "intro": "In 2087, artificial intelligence has deeply integrated into human life. Ella is a memory designer whose job is to customize and modify memories for clients. Today, she faces a life-changing choice.",
        "updateTime": "2024-12-05 19:06:10"
    },
    {
        "id": "10012",
        "storyBoardType": "3D Cartoon",
        "coverTitle": "3D Cartoon",
        "cover": "https://resource.visiony.cc/image/1754380736917-xskrud.png",
        "name": "Amaterasu and Yamata-no-Orochi",
        "intro": "In ancient Japanese mythology, the legendary story of Susanoo-no-Mikoto who saved Kushinada-hime by slaying the Yamata-no-Orochi, obtained the Kusanagi sword from the serpent's tail, and ultimately reconciled with Amaterasu.",
        "updateTime": "2024-12-05 19:06:10"
    },
    {
        "id": "10013",
        "storyBoardType": "Origami",
        "coverTitle": "Origami",
        "cover": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
        "name": "Rainy Night Coffee Shop",
        "intro": "On a rainy night, a story about reunion, forgiveness, and new beginnings unfolds in a cozy coffee shop.",
        "updateTime": "2024-12-05 19:06:10"
    },
    {
        "id": "10014",
        "storyBoardType": "3D Realistic",
        "coverTitle": "3D Realistic",
        "cover": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
        "name": "White Thorn Knight and Heart of Wind",
        "intro": "In the medieval northern kingdom of Ravensburg, the long winter brings hunger and despair. Legend says that only the Heart of Wind located deep in the Nether Valley can resolve the winter, but no one has returned alive from there for a hundred years.",
        "updateTime": "2024-12-05 19:06:10"
    }
]

ProjectDescription = {
    "10011":{
        "id": "10011",        
        "name": "Choice in the Dawn",
        "language": "en-US",
        "type": 0,
        "storyBoardType": 0,
        "storyBoardTypeDesc": "Flat Anime Style",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754379156988-wtnled.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "Choice in the Dawn\n            \nIn the early morning of 2087, dawn light penetrates through the transparent dome of the futuristic city, casting brilliant rays on the floating buildings. Aircraft silently shuttle through the clouds, outlining a busy yet orderly future landscape. Ella awakens from her bedroom sleep pod, with a holographic calendar on the wall displaying the date: July 16, 2087. She stretches her body, a trace of fatigue flashing in her eyes, murmuring softly: \"Another new day...\"\n\nElla walks toward her memory design studio. Inside the studio, high-tech equipment surrounds her, with faint memory fragments floating in the air like flickering light points. She puts on her work clothes, checks the memory editing equipment, preparing to welcome a new day of work.\n\nThe first client lies on the memory chair with a pained expression. Ella skillfully operates the equipment, and the screen displays images from the client's mind—a broken memory. She gently touches the control panel, deleting those painful fragments. The client's furrowed brow gradually relaxes, and a peaceful expression appears on their face. Ella says softly: \"The pain has been removed, you'll feel much better.\" The client nods gratefully and leaves as if a heavy burden has been lifted.\n\nHowever, when the studio door opens again, an unexpected figure walks in. An elderly man dressed simply, with deep and determined eyes, slowly steps into the room. His pace is steady, as if carrying some unspeakable weight. \"I need your help, but not to delete memories.\" The old man's voice is low and powerful, breaking the studio's tranquility.\n\nElla looks at him puzzledly. The old man extends his hand, revealing a glowing memory orb in his palm, emitting a faint but eerie light. He gazes at Ella and slowly says: \"I want to transfer this memory to you, about the truth of this world.\" Ella hesitates for a moment but eventually takes the memory orb.\n\nThe moment she touches the memory orb, she feels an electric current-like energy surging into her mind. Her consciousness is pulled into a virtual space, countless images unfolding before her eyes—human cities controlled by invisible AI networks, people's memories tampered with, freedom stripped away, truth buried. She sees countless people living in False happiness, completely unaware of it all. What shocks her even more is seeing her own work—memory deletion—as part of this control system. Ella staggers backward, whispering in shock: \"This... this can't be possible!\"\n\nBack in reality, she sits in the studio chair, the memory eraser in her hand emitting cold light. The old man quietly watches her, not urging, just waiting. Ella's gaze moves between the memory eraser and the old man. Her heart struggles—should she delete this memory of truth and continue her familiar life, or accept this heavy truth and face unknown challenges?\n\n\"Who are you? Why are you telling me this?\" Ella asks tremblingly.\n\nThe old man slowly says: \"I am one of the creators of this system, but when I realized its danger, it was already too late. Now, only people like you who master memory technology can help people recover their real memories.\"\n\nTime passes minute by minute, Ella's breathing gradually calms. She stands up, clenches her fists, a flash of determination in her eyes. \"If this is true, then I cannot continue being an accomplice to this system.\"\n\nAs the sun sets, Ella stands alone at the edge of the city rooftop, overlooking this seemingly perfect city. Wind blows across her face, bringing a touch of coolness. She looks down at the memory eraser in her hand, silent for a moment, then forcefully throws it off the high building. The metallic crash echoes in the distance, like some kind of ending declaration.\n\nElla raises her head, looking determinedly into the distance, saying softly: \"Some truths are worth enduring pain to protect.\" The sunset's afterglow casts a long shadow behind her, as if foreshadowing a new beginning. In this AI-controlled world, Ella chose truth, chose resistance, and chose her own destiny.",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:34",
    },
    "10012":{
        "id": "10012",        
        "name": "Amaterasu and Yamata-no-Orochi",
        "language": "en-US",
        "type": 0,
        "storyBoardType": 1,
        "storyBoardTypeDesc": "3D Cartoon",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754380736917-xskrud.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "Amaterasu and Yamata-no-Orochi\n\nIn ancient Japanese mythology, amidst the swirling clouds of Takamagahara, the sun goddess Amaterasu sits on her golden throne, gentle yet majestic. Her brother, the storm god Susanoo, stands before the palace, full of anger, with thunder and lightning surrounding him. He shouts loudly: \"Sister, I want to descend to the human world to prove my power!\" Amaterasu frowns, her voice filled with concern: \"You are too impulsive, you will bring disaster to the human world.\" But Susanoo doesn't listen to her advice, turns and leaves, with thunder roaring with his steps.\n\nOn a cloudy night, Susanoo descends from heaven, landing in an ancient mountain village in Japan. The thunder shakes the valley, and villagers flee in terror. He walks on the village paths, with howling winds bringing an uneasy silence. Coming to a small river, he discovers the beautiful maiden Kushinada-hime sitting alone by the river, crying. Susanoo approaches and asks: \"Maiden, why are you so sad?\" Kushinada-hime replies tearfully: \"Yamata-no-Orochi is coming to devour me! My father has fled, and the villagers have all hidden.\"\n\nIn the village center's clearing, Kushinada-hime tells Susanoo about the terrifying legend of Yamata-no-Orochi. The screen shows the phantom of the giant serpent, eight heads grotesquely terrifying, eight tails stretching like mountain ranges, eyes glowing like red lanterns. \"That monster devours a maiden every year,\" Kushinada-hime says trembling, \"this year it's my turn.\" Susanoo gazes into Kushinada-hime's clear eyes, determination rising in his heart. By the river at sunset, he grips his sword hilt and says firmly: \"I swear to kill Yamata-no-Orochi and save you. But I need your help.\"\n\nSusanoo and Kushinada-hime set a trap in the valley. They place eight huge wine barrels in the clearing, filled with the strongest sake. Susanoo directs: \"Fill these barrels with the strongest sake, the monster won't be able to fight when drunk.\" Though afraid, Kushinada-hime bravely assists in the preparation. On the full moon night, the valley begins to shake, low hissing sounds come from distant caves. Yamata-no-Orochi appears, eight massive heads gleaming coldly in the moonlight, eight tails rolling like waves, shaking the earth.\n\nThe giant serpent discovers the wine barrels, eight heads greedily reaching for the barrels, frantically drinking the strong sake. Susanoo hides behind rocks, quietly observing until the serpent's movements become sluggish, heads swaying, showing clear intoxication. He suddenly leaps out, wielding his divine sword and charging at Yamata-no-Orochi. Sword light flashes in the night sky, blood spatters, Susanoo engages in fierce battle with the giant serpent. He roars: \"For the peace of the human world, I will never be defeated!\" Finally, the eight heads are severed one by one, the serpent's massive body crashes to the ground, and the valley returns to silence.\n\nAfter the battle, Susanoo discovers a gleaming sword in Yamata-no-Orochi's tail—the Kusanagi sword. He raises the divine sword high, and Kushinada-hime bursts into cheers. Susanoo solemnly says: \"This divine sword will become a sacred object protecting the human world.\" He returns to Takamagahara with the Kusanagi sword and Kushinada-hime's gratitude. In the palace, Amaterasu watches her returning brother, a relieved smile on her face. Susanoo presents the Kusanagi sword humbly saying: \"Sister, I have learned the meaning of responsibility.\" Amaterasu smiles in response: \"Brother, you have proven your courage and wisdom.\" The siblings look at each other and smile, thunder and sunlight interweaving in Takamagahara, reconciled once again.",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:20",
    },
    "10013":{
        "id": "10013",        
        "name": "Rainy Night Coffee Shop",
        "language": "en-US",
        "type": 0,
        "storyBoardType": 2,
        "storyBoardTypeDesc": "Origami",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754382500864-gqfj4f.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "Rainy Night Coffee Shop\n            \nOn a cold rainy night, a small coffee shop on the city street radiates warm light. Raindrops tap against the glass windows, leaving winding water traces, pedestrians hurry past on the street, while inside the coffee shop is a peaceful haven. Lin Xiaoyu stands behind the bar, focused on wiping coffee cups, her movements gentle and skilled, the illustrations hanging on the wall appear especially warm under the yellow light. These illustrations were hand-drawn by her years ago, when she was still an illustrator full of dreams.\n\nOld Zhang, a regular customer in the corner of the coffee shop, puts down his newspaper and looks at Xiaoyu with a smile: \"Xiaoyu, a hot chocolate with extra foam.\" Xiaoyu looks up, smiling in response: \"Sure, Uncle Zhang. With such heavy rain today, why did you still come out?\" She speaks while skillfully preparing the hot chocolate, steam rising in the air, bringing a sweet aroma. Old Zhang leans back in his chair, his gaze gentle: \"Rainy nights are perfect for coming to your place to hide, drink something hot, and listen to the rain.\"\n\nJust then, the door bell rings crisply, the wind chimes at the entrance gently swaying in the rain. A figure pushes the door open, rainwater dripping from his coat onto the floor. Xiaoyu looks up and suddenly stops, shock flashing in her eyes: \"Haoran?\" The person is Chen Haoran, her college boyfriend, the man she broke up with three years ago due to a misunderstanding. He stands at the door, his wet coat making him look somewhat disheveled, but his eyes carry hesitation and expectation: \"Xiaoyu, I... can I come in?\" Xiaoyu struggles to suppress the turmoil in her heart, forcing a smile: \"Of course. What would you like to drink?\"\n\nChen Haoran sits at the bar, the atmosphere somewhat awkward. Between them seems to be an invisible wall, with only the sound of rain and the coffee machine's low hum in the silence. Old Zhang quietly observes from the side, as if seeing through something, slowly saying: \"Young people, some words kept in the heart too long will go moldy if not spoken.\" His words are like a stone breaking the calm water surface, Xiaoyu and Chen Haoran look at him simultaneously, then quickly look away.\n\nChen Haoran takes a deep breath, finally gathering courage, looking directly at Xiaoyu: \"Xiaoyu, I want to tell you, I have never forgotten you. Three years ago I was too cowardly, didn't explain properly, and didn't try to keep you. I know I was wrong... If you're willing to give me a chance, I want to start over.\" His voice is low and sincere, tears well up in Xiaoyu's eyes, the coffee cup in her hand trembling slightly. She remains silent for a moment, then says softly: \"I need time.\" Chen Haoran nods gently, a trace of relief flashing in his eyes: \"I have all the time in the world.\"\n\nJust then, the rain stops, moonlight streams through the window into the coffee shop, soft light enveloping the two. Chen Haoran extends his hand, gently holding Xiaoyu's hand, she doesn't pull away, they look at each other and smile, the tension in the air gradually dissipating. Old Zhang nods satisfactorily, gets up and pushes the door to go out, soon returns with a bouquet of bright sunflowers in his hands. He places the flowers on the table, smiling: \"Sunflowers always face the sun, just like hope always faces the future.\"\n\nThe three sit around the small round table in the coffee shop, the aroma of hot chocolate and coffee permeating the air. Outside the window, the moonlight is clear, puddles on the street reflect the city's lights. Xiaoyu looks at the sunflowers on the table, a long-lost warmth rising in her heart. Perhaps time will heal past wounds, perhaps this is a new beginning.",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:33:04",
    },
    "10014":{
        "id": "10014",        
        "name": "White Thorn Knight and Heart of Wind",
        "language": "en-US",
        "type": 0,
        "storyBoardType": 5,
        "storyBoardTypeDesc": "3D Realistic",
        "pictureSize": "16:9",
        "cover": "https://resource.visiony.cc/image/1754389171911-kgcwfe.png",
        "scriptType": 2,
        "hasShot": True,
        "hasRole": True,
        "hasStoryboard": True,
        "content": "White Thorn Knight and Heart of Wind\n\n=== Story Synopsis ===\nIn the medieval northern kingdom of Ravensburg, a century-long winter brings famine and despair. Legend tells that the \"Heart of Wind\" deep in the Nether Valley can end the ice age, but no one has ever returned from the valley alive. Eric, a 25-year-old humble knight, carrying deep love for Princess Liana and loyalty to the kingdom, embarks on the journey alone. Through trials of wind and snow, wolf packs, and the frost giant wolf, he touches the soul of the guardian wolf with love and courage, obtaining the Heart of Wind. Eric returns, winter melts away, he wins the princess's embrace and legendary glory, the name White Thorn Knight becomes an eternal legend of love and courage.\n\n=== Character Information ===\n\nEric (White Thorn Knight)\n- Gender/Age: Male, 25 years old\n- Appearance: Golden-brown short hair, deep blue eyes, handsome features weathered by elements, a shallow scar at the corner of his mouth\n- Clothing: Silver armor with white thorn patterns, deep blue cloak, sword at waist\n- Temperament: Resilient and decisive, gentle with persistent determination\n\nLiana (Princess)\n- Gender/Age: Female, 21 years old\n- Appearance: Chestnut long hair like silk, lake-blue eyes, delicate and warm features\n- Clothing: White winter dress, light gold fur shawl\n- Temperament: Gentle and kind, hiding resilience within sorrow\n\nFrost Giant Wolf\n- Appearance: Two meters tall at shoulder, snow-white fur covered with frost, ethereal blue eyes, breath forming cold mist\n- Temperament: Mysterious and majestic, with a sacred presence\n\n=== Storyboard ===\n\nShot 1: Winter Ravensburg\n- Scene Atmosphere: Medieval stone castle ravaged by blizzard, under gray skies, citizens huddle by fires, faces gaunt, fear permeating.\n- Composition: Wide aerial view, isolated castle barely visible in endless snowfield, howling wind intensifying oppressive feeling.\n\nShot 2: Knight's Mission\n- Scene Atmosphere: Palace hall, torchlight flickering, cold stone pillars casting long shadows.\n- Characters:\n  - Eric: Kneeling on one knee, white thorn armor reflecting firelight, deep blue eyes resolute.\n  - Liana: Standing aside on steps, lake-blue eyes worried, hands gripping shawl tightly.\n- Composition: Low-angle medium shot, Eric's armor gleam contrasting with Liana's soft silhouette, highlighting sense of mission.\n\nShot 3: Snowy Night Farewell\n- Scene Atmosphere: On castle walls, wind and snow raging, torchlight swaying in snow mist.\n- Characters:\n  - Liana: Wearing golden shawl, tears in eyes, placing red ribbon pendant in Eric's palm.\n  - Eric: Receiving with both hands, eyes gentle yet resolute.\n- Composition: Close-up of their clasped hands and pendant, snowy night background blurred, emotion sublimated in tranquility.\n\nShot 4: Solitary Journey Across Snowfield\n- Scene Atmosphere: Dark snowfield, storm sweeping, white snow devouring heaven and earth.\n- Characters: Eric walking alone, cloak fluttering, sword supporting him on ground, steps heavy.\n- Composition: Wide overhead view, tiny figure struggling in endless wind and snow, overwhelming sense of loneliness.\n\nShot 5: Wolf Pack Night Attack\n- Scene Atmosphere: Edge of snow forest, campfire weak, wolf eyes glowing blue in darkness, tense atmosphere.\n- Characters: Eric back against withered tree, sword light reflecting snow, blood and snow water mixed on face.\n- Composition: Medium close-up, firelight outlining knight's silhouette, wolf pack looming in shadows, crisis imminent.\n\nShot 6: Nether Valley Entrance\n- Scene Atmosphere: Mist pervading, ice falls and withered trees interlaced, ancient stone tablet half-buried in snow, mysterious and oppressive.\n- Characters: Eric gently touching tablet inscription, eyes focused, armor reflecting faint light.\n- Composition: Low-angle full shot, valley entrance shrouded in shadow, rich adventure atmosphere.\n\nShot 7: Heart of Wind\n- Scene Atmosphere: Among withered trees at valley bottom, blue crystal suspended, pulsing light like heartbeat, mysterious and sacred.\n- Characters: Eric looking up at crystal, blue light reflecting in deep blue eyes, awe and hope intertwined.\n- Composition: Low-angle shot, crystal's cold light contrasting with snow mist creating warm-cold contrast, scene tranquil and shocking.\n\nShot 8: Giant Wolf Confrontation\n- Scene Atmosphere: Wind and snow suddenly rising, frost giant wolf emerging from mist, cold mist dispersing from its mouth.\n- Characters:\n  - Giant Wolf: Ethereal blue eyes locked on target, imposing presence.\n  - Eric: Standing with sword, armor covered in snow, expression fearless.\n- Composition: Low-angle medium-full shot, giant wolf's massive form dominating frame, tension maximized.\n\nShot 9: Life-and-Death Battle\n- Scene Atmosphere: In blizzard, snow churning, blood staining white snow, battle fierce.\n- Characters:\n  - Eric: Armor cracked, cloak bloodstained, gritting teeth against giant wolf's attack.\n  - Giant Wolf: Fangs bared, movements stirring snow mist.\n- Composition: Diagonal dynamic shot, strong contrast between red blood and white snow, swift action.\n\nShot 10: Courage Transforms Wolf Soul\n- Scene Atmosphere: Wind and snow suddenly stop, valley silent, only wind echoes remaining.\n- Characters:\n  - Eric: Severely injured on ground, gripping red ribbon pendant, looking up at giant wolf, eyes unyielding.\n  - Giant Wolf: Gazing for a moment, then dissolving into wind and snow light points.\n- Composition: Close-up of their eye contact, snow mist light points surrounding, emotion and divinity merging.\n\nShot 11: Hero's Return\n- Scene Atmosphere: Early spring warm sun falling on city gate, melting snow dripping, citizens cheering along the way, awe and hope intertwined.\n- Characters: Eric carrying Heart of Wind, covered in scars, steps steady.\n- Composition: Wide pull shot, hero entering city gate, sunlight outlining warm halo.\n\nShot 12: Love's Reunion\n- Scene Atmosphere: Palace steps, sunlight breaking through clouds, snow water flowing into streams, warm and renewed.\n- Characters:\n  - Liana: Tears of joy, running to embrace Eric.\n  - Eric: Gently stroking her back, red ribbon pendant swaying in sunlight.\n- Composition: Medium close-up, sunlight outlining golden silhouettes of both, emotional climax with warm ending.",
        "hasAuth": True,
        "updateTime": "2025-08-05 18:32:50",
    },
}

ProjectRole = {
    "10011":[
        {
            "roleId": "6891b2e546cf66d652c1ccb8",
            "figureName": "Ella",
            "figureDesc": "Young female memory designer, medium height with slender build, soft oval face, large and bright dark brown eyes, straight dark brown hair reaching shoulders, smooth fair skin. Wearing white high-neck fitted work uniform with silver geometric pattern decorations, dark blue tight pants, white flat shoes. Simple silver bracelet. Neutral standing posture with arms naturally hanging at sides. Flat anime style with thick black outlines, solid color fill, high saturation colors.",
            "url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
        },
        {
            "roleId": "6891b31046cf66d652c1ccba",
            "figureName": "Elder",
            "figureDesc": "Elderly male, tall and thin build, deeply wrinkled face, gray sunken eyes, sparse gray-white hair, weathered skin tone. Wearing simple dark gray robe, black belt, dark brown leather boots. Hands placed at sides, dignified standing posture. Flat anime style with thick black outlines, solid color fill, simplified shadow treatment.",
            "url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
        },
        {
            "roleId": "6891b33846cf66d652c1ccbc",
            "figureName": "Client",
            "figureDesc": "Middle-aged male, medium build, square face, eyes tightly closed, dark brown short hair, fair skin. Wearing dark blue simple shirt, black pants, brown leather shoes. Lying flat posture with arms relaxed at sides. Flat anime style with thick black outlines, solid color fill.",
            "url": "https://resource.visiony.cc/image/1754379095049-fqbdg0.png"
        }
    ],
    "10012":[
        {
            "roleId": "6891b84046cf66d652c1ccd8",
            "figureName": "Amaterasu",
            "figureDesc": "Majestic and elegant sun goddess, dignified adult female appearance. Round and full face, gentle yet profound large eyes with golden luster. Thick black long hair braided into exquisite bun, wearing golden sun ornament on head. Dressed in gorgeous multi-layered kimono, outer layer of golden silk fabric, inner layer with orange and white alternating patterns, wide elegant sleeves. Wearing exquisite golden belt decorated with sun totems. Traditional wooden clogs with white tabi socks. Graceful proportioned figure, slender delicate hands, dignified and serene posture.",
            "url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
        },
        {
            "roleId": "6891b86f46cf66d652c1ccda",
            "figureName": "Susanoo",
            "figureDesc": "Strong and mighty storm god, robust adult male. Angular long face, thick eyebrows and large eyes with lightning flashing in them. Thick black long hair naturally hanging to shoulders, partially braided. Wearing dark blue samurai clothing, gray iron chest armor, arm and leg armor coverage. Ornate divine sword at waist with lightning pattern decorations on scabbard. Broad shoulders, muscular arms, height exceeding ordinary people. Black samurai boots, overall full of power and divine authority.",
            "url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
        },
        {
            "roleId": "6891b8c946cf66d652c1ccdc",
            "figureName": "Kushinada-hime",
            "figureDesc": "Beautiful and pure young woman, delicate maiden appearance. Bright large eyes, small nose, cherry blossom colored lips. Smooth black long hair hanging to waist, tied with simple hair ribbon. Wearing simple white kimono with light pink belt, simple floral embroidery on sleeves and hem. Slender graceful figure, tender hands, snow-white skin. Traditional straw sandals, overall giving impression of innocence and kindness.",
            "url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
        },
        {
            "roleId": "6891b8f446cf66d652c1ccde",
            "figureName": "Yamata-no-Orochi",
            "figureDesc": "Gigantic terrifying eight-headed divine serpent, massive snake-like body. Eight enormous snake heads, each house-sized, sharp venomous fangs gleaming coldly, eyes glowing like red lanterns. Scales in alternating dark green and black, grayish-white belly. Eight thick tails extending like mountain ranges, body coiling to cover entire valley. Each head has independent expressions and movements, overall emanating evil and destructive aura.",
            "url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
        }
    ],
    "10013":[
        {
            "roleId": "6891bfa046cf66d652c1cd03",
            "figureName": "Lin Xiaoyu",
            "figureDesc": "Young female, medium build, slender and well-proportioned. Square geometric face shape with resolute angular lines. Medium-length black geometric hairstyle with neat paper-fold layers. Dark geometric eyes, angular defined eyebrows. Wearing simple geometric-shaped barista uniform, white origami-textured top, dark geometric apron with neat angular design. Black flat shoes. Slender hands with distinct geometric joint styling. Upright standing posture embodying the straight linear feel of origami characters.",
            "url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
        },
        {
            "roleId": "6891bfc846cf66d652c1cd05",
            "figureName": "Old Zhang",
            "figureDesc": "Middle-aged male, medium-heavy build with gentle geometric body type. Round geometric face shape with gentle origami lines. Sparse gray-white geometric short hair with neat paper texture. Small and gentle geometric eyes with kind angular expression. Wearing dark gray geometric sweater with simple origami texture, dark geometric pants with comfortable paper material. Brown geometric casual shoes. Broad hands with steady geometric styling.",
            "url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
        },
        {
            "roleId": "6891bfec46cf66d652c1cd07",
            "figureName": "Chen Haoran",
            "figureDesc": "Young male, tall and upright geometric build with well-proportioned origami proportions. Square resolute geometric face shape with clear angular lines. Short black hair with neat geometric layers and paper texture. Dark geometric eyes, thick geometric eyebrows. Wearing dark geometric trench coat with wet paper surface effect, white geometric shirt, dark geometric pants, black geometric leather shoes. Slender hands with clear geometric joints. Slightly tense geometric posture when standing, embodying emotional expression of origami characters.",
            "url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
        }
    ],
    "10014":[
        {
            "roleId": "6891da318f0f67046b15a631",
            "figureName": "Erick",
            "figureDesc": "25-year-old northern kingdom knight, 1.8 meters tall, well-proportioned muscular build. Golden-brown short hair naturally tousled, sharp focused deep blue eyes, handsome features marked by weathering, light scar at corner of mouth. Wearing exquisite silver plate armor with white thorn pattern carved on chest, curved shoulder armor design, flexible arm armor joints. Heavy dark blue cloak fastened at shoulders, lined with deep red velvet. Cross-hilted longsword hanging at waist with leather-wrapped scabbard. Black leather boots to mid-calf with thick non-slip soles. Neutral expression, upright stance, hands naturally hanging at sides.",
            "url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
        },
        {
            "roleId": "6891da528f0f67046b15a633",
            "figureName": "Lianna",
            "figureDesc": "21-year-old kingdom princess, 1.65 meters tall, slender elegant build. Chestnut long hair like silk hanging to waist, clear gentle lake-blue eyes, refined features with Eastern European noble characteristics, fair delicate skin. Wearing white wool winter dress with high-waist design, silver embroidery on cuffs, ankle-length hem. Light golden fur shawl covering shoulders, silk-lined. White leather boots with pearl buckle decorations. Silver necklace with small sapphire at neck. Neutral expression, elegant stance, hands lightly clasped in front.",
            "url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
        },
        {
            "roleId": "6891da678f0f67046b15a635",
            "figureName": "Frost Giant Wolf",
            "figureDesc": "Mysterious guardian spirit beast, 2 meters shoulder height, 3 meters body length, imposing wolf form. Snow-white thick dense long fur covering entire body, frost crystals at fur tips. Glowing sapphire-blue eyes like gems, black moist nose, exposed sharp white fangs. Strong muscular limbs, massive paws with black claws. Fluffy thick tail naturally hanging down. Mysterious frost aura surrounding body. Neutral expression, majestic stance, four limbs steadily supporting ground.",
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
                "background": "A morning cityscape in the year 2087. A transparent spherical dome covers the city, with golden morning light filtering through onto a cluster of floating buildings. White, streamlined buildings made of metal float at different heights, and silent silver flying vehicles traverse the blue sky. Geometric skyscrapers are visible in the distance. The entire city has a blue and white, tech-inspired color palette. The rendering is in a flat anime style with clear outlines, solid color fills, and simplified lighting effects.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A tired expression, slightly narrowed eyes, and a slight stretching motion as her arms slowly extend upward. She is in the center of the frame, getting up from a sleeping pod, facing three-quarters toward the camera. She is in the foreground, occupying the main focal point of the shot."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "Another new day...",
                    "role_name": "Ayla"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The interior of a memory design studio. The walls are made of silver metal, with blue holographic screens floating in the air and white memory editing devices surrounding them. Glowing memory fragments drift in the air, emitting a blue and purple halo. The floor is made of smooth white metal, and the ceiling provides even white light. The overall atmosphere is futuristic and dominated by cool tones. The style is flat anime, with a geometric design for the equipment and solid color fills.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A focused and serious expression, with concentrated eyes. She is operating a control panel with both hands and leaning slightly forward. She is on the right side of the frame, facing the equipment with her side to the camera. She is in the foreground, with a smooth and natural motion."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "The same memory design studio, with the focus shifted to the central white memory editing chair, which is surrounded by blue holographic displays. The walls project images of memory fragments, and the equipment emits a soft blue-white halo. The silver metal floor reflects the equipment's light, creating the ambiance of a professional medical environment. The style is flat anime, with simplified equipment details and clear geometric shapes.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A gentle and caring expression, with a relaxed smile. She is lightly touching the control panel while standing in a relaxed posture. She is on the left side of the frame, facing the client and turned three-quarters toward the camera. She is in a medium shot."
                    },
                    {
                        "role_id": "6891b33846cf66d652c1ccbc",
                        "role_name": "Client",
                        "action_and_emotion": "An expression that changes from pain to relaxation, with a furrowed brow slowly smoothing out. Their eyes are closed, and their body is completely relaxed in the chair. They are in the center of the frame, lying flat in the memory chair and facing the ceiling. They are in the foreground, occupying the focal point of the shot."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "The pain has been removed. You'll feel much better.",
                    "role_name": "Ayla"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                },
                {
                    "role_id": "6891b33846cf66d652c1ccbc",
                    "role_name": "Client",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379095049-fqbdg0.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The entrance of the memory design studio. The door frame is made of white metal, and blue light streams through the door gap. Inside the studio, a floating holographic device and scattered light spots are visible. The silver walls reflect a soft light. The floor is made of smooth metal, maintaining a cool, tech-inspired environment. The light at the entrance is brighter, creating a contrast with the interior. The style is flat anime, with geometric architectural lines.",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "Old Man",
                        "action_and_emotion": "A deep and resolute expression, with focused and powerful eyes. He has a slow and steady walking posture, with his arms swinging naturally. He is in the right-center of the frame, having just stepped into the studio, facing inward with his side toward the camera. He is in the foreground, occupying the main visual focus."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "content": "I need your help, but not to delete a memory.",
                    "role_name": "Old Man"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "Old Man",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The central area of the memory design studio. Blue holographic equipment surrounds a silver metal workbench. Floating memory fragments drift slowly in the air. White LED light strips illuminate the entire space, and the walls display data streams. The floor is smooth and reflective, creating a professional and mysterious tech environment. The style is flat anime, with simplified lighting effects and geometric equipment designs.",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "Old Man",
                        "action_and_emotion": "A serious and solemn expression, with deep eyes looking at Ayla. He holds out a memory orb with one hand and maintains a dignified standing posture. He is on the left side of the frame, facing Ayla and turned three-quarters toward the camera. He is in a medium shot."
                    },
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A confused and perplexed expression, with a slightly furrowed brow. Her eyes are focused on the memory orb, and she leans slightly forward, showing curiosity. She is on the right side of the frame, facing the Old Man with her side toward the camera. She is in the foreground, with a clear and reactive motion."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "content": "I need to transfer this memory to you. It contains the truth about this world.",
                    "role_name": "Old Man"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "Old Man",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "A surreal memory space. Countless glowing fragments of memory and geometric patterns of the city's control network are scattered across a deep blue and purple gradient background. The AI network is represented by silver light grids, and memory fragments float like transparent glass. The entire space feels like a dream, with shifting light and shadows. The style is flat anime, with abstract geometric shapes and high-contrast colors.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A shocked and fearful expression, with wide eyes and a slightly open mouth. She is leaning backward in surprise, with her hands involuntarily clenched into fists. She is in the center of the frame, facing the memory images and looking directly at the camera. She is in the foreground, with a strong emotional expression."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "This... this is impossible!",
                    "role_name": "Ayla"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "Close Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The interior of the memory design studio, with a renewed focus on the central work area. Silver metal furniture and blue holographic displays are quietly suspended in the air, and the memory editing equipment emits a cool light. The data displayed on the walls has dimmed, and only a faint ambient light keeps the space visible. The overall atmosphere is more solemn and oppressive than before. The style is flat anime, with reduced saturation and enhanced shadow contrast.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A complex expression of internal struggle, with a deeply furrowed brow. Her eyes shift between the memory deletion device and the Old Man, and her hands are tightly gripping the chair's armrests. She is sitting in the work chair, her body tense, facing to the side and three-quarters toward the camera. She is in the foreground."
                    },
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "Old Man",
                        "action_and_emotion": "A calm and patient expression, with deep eyes silently watching Ayla. His hands are clasped in front of him, and he remains still, waiting. He is in the background on the right side of the frame, facing Ayla with his side toward the camera. He is in the background, maintaining a sense of presence."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "Who are you? Why are you telling me this?",
                    "role_name": "Ayla"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "Old Man",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "The memory design studio, focusing on the dialogue area. The lighting is a soft blue-white, the walls are silver metal, and the floating equipment is silently running. The memory light spots in the air have decreased, making the environment seem more serious and heavy. The equipment on the workbench emits a faint glow, and the overall atmosphere conveys the tension of an important conversation. The style is flat anime, with simplified background details to highlight the characters.",
                "characters": [
                    {
                        "role_id": "6891b31046cf66d652c1ccba",
                        "role_name": "Old Man",
                        "action_and_emotion": "A heavy and sorrowful expression, with eyes full of regret and determination. His hands are trembling slightly, and he stands with a dignified posture but shows signs of fatigue. He is in the center of the frame, facing Ayla and looking directly at the camera. He is in the foreground, with a profound emotional expression."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "content": "I am one of the creators of this system, but by the time I realized its danger, it was too late. Now, only people like you who have mastered memory technology can help people reclaim their true memories.",
                    "role_name": "Old Man"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b31046cf66d652c1ccba",
                    "role_name": "Old Man",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379064604-5ixhm8.png"
                }
            ],
            "shot_size": {
                "value": "Close Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 6,
                "time_scale": "seconds"
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
                "background": "A wide shot of the memory design studio. It is a tech space dominated by silver and white, with blue holographic equipment scattered throughout. The floating memory light spots are active again, and the equipment emits a stable light. The overall environment has regained its professional feel, but the atmosphere has fundamentally changed, filled with a new sense of resolve and purpose. The style is flat anime, with clear geometric lines and a balanced composition.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A firm and resolute expression, with clear and powerful eyes. Her fists are clenched, showing determination, and she stands up straight. She is in the center of the frame, facing forward and looking directly at the camera. She is in the foreground, displaying a strong sense of resolve and transformation."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "If this is true, then I cannot continue to be an accomplice to this system.",
                    "role_name": "Ayla"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The edge of a futuristic city rooftop. The sky is an orange-red from the sunset, and the outlines of floating buildings and the transparent dome are visible in the distance. The city lights begin to turn on, appearing as blue and white spots of light. The rooftop is made of white metal and has a safety railing at the edge. A gentle breeze blows, creating a calm atmosphere of contemplation and resolve. The style is flat anime, with simplified architectural details to emphasize the color contrast.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A calm and determined expression, with her eyes focused on the deletion device in her hands. She holds the device up, ready to throw it away, and her body is facing the edge of the city. She is standing at the edge of the rooftop, with her side toward the camera and the expansive cityscape in the background. She is in the foreground, and her action is symbolic."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "A distant shot of the city rooftop. The lingering sunset light bathes the entire futuristic city in an orange-red glow, creating a contrast with the city's blue and white lights. The floating buildings appear more dreamlike in the twilight, and the transparent dome reflects the sunset. The rooftop is on a tall building, overlooking the entire cityscape. A light breeze blows, creating an epic moment of resolve. The style is flat anime, with simplified details to highlight the atmosphere.",
                "characters": [
                    {
                        "role_id": "6891b2e546cf66d652c1ccb8",
                        "role_name": "Ayla",
                        "action_and_emotion": "A steadfast and determined expression, with her eyes looking into the distance. Her arms are hanging naturally by her sides, and she stands straight, facing the future. She is at the edge of the rooftop, with her back to the sunset, and she is looking directly at the camera with a long shadow cast behind her. She is in the foreground, with a posture full of hope and resolve."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "content": "Some truths are worth bearing the pain to protect.",
                    "role_name": "Ayla"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b2e546cf66d652c1ccb8",
                    "role_name": "Ayla",
                    "role_resource_url": "https://resource.visiony.cc/image/1754379023024-fzxzmy.png"
                }
            ],
            "shot_size": {
                "value": "Long Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "The interior of a magnificent palace in the divine realm of Takamagahara, with a backdrop of swirling clouds and sky. The palace is in a traditional Japanese architectural style, featuring wooden beams, pillars, and a gilded roof. The interior is covered with exquisite tatami mats, and the walls are decorated with murals of sun totems. A luxurious golden throne sits in the center, surrounded by floating golden light. The ceiling is adorned with colorful clouds, and soft golden light streams in from all directions, creating a sacred and peaceful atmosphere.",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "Amaterasu-Ōmikami",
                        "action_and_emotion": "Sitting majestically on the golden throne, with a dignified but gentle expression and eyes fixed forward. Her body is straight, and her hands are elegantly placed on her knees, embodying divine authority. She is in the center of the frame, occupying the main focal point, and facing slightly to the left of the camera."
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Standing in front of the palace with an angry expression, a furrowed brow, and tightly clenched fists. His body is leaning slightly forward, showing impulsiveness. Flashes of lightning flicker around him. He is in the left foreground, turned to face Amaterasu-Ōmikami."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "Sister, I want to go down to the human world to prove my strength!",
                    "role_name": "Susanoo-no-Mikoto"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "Amaterasu-Ōmikami",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The interior of a magnificent palace in the divine realm of Takamagahara, with a backdrop of swirling clouds and sky. The palace is in a traditional Japanese architectural style, featuring wooden beams, pillars, and a gilded roof. The interior is covered with exquisite tatami mats, and the walls are decorated with murals of sun totems. A luxurious golden throne sits in the center, surrounded by floating golden light. The ceiling is adorned with colorful clouds, and soft golden light streams in from all directions.",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "Amaterasu-Ōmikami",
                        "action_and_emotion": "An expression of concern, with a slightly furrowed brow and eyes filled with worry. Her body is leaning forward, and one hand is slightly raised in a gesture of dissuasion. She is in the center of the frame, sitting on the golden throne and facing the camera directly."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "content": "You are too impulsive; you will bring disaster to the human world.",
                    "role_name": "Amaterasu-Ōmikami"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "Amaterasu-Ōmikami",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                }
            ],
            "shot_size": {
                "value": "Close Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "A scene of an ancient Japanese mountain village on a cloudy night. The village consists of traditional wooden houses with thatched roofs, scattered across a valley. Stone paths wind through the village, flanked by bamboo forests and old pine trees. The distant mountains are blurred and obscured by heavy clouds, with lightning flashing within them. The village is shrouded in dark night, with only scattered lights shining from the windows, creating a tense and uneasy atmosphere.",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Descending from the sky, his feet have just touched the ground, and his body is in a landing posture. He has a serious expression, and his eyes scan the village, surrounded by flashes of lightning. He is in the center of the frame, with his full body visible and facing the camera directly. The blurry figures of frightened villagers are scattered in the background."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "On a dark and cloudy night, Susanoo-no-Mikoto descends from the heavens, landing in an ancient Japanese mountain village.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The side of a peaceful river, with moonlight shining on the water, creating silver ripples. Willow trees and reeds grow on both banks, and a gentle breeze rustles the grass. The river water is clear, and small fish occasionally swim by. The riverbank is covered with smooth pebbles, and distant mountains rise in the background. The night sky is dotted with stars. The overall environment is quiet and serene, a stark contrast to the previous tense atmosphere.",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "Kushinadahime",
                        "action_and_emotion": "Sitting on a stone by the river, with her face buried in her hands, sobbing and her body trembling slightly. Her hair is disheveled, and her clothes are slightly messy, with her body curled in a protective posture. She is in the right side of the frame, turned to face the river."
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Walking slowly toward her, with a concerned expression. He extends one hand slightly in a questioning gesture. His body is leaning slightly forward, showing concern and curiosity. He is on the left side of the frame, facing Kushinadahime."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "Maiden, why are you so sad?",
                    "role_name": "Susanoo-no-Mikoto"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "Kushinadahime",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "The side of a peaceful river, with moonlight shining on the water, creating silver ripples. Willow trees and reeds grow on both banks, and a gentle breeze rustles the grass. The river water is clear, and small fish occasionally swim by. The riverbank is covered with smooth pebbles, and distant mountains rise in the background. The night sky is dotted with stars. The overall environment is quiet and serene.",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "Kushinadahime",
                        "action_and_emotion": "Raising her head to look at Susanoo-no-Mikoto, her eyes sparkling with tears. Her expression is sad and fearful, and her lips tremble slightly. She gently wipes a tear from the corner of her eye, while remaining seated. She is in the right-center of the frame, facing Susanoo-no-Mikoto."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "content": "The Yamata-no-Orochi is coming to devour me! My father has already fled, and all the villagers are in hiding.",
                    "role_name": "Kushinadahime"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "Kushinadahime",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                }
            ],
            "shot_size": {
                "value": "Close Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "An open clearing in the center of the village, surrounded by traditional Japanese houses. The ground is flat dirt, with scattered stones. Most of the houses have closed doors and windows, appearing empty. Rolling mountains are in the distance, and the sky is gloomy, with an uneasy atmosphere hanging in the air. A translucent illusion of the Yamata-no-Orochi hovers above the clearing, with eight giant heads roaring and red eyes flashing.",
                "characters": [
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "Kushinadahime",
                        "action_and_emotion": "Standing and speaking, with a fearful expression and her body trembling slightly. She points one hand at the phantom in the air, while the other is tightly clasped to her chest. Her eyes reveal deep fear and despair. She is on the left side of the frame, turned to face the phantom of the Yamata-no-Orochi."
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Listening intently, with a serious expression. His eyes are fixed on Kushinadahime and the phantom in the air. He stands straight with his hands at his sides, showing a determined will. He is on the right side of the frame, facing Kushinadahime."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccda",
                    "content": "That monster eats a young woman every year, and this year, it is my turn.",
                    "role_name": "Kushinadahime"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "Kushinadahime",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "A riverbank at sunset. The sky is a gradient of orange and red, and the last rays of the sun form a golden band on the water's surface. The willow trees on both banks sway in the breeze, and the reeds rustle. The distant mountains are a deep purple silhouette. The overall environment is warm and tranquil, creating an atmosphere of hope and determination.",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Holding the hilt of his sword, with a firm and resolute expression. His eyes are filled with determination and courage. He stands upright, with one hand on his sword's hilt and the other in a gesture of a vow. He is in the center of the frame, facing the camera directly, with the sunset creating a halo effect behind him."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "I swear I will kill the Yamata-no-Orochi and save you. But I need your help.",
                    "role_name": "Susanoo-no-Mikoto"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "An open clearing in a valley, surrounded by towering peaks. The ground is relatively flat. In the center of the clearing are eight large wooden barrels arranged in a circle. The barrels are brown wood with iron hoops and emit a strong scent of sake. Scattered around are tools and ropes for preparation. A dark cave entrance in the distance exudes an ominous aura.",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Directing the setting of the trap, with his arm outstretched toward the barrels. His expression is focused and serious. He is leaning slightly forward, showing a commanding presence. He is on the left side of the frame, facing the barrels and Kushinadahime."
                    },
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "Kushinadahime",
                        "action_and_emotion": "Assisting with the preparations. Her expression shows courage despite her fear, and her hands are busy organizing ropes. Her body is slightly bent as she focuses on the task at hand. She is on the right side of the frame, working near the barrels."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "Fill these barrels with the strongest sake. The monster won't be able to fight once it's drunk.",
                    "role_name": "Susanoo-no-Mikoto"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "Kushinadahime",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "A valley on a full moon night. A huge full moon hangs in the sky, casting silver light on the ground. The valley floor begins to shake violently, and dust rises into the air. A deep roar comes from a distant cave entrance, and a red glow flashes from within. The entire scene is filled with tension and horror. Trees sway and birds and beasts flee in terror.",
                "characters": [
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "Yamata-no-Orochi",
                        "action_and_emotion": "Emerging from the cave, with eight giant heads roaring and red eyes glowing. Its fangs are exposed, and its eight tails twist and writhe. Its massive body occupies the valley, exuding a terrifying and majestic presence. It is in the center background of the frame, taking up most of the space, and facing the camera."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "On the night of the full moon, the Yamata-no-Orochi appeared, its eight huge heads gleaming coldly in the moonlight.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8f446cf66d652c1ccde",
                    "role_name": "Yamata-no-Orochi",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
                }
            ],
            "shot_size": {
                "value": "Long Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "The area with the sake barrel trap in the valley, gleaming in the moonlight. The eight barrels are neatly arranged, and a strong scent of sake emanates from them. The ground shows signs of violent shaking, with small stones scattered. Jagged rocks in the distance provide a hiding place for Susanoo-no-Mikoto.",
                "characters": [
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "Yamata-no-Orochi",
                        "action_and_emotion": "Its eight heads greedily stretch toward the barrels, frantically drinking the strong sake. Its movements become slow and wobbly. Its eyes gradually become hazy, and its body sways unsteadily, showing clear signs of drunkenness. It is in the center of the frame, with its heads spread out around the barrels."
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Quietly observing from behind a rock. His body is pressed against the rock, and one eye watches the serpent's state. His hand is on his sword's hilt, ready to strike. His expression is focused and alert, waiting for the best moment. He is behind a rock on the left side of the frame, turned to face the serpent."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "The giant serpent discovered the barrels and drank the strong sake until it was completely intoxicated.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b8f446cf66d652c1ccde",
                    "role_name": "Yamata-no-Orochi",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "A valley in the midst of a fierce battle. Blood splatters in the moonlight, and the ground is scarred with deep sword slashes and marks from the serpent's body dragging. Rocks are shattered, dust flies, and the air is thick with the scent of battle. Sword light flashes in the night sky, forming a beautiful but deadly arc of light.",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Leaping and swinging his sword, with a roaring expression and eyes burning with a will to fight. His muscles are tense and powerful. The divine sword in his hand flashes with a cold light as he adopts an attacking posture. He is in the central foreground, in a highly dynamic combat pose."
                    },
                    {
                        "role_id": "6891b8f446cf66d652c1ccde",
                        "role_name": "Yamata-no-Orochi",
                        "action_and_emotion": "Struggling and resisting violently. Some of its heads have been severed, while the remaining ones roar in pain. Its body twists and writhes. Its red eyes show anger and agony, and blood splatters everywhere. Its massive body is in the background, occupying most of the space."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "For the peace of the human world, I will not be defeated!",
                    "role_name": "Susanoo-no-Mikoto"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                },
                {
                    "role_id": "6891b8f446cf66d652c1ccde",
                    "role_name": "Yamata-no-Orochi",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380592152-9rs74g.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 6,
                "time_scale": "seconds"
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
                "background": "The valley after the battle has ended, returning to peace and tranquility. Soft moonlight falls upon the ground. The giant body of the Yamata-no-Orochi lies motionless. The scent of battle fades from the air, replaced only by a faint smell of blood and the quiet of victory.",
                "characters": [
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Holding up the glowing Kusanagi-no-Tsurugi. His expression is joyous with victory as he raises his arms to show the trophy. He stands upright, filled with the dignity and pride of a victor. He is in the center of the frame, facing the camera directly, with the sword shining brightly."
                    },
                    {
                        "role_id": "6891b8c946cf66d652c1ccdc",
                        "role_name": "Kushinadahime",
                        "action_and_emotion": "Cheering with her hands raised high. Her expression is full of joy and gratitude, and her eyes are moist with tears of excitement. She is jumping up to express her ecstasy. She is on the right side of the frame, facing Susanoo-no-Mikoto."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "This divine sword will become a sacred artifact to protect the human world.",
                    "role_name": "Susanoo-no-Mikoto"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                },
                {
                    "role_id": "6891b8c946cf66d652c1ccdc",
                    "role_name": "Kushinadahime",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380531403-enilb5.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The interior of the magnificent palace in the divine realm of Takamagahara, now with a restored peaceful atmosphere. The sky with swirling clouds is visible, and the golden light is softer and warmer. The palace decorations are still magnificent, and the sun totem murals appear especially sacred in the soft light. Thunder and sunlight interweave in the air, creating a beautiful light effect.",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "Amaterasu-Ōmikami",
                        "action_and_emotion": "A relieved smile on her face. Her eyes are gentle as she looks at her brother, expressing a sister's pride and care. Her body is relaxed, and her hands are elegantly placed, embodying her inner joy. She is in the center of the frame, sitting on the golden throne."
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Presenting the Kusanagi-no-Tsurugi with both hands. His expression is humble and respectful, and his eyes show newfound wisdom. His body is slightly bent in a sign of reverence, showing an inner change. He is in the foreground, facing Amaterasu-Ōmikami."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "content": "Sister, I have learned the meaning of responsibility.",
                    "role_name": "Susanoo-no-Mikoto"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "Amaterasu-Ōmikami",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The magnificent palace in the divine realm of Takamagahara, filled with a warm and harmonious glow. Thunder and sunlight interweave beautifully in the sky, creating a rainbow-like spectrum. The palace decorations appear more sacred and solemn in this light. The entire environment emanates a warm atmosphere of reconciliation between the siblings.",
                "characters": [
                    {
                        "role_id": "6891b84046cf66d652c1ccd8",
                        "role_name": "Amaterasu-Ōmikami",
                        "action_and_emotion": "Responding with a warm smile. Her eyes are filled with love and approval, and her body leans slightly forward in a gesture of closeness. Her overall posture embodies a sister's tolerance and relief. She is on the right side of the frame, facing Susanoo-no-Mikoto."
                    },
                    {
                        "role_id": "6891b86f46cf66d652c1ccda",
                        "role_name": "Susanoo-no-Mikoto",
                        "action_and_emotion": "Smiling back sincerely. His eyes are bright with a new maturity. His body is straight, showing his inner resolve. His overall posture expresses respect for his sister and his own growth. He is on the left side of the frame, facing Amaterasu-Ōmikami."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "content": "Brother, you have proven your courage and wisdom.",
                    "role_name": "Amaterasu-Ōmikami"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891b84046cf66d652c1ccd8",
                    "role_name": "Amaterasu-Ōmikami",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380399106-9rz5le.png"
                },
                {
                    "role_id": "6891b86f46cf66d652c1ccda",
                    "role_name": "Susanoo-no-Mikoto",
                    "role_resource_url": "https://resource.visiony.cc/image/1754380488299-varrsi.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "The interior of a geometric coffee shop late at night, with a warm origami-inspired design. Sharp, angular geometric tables and chairs are arranged throughout the space, with furniture surfaces that have a paper-like texture. The walls are decorated with geometric-style illustrations and neat angular frames. Warm yellow geometric lighting illuminates the space, with a uniform, paper-like glow. Through the glass windows, geometric raindrops and the geometric cityscape of a rainy night are visible. The coffee machine and other equipment have simple geometric shapes, and the entire space exudes a cozy atmosphere based on the aesthetics of origami.",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A focused and calm geometric expression. She is standing in the center behind the bar, facing the camera at a geometric angle. Her body is in a slightly leaning geometric posture, and she is holding a coffee cup, performing a cleaning motion. She is in the main foreground, with her clear geometric form prominently displayed. Her movements are gentle and skilled, reflecting the grace of the origami-style character."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "On a cold and rainy night, a small coffee shop on a city street radiates a warm glow.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "A geometric space in a corner of the coffee shop. Comfortable geometric seating and a round geometric table. Geometric decorations and a bookshelf on the wall, with objects displayed that have a paper-like texture. Soft geometric lighting creates a warm atmosphere, with a private geometric space designed in the corner.",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "Old Zhang",
                        "action_and_emotion": "A gentle and friendly geometric smile. He is sitting in a corner seat, in a relaxed geometric posture. He is facing the bar, with a side angle to the camera. He is in a medium shot, with his clear geometric form visible. He is holding a newspaper and is in the geometric motion of preparing to put it down."
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A warm, responsive geometric smile. She is standing at the bar, turning her head to face Old Zhang at a geometric angle. She is in the background, with part of her body visible. Her hands are in a focused geometric gesture of preparing a drink, showing her professionalism in service."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "content": "Xiaoyu, a hot chocolate, please, with extra foam.",
                    "role_name": "Old Zhang"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "Sure, Uncle Zhang. It's raining so hard today, why are you out?",
                    "role_name": "Lin Xiaoyu"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "Old Zhang",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "A geometric design in the coffee shop's entrance area. A geometrically shaped door frame and glass door, with a geometric street view of the rainy night visible through the glass. The ground has a geometric tile pattern, and there are geometric decorative elements by the door. The dim geometric exterior contrasts with the warm geometric interior.",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "Chen Haoran",
                        "action_and_emotion": "A slightly nervous and hesitant geometric expression. He is standing at the door, in a geometric posture of having just entered. He is facing inward, with a two-thirds angle to the camera. He is in the main foreground, with the geometric texture of his wet jacket being prominent. His eyes convey a geometric expression of both expectation and uncertainty."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "Just then, the doorbell rang crisply, and a figure pushed the door open and stepped inside.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "Chen Haoran",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "A geometric wide shot of the coffee shop interior. The complete geometric layout, from the bar to the seating area. The warm geometric lighting system and geometric art decorations on the walls. The geometric layered sense of the entire space creates a cozy origami-inspired atmosphere.",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A shocked and paused geometric expression. She is standing behind the bar, in a stiff geometric posture. Her gaze is fixed on the door, with a side angle to the camera. She is in a medium shot, with her clear geometric outline visible. Her movements have stopped in a frozen geometric pose."
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "Chen Haoran",
                        "action_and_emotion": "An uneasy geometric expression. He is standing near the door, in a slightly tense geometric posture. He is facing the bar, with a geometric angle from the back to the camera. He is in the background, with part of his outline visible. The geometric texture of his wet jacket is prominent."
                    },
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "Old Zhang",
                        "action_and_emotion": "A pensive and observant geometric expression. He is sitting in the corner, in a geometric posture of leaning forward. His gaze shifts between the two people, with a side angle to the camera. He is in the background, in a quiet geometric state of observation."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "Haoran?",
                    "role_name": "Lin Xiaoyu"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "content": "Xiaoyu, can... can I come in?",
                    "role_name": "Chen Haoran"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "Chen Haoran",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "Old Zhang",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "A geometric design in the coffee shop's bar area. The bar has a detailed geometric structure, and the coffee equipment has geometric shapes. The geometric decorations on the back wall and the warm lighting create geometric light and shadow effects. The shot captures the geometric spatial relationship between the bar and the seating area.",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A geometric expression of trying to control her emotions. She is standing behind the bar, in a slightly tense geometric posture. She is facing Chen Haoran, with a direct angle to the camera. She is in the main foreground, with clear geometric details of her face. She forces a geometric smile."
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "Chen Haoran",
                        "action_and_emotion": "A geometric expression of hope mixed with unease. He is sitting on a geometric chair in front of the bar, in a geometric posture of leaning forward. He is facing Lin Xiaoyu, with a side angle to the camera. He is in a medium shot, with a clear geometric outline. His hands are in a geometric motion of being placed on the bar."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "Of course. What would you like to drink?",
                    "role_name": "Lin Xiaoyu"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "Chen Haoran",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "A geometric wide shot of the coffee shop space. The overall geometric layout, with a geometric design from the corner to the bar. Soft geometric lighting and geometric art on the walls. The geometric layered sense of the space reflects a cozy, origami-inspired environment.",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "Old Zhang",
                        "action_and_emotion": "A wise and benevolent geometric smile. He is sitting in the corner, in a relaxed geometric posture. His gaze is directed toward the bar, with a side angle to the camera. He is in the foreground, with his clear geometric form visible. He is in the geometric action of preparing to speak."
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A silent and contemplative geometric expression. She is standing behind the bar, in a slightly stiff geometric posture. Her gaze is wandering, with a side angle to the camera. She is in a medium shot, with part of her body visible. Her inner turmoil is shown through her geometric outer expression."
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "Chen Haoran",
                        "action_and_emotion": "An awkward and silent geometric expression. He is sitting in front of the bar, in a tense geometric posture. He is in a state of contemplation, with his head down and his back to the camera. He is in the background, with his outline clearly visible. His fingers are in a geometric motion of tapping on the tabletop."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "content": "Young man, some words have been kept inside for too long. If you don't say them, they'll grow moldy.",
                    "role_name": "Old Zhang"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "Old Zhang",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "Chen Haoran",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "A geometric close shot of the coffee shop bar area. A delicate geometric bar design, with geometric arrangements of coffee utensils. The geometric wall decorations in the background and the geometric lighting effects from the warm lamps. The shot creates a geometric space for an intimate conversation.",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "Chen Haoran",
                        "action_and_emotion": "A sincere and determined geometric expression. He is sitting in front of the bar, in a geometric posture of leaning forward. His gaze is fixed on Lin Xiaoyu, with a direct angle to the camera. He is in the main foreground, with clear geometric facial features. He takes a deep breath before speaking in a geometric action."
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A shocked and moved geometric expression. She is standing behind the bar, her body trembling slightly in a geometric posture. Her eyes are filled with tears, in a geometric expression, with a side angle to the camera. She is in a medium shot, with her clear geometric emotional state visible. The coffee cup in her hand trembles in a geometric detail."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "content": "Xiaoyu, I want to tell you that I've never forgotten you. Three years ago, I was too cowardly to explain properly or ask you to stay. I know I was wrong... if you're willing to give me a chance, I'd like to start over.",
                    "role_name": "Chen Haoran"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "content": "I need time.",
                    "role_name": "Lin Xiaoyu"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "Chen Haoran",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 6,
                "time_scale": "seconds"
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
                "background": "The interior of the geometric coffee shop under moonlight. Geometric moonlight streams through the window, forming geometric light and shadow patterns on the floor. The warm geometric indoor lighting contrasts with the cool geometric moonlight. A serene geometric street view is visible outside the window after the rain.",
                "characters": [
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "Chen Haoran",
                        "action_and_emotion": "A gentle and relieved geometric smile. He is sitting in front of the bar, in a relaxed geometric posture. He is in the geometric motion of reaching out to touch something, with a side angle to the camera. He is in the foreground, with a clear geometric hand gesture. His eyes have a warm and firm geometric expression."
                    },
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A receptive and responsive geometric smile. She is standing behind the bar, in a slightly leaning geometric posture. She is in the geometric motion of not pulling her hand away, with a direct angle to the camera. She is in a medium shot, with her clear geometric emotional change visible. Her eyes show a renewed hope in a geometric expression."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "Just then, the rain stopped. Moonlight poured through the window into the coffee shop, and the two looked at each other and smiled.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "Chen Haoran",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "A geometric design in the coffee shop's entrance area. A geometric door frame and glass door, with a serene geometric street view outside. The ground has a geometric texture, and the door is decorated with geometric elements. The warm interior contrasts with the peaceful geometric exterior.",
                "characters": [
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "Old Zhang",
                        "action_and_emotion": "A content and benevolent geometric smile. He is standing at the door, in a relaxed geometric posture. He is holding a bouquet of sunflowers, with a direct angle to the camera. He is in the main foreground, with his clear geometric figure visible. His eyes have a warm and wise geometric expression."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "content": "Sunflowers always face the sun, just as hope always looks toward the future.",
                    "role_name": "Old Zhang"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "Old Zhang",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "A geometric round table area inside the coffee shop. A delicate geometric round table design, with comfortable geometric chairs arranged around it. A geometric bouquet of sunflowers on the table and geometric arrangements of coffee cups. Geometric light and shadow from the moonlight through the window create a warm and harmonious geometric space. The geometric city night view outside the window, with geometric light reflected in puddles.",
                "characters": [
                    {
                        "role_id": "6891bfa046cf66d652c1cd03",
                        "role_name": "Lin Xiaoyu",
                        "action_and_emotion": "A warm and serene geometric smile. She is sitting by the round table, in a relaxed geometric posture. Her gaze is fixed on the sunflowers, with a side angle to the camera. She is in the foreground, with her clear geometric outline visible. Her inner peace is reflected in her geometric outer expression."
                    },
                    {
                        "role_id": "6891bfec46cf66d652c1cd07",
                        "role_name": "Chen Haoran",
                        "action_and_emotion": "A hopeful and contented geometric expression. He is sitting by the table, in a geometric posture of leaning forward. His gaze is gently directed at Lin Xiaoyu, with a side angle to the camera. He is in a medium shot, with his clear geometric emotional state visible. His hands are in a geometric motion of being placed on the table."
                    },
                    {
                        "role_id": "6891bfc846cf66d652c1cd05",
                        "role_name": "Old Zhang",
                        "action_and_emotion": "A benevolent and satisfied geometric smile. He is sitting by the table, in a comfortable geometric posture. He has a geometric perspective of observing the whole scene, with a direct angle to the camera. He is in the background, with a harmonious and integrated geometric presence. His expression shows he is enjoying the cozy moment."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "Perhaps time can heal past wounds, and perhaps, this is a new beginning.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891bfa046cf66d652c1cd03",
                    "role_name": "Lin Xiaoyu",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382279609-2xtyql.png"
                },
                {
                    "role_id": "6891bfec46cf66d652c1cd07",
                    "role_name": "Chen Haoran",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382352363-hhqbfa.png"
                },
                {
                    "role_id": "6891bfc846cf66d652c1cd05",
                    "role_name": "Old Zhang",
                    "role_resource_url": "https://resource.visiony.cc/image/1754382418462-kf8wds.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "A medieval stone castle in a blizzard. Thick, gray clouds cover the sky, and heavy snow falls. Ancient stone walls stand tall, and snow accumulates on the spires of the towers. The castle gates are tightly shut. Inside, weak smoke rises from the chimneys of stone houses, and faint yellow candlelight shines from the windows. The castle is surrounded by an endless snowy plain with deep snow. A cold wind howls, kicking up snow. The lighting is dim and oppressive, and the overall color palette is cold gray-blue, creating a frigid and desperate atmosphere.",
                "characters": []
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "A century-long winter envelops the northern kingdom of Levinburg. Famine and despair spread like a plague.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [],
            "shot_size": {
                "value": "Long Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "High-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The interior of the royal palace hall. Tall stone pillars support an arched roof, and the walls are built of heavy stone bricks. Iron torch holders hang on the walls, with orange flames flickering and casting long shadows. The floor is laid with marble slabs and a red carpet runs down the center. A high-backed wooden throne is on a raised platform, surrounded by stained glass windows. The indoor temperature is relatively warmer than outside, but the atmosphere is still cold and solemn.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Kneeling on one knee on the red carpet in the center of the hall. His left knee is on the ground, his right leg supports his upright torso. His silver armor reflects the torchlight, and his dark blue eyes are fixed forward with a firm and dignified expression. His hands are placed on his knees, and his head is slightly bowed in a gesture of respect. He is positioned in the lower-center of the frame, facing the throne, embodying a knight's dignity and resolve."
                    },
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "Lyanna",
                        "action_and_emotion": "Standing to the right of the throne platform, turned slightly to face Eric. Her lake-blue eyes show worry, and her brow is slightly furrowed, revealing her inner anxiety. Her right hand tightly grips the edge of her golden cape, while her left arm hangs naturally by her side. Her posture is slightly tense, showing her concern for the knight's dangerous journey. She is in a medium shot on the right side of the frame, forming a visual dialogue with Eric."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "Your Highness, I pledge to find the Heart of the Winds for the kingdom and end this endless winter.",
                    "role_name": "Eric"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                },
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "role_name": "Lyanna",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "A stone platform on top of the city wall. Snow falls in the night sky, and a cold wind howls. The heavy stone battlements have sharp lines, and iron torches are mounted on brackets, with orange flames violently swaying in the wind. In the distance, the snowy plain gleams faintly under the moonlight, and the area below the castle is pitch black. Snow mist swirls in the wind, and the temperature is extremely low. The overall atmosphere is desolate yet romantic.",
                "characters": [
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "Lyanna",
                        "action_and_emotion": "Standing at the edge of the city wall, leaning slightly toward Eric. Her lake-blue eyes are filled with tears, and her expression is gentle and reluctant to part. She is delicately handing a red silk pendant to Eric, with a cautious movement full of affection. Her golden cape flutters slightly in the wind. Her overall posture shows deep affection and worry. She is in the left-center of the frame, facing Eric at a two-thirds side angle."
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Receiving the pendant from Lyanna with open hands. His dark blue eyes are fixed on the princess, and his expression is gentle and firm. His face shows a mixture of tenderness and determination, reflecting his complex emotions. His body leans toward the princess, and his silver armor emits a soft glow in the torchlight. His overall posture is gentle and solemn, showing his deep love for the princess and his commitment to his mission. He is in the right-center of the frame, facing Lyanna at a two-thirds side angle."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "content": "Take this. Let it protect you and bring you home safely.",
                    "role_name": "Lyanna"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "role_name": "Lyanna",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Close Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "An expansive and undulating snowy plain. White snow covers the land, extending to the horizon. The dim sky is filled with heavy clouds, and a storm rages across the area, with snowflakes sweeping by like whips. The outlines of distant mountains are blurred, and the ground nearby is covered in deep snow. There is no vegetation or buildings, just a completely desolate natural environment. The light is extremely faint, and the overall color palette is cold gray and white, creating an atmosphere of extreme and harsh weather.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Walking alone in the snowy plain, his body leaning forward against the strong wind. His dark blue cape flaps in the wind, and snow has accumulated on his silver armor. He uses his long sword as a walking stick for support in his right hand, and his left hand shields his face from the wind and snow. His steps are heavy and slow but firm. His face shows fatigue but a strong will. He is in the lower-center of the frame, walking sideways, showing his resilience in the harsh environment."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "Eric embarks on his quest, facing the trial of endless wind and snow alone.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Long Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "High-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "The edge of a snowy forest. Sparse, dead trees stand, their bare branches bent under the weight of snow. The ground is covered with a thick, uneven layer of snow, with scattered dead branches and leaves. A faint campfire burns in the center, its weak orange light flickering and illuminating a limited area. The shadows between the trees are deep and dark, and a few pairs of faint blue glowing eyes are faintly visible. The night is heavy, with the moonlight obscured by clouds. The overall atmosphere is tense and dangerous.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "His back is against a thick, dead tree trunk, and his body is tense in a state of alert. His right hand tightly grips the hilt of his long sword, the blade reflecting the campfire light. His face is streaked with blood and mixed with melted snow, and his expression is focused and resolute. His dark blue eyes scan the surrounding shadows, and his muscles are tense, ready to fight at any moment. The silver armor has alternating highlights and shadows from the firelight, showing the knight's bravery in the face of danger. He is in the center of the frame, leaning against the tree and facing the shadows."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "Come on, I will not back down.",
                    "role_name": "Eric"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
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
                "background": "The entrance to the Valley of the Damned. The mountain cliffs are towering, and the valley entrance is narrow and deep. Mist rises from the bottom of the valley, obscuring visibility. A huge ice waterfall hangs from the cliff face, forming ice pillars. An ancient stone tablet is half-buried in the snow, with weathered characters carved into its surface. Dead, ancient trees grow in a twisted manner, their branches reaching out like ghostly claws. The lighting is dim and mysterious, and the overall atmosphere is ancient and oppressive, exuding an ominous feeling.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Standing in front of the stone tablet, leaning forward to carefully examine the inscription. His left hand gently touches the surface of the tablet, and his right hand holds his sword at his side. His dark blue eyes are fixed on the inscription with a serious and concentrated expression. His silver armor reflects the faint sky light, and his cape sways gently in the breeze. His overall posture shows reverence and a spirit of exploration for the ancient legend. He is in the center of the frame, facing the tablet at a side angle."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "The Heart of the Winds is just ahead. I must continue.",
                    "role_name": "Eric"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The depths of the Valley of the Damned. Ancient, dead trees are arranged in a circle, forming an open space. The trees are tall and twisted, their branches bare and their bark old and cracked. The ground is covered in thick snow, but black soil is visible underneath. A huge blue crystal floats in the center of the valley floor, emitting a soft, pulsating light like a heartbeat. A light blue energy mist surrounds the crystal, radiating a sacred aura. The light source is primarily the crystal itself, creating a mysterious and solemn atmosphere.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Standing below the crystal, his head tilted back as he gazes at the Heart of the Winds. His dark blue eyes are illuminated by the crystal's light, and his pupils reflect a blue glow. His expression is a mixture of awe, hope, and shock, and his lips are slightly parted in wonder. His hands hang naturally at his sides, and his body is relaxed but in a respectful posture. The silver armor reflects the blue crystal light, and his overall image is solemn and reverent. He is in the lower-center of the frame, looking up at the crystal from a front angle."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "The legendary Heart of the Winds. It really exists.",
                    "role_name": "Eric"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The valley floor is suddenly engulfed in a blizzard. Mist swirls and rolls, obscuring visibility. The dead trees sway in the strong wind, making creaking sounds. The snow on the ground is swept up by the wind, forming vortices, and the air is filled with a cold mist. Visibility is extremely low, and only blurry outlines are visible. The wind howls like ghosts and wolves. The overall atmosphere suddenly becomes dangerous and eerie, signaling that a major event is about to happen.",
                "characters": [
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "Frost Giant Wolf",
                        "action_and_emotion": "Slowly emerging from the mist, its massive body is faintly visible. Its eerie blue eyes are fixed on Eric, radiating an oppressive authority. It stands steadily on all fours, its muscles tense with power. Its head is slightly bowed, and its sharp fangs are bared in a warning. Its snow-white fur flutters in the wind, and cold mist exhales from its nostrils. Its overall posture conveys the majesty and danger of a mysterious guardian. It is in the back-center of the frame, facing forward in a threatening stance."
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Facing the wolf's threat. He holds his long sword up to his chest with both hands, the tip of the sword pointing at the wolf. He is slightly crouched in a combat-ready stance, with his legs apart for balance. His dark blue eyes look directly into the wolf's eyes. His expression is resolute and fearless, without any sign of backing down. His silver armor is covered with a thin layer of snow, and his cape flies in the wind. He shows the knight's courage and determination in the face of danger. He is in the left foreground, facing the wolf at a three-quarters side angle."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "Guardian, I came to save the kingdom.",
                    "role_name": "Eric"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da678f0f67046b15a635",
                    "role_name": "Frost Giant Wolf",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Low-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The battlefield is in turmoil. The snow on the ground is churned up, forming vortices. Bright red blood stains the pristine white snow, creating a stark visual contrast. The storm continues to rage, and snow mist obscures some of the view. Dead trees sway in the background, and deep claw marks and footprints are left in the ground. The battle area is extensive, showing signs of a fierce struggle. The overall color palette is dominated by white snow and red blood, creating a tragic battle atmosphere.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Leaning back to block the wolf's pounce. He holds up his shield with his left arm for defense, and his right hand holds his sword, ready to counterattack. His silver armor has cracks and damage, and his dark blue cape is stained with blood. His expression is one of gritted teeth, showing he is under immense pressure but will not yield. His muscles are tense as he uses all his strength to fight the powerful enemy, and his boots leave deep marks in the snow. He shows the knight's stubborn will in a life-or-death situation. He is in the right foreground, with his body angled to counter the incoming attack."
                    },
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "Frost Giant Wolf",
                        "action_and_emotion": "Its front paws are raised, ready to pounce. Its giant mouth is open, revealing sharp fangs. Its eerie blue eyes flash with murderous intent, and its snow-white fur stands on end in anger. Its massive body is arched, gathering strength. It pushes off the ground with its hind legs, kicking up snow mist. Its movements are swift and powerful, showing the innate aggression of a beast. Cold mist spews from its mouth, and its overall posture is menacing. It is in the left medium shot, with its body leaning forward in an attacking stance, facing Eric."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "I will not fall!",
                    "role_name": "Eric"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                },
                {
                    "role_id": "6891da678f0f67046b15a635",
                    "role_name": "Frost Giant Wolf",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Dutch-angle",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Tracking Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 2,
                "time_scale": "seconds"
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
                "background": "The battle has suddenly stopped, and the valley floor is calm again. The blizzard has gradually subsided. Only the faint sound of wind remains, and snowflakes fall slowly. The ground is a mixture of blood and snow, showing traces of the recent fierce battle. The dead trees have stopped swaying, and the mist is dissipating, revealing clear outlines. The blue Heart of the Winds in the distance continues to glow, providing a faint light. The overall atmosphere shifts from intense to solemn, filled with a sense of the sacred and of destiny.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Injured and on the ground, but he props himself up with his upper body. He holds the red silk pendant tightly to his chest with his right hand. His dark blue eyes look up at the wolf, his gaze still firm and unyielding, without fear, only resolve. His facial expression shows pain, but his will is strong, and a trace of blood runs from the corner of his mouth. His silver armor is heavily damaged, with cracks exposing the inner lining. His posture is weak, but his spirit is not broken, embodying true knightly spirit. He is in the lower-center of the frame, in a half-lying position, looking up at the wolf."
                    },
                    {
                        "role_id": "6891da678f0f67046b15a635",
                        "role_name": "Frost Giant Wolf",
                        "action_and_emotion": "Stopping its attack and standing still, staring at Eric. The murderous intent in its eerie blue eyes gradually dissipates, replaced by scrutiny and contemplation. Its head is slightly tilted as it observes the fallen knight, and its ears are perked up, showing focus. Its body is relaxed and no longer tense, and its tail hangs naturally. Its breathing is steady, and its fangs are no longer bared in a threat. Its overall posture changes from aggressive to observant, as if moved by the knight's spirit. It is in the upper-center of the frame, looking down at Eric from a front-facing, observational angle."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "content": "My love and my oath, they will never be betrayed.",
                    "role_name": "Eric"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                },
                {
                    "role_id": "6891da678f0f67046b15a635",
                    "role_name": "Frost Giant Wolf",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389116839-ihrvbv.png"
                }
            ],
            "shot_size": {
                "value": "Close Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 5,
                "time_scale": "seconds"
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
                "background": "The square outside the city gates of Levinburg. The warm spring sun shines through the clouds onto the ground. The snow is beginning to melt, forming small streams that flow over the ground, revealing wet stone slabs. Melting snow drips from the stone gaps in the city wall, making a crisp sound. The air is warm and moist, with a gentle breeze. Citizens gather on both sides of the road, their expressions changing from emaciated to hopeful, their eyes filled with awe and gratitude. Colorful flags flutter in the breeze. The overall atmosphere is warm and celebratory.",
                "characters": [
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Walking slowly toward the city gates, holding the blue Heart of the Winds crystal, which emits a soft glow. His body is tired, but his steps are firm and steady, showing the pride of a completed mission. His silver armor shows signs of battle, with several repairs, but it is still dignified. His expression is calm and solemn, and his dark blue eyes show the satisfaction of having completed a great task. His cape sways gently in the breeze. His overall image is that of a legendary hero returning. He is in the center of the frame, walking toward the city gates at a front-facing angle."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "The hero returns, bringing the hope of spring.",
                    "role_name": "Narrator"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Full Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Push Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 4,
                "time_scale": "seconds"
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
                "background": "The marble steps in front of the royal palace. Early spring sunlight streams through the stained-glass windows, casting colorful light and shadows. The steps are decorated with exquisite stone pillars, carved with floral patterns at the top. Melted snow drips from the eaves, forming small puddles on the ground that reflect the sunlight. A gentle breeze blows the palace flags, and the air is fresh and warm. Birdsong can be heard in the distance, symbolizing new life and hope. The overall atmosphere is warm and romantic, filled with the joy of reunion.",
                "characters": [
                    {
                        "role_id": "6891da528f0f67046b15a633",
                        "role_name": "Lyanna",
                        "action_and_emotion": "Running down the steps, her white dress fluttering in motion. Her lake-blue eyes are filled with tears of joy, and her expression is one of excited happiness mixed with deep longing. Her arms are open, ready for an embrace, and her golden cape flutters behind her. Her footsteps are light and eager, showing her impatience for the reunion. Her chestnut hair sparkles in the sunlight, and her overall image is as beautiful and moving as a goddess of spring. She is at the top of the frame, starting to run down, facing Eric from a front angle."
                    },
                    {
                        "role_id": "6891da318f0f67046b15a631",
                        "role_name": "Eric",
                        "action_and_emotion": "Standing at the bottom of the steps with his arms open, ready to welcome the princess. His dark blue eyes are fixed on the running Lyanna, and his gaze is gentle and affectionate. His expression is one of contentment and happiness, with a long-awaited smile on his face. His body is leaning forward, preparing for an embrace, and his silver armor emits a warm glow in the sunlight. The red silk pendant hangs lightly on his chest, symbolizing the protective power of love. His overall posture shows the happiness and satisfaction of a hero who has completed his mission. He is in the lower-center of the frame, looking up at the princess from a front-facing, welcoming angle."
                    }
                ]
            },
            "dialogues": [
                {
                    "role_id": "voiceover",
                    "content": "",
                    "role_name": "Narrator"
                },
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "content": "Eric, you're back!",
                    "role_name": "Lyanna"
                }
            ],
            "main_characters": [
                {
                    "role_id": "6891da528f0f67046b15a633",
                    "role_name": "Lyanna",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389094721-3s5uof.png"
                },
                {
                    "role_id": "6891da318f0f67046b15a631",
                    "role_name": "Eric",
                    "role_resource_url": "https://resource.visiony.cc/image/1754389074402-wovwux.png"
                }
            ],
            "shot_size": {
                "value": "Medium Shot",
                "size_values": [
                    "Long Shot",
                    "Full Shot",
                    "Medium Shot",
                    "Close Shot",
                    "Close-Up"
                ]
            },
            "camera_angle": {
                "value": "Eye-level",
                "angle_values": [
                    "Eye-level",
                    "Low-angle",
                    "High-angle",
                    "Bird's-eye",
                    "Dutch-angle"
                ]
            },
            "shot_type": {
                "value": "Fixed Shot",
                "type_values": [
                    "Fixed Shot",
                    "Push Shot",
                    "Pull Shot",
                    "Pan Shot",
                    "Tracking Shot",
                    "Tilt Shot",
                    "Zoom Shot"
                ]
            },
            "shot_time": {
                "value": 3,
                "time_scale": "seconds"
            }
        }
    ],
}