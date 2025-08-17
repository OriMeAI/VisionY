class StringUtils {
  constructor() {}

  /**
   * 通过百分比字符串获取数字
   */
  getNumByPercentStr(percentStr: string) {
    return percentStr ? parseFloat(percentStr.replace("%", "")) / 100 : 0;
  }
  /**
   * 通过数字获取百分比字符串
   */
  getPercentStrByNum(num: number) {
    return num ? `${Math.round(num * 100)}%` : "0%";
  }
  /**
   * 前位补0
   */
  prefixZero(numStr: string): string {
    return numStr.padStart(2, "0");
  }
  getUrlParam(name: string): string {
    let paramValue = "";
    const params = new URLSearchParams(location.search);
    // 遍历查询参数对象
    for (const [key, value] of params.entries()) {
      if (key === name) {
        paramValue = value;
      }
    }
    return paramValue;
  }
}
export default new StringUtils();
