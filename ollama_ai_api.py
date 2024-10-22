from langchain_core.prompts import ChatPromptTemplate
from langchain_ollama.llms import OllamaLLM



model = OllamaLLM(model="llama3.1")



def ask_ollama(question, prevous_question):
    context_str = prevous_question
    template = """Use the previous conversation to answer the question at the end. If the previous question is not relevant ignore the prevoious question (context) and answer the new auestion like the context is an empty string. If you don't know the answer, just say that you don't know, don't try to make up an answer.\n\n{context}\n\nQuestion: {question}\nHelpful Answer:"""

    prompt = ChatPromptTemplate.from_template(template)

    chain = prompt | model

    return  chain.invoke({"question": question, "context": context_str})


