from backend.connectwolf import WolfConnect

if __name__ == "__main__":
    user_query = input("\nQuery: ")

    ask = WolfConnect(
        appid="2HPKYW-33TYAJLGTY",
        query=user_query
    )

    print("\n"*2)
    # print(ask.short_query())
    # print(ask.spoken_query())
    print(ask.llm())
    print("\n"*2)
