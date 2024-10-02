import random
import math

try:
    type = int(input("What do you want?\n1)Encode (type 1)\n2)Decode (type 2)\n"));
    # type = 2;
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
        print(arr);
        
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
                num1 = math.floor(random.random()*100);
                num2 = math.floor(random.random()*100);
                num3 = math.floor(random.random()*100);
                newWord += f"{chr(num1)}{chr(num2)}{chr(num3)}"
                for i in range(1,len(word)):
                    newWord += word[i];
                newWord += word[0];
                num1 = math.floor(random.random()*100);
                num2 = math.floor(random.random()*100);
                num3 = math.floor(random.random()*100);
                newWord += f"{chr(num1)}{chr(num2)}{chr(num3)}"
                print(newWord);
                encodedArr.append(newWord);
                newWord = "";
        # for word in encodedArr:
        #     encodedMessage += 
        encodedMessage = ' '.join(encodedArr);
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
        newWord = ""
        
        for word in arr:
            if(len(word) < 3):
                for i in range(len(word)):
                    newWord += word[len(word)-i-1];
                decodedArr.append(newWord);
                newWord = ""
            else:
                w = ""
                # for i in range(len(word)):
                    # w = word.translate({ord(word[i]): None})
                w = word[3:len(word)-3];
                w = w[len(w)-1] + w[0:len(w)-1];
                    # print(i);
                    # print(f"{word[i]}");
                decodedArr.append(w);
            
    #             word += word[i];
        #         newWord += word[0];
                
                
        #         newWord += f"{chr(num1)}{chr(num2)}{chr(num3)}"
        #         print(newWord);
        #         encodedArr.append(newWord);
        #         newWord = "";
        # # for word in encodedArr:
        # #     encodedMessage += 
        # encodedMessage = ' '.join(encodedArr);
        # print("Encoded message:\n", encodedMessage);
        
except:
    print("Invalid input. Please try again.")
    exit();
