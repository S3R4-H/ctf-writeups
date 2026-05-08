def extract_trunk():
    # From exiftool output
    key = b"6899efc8f52bffb08c5ac45deee24f64"
    offset = 0x10008581
    video_path = "../items/bembembem.mp4"
    output_zip = "trunk.zip"

    try:
        with open(video_path, "rb") as f:
            f.seek(offset)
            encrypted_data = f.read()

        # XOR logic: beast wears the key on its forehead
        decrypted_data = bytearray()
        for i in range(len(encrypted_data)):
            decrypted_data.append(encrypted_data[i] ^ key[i % len(key)])

        with open(output_zip, "wb") as f:
            f.write(decrypted_data)
        
        print(f"Success! '{output_zip}' created.")
        print("Now use the 8-character password from the spectrogram (42:00) to open it.")

    except FileNotFoundError:
        print("Error: bembembem.mp4 not found in this folder.")

extract_trunk()
