from PIL import Image
import sys


def image_to_hex(filename):
    im = Image.open(filename)
    hex_image = [0] * (128 * 128)

    for block_row in range(8):
        for col in range(128):
            hex_image[col + block_row * 128] = 0
            for row in range(8):
                y = 7 - row
                rgb = im.getpixel((col, y + block_row * 8))

                if not rgb == (255, 255, 255):
                    hex_image[col + block_row * 128] |= (1 << y)

    return hex_image


def generate_intel_hex(image_hex, start_at):
    intel_hex_format = "%02X%04X00%s"
    results = []

    for hex_idx in range(0, 1024, 16):
        hex_data = "".join([("%02X" % h) for h in image_hex[hex_idx:hex_idx + 16]])
        intel_hex = intel_hex_format % (16, start_at + hex_idx, hex_data)
        crc = "%02X" % crc8(intel_hex)
        results.append(":" + intel_hex + crc)

    return results


def print_usage():
    print("Usage:")
    print("  python3 image_to_hex.py [FILENAME] [START POSITION(hex)]")


def crc8(hex_data):
    total = 0
    for idx in range(0, len(hex_data), 2):
        total += int(hex_data[idx:idx + 2], 16)

    checksum = (~total + 1) & 0x000000FF

    return checksum


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print_usage()
        sys.exit(1)

    image_filename = sys.argv[1]
    start_position = int(sys.argv[2], 16)

    image_hex = image_to_hex(image_filename)
    # for i in range(0, 1024, 16):
    #     print("".join([("%02x" % h) for h in image_hex[i:i + 16]]))

    intel_hex = generate_intel_hex(image_hex, start_position)
    print("\n".join(intel_hex))

    sys.exit(0)
