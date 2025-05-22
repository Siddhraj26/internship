with open("C:\\Users\\SIDDHRAJSINH\\OneDrive\\Pictures\\siuu.jpg","rb") as f:
    data =f.read()
    with open("C:\\Users\\SIDDHRAJSINH\\OneDrive\\Pictures\\abc.jpg","wb") as f:
        f.write(data)