from langchain_openai import ChatOpenAI


def main():
    llm = ChatOpenAI()
    message = llm.invoke("How can langsmith help with testing?")
    print(message)


if __name__ == '__main__':
    main()
