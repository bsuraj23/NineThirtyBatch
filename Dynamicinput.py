def read_input_line():
    line=input("Enter values separated by space:")
    elements=line.split()
    parsedline=[]
    for item in elements:
        if item=="True":
            parsedline.append(True)
        elif item=="False":
            parsedline.append(False)
        else:
            try:
                parsedline.append(int(item))
            except:
                try:
                    parsedline.append(float(item))
                except:
                    parsedline.append(item)
    return parsedline
parsed_list=read_input_line()
print(parsed_list)