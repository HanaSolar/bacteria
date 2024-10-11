import cv2

# Load the GIF file (the file should be in the same directory as this script). This file is already in grayscale with contours drawn on it.
g_file = "bacteria_right.gif"
cap = cv2.VideoCapture(g_file)

# Get total number of frames
no_of_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

# Total number of frames
print("Total number of frames:", no_of_frames)

# A Function to get bacteria counts in a frame
def get_bacteria_counts(frame):
    # An algorithm to count bacteria in the frame
    
    print (frame.shape)

    if frame is None:
        print("Error: Unable to load the image.")
        exit()

    # Convert the image to grayscale
    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    # Apply thresholding to binarize the image
    #_, binary = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
 
    # Find contours in the thresholded image
    contours, _ = cv2.findContours(frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    # Count the number of contours (assumed to be bacteria)
    # print("Number of contours:", contours)
    count = len(contours)

    print("Number of bacteria detected:", count)

    return count
    

# Output file name
out_file = "counts.txt"

# Open the output file for writing
with open(out_file, "w") as f:
    # Process each frame
    for frame_no in range(no_of_frames):
        # Read the frame
        ret, frame = cap.read()
        if not ret:
            break
        
        # Convert frame to grayscale for processing
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        
        # Estimate bacteria count in the frame
        bacteria_count = get_bacteria_counts(gray_frame)
        
        # Write the count to the output file
        f.write(str(bacteria_count) + "\n")
        
        # Print the count for confirmation
        print("Frame {}: Bacteria count = {}".format(frame_no, bacteria_count))

# Release the capture
cap.release()