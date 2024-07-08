# tag = soup.title        # Grabs a Tag from the BeautifulSoup Structure
    # print( tag )            
    # print( tag.name )       # Tag has a name
    # print( tag.attrs )      # {}

    tag = soup.p
    tag.string = ' '.join( tag.string.split( ) )

    print( f"tag              | {tag}" )
    print( f"tag name         | {tag.name}" )               # Tag has a name
    print( f"tag attrs        | {tag.attrs}" )              # {}
    print( f"tag keys         | {tag.attrs.keys( )}" )      # dict_keys(['id', 'class'])
    print( f"tag id           | {tag['id']}" )
    print( f"tag class        | {tag['class']}" )           # []
    print( f"tag string       | {tag.string} | {type(tag.string)}" )
    print( f"tag text         | {tag.text} | {type(tag.text)}" )
    print( f"tag content      | {tag.contents} | {type(tag.contents)}" )

    print( )
    searchTag = "body"
    sampleTags = soup.find( searchTag ).children
    tagDict:dict = {}
    count = 1

    for x in sampleTags:
        if str( x.name ) != "None":
            if str( x.name ) in tagDict:
                tagDict[ str(x.name) ] += 1
            else:
                tagDict[ str(x.name) ] = 1
                
            # print( f">>{count} | {x.name}" )
            count += 1
    
    print( f"Search Tag:       {searchTag}" )
    print( f"Total Tags Found: {count}" )
    print( f"Total Tags Count: {tagDict}" )