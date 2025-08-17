class ArrayUtils {
  constructor() {}

  /**
   * 通过keyName和keyValue获取数组中的某一项
   */
  //   getRecordById<T>(arr: T[], keyName: string, keyValue: number | string): T {
  //     return arr.filter((item) => item[keyName] === keyValue)[0];
  //   }

  getRecordById(arr: any[], keyName: string, keyValue: number | string) {
    return arr.filter((item) => item[keyName] === keyValue)[0];
  }
}
export default new ArrayUtils();
