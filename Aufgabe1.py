import os

def save_ppm(frame):
    output_path = os.path.join(os.path.dirname(__file__), "output")
    output_file = os.path.join(output_path, "image_{:03d}.ppm".format(frame)) # for each frame -> animation
    os.makedirs(output_path, exist_ok=True)
    with open(output_file, "w") as ppm_file:


        # header
        width = 256
        height = 256
        header = "P3\n{w} {h}\n255\n".format(w=width, h=height)
        ppm_file.write(header)

        for y in range(height):
            for x in range(width):
                # offset color with time and wrap around color range
                red = (x + frame) % 256
                green = (y + frame) % 256
                value = "{r} {g} {b} ".format(r=red, g=green, b=0)
                ppm_file.write(value)
            ppm_file.write("\n") 

        ppm_file.close() 

start = 0
end = 256
#animation
for t in range(start, end):
    print("Frame:", t)
    save_ppm(t)