import os
import openai

def gpt3_answer(item, fine_tuned_model, is_log=False):
    

  result = openai.Completion.create(model = fine_tuned_model, 
                                    max_tokens = 40,
                                    prompt=str(item), temperature = 0.4)['choices'][0]['text'] 
    
  if is_log: print('- ', item, ': ', result)
    
  return result


if __name__ == "__main__":

    os.environ["OPENAI_API_KEY"] = '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'
    openai.api_key = os.getenv('OPENAI_API_KEY')

    """
    with open("finetune_data_prepared.jsonl", encoding='utf-8') as f:

        file_id = openai.File.create(file = f, purpose = 'fine-tune')

    """

    #response = openai.FineTune.create(training_file = 'file-EO03qUxhhiXZalTXPE3OVd5w', model = 'babbage')
    #print(response)

    #response = openai.FineTune.retrieve(id = "ft-dztm8zdbNrTPv7IblMl5Ilks")
    #print(response)

    result = gpt3_answer(item = 'how is research at sastra?', fine_tuned_model = "babbage:ft-personal-2022-06-06-17-26-20")
    print(result)