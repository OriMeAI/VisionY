import { StoryboardShot } from "./../../../../../types/storyboard";

// 获取指定类型的属性值
export const getCellValue = <T>(
  shot: StoryboardShot | null,
  propertyName: string
): T | null => {
  if (!shot) return null;
  return ((shot as any)[propertyName] as T) || null;
};



// 获取下一个镜头
export const getNextShot = (
  shots: StoryboardShot[],
  currentShotIndex: number
): number | null => {

  // 如果当前场景还有下一个镜头
  if (currentShotIndex < shots.length - 1) {
    return currentShotIndex + 1;
  }

  // 如果已经是最后一个镜头
  return null;
};

// 获取上一个镜头
export const getPrevShot = (
  shots: StoryboardShot[],
  currentShotIndex: number
): number | null => {
  // 如果当前场景还有上一个镜头
  if (currentShotIndex > 0) {
    return currentShotIndex - 1;
  }
  // 如果已经是第一个镜头
  return null;
};

// 获取角色图片URL的辅助函数
export const getRoleImageUrl = (roleId: string, currentShot: any): string => {
  if (!currentShot || roleId === "voiceover") return null;

  // 如果缓存中没有，尝试从main_characters中获取角色资源URL
  const mainCharacters = currentShot.main_characters || [];
  const mainCharacter = mainCharacters.find(
    (char: any) => char.role_id === roleId
  );
  if (mainCharacter && mainCharacter.role_resource_url) {
    return mainCharacter.role_resource_url;
  }

  // 尝试从scene_description.characters中获取角色资源URL
  const sceneDescription = currentShot.scene_description || {};
  const characters = sceneDescription.characters || [];
  const character = characters.find((char: any) => char.role_id === roleId);
  if (character && character.resource_url) {
    return character.resource_url;
  }

  // 如果都找不到，返回空字符串
  return null;
};
