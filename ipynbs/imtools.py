def imresize(im, size):
    """
    Resize an image array using PIL.
    
    im: An image object.
    size: A tuple of the target size.
    """
    
    pil_im = Image.fromarray(uint8(im))
    return array(pil_im.resize(size))

def histeq(im, nbr_bins = 256):
    """Histogram equalization of a grayscale image."""
    
    imhist, bins = histogram(im.flatten(), nbr_bins, density = True)
    cdf = imhist.cumsum()
    
    cdf = 255 * cdf / cdf[-1]
    
    im2 = interp(im.flatten(), bins[:-1], cdf)
    return im2.reshape(im.shape), cdf