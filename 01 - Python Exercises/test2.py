import pyautogui
import time
import win32clipboard

# Click on the browser
# Open Developers Tool
waitTime:float = 1

pyautogui.moveTo( 178, 369, 0.25 )  
time.sleep( waitTime )
pyautogui.click( )
time.sleep( waitTime )
pyautogui.press( 'f12' )
time.sleep( waitTime )


# Start looking for HTML
pyautogui.moveTo( 1167, 175, 0.25 ) 
time.sleep( waitTime ) 
pyautogui.click( )
time.sleep( waitTime ) 
pyautogui.hotkey('ctrl', 'c')
time.sleep( waitTime ) 


# Search for Results Job Div
fileName:str = "test.html"
win32clipboard.OpenClipboard()

with open( fileName, 'w', encoding='utf-8' ) as myFile:
    myFile.write( win32clipboard.GetClipboardData( ) )

win32clipboard.CloseClipboard()

pyautogui.press( 'f12' )
print( f"End of Copying HTML to {fileName}.... " )