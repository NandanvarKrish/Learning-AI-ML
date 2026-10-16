# TASK-1:- OUTPUT PREDICTOR

model_name   = "GPT-4"
version      = 4
accuracy     = 0.973
is_deployed  = True

print(model_name)
print(type(version))
print("Accuracy: " + str(accuracy))
print(is_deployed)
# print("Version: " + version) # Error bcoz version is int
print("Version: " + str(version)) #Converted ine to string
