source_path = "source.jpg"
binary_file = "img_binary.bin"
output_img = "retrived.jpg"

while True:
    print("1.store the image in binary\n2.Retrive the image\n3.exit")
    choice = int(input("Enter your choice :"))
    if choice == 1:
        try:
            with open(source_path,"rb")as img:
                data = img.read()
            with open(binary_file,"wb") as bin_file:
                bin_file.write(data)
            print("image successfully stored in binary file")
        except:
            print("error occured")
    elif choice == 2:
        try:
            with open(binary_file,"rb")as img:
                data = img.read()
            with open(output_img,"wb") as bin_file:
                bin_file.write(data)
            print("image retrived successfully ")
        except:
            print("error occured")
    elif choice == 3:
        print("Program terminated")
        break
    else:
        print("Invalid try again!!!")