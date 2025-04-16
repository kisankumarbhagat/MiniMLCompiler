def optimize_ir(ir):
    # Optimizing IR by merging layers where applicable (simplified version)
    optimized_ir = []
    for i in range(len(ir)):
        if "ACTIVATION" in ir[i] and i + 1 < len(ir) and "DENSE" in ir[i + 1]:
            optimized_ir.append(ir[i] + " + " + ir[i + 1])
        else:
            optimized_ir.append(ir[i])
    return optimized_ir
