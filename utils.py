def save_output(output_path, ir, optimized_ir, final_code):
    # Save the IR, optimized IR, and final generated code to a text file
    with open(output_path, "w") as f:
        f.write("Intermediate Representation:\n")
        f.write("\n".join(ir) + "\n\n")
        
        f.write("Optimized IR:\n")
        f.write("\n".join(optimized_ir) + "\n\n")
        
        f.write("Generated Code:\n")
        f.write(final_code + "\n")
