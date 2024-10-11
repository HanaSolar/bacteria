import cv2

# Load the animated GIF
gif_file = "bacteria_right.gif"
cap = cv2.VideoCapture(gif_file)

# Get total number of frames
total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Read the image with contours drawn on it
# image_with_contours = cv2.imread('bacteria_right.jpg')
# gray_image = cv2.cvtColor(image_with_contours, cv2.COLOR_BGR2GRAY)

bacteria_count = 0
# Find contours


# Iterate through oval contours

def estimate_bacteria_count(contours):
    for oval_contour in contours:
        bacteria_count = 0
        # Calculate the bounding box of the oval contour
        x, y, w, h = cv2.boundingRect(oval_contour)
        
        # Iterate through all contours again to find inner contours (bacteria) within the oval contour
        for contour in contours:
            # Ignore the same contour and any contour outside the bounding box of the oval
             if contour is oval_contour or not (x <= contour[:, 0].min(axis=0)[0] and y <= contour[:, 0].min(axis=0)[1] and
                                                x + w >= contour[:, 0].max(axis=0)[0] and
                                                y + h >= contour[:, 0].max(axis=0)[1]):
                continue

        bacteria_count += 1
    return bacteria_count
        
# Output file name
output_file = "bacteria_counts.txt"

# Open the output file for writing
with open(output_file, "w") as f:
    # Process each frame
    for frame_no in range(total_frames):
        # Read the frame
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale for processing
        # gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Estimate bacteria count in the frame
        bacteria_count = estimate_bacteria_count(frame)
        
        # Write the count to the output file
        f.write(str(bacteria_count) + "\n")
        
        # Print the count for confirmation
        print("Frame {}: Bacteria count = {}".format(frame_no, bacteria_count))

# Release the capture
cap.release()


