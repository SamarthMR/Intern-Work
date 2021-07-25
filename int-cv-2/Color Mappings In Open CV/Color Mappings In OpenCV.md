# Color Spaces in OpenCV

![cover](https://github.com/sreelakshmig009/Intern-Work/blob/color_spaces/int-cv-2/Color%20Mappings%20In%20Open%20CV/Images/Cover.jpeg)


* <b>Color spaces</b> are a way to represent the color channels present in the image that gives the image that particular hue. 
 
* There are several different color spaces and each has its own significance.

* Some of the popular color spaces are RGB (Red, Green, Blue), CMYK (Cyan, Magenta, Yellow, Black), HSV (Hue, Saturation, Value), etc.

### BGR color space:

* RGB is OpenCV's default colour space.

* It does, however, store colour in the BGR format.\

* It's an additive colour model in which the various intensities of Blue, Green, and Red produce various hues of colour.

<img src = "https://github.com/sreelakshmig009/Intern-Work/blob/color_spaces/int-cv-2/Color%20Mappings%20In%20Open%20CV/Images/bgr.png" width="200" height="200">

### HSV color space(for hue, saturation, value):

* It uses a cylindrical representation of RGB colour points to store colour information.

* It tries to capture the colours as seen by the human eye.

* The hue ranges from 0-179, while the saturation ranges from 0-255 and the value ranges from 0-255

*  It's primarily used for colour segmentation.

<img src = "https://github.com/sreelakshmig009/Intern-Work/blob/color_spaces/int-cv-2/Color%20Mappings%20In%20Open%20CV/Images/hsv.jpg" width="200" height="200">

### HSL color space (for hue, saturation, lightness):

* The lightness dimension resembles the shifting amounts of black or white paint in the mixing in the HSL representation, which simulates how different colours mix together to create colour in the real world

* E.g. to create "light red", a red pigment can be mixed with white paint; this white paint corresponds to a high "lightness" value in the HSL representation

* At a lightness value of 12, fully saturated colours are put around a circle, with a lightness value of 0 or 1 corresponding to entirely black or white, respectively.

<img src = "https://github.com/sreelakshmig009/Intern-Work/blob/color_spaces/int-cv-2/Color%20Mappings%20In%20Open%20CV/Images/hsl.png" width="200" height="200">

### CMYK color space: 

* It is a subtractive colour space, unlike RGB.

* The CMYK model masks colours on a lighter, usually white, backdrop partially or completely. 

* Light that might normally be reflected is reduced by the ink.

* Because inks “subtract” the hues red, green, and blue from white light, this paradigm is called subtractive.

* White light with red leaves turned cyan, green leaves turned magenta, and blue foliage turned yellow.

<img src = "https://github.com/sreelakshmig009/Intern-Work/blob/color_spaces/int-cv-2/Color%20Mappings%20In%20Open%20CV/Images/cmyk.png" width="200" height="200">
