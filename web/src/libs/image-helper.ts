import { ImageSize } from "./interfaces";

class ImageHelper {
  constructor() {}

  /**
   * 通过预加载图片获取图片的宽高
   */
  preloadImage(src: string): Promise<ImageSize> {
    const promise: Promise<ImageSize> = new Promise(function (resolve, reject) {
      const img = new Image();
      img.src = src;
      img.onload = function () {
        if (!img.width || !img.height) {
          reject("Image size is 0");
        }
        resolve({
          width: img.width,
          height: img.height,
        });
      };
      img.onerror = function(e) {
        reject("Failed to load image: " + e);
      };
    });
    return promise;
  }
}
export default new ImageHelper();
