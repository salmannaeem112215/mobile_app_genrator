import os

def find_nonexistent_files(file_list):
    nonexistent_files = [file for file in file_list if not os.path.exists(file)]
    return nonexistent_files

# Example usage:
if __name__ == "__main__":
    list2 = [
"anon.png",
"casmart.png",
"footcap.png",
"loopstudio.png",
"nftc.png",
"ridex.png",
"shoppie.png",
"cart_page.png",
"bruce.png",
"devfolio.png",
"drew.png",
"ethan.png",
"jack.png",
"wren.png",
"desinic.png",
"digitalmedia.png",
"pixstock.png",
"techx.png",
"cook.png",
"crispy.png",
"grilli.png",
"filmlane.png",
"tvflix.png",
"cineflix.png",
"tourest.png",
"tourly.png",
"travelia.png",
"easybank.png",
"page_mac.png",
"educator.png",
"eduweb.png",
"unigine.png",
"gamics.png",
"homeverse.png",
"realvine.png",
"product_widget.png",
"transportio.png",
"admin_dashboard.png",
"wildvine.png",
"blogy.png",
"dairy.png",
    ]

    nonexistent_files_list2 = find_nonexistent_files(list2)

    print("Nonexistent files in List 2:", nonexistent_files_list2)
