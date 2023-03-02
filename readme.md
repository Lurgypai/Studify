# Studify

This is a script to convert an image into a Lego stud mural. It was written to be run on linux, but could easily be run on any other platform that supports python.

### Execution
Usage:
`
studify <image> <palette>
`

Example usage:
`
./studify test_image.png palettes/warm.png
`

### Output
Studify will output the pieces required to the console (named according to their bricklink names), as well as a PNG converted to match the colors used, named `output.png`.

### Palettes
A selection of palettes are included. You can easily create your own palettes by copying and modifying the 'basic' pallete, (and you can mix in the shiny or trans color palettes as well). However, due to a bug in how PIL converts images to palettes, the palettes must be saved as *indexed* PNG's, with only the palette colors included in the color index.

### Tips
For best results, use images with relatively high contrast and saturation. A more spread out color space in the image helps the script to map more colors to the output image.

