import mammoth from 'mammoth';
import * as XLSX from 'xlsx';

/**
 * 文件类型枚举
 */
export enum FileType {
  TXT = 1,
  DOCX = 2,
  XLSX = 3,
  UNKNOWN = 0
}

/**
 * 文件读取结果接口
 */
export interface FileReadResult {
  content: string;
  fileType: FileType;
  success: boolean;
  error?: string;
}

/**
 * 文件读取类
 * 用于读取不同类型文件的内容
 */
export class FileReader {
  /**
   * 根据文件扩展名获取文件类型
   * @param fileName 文件名
   * @returns 文件类型
   */
  private static getFileType(fileName: string): FileType {
    const extension = fileName.split('.').pop()?.toLowerCase();
    
    switch (extension) {
        case 'txt':
            return FileType.TXT;
        case 'docx':
            return FileType.DOCX;
        case 'xlsx':
        case 'xls':
            return FileType.XLSX;
        default:
            return FileType.UNKNOWN;
    }
  }

  /**
   * 读取文本文件内容
   * @param file 文件对象
   * @returns Promise<string> 文件内容
   */
  private static readTextFile(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new globalThis.FileReader();
      reader.onload = (e) => {
        resolve(e.target?.result as string || '');
      };
      reader.onerror = (e) => {
        reject(new Error('Read file error'));
      };
      reader.readAsText(file);
    });
  }

  /**
   * 读取DOCX文件内容
   * @param file 文件对象
   * @returns Promise<string> 文件内容
   */
  private static async readDocxFile(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new globalThis.FileReader();
      reader.onload = async (e) => {
        try {
          const arrayBuffer = e.target?.result as ArrayBuffer;
          const result = await mammoth.extractRawText({ arrayBuffer });
          resolve(result.value);
        } catch (error) {
          reject(new Error('Read docx file failed'));
        }
      };
      reader.onerror = () => {
        reject(new Error('ead docx file failed'));
      };
      reader.readAsArrayBuffer(file);
    });
  }

  /**
   * 读取Excel文件内容
   * @param file 文件对象
   * @returns Promise<string> 文件内容
   */
  private static async readExcelFile(file: File): Promise<string> {
    return new Promise((resolve, reject) => {
      const reader = new globalThis.FileReader();
      reader.onload = (e) => {
        try {
          const arrayBuffer = e.target?.result as ArrayBuffer;
          const workbook = XLSX.read(arrayBuffer, { type: 'array' });
          
          let result = '';
          // 遍历所有工作表
          workbook.SheetNames.forEach(sheetName => {
            const worksheet = workbook.Sheets[sheetName];
            const json = XLSX.utils.sheet_to_json(worksheet, { header: 1 });
            
            // 添加工作表名称
            result += `[${sheetName}]\n`;
            
            // 将每行数据转换为字符串
            json.forEach((row: any) => {
              if (Array.isArray(row)) {
                result += row.join('\t') + '\n';
              }
            });
            
            result += '\n';
          });
          
          resolve(result.trim());
        } catch (error) {
          reject(new Error('Read excel file failed'));
        }
      };
      reader.onerror = () => {
        reject(new Error('Read excel file failed'));
      };
      reader.readAsArrayBuffer(file);
    });
  }

  /**
   * 读取文件内容
   * @param file 文件对象
   * @returns Promise<FileReadResult> 文件读取结果
   */
  public static async readFile(file: File): Promise<FileReadResult> {
    try {
      const fileType = this.getFileType(file.name);
      
      if (fileType === FileType.UNKNOWN) {
        return {
          content: '',
          fileType: FileType.UNKNOWN,
          success: false,
          error: 'Can not support file type，please upload .txt .docx or .xlsx file'
        };
      }
      
      let content = '';
      
      switch (fileType) {
        case FileType.TXT:
          content = await this.readTextFile(file);
          break;
        case FileType.DOCX:
          content = await this.readDocxFile(file);
          break;
        case FileType.XLSX:
          content = await this.readExcelFile(file);
          break;
      }
      
      return {
        content,
        fileType,
        success: true
      };
    } catch (error) {
      return {
        content: '',
        fileType: FileType.UNKNOWN,
        success: false,
        error: error instanceof Error ? error.message : 'Read file failed'
      };
    }
  }
}

export default FileReader;