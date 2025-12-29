import xmlrpc.client
from llama_index.core import SimpleDirectoryReader, VectorStoreIndex
from llama_index.llms.ollama import Ollama
from llama_index.embeddings.ollama import OllamaEmbedding


# Connect to Odoo
url = "http://localhost:8069"
db = "Demo"
username = "mohammed.roqa@digitalsol.ae"
password = "Pa$$w0rd"

common = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/common")
uid = common.authenticate(db, username, password, {})
models = xmlrpc.client.ServerProxy(f"{url}/xmlrpc/2/object")

embed_model = OllamaEmbedding(
    model_name="gpt-oss:120b-cloud",
    base_url="http://localhost:11434"
)

# LlamaIndex setup
documents = SimpleDirectoryReader("../document_analyzer/documents").load_data()
index = VectorStoreIndex.from_documents(
    documents,
    embed_model=embed_model
)
llm = Ollama(model="gpt-oss:120b-cloud", base_url="http://localhost:11434")
query_engine = index.as_query_engine(llm=llm)


# Test Connect
response = llm.complete("Say hello")
print("✓ LlamaIndex + Ollama connected!")
print(f"Response: {response}")

# Query and send results back to Odoo
response = query_engine.query("Extract invoice details")

# Write back to Odoo (example: create a record)
result = models.execute_kw(db, uid, password, 'ir.attachment', 'create', [{
    'name': 'AI Analysis',
    'datas': str(response).encode(),
    'res_model': 'account.invoice',
}])
