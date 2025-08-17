// 分镜数据结构定义

// 分镜资源
export interface ShotResource {
  shot_resource_url: string;
  is_HD: boolean;
  shot_resource_id: string;
}

// 角色
export interface Character {
  role_id: string;
  role_name: string;
  action_and_emotion: string;
}

// 场景描述
export interface SceneDescription {
  background: string;
  characters: Character[];
}

// 对白
export interface Dialogue {
  role_id: string;
  content: string;
  role_name: string;
}

// 主要角色
export interface MainCharacter {
  role_id: string;
  role_name: string;
  role_resource_url: string;
}

// 镜头视角
export interface ShotSize {
  value: string;
  size_values: string[];
}

// 相机角度
export interface CameraAngle {
  value: string;
  angle_values: string[];
}

// 镜头类型
export interface ShotType {
  value: string;
  type_values: string[];
}

// 镜头时间
export interface ShotTime {
  value: string;
  time_scale: string;
}

// 分镜项
export interface StoryboardShot {
  shot_id: string;
  shot_resource: ShotResource;
  scene_description: SceneDescription;
  dialogues: Dialogue[];
  main_characters: MainCharacter[];
  shot_size: ShotSize;
  camera_angle: CameraAngle;
  shot_type: ShotType;
  shot_time: ShotTime;
}

// 分镜数据响应
export interface StoryboardResponse {
  code: number;
  data: StoryboardShot[];
  msg: string;
}