import os
import onnx

def load_onnx_model(path):
    # Validate if the model file exists
    if not os.path.exists(path):
        print(f"Model file not found: {path}")
        return None

    try:
        # Load the ONNX model
        model = onnx.load(path)
        
        # Check if the model is valid
        onnx.checker.check_model(model)
        print("Model is valid!")

        return model
    except onnx.onnx_cpp2py_export.checker.ValidationError as e:
        print(f"Model validation error: {e}")
        return None
    except Exception as e:
        print(f"Error loading model: {e}")
        return None
