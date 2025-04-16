from onnx_loader import load_onnx_model
from ir_generator import generate_ir
from optimizer import optimize_ir
from codegen import generate_code
from utils import save_output

MODEL_PATH = "models/sample_model.onnx"  # Path to your ONNX model
OUTPUT_PATH = "outputs/output.txt"      # Output file path

# Load and validate ONNX model
model = load_onnx_model(MODEL_PATH)
if model is None:
    exit()  # Exit if model could not be loaded

# Generate IR from the model
ir = generate_ir(model)
print("Intermediate Representation:")
print("\n".join(ir))

# Optimize IR
optimized_ir = optimize_ir(ir)
print("\nOptimized IR:")
print("\n".join(optimized_ir))

# Generate code from the optimized IR
final_code = generate_code(optimized_ir)
print("\nGenerated Code:")
print(final_code)

# Save output to a text file
save_output(OUTPUT_PATH, ir, optimized_ir, final_code)
print(f"\nAll output saved to: {OUTPUT_PATH}")
