import { useSortable } from "@dnd-kit/sortable";
import { CSS } from "@dnd-kit/utilities";
import sortIcon2 from "./../../../../../../assets/images/pages/boardView/sort_icon_2.svg";

interface IProps {
  id: string; // 项目内容
}

const SortableItem: React.FC<IProps> = ({ id }: IProps) => {
  const { attributes, listeners, setNodeRef, transform, transition } =
    useSortable({ id });

  const style = {
    transform: CSS.Translate.toString(transform), // 将坐标转换为 CSS transform
    transition,
  };

  return (
    <div ref={setNodeRef} style={style} {...attributes}>
      <img {...listeners} src={sortIcon2} alt="sort" className="mr-2" />
      {id}
    </div>
  );
};

export default SortableItem;
