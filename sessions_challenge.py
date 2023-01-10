import subprocess
import os

### GLOBAL VARIABLES ###
props_dict = {}




### FUNCTIONS ###
def init(props):
    global props_dict
    print("Python: starting challenge init()")

    # Save properties in the global variable
    props_dict = props
    
    # Execute the challenge once during the init, so key is calculated from the beginning
    executeChallenge()
    return 0




def executeChallenge():
    print("Python: starting executeChallenge()")

    text=os.popen('query user').read()
    #print(text)

    text=text[80:]
    
    sessions=text.split('\n')
    for i,session in enumerate(sessions):
        #print("Clave: "+str(i)+" value: "+session[:-28])
        sessions[i]=session[:-23]
    #Remove last
    sessions.pop()
    #print(sessions)
    key=""
    key='-'.join(sessions)
    # Get key as UTF-8 and calculate its length
    key = bytes(key, 'utf-8')
    key_size = len(key)

    # The result is a tuple (key, key_size)
    result = (key, key_size)
    #print("Python:", result)
   
    return result


if __name__ == "__main__":
    # Use a dictionary as example of properties obtained from the json
    props_example_dict = {"param1": "hola", "param2": 3}
    init(props_example_dict)
    executeChallenge()








