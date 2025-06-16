def save_ppm(width, height, buffer): 
    # Create a path and file and open it for writing    
    output_path = os.path.join(os.path.dirname(__file__), "output")    
    output_file = os.path.join(output_path, "image.ppm")    
    os.makedirs(output_path, exist_ok=True)    
    with open(output_file, "w") as ppm_file:
        # Write the header    
        header = "P3\n{w} {h}\n255\n".format(w=width, h=height)    
        ppm_file.write(header)

        # Write the pixel data
        for i in range(0, len(buffer), 3):
            line = "{} {} {}\n".format(buffer[i], buffer[i+1], buffer[i+2])
            ppm_file.write(line)

def set_raster_coordinate(x, y, r, g, b, width, buffer):
    if 0 <= x < width and 0 <= y < height:
        offset = 3 * x + (width * 3) * y 
        if 0 <= offset + 2 < len(buffer):
            buffer[offset] = r 
            buffer[offset + 1] = g 
            buffer[offset + 2] = b

def perspective_divide(p, image_plane_distance): 
    return [        
        image_plane_distance * p[0] / p[2],        
        image_plane_distance * p[1] / p[2],        
        image_plane_distance,    
    ]      

def view_to_raster(v, width, height):  
    raster_X = ((v[0] + 1) / 2) * width  
    raster_Y = ((1 - v[1]) / 2) * height 
    return [round(raster_X), round(raster_Y)]
