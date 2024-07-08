from bs4 import BeautifulSoup
from typing import List

# ================================================
#  Function
# ================================================
def writeWebPageToFile( link:str ) -> str:
    import requests

    with open( 'website.html', 'w' ) as myFile:
        content = requests.get( link ).text
        myFile.write( content )

    return 'Done...'

def cleanHREF( link:List ) -> str:
    copy = link.copy( )
    if copy[0] == '/':
        del copy[0]

    return ''.join( copy )


def isFullyQualifyLink( link:str ) -> bool:
    if link_attrs['href'].startswith( ('https://', 'http://') ):
        return True
    else:
        return False

# ================================================
#  Main
# ================================================
link = "https://www.blueletterbible.org/"            # Main Page scrapping
# print( writeWebPageToFile( link ) )

with open( 'website.html', 'r' ) as myFile:
    content = myFile.read( )
    soup    = BeautifulSoup( content, 'lxml' )

    singleLink = soup.find( "a" )
    all_links = soup.find_all( "a" )
    print( f"There are {len( all_links )} anchor tags" )


# ======================================
#  Parse All Link and store them in CSV
# ======================================
print( "\n\n")
linkData:dict = {}

for i, anchorTag in enumerate( all_links ):
    link_attrs = anchorTag.attrs
    imgTag     = anchorTag.find( 'img' )
    valueName  = ""
    hrefLink   = ""

    # ==========================================
    #  Parse Name
    # ==========================================
    if str(imgTag) != "None":       # Dealing with Images
        valueName = imgTag['alt']
    else:                           # Dealing with Anchor
        valueName = ' '.join( anchorTag.text.split( ) )


    # ==========================================
    #  Clean Up Links
    # ==========================================
    if 'href' in link_attrs.keys( ):
        if isFullyQualifyLink( link_attrs['href'] ):
            hrefLink = f"{link_attrs['href']}"
        else:
            cleanLink = link + cleanHREF( list( link_attrs['href'] ) )
            hrefLink = f"{cleanLink}"

    # ==========================================
    #  Check if Link Exist before Storing
    # ==========================================
    if hrefLink != "":
        if valueName not in linkData.keys( ):
            linkData[valueName] = hrefLink

            
# ==========================================
#  Store it permanently 
# ==========================================
with open( "anchorList.csv", 'w', encoding='utf-8' ) as myFile:
    for key, value in linkData.items( ):
        myFile.write( f"\"{key}\", {value}\n" )
