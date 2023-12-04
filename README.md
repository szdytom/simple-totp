# simple-totp

A simple script to calculate Time-based One-Time Password.

## Features

- **Standard TOPT**: Implements standard TOTP (RFC6238), tested against Google Authenticator.
- **Offline**: All data and secrets are saved and processed locally.
- **Zero-dependency**: Does not depend on other libraries except Python's standard library.
- **Lightweight**: Less than 100 LOC, nowhere to hide any backdoors.

## Installing

You only need to download the script file `totp.py` (you also need to make sure Python3 is installed on your computer).

## Usage

You need to save your TOTP key in a file in base32 format. If you are interacting with GitHub 2FA, you can click the "setup key" button to get that code. Otherwise, you may need to scan a certain QR code (provided by the website) and extract the secret key manually.

In most cases, the QR code will contain a URI similar to:

```plain
otpauth://totp/Passkou?secret=6shyg3uens2sh5slhey3dmh47skvgq5y&issuer=Test
```

You just need the part after `secret=`, in the above example, it is `6shyg3uens2sh5slhey3dmh47skvgq5y`, and save the string in a plain text file. (Note: usually, you may want to switch that file to permission 600).

After that, you can simply call the script by the following command.

```sh
./totp.py <path-to-your-secret-file>
```

## Contributing

I'd like to see contributions from the community. If you experience bugs, feel free to open an issue. There are a lot more features that can be added, for example,

- Configurable time step length (currently hardcoded number 30), hash algorithm (currently SHA-1 only), and code length (currently hardcoded 6) via command-line arguments.
- Recognise other secret formats such as binary, hex, or mnemonic phrases.
- A TUI or even a GUI interface.

If you have implemented any enhancement(not necessarily limited to the list above), please open a pull request.

## License

The content in this repository is licensed under the MIT License, with absolutely no warranty of any kind, see `LICENSE` for details.


