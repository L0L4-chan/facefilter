import gradio as gr
import numpy as np
import mediapipe as mp
import cv2
import os

# FaceMesh initialization
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh(static_image_mode=True)

# Function to overlay glasses filter
def apply_filter(img, filter_name="black.png"):
    filter_path = os.path.join("filters", filter_name)

    if not os.path.exists(filter_path):
        return img

    filter_img = cv2.imread(filter_path, cv2.IMREAD_UNCHANGED)
    if filter_img is None:
        return img

    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = face_mesh.process(img_rgb)
    if not result.multi_face_landmarks:
        return img

    annotated = img.copy()

    for face_landmark in result.multi_face_landmarks:
        ih, iw, _ = img.shape

        left_eye = face_landmark.landmark[33]
        right_eye = face_landmark.landmark[263]

        x1 = int(left_eye.x * iw)
        x2 = int(right_eye.x * iw)
        y1 = int(left_eye.y * ih)
        y2 = int(right_eye.y * ih)

        cx = int((x1 + x2) / 2)
        cy = int((y1 + y2) / 2)

        eye_width = int(np.linalg.norm([x2 - x1, y2 - y1]) * 2)

        scale = eye_width / filter_img.shape[1]
        new_w = int(filter_img.shape[1] * scale)
        new_h = int(filter_img.shape[0] * scale)
        resized_filter = cv2.resize(filter_img, (new_w, new_h), interpolation=cv2.INTER_AREA)

        top_left_x = cx - new_w // 2
        top_left_y = cy - new_h // 2

        overlay_image(annotated, resized_filter, top_left_x, top_left_y)
        break

    return annotated

# Overlay helper
def overlay_image(background, overlay, x, y):
    h, w = overlay.shape[:2]
    if x < 0 or y < 0 or x + w > background.shape[1] or y + h > background.shape[0]:
        return

    b, g, r, a = cv2.split(overlay)
    overlay_rgb = cv2.merge((b, g, r))
    mask = a / 255.0

    roi = background[y:y + h, x:x + w]
    blended = (roi * (1 - mask[..., None]) + overlay_rgb * mask[..., None]).astype(np.uint8)
    background[y:y + h, x:x + w] = blended

# Image processing wrapper
def process_img(image, filter_name):
    if image is None:
        return None
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    result = apply_filter(image, filter_name)
    result = cv2.cvtColor(result, cv2.COLOR_BGR2RGB)
    return result

# Selector for source input
def dinamic_interface(option, img_upload, img_webcam, filter):
    if option == "Upload":
        return process_img(img_upload, filter)
    elif option == "WebCam":
        return process_img(img_webcam, filter)

# UI definition
def demo():
    with gr.Blocks() as app:
        gr.Markdown("# 👓 AI Glasses Filter")
        gr.Markdown("Using AI/VA technology to try on glasses virtually!")

        input_mode = gr.Dropdown(["Upload", "WebCam"], 
                                 label="Select input source", 
                                 value="Upload")

        img_upload = gr.Image(type="numpy", label="Upload image", visible=True)
        img_webcam = gr.Image(sources="webcam", type="numpy", label="WebCam capture", visible=False)

        gr.Markdown("## Choose your glasses model")

        with gr.Row():
            gr.Image(value="filters/black.png", label="Black", height=80, width=100, interactive=False)
            gr.Image(value="filters/carey.png", label="Carey", height=80, width=100, interactive=False)

        filter_selector = gr.Dropdown(
            ["black.png", "carey.png"],
            label="Select glasses model",
            value="black.png"
        )

        btn = gr.Button("Apply glasses")
        output = gr.Image(label="Result")

        # Toggle logic between upload/webcam
        def toggle_input_mode(source):
            return (
                gr.update(visible=(source == "Upload")),
                gr.update(visible=(source == "WebCam"))
            )

        input_mode.change(fn=toggle_input_mode, inputs=input_mode, outputs=[img_upload, img_webcam])

        btn.click(fn=dinamic_interface, 
                  inputs=[input_mode, img_upload, img_webcam, filter_selector],
                  outputs=output)

    return app

