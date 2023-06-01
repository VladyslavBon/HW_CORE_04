def main():

    def input_error(func):
        def inner(string):
            try:
                func(string)
            except IndexError:
                print("Give me name and phone please")
            except (KeyError, ValueError):
                print("Enter user name")
        return inner
    
    @input_error
    def handler_add(string):
        parser = string.split(" ")
        dictionary.update({parser[1].capitalize(): parser[2]})

    @input_error
    def handler_change(string):
        parser = string.split(" ")
        dictionary.update({parser[1].capitalize(): parser[2]})
    
    @input_error
    def handler_phone(string):
        parser = string.split(" ")
        print(dictionary[parser[1].capitalize()]) 

    dictionary = {}
    while True:
        string = input().lower()
        if string in ["good bye", "close", "exit"]:
            print("Good bye!")
            break
        elif string == "hello":
            print("How can I help you?")
        elif string == "show all":
            for k, v in dictionary.items():
                print(k, v)
        elif string.startswith("add"):
            handler_add(string)
        elif string.startswith("change"):
            handler_change(string)
        elif string.startswith("phone"):
            handler_phone(string)
    
if __name__ == "__main__":
    main()