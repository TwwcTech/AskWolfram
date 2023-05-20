from backend.connectwolf import WolfConnect

if __name__ == "__main__":
    user_query = input("Query: ")

    ask = WolfConnect(
        appid="2HPKYW-33TYAJLGTY",
        query=user_query
    )

    print("\n"*2, ask.short_query(), "\n"*2)
    print("\n"*2, ask.spoken_query(), "\n"*2)
