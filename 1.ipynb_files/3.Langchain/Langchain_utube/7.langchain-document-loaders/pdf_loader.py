from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader(r"C:\MY_Folder\MY_Courses\1.GEN_AI_LIVE_Classes\ipynb_files\3.Langchain\Langchain_utube\7.langchain-document-loaders\dl-curriculum.pdf")

docs = loader.load()

print(len(docs))

print(docs[0].page_content)
print(docs[1].metadata)