# task_2.py
# This script demonstrates list slicing to extract and reverse elements.

def demonstrate_slicing():
    """
    Creates a list of numbers, extracts the first five,
    reverses them, and prints the results.
    """
    # 1. Create a list of numbers from 1 to 10.
    original_list = list(range(1, 11))
    print(f"Original list: {original_list}")

    # 2. Extract the first five elements using slicing.
    # The slice [0:5] or simply [:5] gets elements from index 0 up to (but not including) 5.
    extracted_elements = original_list[:5]
    print(f"Extracted first five elements: {extracted_elements}")

    # 3. Reverse the extracted elements.
    # The slice [::-1] creates a reversed copy of the list.
    reversed_elements = extracted_elements[::-1]
    print(f"Reversed extracted elements: {reversed_elements}")

# Main execution block
if __name__ == "__main__":
    demonstrate_slicing()
