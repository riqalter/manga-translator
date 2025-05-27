from ultralytics import YOLO
import torch 
import cv2
import os

def detect_objects(model_name, camera_index):
    print(f"Loading model {model_name}...")

    try:
        device = 'cuda' if torch.cuda.is_available() else 'cpu'
        print(f"Using device: {device}")
        model = YOLO(model_name).to(device)
        print("Model Class:", model.names)
    except Exception as e:
        print(f"Error loading model {model_name}: {e}")
        return
    
    print("using camera index:", camera_index)
    cap = cv2.VideoCapture(camera_index)

    if not cap.isOpened():
        print(f"Error: Could not open camera with index {camera_index}")
        return
    
    print("Camera opened successfully.")
    print("press 'q' to quit")

    try:
        while True:
            ret, frame = cap.read()
            if not ret:
                print("error: Could not read frame from camera")
                break

            results = model.predict(frame, device=device, verbose=False)

            anotated_frame = results[0].plot()

            cv2.imshow("Object Detection", anotated_frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                print("Quitting...")
                break
    except Exception as e:
        print(f"An error occurred during detection: {e}")
    finally:
        cap.release()
        cv2.destroyAllWindows()
        print("Camera released and windows closed.")

if __name__ == "__main__":
    model_name = os.path.join("runs/detect/train/weights/", "best.pt")
    camera_index = 0  # Change this to your camera index if needed
    detect_objects(model_name, camera_index)
