import filters

def main():
    filename = input("Enter file name: ")

    im = filters.load_img(filename)


    filters.show_img(im)
    filters.save+img(im, "newfilename. jpg")


    if__name__== '__main__':
        main()
