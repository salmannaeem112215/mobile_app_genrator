import os

def get_image_filenames(directory):
   """
   Returns a list of image filenames with extensions from a given directory.

   Args:
       directory (str): The path to the directory containing the images.

   Returns:
       list: A list of image filenames with extensions.
   """

   image_filenames = []
   for filename in os.listdir(directory):
       if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.gif', '.bmp', '.tiff', '.webp')):
           image_filenames.append(filename)

   return image_filenames

# Example usage:
images_folder = "./"  # Replace with the actual path to your images folder
image_filenames = get_image_filenames(images_folder)
print(image_filenames)
