def generate_code(optimized_ir):
    # Convert IR into code
    code = []
    for layer in optimized_ir:
        code.append(f"// {layer}")  # Add comments for each layer in code
    return "\n".join(code)
