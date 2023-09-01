# from llama_cpp import Llama
from langchain.llms import LlamaCpp
from langchain import PromptTemplate, LLMChain
from langchain.callbacks.manager import CallbackManager
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

def main():
# Make sure the model path is correct for your system!
    llm = LlamaCpp(model_path="/Users/vietqnguyen/Developer/llama.cpp/models/llama-2-13b-chat/ggml-model-q4_0.bin", verbose=False)
    question = input("\n\nQuestion:\n")
    question = "Q:%s?" % question
    conversation = question
    while question != "quit":
        output = llm(conversation + " A: ",temperature=0, max_tokens=4000, stop=["Q:"], echo=True)
        print("\nResponse:\n",output.strip())
        conversation = conversation + " A: " + output + " "
        question = input("\n\nQuestion:\n")
        question = "Q:%s?" % question
        conversation = conversation + question

if __name__ == "__main__":
    main()