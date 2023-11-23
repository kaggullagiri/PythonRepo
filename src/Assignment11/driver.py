from src.Assignment11.util import round_array

if __name__ == "__main__":
    input_array = input("Enter space-separated numbers: ").split()
    floor_result, ceil_result, rint_result = round_array(input_array)

    print("Floor:", floor_result)
    print("Ceil:", ceil_result)
    print("Rint:", rint_result)