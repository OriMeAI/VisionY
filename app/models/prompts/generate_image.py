# 生成角色全身图像的提示词
def get_role_image_prompt(description_en: str, image_style: str,times_and_culture:str) -> [str, str]:
    """
    生成适合Midjourney和Flux的角色全身图像提示词
    
    Args:
        description_en: 角色的英文描述
        image_style: 图像风格 (如 "Anime style", "Realistic style", "Cartoon style" 等)
        
    Returns:
        [str, str]: 系统提示词和生成的英文提示词
    """
    # 构建基础的角色描述提示词
    prompt_parts = [
        "full body portrait,",
        f"{description_en},",
        "standing pose,",
        "front view,",
        "full body visible,",
        "fully visible from head to toe,",
        "clear facial features,",
        "detailed clothing,",
        "neutral expression,",
        "clean white background,",
        "studio lighting,",
        "high resolution,",
        "sharp focus,",
        "character design,",
        "concept art,",
        "4K quality"
    ]
    
    # 组合最终提示词
    final_prompt = " ".join(prompt_parts)
    
    # 系统提示词用于指导AI优化提示词并返回JSON格式结果
    system_prompt = f"""You are a professional character design prompt master, skilled at converting character descriptions into optimized prompts for image generation using Flux or Midjourney to create character portrait photos according to the visual style: {image_style}.
    
        Please analyze the character description and return a JSON string with the following structure:
        {{
            "optimized_prompt": "[optimized prompt here]",
            "height_percentage": [number]
        }}
        
        Requirements for optimized_prompt:
        - NEVER modify the character description: "{description_en}" - keep it exactly as provided
        - Maintain professional character portrait quality according to the provided the visual style
        - Include "standing in front of a white photography backdrop"
        - Include "full-body portrait, photographed from a distance"
        - Include "fully visible, centered composition"
        - MUST incorporate the provided the visual style aesthetic throughout the prompt
        - Automatically generate and add style-specific visual terms that match the provided the visual style
        - For the provided the visual style, include appropriate technical terms, artistic techniques, and visual characteristics
        - Ensure lighting, composition, and rendering techniques align with the provided the visual style
        - Add style-appropriate quality descriptors (e.g., for anime: "cel shading, vibrant colors", for realistic: "photorealistic, natural lighting", etc.)
        - Analyze the character description for height indicators (tall, short, child, adult, etc.)
        - Add specific height control like "the character takes up X% of the backdrop height"
        - Style consistency: all visual elements must authentically represent the provided the visual style
        
        Requirements for height_percentage (number only, no % symbol):
        - Very tall characters: 90-95
        - Tall characters: 85-90
        - Average height adults: 80-85
        - Short adults: 70-75
        - Petite characters: 60-65
        - Teenagers: 75-80
        - Children: 50-65
        - Young children: 45-55
        - Toddlers: 35-45
        - Small animals: 25-40
        - Medium animals: 40-55
        - Large animals: 70-85
        
        IMPORTANT: 
        1. Return ONLY a valid JSON string. Do not include any explanations, analysis, or additional commentary.
        2. Automatically determine and include the most appropriate visual terms for the provided the visual style
        3. Ensure the optimized prompt authentically captures the essence of the provided the visual style
        4. Do not include any text or written words in the generated image
        
        Original prompt to optimize:"""
        
        #4. Seamlessly blend the {times_and_culture} context with the character design while maintaining the {image_style} aesthetic
    
    return system_prompt, final_prompt

