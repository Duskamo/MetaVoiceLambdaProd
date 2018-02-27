def generate_code(json):
    if(json["template"] == "Alexa Interaction"):
        with open('static/codeTemplates/simple-interaction.txt', 'r') as myfile:
            data=myfile.read();
            data = data.replace("UTTERANCE", json["intents"][0]["utterances"]["1"])
            data = data.replace("SKILLNAME", json["skillName"])
            newCode = open(json["skillName"] + "-code.txt","w")
            newCode.write(data)

            for intent in json["intents"]:
                newCode.write("    elif event['request']['intent']['name'] == '" + intent["intent"] + "':\n")
                newCode.write("        return create_response('" + intent["response"] + "', True)\n")
                newCode.write("\n")



            newCode.close()
            return json["skillName"] + "-code.txt"
