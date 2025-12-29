from odoo import http
import requests
import json

class DocumentController(http.Controller):
    @http.route('/analyze_document', type='json', auth='user')
    def analyze_document(self, **kwargs):
        try:
            # Call your external LlamaIndex service
            response = requests.post('http://localhost:5000/query', 
                json={'query': kwargs.get('query')})
            return response.json()
        except Exception as e:
            return {'error': str(e)}