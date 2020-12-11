import numpy as np

#Initializing some weight vector, Randomly !!
w = np.array([-0.1, -0.2, 0.1])

for epoch in range(1,51):
    
    print("\n\n\n\n\nThis is epoch number:" , epoch)

    print("This is the weight vector::",w)
    
    # Initializing Input Matrix
    x = np.array([[1,0,0],[1,0,1],[1,1,0],[1,1,1]])
    
    # Initializing True outputs / Expected outputs matrix
    y = np.array([0,1,1,1])       
    print("The length of the input matrix is :",len(x))
    Error = 0
    for i in range(0,len(x)):
      print("This is step/pattern no.", i+1)
      print("Initial Error :", Error)
      print("Current Weight vector :",w)
      print("Current sample/pattern:",x[i])
      dp = np.dot(w,x[i])
      print("This is dp :",dp)
      if dp >= 0:
         predicted_output = 1
      else:
         predicted_output = 0
      print("Predicted output", predicted_output)
      if (predicted_output == 0 and y[i] == 1) :
        w = w + x[i]
       
      if predicted_output == 1 and y[i] == 0 :
        w = w - x[i]
      Error = Error + 0.5*((predicted_output - y[i]) ** 2)
      print("Calculated Error for current step : ", Error)

    if Error == 0:
        break
    
    print("Error : ", Error)
print("Final Adjusted Weight vector:",w)
print("Perceptron Learning Completes here ....")

