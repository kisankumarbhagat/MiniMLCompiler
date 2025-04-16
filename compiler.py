import json
from ir_generator import generate_ir
from optimizer import optimize_ir
from codegen import generate_code

# Load model
with open("model.json", "r") as f:
    model = json.load(f)

# Step 1: Generate IR
ir = generate_ir(model)
print("Intermediate Representation:")
print("\n".join(ir))

# Step 2: Optimize IR
optimized_ir = optimize_ir(ir)
print("\nOptimized IR:")
print("\n".join(optimized_ir))

# Step 3: Generate Code
final_code = generate_code(optimized_ir)
print("\nGenerated Code:")
print(final_code)

# Save output to a text file
output = []
output.append("Intermediate Representation:\n" + "\n".join(ir))
output.append("Optimized IR:\n" + "\n".join(optimized_ir))
output.append("Generated Code:\n" + final_code)

with open("output.txt", "w") as out_file:
    out_file.write("\n\n".join(output))

print("\nOutput saved to output.txt")

