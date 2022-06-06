import os
import openai



if __name__ == "__main__":

    os.environ["OPENAI_API_KEY"] = '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'
    openai.api_key = os.getenv('OPENAI_API_KEY')

    #response = openai.FineTune.create(training_file = 'file-EO03qUxhhiXZalTXPE3OVd5w', model = 'babbage')
    #print(response)

    response = openai.FineTune.retrieve(id='file-EO03qUxhhiXZalTXPE3OVd5w')
    print(response)