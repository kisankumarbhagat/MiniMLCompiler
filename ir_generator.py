def generate_ir(model):
    # Dummy function to generate an IR based on model structure
    # For now, we're simulating an IR based on layers
    ir = []
    ir.append("INPUT shape=[784]")  # Example: Input layer
    ir.append("DENSE units=64 weights=W1 biases=b1")  # First Dense layer
    ir.append("ACTIVATION function=relu")  # Activation function after Dense layer
    ir.append("DENSE units=10 weights=W2 biases=b2")  # Output layer
    ir.append("ACTIVATION function=softmax")  # Softmax activation for classification
    return ir
