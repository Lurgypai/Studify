#!/bin/bash

rm -r outputs
mkdir -p outputs/palettes

for palette in palettes/*; do
    echo "Testing palette ${palette}"
    ./studify.py test_img.png ${palette}
    mv output.png outputs/${palette}
    echo ""
done
