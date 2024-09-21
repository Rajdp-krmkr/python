import random
import math

try:
    type = int(input("What do you want?\n1)Encode (type 1)\n2)Decode (type 2)\n"));
    # print(random.random());
    # type = 1;
    if(type == 1):
        message = input("Enter the message you want to encode:\n");
        letter = "";
        arr = [];
        
        for x in message:
            if(x == " "):
                arr.append(letter);
                letter = "";
            else:
                letter += x;
        arr.append(letter);
        
        encodedArr = [];
        encodedMessage = ""
        newWord = ""
        
        for word in arr:
            if(len(word) < 3):
                for i in range(len(word)):
                    newWord += word[len(word)-i-1];
                encodedArr.append(newWord);
                newWord = ""
            else:
                num1 = math.floor(33 + random.random()*94);   #ASCII values of printable characters
                num2 = math.floor(33 + random.random()*94);
                num3 = math.floor(33 + random.random()*94);
                # print("num3 :",num3,chr(num3));
                newWord += f"{chr(num1)}{chr(num2)}{chr(num3)}"
                
                print(newWord);
                
                for i in range(1,len(word)):
                    newWord += word[i];                     #placing the first letter of the word at the end of the word
                newWord += word[0];
                
                print(newWord);
                
                num1 = math.floor(33 + random.random()*94);
                num2 = math.floor(33 + random.random()*94);
                num3 = math.floor(33 + random.random()*94);
                # print("num6 :",num3,chr(num3));
                newWord += f"{chr(num1)}{chr(num2)}{chr(num3)}"
                
                print(newWord);
                encodedArr.append(newWord);
                newWord = "";

        encodedMessage = ' '.join(encodedArr);
        encodedMessage = encodedMessage[0: len(encodedMessage)];
        print("Encoded message:\n", encodedMessage);
        
    elif(type == 2):
        message = input("Enter the message you want to decode:\n");
        arr= []
        letter = "";

        for x in message:
            if(x == " "):
                arr.append(letter);
                letter = "";
            else:
                letter += x;
        arr.append(letter);
        print(arr);
        
        decodedArr = [];
        decodedMessage = ""
        newWord =""
        
        for word in arr:
            if(len(word) < 3):
                for i in range(len(word)):
                    newWord += word[len(word)-i-1];
                    print(newWord);
                decodedArr.append(newWord);
            else:
                w = ""
                w = word[3:len(word)-3];

                w = w[len(w)-1 : len(w)] + w[0:len(w)-1];
                print(w);
                decodedArr.append(w);
        print("Decoded message:\n", ' '.join(decodedArr));     
            
except:
    print("Invalid input. Please try again.")
    exit();
