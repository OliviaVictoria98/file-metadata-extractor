import exifread

def extract_metadata(image_path):
    try:
        with open(image_path, 'rb') as img_file:
            tags = exifread.process_file(img_file, details=False)
            if not tags:
                print("No metadata found.")
            else:
                print(f"\nMetadata for {image_path}:\n")
                for tag in tags:
                    print(f"{tag:30}: {tags[tag]}")
    except FileNotFoundError:
        print("Error: File not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    path = input("Enter the path to the image file: ")
    extract_metadata(path)
