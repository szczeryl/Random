# snorlax_bitmap.py
WIDTH = 320
HEIGHT = 240

def make_snorlax_face():
    import numpy as np
    bmp = np.zeros((HEIGHT, WIDTH), dtype=np.uint8)
    
    # Example: simple ellipse for face
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # Normalize coordinates to center
            cx, cy = WIDTH//2, HEIGHT//2
            dx = (x - cx) / (WIDTH//2)
            dy = (y - cy) / (HEIGHT//2)
            if dx*dx + dy*dy <= 1.0:  # ellipse boundary
                bmp[y,x] = 1  # black pixel
    return bmp

def to_bytes(bmp):
    WIDTH_BYTES = WIDTH // 8
    vector = []
    for row in bmp:
        for i in range(WIDTH_BYTES):
            byte = 0
            for bit in range(8):
                byte <<= 1
                byte |= row[i*8 + bit]
            vector.append(f"{byte:02X}")
    return vector

bmp = make_snorlax_face()
vec = to_bytes(bmp)
# Write to COE file
with open("snorlax.coe","w") as f:
    f.write("memory_initialization_radix=16;\n")
    f.write("memory_initialization_vector=\n")
    for i in range(0,len(vec),16):
        f.write(",".join(vec[i:i+16]) + ",\n")
