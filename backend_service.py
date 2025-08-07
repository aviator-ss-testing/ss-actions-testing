"""
Backend service for testing FlexReview team filtering.
This file should trigger @aviator-ss-testing/ss-be team.
"""

def process_data(data):
    """Process incoming data"""
    return {"status": "processed", "data": data}


def validate_input(input_data):
    """Validate input parameters"""
    if not input_data:
        return False
    return True


class BackendService:
    def __init__(self):
        self.initialized = True
    
    def handle_request(self, request):
        if self.validate_input(request):
            return self.process_data(request)
        return {"error": "Invalid input"}
