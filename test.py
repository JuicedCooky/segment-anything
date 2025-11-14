from segment_anything import SamPredictor, sam_model_registry
import cv2
import sys

selected_box = None
selected_point = None
mode = None

def mouse_callback(event, x, y, flags, param):
    global mode, selected_box, selected_point

    if mode == "point":
        if event == cv2.EVENT_LBUTTONDOWN:
            selected_point = (x,y)


if __name__ == "__test__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--image-path", type=str)
    parser.add_argument("--output-path", type=str)

    args = parser.parse_args()

    #
    image = cv2.imread(args.image_path)
    cv2.namedWindow("Image")
    cv2.setMouseCallback("Image", mouse_callback)

    while True:
        display = image.copy()

        if selected_point:
            cv2.circle(display, selected_point, 5, (0,0,255), -1)

        cv2.imshow("Image", display)
        key = cv2.waitKey(1)    

        if key == ord('p'):
            mode =  "point"
        if key == ord('b'):
            mode = "box"
        if key == 27:
            break

    cv2.destroyAllWindows()


# sam = sam_model_registry["default"](checkpoint="sam_vit_h_4b8939.pth")
# predictor = SamPredictor(sam)
# predictor.set_image("./assets/oct-29-2004.png")
# masks, _, _ = predictor.predict(<input_prompts>)