# Custom QR Maker
Simple script and interface for creating QR codes

I used the qrcode library to generate codes to prevent the need for using a 3rd party service to create them on the fly.

Basic script just asks for string to QR-ify and output filename (will save to cwd).

Interface version uses PySimpleGui to generate a user-friendly interface that also asks where you'd like to save the output. That file is the basis for the .exe version (generated with auto-py-to-exe) that I can easily distribute to colleagues that may not be running Python.

I'd like to get around to adding support for customization options, but right now it just generates QR codes using the qrcode library default.
