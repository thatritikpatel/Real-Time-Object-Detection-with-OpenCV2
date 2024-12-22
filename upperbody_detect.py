import cv2

def detect_upperbody_live():
    # Load the pre-trained Haar Cascade XML classifier for upper body
    upperbody_cascade = cv2.CascadeClassifier('model/haarcascade_upperbody.xml')

    # Open the webcam (0 is usually the default camera)
    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        # Read a frame from the webcam
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to capture frame.")
            break

        # Convert the frame to grayscale
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

        # Enhance contrast using histogram equalization
        gray = cv2.equalizeHist(gray)

        # Detect upper bodies in the frame with adjusted parameters
        upper_bodies = upperbody_cascade.detectMultiScale(
            gray, 
            scaleFactor=1.2,  # Slightly increase scale factor for reduced false positives
            minNeighbors=5,   # Increase minNeighbors to filter weak detections
            minSize=(50, 50), # Restrict detection to larger sizes
            maxSize=(300, 300) # Avoid detecting overly large objects
        )

        # Draw rectangles around detected upper bodies
        for (x, y, w, h) in upper_bodies:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Display the result
        cv2.imshow('Upper Body Detection', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release the webcam and close all windows
    cap.release()
    cv2.destroyAllWindows()

# Run live detection
detect_upperbody_live()
