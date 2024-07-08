from PIL import Image

'''
    The image must be the same size, same number of bands (channel)
    The right color format (RGBA)
'''
img1 = Image.open( "Prototype/images/testStar.png", 'r' ).convert( "RGBA" )
img2 = Image.open( "Prototype/images/surprised_Emjoi.png", 'r' ).convert( "RGBA" )

#img1 = img1.resize( (512, 512) )
img2 = img2.transpose( Image.Transpose.FLIP_TOP_BOTTOM )

intermediate = Image.alpha_composite( img2, img1 )

intermediate.save( "somewhere.png" )
