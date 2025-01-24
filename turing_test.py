def turing_machine_reverse(input_tape):  
    tape = list(input_tape)  # Convert input string to a list  
    head = 0                 # Start at position 0  
    state = "start"          # Initial state  

    while True:  
        if state == "start":  
            # Move head to the end of the input  
            if head >= len(tape):  
                # Add a separator '#' and switch to reverse state  
                tape.insert(head, '#')  
                state = "reverse"  
                head -= 1  # Move back to the last symbol  
            else:  
                head += 1  

        elif state == "reverse":  
            left = 0          # Left pointer starts at 0  
            right = head - 1  # Right pointer starts at last symbol before '#'  

            # Swap symbols until pointers meet  
            while left < right:  
                tape[left], tape[right] = tape[right], tape[left]  
                left += 1  
                right -= 1  

            state = "halt"    # Transition to halt state  

        elif state == "halt":  
            # Remove the '#' separator and return the result  
            return ''.join(tape).replace('#', '')  

# Test the Turing Machine  
input_str = "100000"  
output = turing_machine_reverse(input_str)  
print(f"Original: {input_str}\nReversed: {output}")  