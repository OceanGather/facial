from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

def draw_boxes(img,boxes,color,size):
    size = int(size/150)
    for box in boxes:
        x1,y1 = box[0]
        x2,y2 = box[1]
        
        for i in range(x1,x2):
            for j in range(y1 - size//2,y1 + size//2):
                img[j][i] = color

            for j in range(y2 - size//2,y2 + size//2):
                img[j][i] = color

        for j in range(y1,y2):
            for i in range(x1 - size//2,x1 + size//2):
                img[j][i] = color

            for i in range(x2 - size//2,x2 + size//2):
                img[j][i] = color

    return img

def get_label(path,width,height):
    str_label = ''
    str_labels = []
    boxes = []
    with open(path) as f:
        lines = f.readlines()
        for line in lines:
            label = line.split('\n')[0].split(' ')[0:5]
            print(label)
            str_label = ' '.join(label)
            str_labels.append(str_label)

            x = int(float(label[1]) * width)
            y = int(float(label[2]) * height)
            box_width = int(float(label[3]) * width)
            box_height = int(float(label[4]) * height)

            x1 = x - box_width // 2
            y1 = y - box_height // 2
            x2 = x + box_width // 2
            y2 = y + box_height // 2

            box = ((x1,y1),(x2,y2))
            boxes.append(box)

    str_labels = '\n'.join(str_labels)
    str_labels += '\n'
    with open(path, 'w') as f:
        f.write(str_labels)

    return boxes

if __name__ == '__main__':
    img = Image.open('./dataset/images/train/00003.jpg')
    img = np.array(img)
    height,width,_ = img.shape

    boxes = get_label('./dataset/labels/train/00003.txt',width,height)
    color = (123, 104, 238)
    img = draw_boxes(img,boxes,color,min(height,width))

    plt.imshow(img)
    plt.axis('off') # 关掉坐标轴为 off
    plt.title('image') # 图像题目
    plt.show()
    