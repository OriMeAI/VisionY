// 编辑页头部底部总高度
const EDITOR_PAGE_HEAD_AND_FOOT_HEIGHT = 310;

class DrawHelper {
  constructor() {}
  getWinW(): number {
    return (
      window.innerWidth ||
      document.documentElement.clientWidth ||
      window.screen.width
    );
  }
  getWinH(): number {
    return (
      window.innerHeight ||
      document.documentElement.clientHeight ||
      window.screen.height
    );
  }
  getContainerHeight(): number {
    return this.getWinH() - EDITOR_PAGE_HEAD_AND_FOOT_HEIGHT;
  }
}
export default new DrawHelper();
