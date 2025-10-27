def main():
    print("Hello from star-struck!")
    
def first_pattern():
    for i in range(5):
        print(5*'*')

def second_pattern():
    for i in range(5):
        print((i+1)*'*')
        
def third_pattern():
    for i in range(5):
        print("".join(str(x+1) for x in list(range(i+1))))

def fourth_pattern():
    for i in range(5):
        print(f'{i+1}'*(i+1))
    


if __name__ == "__main__":
    main()
    fourth_pattern()

