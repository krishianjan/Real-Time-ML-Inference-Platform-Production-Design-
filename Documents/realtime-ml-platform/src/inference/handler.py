import json
import logging
import torch
from ts.torch_handler.base_handler import BaseHandler

logger = logging.getLogger(__name__)

class ModelHandler(BaseHandler):
    def initialize(self, context):
        super().initialize(context)
        self.manifest = context.manifest
        properties = context.system_properties
        model_dir = properties.get("model_dir")
        
        # Load model (placeholder)
        self.model = torch.jit.load(f"{model_dir}/model.pt")
        self.model.eval()
        
        logger.info("Model loaded successfully")
    
    def preprocess(self, data):
        # Convert input to tensor
        inputs = []
        for row in data:
            body = row.get("body")
            if isinstance(body, (str, bytes)):
                body = json.loads(body)
            inputs.append(body.get("features", []))
        
        return torch.tensor(inputs, dtype=torch.float32)
    
    def inference(self, data):
        with torch.no_grad():
            results = self.model(data)
        return results
    
    def postprocess(self, data):
        # Convert tensor to JSON response
        predictions = data.tolist()
        return [{"prediction": p} for p in predictions]

_service = ModelHandler()

def handle(data, context):
    if not _service.initialized:
        _service.initialize(context)
    
    if data is None:
        return None
    
    data = _service.preprocess(data)
    data = _service.inference(data)
    data = _service.postprocess(data)
    return data