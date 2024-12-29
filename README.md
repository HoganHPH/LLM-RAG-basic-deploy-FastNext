<h1>LLM Retrieval Augmented Generation (RAG) - Basic application with FastAPI, NextJS and MongoDB</h1>
<p><b>A basic simulation of RAG system using MongoDB deployed by FastAPI and NextJS </b></p>
![til](./assets/demo.gif)

<h2>Key concept:</h2>
![image]([https://github.com/user-attachments/assets/67bc6f45-c3ef-47f2-b2b8-d3fdad5afc46](https://github.com/HoganHPH/LLM-RAG-basic-deploy-FastNext/blob/main/assets/basic_rag.png))

<h3>Retrieval Augmented Generation (RAG)</h3>
<p><b>There are 5 key components in a basic RAG:</b></p>
<ol>
  <li>Document Loader:</li>
  - <a href='https://python.langchain.com/docs/how_to/document_loader_pdf/'>PDF Loader</a>
  <li>Document Splitter:</li>
  - <a href='https://python.langchain.com/docs/how_to/#text-splitters'>Text Splitter</a>
  <li>Vector Embeddings:</li>
  - Embedding model: <a href='https://huggingface.co/second-state/All-MiniLM-L6-v2-Embedding-GGUF'>HuggingFace Embedding Model - all-MiniLM-L6-v2-Q5_K_M.gguf</a>
  <li>Vector Store</li>
  - <a href='https://python.langchain.com/docs/integrations/vectorstores/mongodb_atlas/'>MongoDB Atlas</a>
  - <a href='https://python.langchain.com/docs/integrations/vectorstores/'>Vector Stores</a>
  <li>Retrieval and Generation</li>
  - Chat model: <a href='https://huggingface.co/microsoft/Phi-3-mini-4k-instruct-gguf'>Hugging Face Chat Model - Phi-3-mini-4k-instruct-q4.gguf</a>
</ol>
<h3>Deployment</h3>
<ol>
  <li>Backend: FastAPI</li>
  <li>Frontend: NextJS</li>
</ol>

<h2>How to run?</h2>
<p><b>!Note: The system need to be run with 2 components (backend and frontend) seperately:</b></p>
<ul>
  <li>Run Backend in the first terminal window:</li>
    <code>
      cd backend
      python main.py
    </code>
  <p><b>!Important: Check installed libs in 'requirements.txt' and environment variables in '.env.example'</b></p>
  <li>Run Frontend in the second terminal window:</li>
    <code>
      cd frontend
      npm run dev
    </code>
</ul>
<h2>Shortcommings</h2>
<ul>
  <li>The system is only allowed to upload only 1 document</li>
  <li>The system use gguf model file to correspond to CPU</li>
  <li>The system is seperated into 2 individual parts (backend and frontend) -> Docker can solve this!</li>
</ul>
<h2>What's next?</h2>
<ul>
  <li>Advanced RAG: RAG with external API</li>
</ul>
