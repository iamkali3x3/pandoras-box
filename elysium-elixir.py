def pandorasBox(hephaestus, prometheus):
    repeated_prometheus = (prometheus * ((len(hephaestus) // len(prometheus)) + 1))[:len(hephaestus)]
    elysium = ''.join(
        '1' if bit != key_bit else '0'
        for bit, key_bit in zip(hephaestus, repeated_prometheus)
    )
    return elysium
if __name__ == "__main__":
    cerberus = input("Whisper the encrypted secrets of the Underworld: ").replace(" ", "")
    pandora = "01001000 01101001 01100101 01110011 01110100"
    olympus = pandorasBox(cerberus, pandora.replace(" ", ""))
    print(f"Decrypted binary: {olympus}")
