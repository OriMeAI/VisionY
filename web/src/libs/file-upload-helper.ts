class FileUploadHelper {
  constructor() {}

  /**
   * 文件大小转换
   */
  formatFileSize(size: number): string {
    if (size < 1024) return `${size} B`;
    if (size < 1024 * 1024) return `${Math.round(size / 1024)} kb`;
    if (size < 1024 * 1024 * 1024)
      return `${Math.round(size / (1024 * 1024))} mb`;
    return `${Math.round(size / (1024 * 1024 * 1024))} gb`;
  }
}
export default new FileUploadHelper();
