def generate_random_string() -> str:
    """
    生成一个32位的随机字符串
    
    Returns:
        str: 32位随机字符串
    """
    import uuid
    # 生成一个UUID并去除连字符，得到32位的十六进制字符串
    return uuid.uuid4().hex