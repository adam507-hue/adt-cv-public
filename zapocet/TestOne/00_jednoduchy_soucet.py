
def add(a: int, b: int) -> int:
    """
    Adds two integers and returns their sum.
    """
    # Naimplementujte funkci tak, aby vracela součet 'a' a 'b'

    if(b>1):
        a = add(a, b-1)
    return(a+1)

def main():
    """
    Main function to demonstrate the add function.
    """
    result = add(15, 23)
    print(f"Součet 5 a 3 je: {result}")

if __name__ == "__main__":
    main()