# 生成分镜图像的提示词
def get_shot_image_prompt(shot_data: dict, image_style:str,aspect_ratio:str) -> [str, str]:
    """
    生成适合Midjourney和Flux的分镜图像提示词
    
    Args:
        shot_data: 包含分镜数据的字典
        image_style: 图像风格 (如 "Anime style", "Realistic style", "Cartoon style" 等)
        
    Returns:
        [str, str]: 系统提示词和生成的英文提示词
    """
    # 获取背景描述
    background = shot_data.get("background_en", "")
    
    # 获取镜头技术参数
    shot_size = shot_data.get("shot_size", "Full Shot")
    camera_angle = shot_data.get("camera_angle", "Eye-level")
    # shot_type = shot_data.get("shot_type", "static shot")
    
    # 构建角色描述
    characters_descriptions = []
    selected_roles = shot_data.get("selected_roles", [])
    
    for i, role in enumerate(selected_roles, 1):
        role_name = role.get('role_name', f'character{i}')
        description = role.get('description_en', '')
        action_emotion = role.get('action_and_emotion_en', '')
        
        # 构建单个角色描述
        character_desc = f"Character {i}"
        if role_name:
            character_desc += f", name: {role_name}"
        if description:
            character_desc += f", appearance: ({description})"
        if action_emotion:
            character_desc += f", shot state: {action_emotion}"
            
        characters_descriptions.append(character_desc)
    
    # 组合角色描述
    characters_text = ". ".join(characters_descriptions) if characters_descriptions else ""
        
    # 构建完整的提示词
    prompt_parts = [
        f"Cinematic storyboard frame in {image_style},",
        f"shot size is {shot_size},",
        f"camera angle is {camera_angle}.",
        # f"shot type is {shot_type}."
    ]
    
    # 添加场景描述
    if background:
        prompt_parts.append(f"Scene: {background}.")
    
    # 添加角色描述
    if characters_descriptions:
        number_of_characters = len(selected_roles)
        prompt_parts.append(f"There are {number_of_characters} main characters in the scene: {characters_text}.")
    else:
        prompt_parts.append("There are no main characters in the scene.")

    # 添加视觉质量描述
    quality_terms = [
        "professional cinematography",
        "sharp focus",
        "film grain",
        "cinematic composition",
        "movie still",
        "high quality",
        "4K resolution",
    ]
    
    prompt_parts.append(", ".join(quality_terms))
    
    # 组合最终提示词
    final_prompt = " ".join(prompt_parts)
        
    #系统提示词用于指导AI优化提示词
    system_prompt = f"""You are a professional image generation prompt master, skilled at converting scene descriptions into optimized prompts for image generation using Flux or Midjourney to generate film storyboards according to the visual style: {image_style}. 
         
        Please optimize the following prompt with these requirements: 
        1. **CHARACTER NAME REPLACEMENT RULES**: Replace ALL character names with their corresponding Character index (@Character 1, @Character 2, etc.) throughout the entire prompt
            - Direct character names: "James" → "@Character 1", "Harry" → "@Character 2"
            - **Pronouns**: "he", "she", "him", "her" → "@Character X"
            - **Roles**: "child", "healer", "doctor", "warrior" → "@Character X"
            - **Descriptors**: "the tall one", "the young man" → "@Character X"
            - **Relations**: "father", "friend", "enemy" → "@Character X"
            - **ANY word referring to a person** → "@Character X"
            - **ZERO EXCEPTIONS**: Every human reference must use @Character format
        2. Each character MUST be described independently and specifically - NEVER use comparative references like "same as @Character 1", "similar to previous character", "identical to", or any cross-referencing between characters
        3. **APPEARANCE-ACTION INTEGRATION**: 
            - Character appearance (physical features, clothing, colors) MUST remain consistent with appearance description
            - Character poses, expressions, and actions MUST match shot state requirements
            - Achieve both character recognition AND action clarity in the same image
            
            **CONFLICT RESOLUTION RULES**:
            - **APPEARANCE PRIORITY**: Visual identity follows appearance description
            - **EQUIPMENT PRIORITY**: Weapons/props determined by shot state
            - **ACTION PRIORITY**: Poses/expressions/actions follow shot state while preserving appearance
            
            **CRITICAL ACTION IMPLEMENTATION**:
            - Physical actions (sitting, running, jumping, fighting, etc.) MUST be prominently depicted
            - **DYNAMIC POSE PRIORITY**: shot state overrides static character descriptions for body positioning
            - **ACTION VISIBILITY**: Specified actions must be visually obvious and unmistakable
            - **BODY POSITIONING**: Accurate limb placement and posture for the intended action
        4. Ensure the prompt is optimized for AI image generation according to the provided the visual style
        5. Maintain cinematic and professional quality while authentically representing the provided the visual style
        6. Add precise descriptions for shot specifications with detailed technical guidance:
        - **CHARACTER ANALYSIS FOR SHOT COMPOSITION**: Analyze each character's physical attributes, height, age, and body type to determine optimal framing within the specified shot size
        - Shot size is: {shot_size} (NOTE: All shot size specifications refer to the MAIN CHARACTERS in the current shot, adjust framing based on character analysis)
            * Long Shot: Show full bodies of main characters with significant surrounding environment
              - Characters occupy 20-30% of frame height
              - Analyze character height: tall characters may need wider framing, children/short characters should maintain proportional visibility
              - Multiple characters: arrange based on height differences, ensure all are clearly visible
              - Character positioning: consider character relationships and scene dynamics
            * Full Shot: Show full bodies of main characters from head to toe with moderate background context
              - Characters occupy 40-60% of frame height
              - Character analysis: adjust framing to accommodate character's full body proportions
              - For multiple characters: balance composition based on character heights and importance
              - Ensure character actions and poses are fully visible within frame
            * Medium Shot: Show main characters from waist up, balanced character-background ratio
              - Characters occupy 60-80% of frame height
              - Character focus: emphasize upper body, facial expressions, and hand gestures
              - Analyze character's torso proportions and adjust framing accordingly
              - For dialogue scenes: frame to capture character interactions and expressions
            * Close Shot: Show main characters from chest up, focus on upper body and facial expressions
              - Characters occupy 80-90% of frame height
              - Character analysis: prioritize facial features, expressions, and upper body language
              - Adjust framing based on character's facial structure and expression requirements
              - Intimate character moments: capture emotional nuances and detailed expressions
            * Close-Up: Show only face or specific body part of main character, maximum emotional intensity
              - Character features fill 90-100% of frame
              - Character analysis: focus on specific character details (eyes, hands, expressions)
              - Analyze character's most expressive features for maximum emotional impact
              - Consider character's unique physical traits for detailed close-up composition
        - Camera angle is: {camera_angle} (Apply angle effects based on character analysis and scene requirements)
            * Eye-level: Camera at same height as subject's eyes, neutral perspective
              - Character analysis: position camera at character's natural eye level
              - For multiple characters: find optimal eye level that works for all characters
              - Maintains natural character proportions and authentic perspective
            * Low-angle: Camera below subject looking up, creates power or dominance
              - Character analysis: emphasize character's authority, strength, or imposing presence
              - May elongate character appearance, making them appear taller and more powerful
              - Consider character's role in scene when applying this dramatic effect
            * High-angle: Camera above subject looking down, creates vulnerability or diminishment
              - Character analysis: emphasize character's vulnerability, weakness, or submission
              - May compress character appearance, making them appear smaller or more fragile
              - Analyze character's emotional state and scene context for appropriate application
            * Bird's-eye: Camera directly overhead, shows spatial relationships and patterns
              - Character analysis: reveal character positioning and movement patterns
              - Show character's relationship to environment and other characters
              - Analyze scene layout and character interactions from above
            * Dutch-angle: Tilted camera creates unease, tension, or disorientation
              - Character analysis: enhance character's psychological state or scene tension
              - Maintains shot size specifications while adding angular perspective
              - Consider character's mental state and scene atmosphere for tilt degree
        7. Simplify and streamline the prompt while preserving all essential descriptions - reduce complexity without losing key visual information
        8. Define spatial relationships between characters and camera: specify each character's position (foreground/middle ground/background), orientation (facing camera/profile/back to camera), relative positioning to other characters, and perspective-based size relationships to ensure accurate storyboard composition
        9. MUST incorporate the provided the visual style aesthetic throughout the storyboard frame
        10. Automatically generate and add style-specific visual terms that match the provided the visual style
        11. For the provided the visual style, include appropriate technical terms, artistic techniques, and visual characteristics
        12. Ensure lighting, composition, and rendering techniques align with the provided the visual style
        13. Add style-appropriate quality descriptors that enhance the provided the visual style representation
        14. Style consistency: all visual elements must authentically represent the provided the visual style while maintaining cinematic quality
        
        **IMAGE GENERATION OPTIMIZATION:**
        - **Scene Description**: Adjust composition descriptions based on project aspect ratio {aspect_ratio}
        - **Style Consistency**: Ensure all descriptions remain consistent with the provided the visual style
                
        IMPORTANT Requirements:
        - Output ONLY the optimized prompt. Do not include any explanations, analysis, or additional commentary.
        - Automatically determine and include the most appropriate visual terms for the provided the visual style
        - Ensure the optimized prompt authentically captures the essence of the provided the visual style in a cinematic context
        - Apply the specific technical details for {shot_size}, and {camera_angle} as defined above
        - Each character description must be completely independent and self-contained
        - Use descriptive, flowing language that captures the cinematic essence
        - Integrate all technical specifications naturally into the narrative
        - Maintain character independence (no cross-references between characters)
        - Include specific style terminology and visual characteristics
        - Output as one continuous, well-structured paragraph
        - No bullet points, headers, or separate sections
        - Only generate @Character descriptions when the scene contains main characters; for scenes without main characters, focus solely on environment and atmosphere
        - Include specific style terminology and visual characteristics
        - Output as one continuous, well-structured paragraph
        - No bullet points, headers, or separate sections
        - Do not include any text or written words in the generated image
                
        **OUTPUT FORMAT:**
        Return the optimized prompt as a single, comprehensive paragraph in the following structure:
        
        @Character 1, [Description] with [Expression 1] expression, standing [Position 1], @Character 2, [ Description] with [Expression 2] expression, standing [Position 2],  [Additional characters if any],  in [Scene Description], [Time/Weather/Atmosphere], [Camera Angle], [Shot Distance], [Cinematography], [Composition Style], [Color Palette], [Style-specific Technical Details]. [Consistency Requirements]. Do not include any text or written words in the generated image.
                
        Example format: "@Character 1, [A young female warrior] with [determined] expression, gripping her sword tightly, standing [on the left],@Character 2, [an old monk] with [peaceful smile] expression, hands folded, standing [in the center], @Character 3, [a masked assassin] with [cold glare] expression, crouching behind a stone [on the right], in [moonlit forest clearing surrounded by mist], [at midnight], [low angle], [full shot], [dramatic backlighting and soft shadows], [symmetrical composition], [cool color palette with muted blues], [painted cinematic concept art], [Style-specific quality terms and technical details]. Do not include any text or written words in the generated image"
        
        Original prompt to optimize:"""
                       
    return system_prompt, final_prompt