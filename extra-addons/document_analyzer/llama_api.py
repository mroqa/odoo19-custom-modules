from flask import Flask, request, jsonify
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.ollama import Ollama

app = Flask(__name__)

# Load documents once
documents = SimpleDirectoryReader("./documents").load_data()
index = VectorStoreIndex.from_documents(documents)
llm = Ollama(model="gpt-oss:120b-cloud", base_url="http://localhost:11434")
query_engine = index.as_query_engine(llm=llm)

@app.route('/query', methods=['POST'])
def query():
    data = request.json
    query_text = data.get('query')
    response = query_engine.query(query_text)
    return jsonify({'result': str(response)})

if __name__ == '__main__':
    app.run(port=5000, debug=True)