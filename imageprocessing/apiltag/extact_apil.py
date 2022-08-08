import apriltag
import argparse
import cv2


# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True,
#     help="path to input image containing AprilTag")
# args = vars(ap.parse_args())
# print("[INFO] loading image...")


# image = cv2.imread(args["image"])
img_path = '/home/levin/workspace/tools/apriltag/images/mapping_feb_2014/IMG_1371.JPG'
# img_path = '/home/levin/workspace/tools/apriltag/images/hallway/IMG_0612.jpg'
# img_path = '/home/levin/workspace/tools/apriltag/images/mapping_feb_2014/1.png'
image = cv2.imread(img_path)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

print("[INFO] detecting AprilTags...")
options = apriltag.DetectorOptions(families="tag36h11", debug=True)
detector = apriltag.Detector(options)
results = detector.detect(gray)
print("[INFO] {} total AprilTags detected".format(len(results)))


for r in results:
    # extract the bounding box (x, y)-coordinates for the AprilTag
    # and convert each of the (x, y)-coordinate pairs to integers
    (ptA, ptB, ptC, ptD) = r.corners
    ptB = (int(ptB[0]), int(ptB[1]))
    ptC = (int(ptC[0]), int(ptC[1]))
    ptD = (int(ptD[0]), int(ptD[1]))
    ptA = (int(ptA[0]), int(ptA[1]))

    # draw the bounding box of the AprilTag detection
    cv2.line(image, ptA, ptB, (0, 255, 0), 2)
    cv2.line(image, ptB, ptC, (0, 255, 0), 2)
    cv2.line(image, ptC, ptD, (0, 255, 0), 2)
    cv2.line(image, ptD, ptA, (0, 255, 0), 2)

    # draw the center (x, y)-coordinates of the AprilTag
    (cX, cY) = (int(r.center[0]), int(r.center[1]))
    cv2.circle(image, (cX, cY), 5, (0, 0, 255), -1)

    # draw the tag family on the image
    tagFamily = r.tag_family.decode("utf-8")
    cv2.putText(image, tagFamily, (ptA[0], ptA[1] - 15),
        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    print("[INFO] tag family: {}".format(tagFamily))
    
cv2.imshow("Image", image)
cv2.waitKey(0)