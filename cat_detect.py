import cv2

# Load the pre-trained Haar Cascade Classifiers for cat face and smile detection
cat_face_cascade = cv2.CascadeClassifier('model\haarcascade_frontalcatface_extended.xml')  # Use custom path for cat face cascade
smile_cascade = cv2.CascadeClassifier('model\\haarcascade_smile.xml')  # Use custom path for smile cascade

# Start video capture from the webcam
cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the webcam
    ret, frame = cap.read()

    # Convert the frame to grayscale (Haar cascades work on grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect cat faces in the image
    cat_faces = cat_face_cascade.detectMultiScale(gray, 1.3, 5)

    # Loop through all cat faces detected
    for (x, y, w, h) in cat_faces:
        # Draw rectangle around the cat face
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

        # Region of interest for detecting smiles (mouth area)
        roi_gray = gray[y:y + h, x:x + w]
        roi_color = frame[y:y + h, x:x + w]

        # Detect smiles in the cat face region
        smiles = smile_cascade.detectMultiScale(roi_gray, 1.8, 20)

        # Loop through all smiles detected
        for (sx, sy, sw, sh) in smiles:
            # Draw rectangle around the smile
            cv2.rectangle(roi_color, (sx, sy), (sx + sw, sy + sh), (0, 255, 0), 2)

    # Display the resulting frame
    cv2.imshow('Cat Face and Smile Detection', frame)

    # Break the loop when the user presses 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the webcam and close the window
cap.release()
cv2.destroyAllWindows()
