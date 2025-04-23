alfabet = "abcdefghijklmnopqrstuvwxyz"

while True:
    print("🄼🄾🄳🄴 🅂🄴🄻🄴🄲🅃🄸🄾🄽, 🄴🄽🅃🄴🅁 '🅀🅄🄸🅃' 🅃🄾 🄴🅇🄸🅃")
    mode = input("Mode (single or text)? ").lower()
    
    if mode == "single":
        print("🅂🄸🄽🄶🄻🄴 🄻🄴🅃🅃🄴🅁 🄼🄾🄳🄴, 🄴🄽🅃🄴🅁 '🅀🅄🄸🅃' 🅃🄾 🄴🅇🄸🅃")
        
        while True:
            letter = input("Number: ")
            if letter == "quit":
                break
            
            print(f"Decoded to {alfabet[int(letter) - 1]}")
            
    elif mode == "text":
        print("🅃🄴🅇🅃 🄼🄾🄳🄴, 🄴🄽🅃🄴🅁 '🅀🅄🄸🅃' 🅃🄾 🄴🅇🄸🅃")
        while True:
            text = input("Encoded text: ")
            if text == "quit":
                break
            
            returnArr = []
            returnText = ""
            textArr = text.replace(".", "").split(" ")
            for letter in textArr:
                returnArr.append(alfabet[int(letter) - 1])
                
            for letter in returnArr:
                returnText += letter
                
            print(f"Decoded text:\n{returnText}")
    elif mode == "quit":
        break
    else:
        print("Unknown type!")

print("Exiting...")
