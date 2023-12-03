import cv2
from imread_from_url import imread_from_url
from YOLOv6 import YOLOv6

# Initialize YOLOv6 object detector
model_path = "D:/Kodingan/nyc/bestmodel.onnx"
yolov6_detector = YOLOv6(model_path, conf_thres=0.35, iou_thres=0.5)

# Read image from local
image_path = 'D:/Kodingan/nyc/img/2.jpeg'
img = cv2.imread(image_path)

# Detect Objects
boxes, scores, class_ids = yolov6_detector(img)

# Define class names (assuming you have the same class names as in your YOLOv6 model)
class_names = ['ambulan', 'bis', 'becak', 'mobil', 'pemadam-kebakaran', 'sepeda-motor', 'truk', 'angkot', 'mobil-polisi', 'manusia']  # Add your class names here

# Initialize a dictionary to store class counts
class_counts = {class_name: 0 for class_name in class_names}

# Iterate through the detected class_ids
for class_id in class_ids:
    class_name = class_names[class_id]
    
    # Update the count for the detected class
    class_counts[class_name] += 1

# Calculate the weight based on class counts
weight = 0
for class_name, count in class_counts.items():
    if class_name == 'mobil':
        weight += count * 2
    elif class_name == 'sepeda-motor':
        weight += count * 1
    elif class_name == 'bis':
        weight += count * 5
    elif class_name == 'becak':
        weight += count * 1
    elif class_name == 'angkot':
        weight += count * 2
    elif class_name == 'ambulan':
        weight += count * 500
    elif class_name == 'pemadam-kebakaran':
        weight += count * 2000
    elif class_name == 'mobil-polisi':
        weight += count * 50
    elif class_name == 'truk':
        weight += count * 5
    else:
        weight += count * 0

def get_weight():
    return weight

cv2.destroyAllWindows()