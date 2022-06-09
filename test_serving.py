import matplotlib.pyplot as plt
import cv2

image = cv2.imread("data/test_image.jpg")

label = [
    {
        "x1": 1049.67529296875,
        "y1": 2049.525146484375,
        "x2": 3697.778076171875,
        "y2": 2390.3642578125,
        "confidence": 0.6516660451889038,
        "class": "Single crack",
        "color": [
            30,
            144,
            255
        ]
    },
    {
        "x1": 3826.751220703125,
        "y1": 1700.506591796875,
        "x2": 5176.32275390625,
        "y2": 2172.30322265625,
        "confidence": 0.49658891558647156,
        "class": "Single crack",
        "color": [
            30,
            144,
            255
        ]
    },
    {
        "x1": 2212.18310546875,
        "y1": 1003.4577026367188,
        "x2": 3799.7392578125,
        "y2": 1278.468505859375,
        "confidence": 0.46236249804496765,
        "class": "Single crack",
        "color": [
            30,
            144,
            255
        ]
    },
    {
        "x1": 3.3751957416534424,
        "y1": 1419.775634765625,
        "x2": 899.6278686523438,
        "y2": 1838.350830078125,
        "confidence": 0.35102155804634094,
        "class": "Single crack",
        "color": [
            30,
            144,
            255
        ]
    }

]

for i, box in enumerate(label):
    print(f"box {i}: {box}")
    x1, y1, x2, y2, cls_name, color = int(box["x1"]), int(box["y1"]),int(box["x2"]),int(box["y2"]), box["class"], box["color"]
    image = cv2.rectangle(image, (x1, y1), (x2,y2), color, thickness=10)

image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
plt.imshow(image)
plt.show()
